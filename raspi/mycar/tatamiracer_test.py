# TatamiRacer Test for Steering Servo and Motor

import pigpio
import tkinter as tk
from tkinter import messagebox
import numpy as np
import os
import re
import time
import threading

pi = pigpio.pi()
gpio_pin0 = 13 #Motor1
gpio_pin1 = 19 #Motor2
gpio_pin2 = 14 #Servo
fname = os.getcwd()+r'/myconfig.py' #for Donkey Car parameter file

#Variable
class cfg: #parameter
    pass
root = tk.Tk()
motor = tk.IntVar()
servo = tk.IntVar()
servo_center = tk.IntVar()
servo_limit = tk.IntVar()
servo_limit_flag = tk.BooleanVar()
throttle_boost_enable_flag = tk.BooleanVar()
throttle = tk.DoubleVar()
steering = tk.DoubleVar()

throttle_start_boost = tk.DoubleVar()
throttle_start_boost_time = tk.DoubleVar()
throttle_upper_limit = tk.DoubleVar()
throttle_lower_limit = tk.DoubleVar()
throttle_steering_boost = tk.DoubleVar()
steering_feel = tk.DoubleVar()
steering_balance = tk.DoubleVar()

throttle_start_boost_time0 = 0.0
throttle_start_boost_val = 0.0
throttle_deadzone=0.01

timer_enable = True
def timer100ms():
    global throttle_start_boost_val,throttle_start_boost_time0
    if not timer_enable:
        return

    throttle_abs = np.abs(throttle.get())
    t_current = time.time()
    if throttle_abs<=throttle_deadzone:
        throttle_start_boost_time0 = t_current
    #Throttle Boost
    t = t_current-throttle_start_boost_time0
    if(t <= throttle_start_boost_time.get()):
        throttle_start_boost_val = throttle_start_boost.get() #Boost mode
    else:
        throttle_start_boost_val = 0.0
        set_throttle(0)

    t = threading.Timer(0.1, timer100ms)
    t.start()

def set_timer():
    t = threading.Thread(target=timer100ms)
    t.start()
    return t
 
def set_config():
    servo_max= cfg.TATAMI_STEERING_LEFT_PWM
    servo_min= cfg.TATAMI_STEERING_RIGHT_PWM
    tmp=int(servo_max-servo_min)/2
    servo_limit.set(tmp)
    servo_limit_flag.set(True)
    throttle_boost_enable_flag.set(True)
    servo_center.set(servo_min+tmp)
    servo.set(servo_center.get())
    motor.set(0)
    throttle.set(0)
    steering.set(0)
    set_motor(0)
    set_servo(0)

    steering_feel.set(cfg.TATAMI_STEERING_FEEL)
    steering_balance.set(cfg.TATAMI_STEERING_BALANCE)
    throttle_start_boost_time.set(cfg.TATAMI_THROTTLE_START_BOOST_TIME)
    throttle_start_boost.set(cfg.TATAMI_THROTTLE_START_BOOST)
    throttle_upper_limit.set(cfg.TATAMI_THROTTLE_UPPER_LIMIT)
    throttle_lower_limit.set(cfg.TATAMI_THROTTLE_LOWER_LIMIT)
    throttle_steering_boost.set(cfg.TATAMI_THROTTLE_STEERING_BOOST)
    status()
    status2()
    disable_button()

def load_config():
    f=open(fname)
    datalist=f.readlines()
    f.close()
    i=0
    for s in datalist:
        tmp = re.match(r'^(TATAMI_[A-z_0-9]+\s*[=].+)#',s)
        if tmp:
            exec('cfg.'+tmp.groups()[0])
        i=i+1
    set_config()
            
