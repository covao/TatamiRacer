# TatamiRacer Servo & Motor Test
import pigpio
import tkinter as tk

pi = pigpio.pi()

root = tk.Tk()
root.minsize(width=640, height=200)
root.title('TatamiRacer Servo & Motor Test')

motor = tk.IntVar()
motor.set(0)
servo = tk.IntVar()
servo.set(0)

gpio_pin0 = 13
gpio_pin1 = 19
gpio_pin2 = 14

def drive_car(n):

    motor_v=int(1000000*(motor.get() / 100.0))
    servo_v=int(1500.0 + 1000*(servo.get() / 100.0))
    if servo_v > 2500:
        servo_v = 2500
    elif servo_v < 500:
        servo_v =500
    l1.config(text='Motor: '+str(motor_v))
    l2.config(text='Servo: '+str(servo_v))
    
    pi.set_mode(gpio_pin2, pigpio.OUTPUT)
    pi.set_servo_pulsewidth(gpio_pin2, servo_v )

    if motor_v > 0:
        pi.set_mode(gpio_pin0, pigpio.OUTPUT)
        pi.hardware_PWM(gpio_pin0, 490, motor_v)
        pi.set_mode(gpio_pin1, pigpio.INPUT)
    else:
        pi.set_mode(gpio_pin1, pigpio.OUTPUT)
        pi.hardware_PWM(gpio_pin1, 490, -motor_v)
        pi.set_mode(gpio_pin0, pigpio.INPUT)

s1 = tk.Scale(root, label = 'Motor: ', orient = 'h',
              from_ = -100.0, to = 100.0, variable = motor, command = drive_car
)
l1 = tk.Label(root, width=20, text='')

s2 = tk.Scale(root, label = 'Servo: ', orient = 'h',
              from_ = -100.0, to = 100.0,  variable = servo, command = drive_car
)
l2 = tk.Label(root, width=20, text='')

s1.pack(fill = 'both')
l1.pack(fill = 'both')
s2.pack(fill = 'both')
l2.pack(fill = 'both')


root.mainloop()

pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.set_mode(gpio_pin2, pigpio.INPUT)

pi.stop()