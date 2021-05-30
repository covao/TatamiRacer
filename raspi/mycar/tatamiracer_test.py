# TatamiRacer Test for Steering Servo and Motor

import pigpio
import tkinter as tk
import numpy as np

pi = pigpio.pi()

gpio_pin0 = 13 #Motor1
gpio_pin1 = 19 #Motor2
gpio_pin2 = 14 #Servo

def drive_car(motor_level,servo_level):

    motor_v=int(1000000*(motor_level / 100.0))
    motor_v=int( motor.get() )
    servo_v=int(00.0 + 1*(servo_level / 1.0))
    if servo_v > 2500:
        servo_v = 2500
    elif servo_v < 500:
        servo_v =500
    
    pi.set_mode(gpio_pin2, pigpio.OUTPUT)
    pi.set_servo_pulsewidth(gpio_pin2, servo_v )

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


#GUI
root = tk.Tk()
root.minsize(width=640, height=200)
root.title('TatamiRacer Test')

servo_ini = 1500
servo_max_offset_ini = 500

motor = tk.IntVar()
motor.set(0)
servo = tk.IntVar()
servo.set(servo_ini)
servo_center = tk.IntVar()
servo_center.set(servo_ini)
servo_max_offset = tk.IntVar()
servo_max_offset.set(servo_max_offset_ini)
servo_limit_flag = tk.BooleanVar()
servo_limit_flag.set(True)


s1 = tk.Scale(root, label = 'Motor: ', orient = 'h',
              from_ = -100.0, to = 100.0, variable = motor, command = lambda x: drive_car(motor.get(),servo.get())
)

l1 = tk.Label(root, width=20, text='')
l2 = tk.Label(root, width=20, text='')

def set_servo():
    servo_max= servo_center.get()+servo_max_offset.get()
    servo_min= servo_center.get()-servo_max_offset.get()
    if servo_limit_flag.get() and servo.get()>servo_max:
        servo.set(servo_max)
    elif servo_limit_flag.get() and servo.get()<servo_min:
        servo.set(servo_min)
    offset = servo.get()-servo_center.get()
    drive_car(motor.get(),servo.get())
    
    t = ' Offset:'+str(offset)+' , Offset Limit:'+str(+servo_max_offset.get())
    l1.config(text=t)
    t = 'Min:'+str(servo_min)
    t = t+ ' , Center:'+str(servo_center.get())
    t = t+' , Max:'+str(servo_max)
    l2.config(text=t)

s2 = tk.Scale(root, label = 'Servo: ', orient = 'h',
              from_ = 500.0, to = 2500.0,  variable = servo, 
              command = lambda x:set_servo()
)

b1 = tk.Button(root, text= 'Off', command = lambda :s1.set(0) )
b2 = tk.Button(root, text= 'Center', command = lambda :s2.set(servo_center.get()))
b3 = tk.Button(root, text= 'Set Servo Center', command = lambda :[servo_center.set(servo.get()),set_servo()])
b4 = tk.Button(root, text= 'Set Servo Limit', command = lambda :[servo_max_offset.set( np.abs(servo.get()-servo_center.get() )),set_servo()])
c1 = tk.Checkbutton(root, text= 'Enable Servo Limit' ,variable = servo_limit_flag, command = lambda :s2.set(servo_center.get()))

s1.pack(fill = 'both')
b1.pack()
s2.pack(fill = 'both')
l1.pack(fill = 'both')
l2.pack(fill = 'both')
b2.pack()
l1.pack(fill = 'both')
b2.pack()

c1.pack(side=tk.RIGHT)
b4.pack(side=tk.RIGHT)
b3.pack(side=tk.RIGHT)
set_servo()
root.mainloop()

pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.set_mode(gpio_pin2, pigpio.INPUT)
pi.stop()