def save_config():
    ret = messagebox.askyesno('Write configuration','Write myconfig.py?')
    if not ret:return    
    f = open(fname)
    datalist=f.readlines()
    f.close()
    servo_max = servo_center.get()+servo_limit.get()
    servo_min = servo_center.get()-servo_limit.get()
    cfg.TATAMI_STEERING_LEFT_PWM = servo_max 
    cfg.TATAMI_STEERING_RIGHT_PWM = servo_min
    cfg.TATAMI_STEERING_FEEL=steering_feel.get()
    cfg.TATAMI_STEERING_BALANCE=steering_balance.get()
    cfg.TATAMI_THROTTLE_START_BOOST_TIME=throttle_start_boost_time.get()
    cfg.TATAMI_THROTTLE_START_BOOST=throttle_start_boost.get()
    cfg.TATAMI_THROTTLE_UPPER_LIMIT=throttle_upper_limit.get()
    cfg.TATAMI_THROTTLE_LOWER_LIMIT=throttle_lower_limit.get()
    cfg.TATAMI_THROTTLE_STEERING_BOOST=throttle_steering_boost.get()
    
    print('Write Parameter into:' + fname)
    i = 0
    for s in datalist:
        tmp = re.match(r'^(TATAMI_[A-z_0-9]+)\s*[=].+(#.+$)',s)
        if tmp:
            varname =tmp.groups()[0]
            val = str( eval('cfg.'+varname) )
            comment = tmp.groups()[1]
            d = varname+" = "+val+" "+comment
            datalist[i] = d+"\n"
            print(d)
        i = i + 1
    f=open(fname,'w')
    f.writelines(datalist)
    f.close()

def init_config():
    load_config()
    set_config()

def set_motor(motor_level):
    motor_v=int(motor_level)
    if motor_v > 0:
        pi.set_PWM_range(gpio_pin0, 100)  # Set PWM range
        pi.set_PWM_dutycycle(gpio_pin0,   motor_v) # Set PWM duty
        pi.set_PWM_frequency(gpio_pin0,490)
        pi.set_PWM_dutycycle(gpio_pin1,   0) # PWM off
    else:
        pi.set_PWM_range(gpio_pin1, 100)  # Set PWM range
        pi.set_PWM_dutycycle(gpio_pin1,   -motor_v) # Set PWM duty
        pi.set_PWM_frequency(gpio_pin1,490)
        pi.set_PWM_dutycycle(gpio_pin0,   0) # PWM off

def set_servo(x):
    servo_v = servo.get()
    servo_max = servo_center.get()+servo_limit.get()
    servo_min = servo_center.get()-servo_limit.get()
    if servo_limit_flag.get() and servo_v > servo_max:
        servo_v = servo_max
    elif servo_limit_flag.get() and servo_v < servo_min:
        servo_v = servo_min
    pi.set_mode(gpio_pin2, pigpio.OUTPUT)
    pi.set_servo_pulsewidth(gpio_pin2, servo_v )
    servo.set(servo_v)
    status()

def set_throttle(x):
    global throttle_start_boost_val
    th_in = throttle.get()
    throttle_abs = np.abs(th_in)
    
    #Steering Boost
    angle_adjust = throttle_lower_limit.get()+np.abs(steering.get())*(throttle_steering_boost.get()-throttle_lower_limit.get())

    #Feeling 
    if throttle_abs < throttle_lower_limit.get():
        throttle_feel = throttle_lower_limit.get()
    elif throttle_abs > throttle_upper_limit.get():
        throttle_feel = throttle_upper_limit.get()
    else:
        slope = throttle_upper_limit.get()-throttle_lower_limit.get()
        throttle_feel = throttle_lower_limit.get() + throttle_abs*slope
                          
    if throttle_abs > throttle_deadzone:
        if throttle_boost_enable_flag.get():
            th = np.sign(th_in)*max(throttle_start_boost_val,angle_adjust,throttle_feel)
        else:
            th = th_in
    else:
        th=0
    s1.set(th*100)
    
def set_steering(x):
    angle = steering.get()
    #Steering Feeling Adjustment
    ang_abs=np.abs(angle)
    steering_half=0.5
    if ang_abs < steering_half:
        slope = steering_feel.get()/steering_half
        angle = np.sign(angle)*ang_abs*slope
    else:
        slope = (1.0-steering_feel.get())/(1.0-steering_half)
        angle = np.sign(angle)* (steering_feel.get()+(ang_abs-steering_half)*slope)
            
    #Steering Balance Adjustment
    if angle>0:
        angle =  angle * (1.0+steering_balance.get())
    else:
        angle =  angle * (1.0-steering_balance.get())
            
    v = servo_center.get()-servo_limit.get()*angle
    s2.set(v)
    set_throttle(0)

def status():
    servo_offset = servo.get()-servo_center.get()
    servo_max = servo_center.get()+servo_limit.get()
    servo_min = servo_center.get()-servo_limit.get()
    s = ' Servo:'+str(servo_offset)
    s = s+' Limit:'+str(servo_limit.get())
    s = s+' (Min:'+str(servo_min)
    s = s+ ' Center:'+str(servo_center.get())
    s = s+' Max:'+str(servo_max)+')'
    l1.config(text=s)

def status2():
    s = 'Start Boost:'+str(throttle_start_boost.get())
    s = s + ' Steering Boost:'+str(throttle_steering_boost.get())
    s = s + ' Lower Limit:'+str(throttle_lower_limit.get())
    s = s + ' Upper Limit:'+str(throttle_upper_limit.get())
    l2.config(text=s)
    
def disable_button():
    if servo_limit_flag.get():
        b3.config(state=tk.DISABLED)
        b4.config(state=tk.DISABLED)
    else:
        b3.config(state=tk.NORMAL)
        b4.config(state=tk.NORMAL)
        
    if throttle_boost_enable_flag.get():
        b12.config(state=tk.DISABLED)
        b11.config(state=tk.DISABLED)
        b9.config(state=tk.DISABLED)
        b8.config(state=tk.DISABLED)
    else:
        b12.config(state=tk.NORMAL)
        b11.config(state=tk.NORMAL)
        b9.config(state=tk.NORMAL)
        b8.config(state=tk.NORMAL)
        
#GUI
root.title('TatamiRacer Test')
root.minsize(width=640, height=480)

#Make GUI
f1=tk.Frame(root)
f1.pack(fill = tk.BOTH)

f3=tk.Frame(root)
f3.pack(fill = tk.BOTH)
f4=tk.Frame(root)
f4.pack(fill = tk.BOTH)
f7=tk.Frame(root)
f7.pack(fill = tk.BOTH)
f6=tk.Frame(root)
f6.pack(fill = tk.BOTH)
f5=tk.Frame(root)
f5.pack(fill = tk.BOTH)
f2=tk.Frame(root)
f2.pack(fill = tk.BOTH)

s1 = tk.Scale(f1, label = 'Motor PWM: ', orient = 'h', from_ = -100.0,
              to = 100.0, variable = motor, command = set_motor)
s1.pack(fill = tk.BOTH)
b1 = tk.Button(f1, text= 'Off', command = lambda :s1.set(0) )
b1.pack()
s2 = tk.Scale(f1, label = 'Servo PWM: ', orient = 'h',
              from_ = 500.0, to = 2500.0,  variable = servo, command =set_servo)
s2.pack(fill=tk.BOTH)
l1 = tk.Label(f3, width=100, text='')
l1.pack(fill=tk.BOTH)
b2 = tk.Button(f1, text= 'Center', command = lambda :[s2.set(servo_center.get()),status()])
b2.pack()
l1.pack(fill=tk.BOTH)
b2.pack()
c1 = tk.Checkbutton(f1, text= 'Enable Servo Limit' ,variable = servo_limit_flag,
                    command = lambda :[s2.set(servo_center.get()),disable_button()] )
c1.pack(side=tk.RIGHT)
b4 = tk.Button(f1, text= 'Set Servo Limit',
               command = lambda :[servo_limit.set( np.abs(servo.get()-servo_center.get() )),status()])
b4.pack(side=tk.RIGHT)
b3 = tk.Button(f1, text= 'Set Servo Center',
               command = lambda:[servo_center.set(servo.get()),status()])
b3.pack(side=tk.RIGHT)
s3 = tk.Scale(f4, label = 'Throttle Level: ', orient = 'h',
              from_ = -1.0, to = 1.0, resolution=0.01,  variable = throttle, command= set_throttle)
s3.pack(fill=tk.BOTH)
b10 = tk.Button(f7, text= 'Forward >', command = lambda:s3.set(0.1) )
b10.pack(side=tk.RIGHT,ipadx=120)
b15 = tk.Button(f7, text= 'Stop', command = lambda:s3.set(0) )
b15.pack(side=tk.RIGHT,ipadx=120)
b16 = tk.Button(f7, text= '< Backward', command = lambda:s3.set(-0.1) )
b16.pack(side=tk.RIGHT,ipadx=120)

c2 = tk.Checkbutton(f4, text= 'Enable Boost&Limit' ,variable = throttle_boost_enable_flag,
                    command = lambda :[disable_button(),s3.set(0)] )
c2.pack(side=tk.RIGHT)
b12 = tk.Button(f4, text= 'Set Upper Limit',
                command = lambda: [throttle_upper_limit.set(s3.get()),status2()] )
b12.pack(side=tk.RIGHT)
b11 = tk.Button(f4, text= 'Set Lower Limit',
                command = lambda: [throttle_lower_limit.set(s3.get()),status2()] )
b11.pack(side=tk.RIGHT)
b9 = tk.Button(f4, text= 'Set Steering Boost',
               command = lambda:[throttle_steering_boost.set(s3.get()),status2()] )
b9.pack(side=tk.RIGHT)
b8 = tk.Button(f4, text= 'Set Start Boost',
               command = lambda:[throttle_start_boost.set(s3.get()),status2()] )
b8.pack(side=tk.RIGHT)

s4 = tk.Scale(f5, label = 'Steering Level: ', orient = 'h',
              from_ = -1.0, to = 1.0, resolution=0.01,  variable = steering, command = set_steering)
s4.pack(fill=tk.BOTH)
b13 = tk.Button(f5, text= 'Center', command = lambda:s4.set(0) )
b13.pack()

s5 = tk.Scale(f5, label = 'Steering Feel:', orient = 'h',length=320, 
              from_ = 0.1, to = 0.9, resolution=0.01, variable = steering_feel )
s5.pack(side=tk.RIGHT)
s6 = tk.Scale(f5, label = 'Steering Balance:', orient = 'h',length=320, 
              from_ = -0.9, to = 0.9, resolution=0.01, variable = steering_balance )
s6.pack(side=tk.RIGHT)
s7 = tk.Scale(f5, label = 'Start Boost Time:', orient = 'h',length=320, 
              from_ = 0.0, to = 3.0, resolution=0.1, variable = throttle_start_boost_time )
s7.pack(side=tk.RIGHT)
l2 = tk.Label(f6, width=100, text='-')
l2.pack(fill=tk.BOTH)

b14 = tk.Button(f2, text= 'Close', command = lambda :root.destroy() )
b14.pack(side=tk.RIGHT)
b5 = tk.Button(f2, text= 'Write myconfig.py', command = save_config )
b5.pack(side=tk.RIGHT)
b7 = tk.Button(f2, text= 'Load myconfig.py',
               command = lambda :[load_config(),s2.set(servo_center.get()),status(),status2()] )
b7.pack(side=tk.RIGHT)

#Start
init_config()
status()
disable_button()
timer_thread=set_timer()
root.mainloop()

#Exit
timer_enable = False
pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.set_mode(gpio_pin2, pigpio.INPUT)
pi.stop()
time.sleep(1)
print('TatamiRacer Test End')

