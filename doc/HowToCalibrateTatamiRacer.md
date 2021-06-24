# How to Calibrate TatamiRacer

## Start TatamiRacaer Test Tool  
Launch "TatamiRacer Test" from shortcut or enter following command from terminal.
~~~
cd ~/mycar
python tatamiracer_test.py
~~~

<img src="../img/tatamiracer_test.jpg" alt="" title="" width="640" height="">

## About TatamiRacer Controller
TatamiRacer controller enhance the motor start torque and feeling.  
This is a block diagram that controls throttle and steering.  
<img src="../img/TatamiRacer_Controller.jpg" alt="" title="" width="640" height="">

## Basic Calibration
### Calibrate Servo PWM
Purpose: Adjust the position of the steering center and steering limit
1. Turn off the "Enable Servo Limit" check button.
2. Adjust center position by "Servo PWM" slider.
3. Click "Set Servo Center" button.
4. Check running straight by "Motor PWM" slider.
5. Move servo PWM slider until steering stop.
7. Click "Set Servo Limit" button.
8. Turn on "Enable Servo Limit".

### Write the parameters to the "myconfig.py" file
1. Click the "Write myconfig.py" button.
2. Press "Yes" in the dialog.

## Advanced Calibration
### Calibrate Throttle Start Boost
Purpose: Smooth acceleration by increasing the starting torque
1. Turn off the "Enable Boost&Limit" check button.
2. Set the throttle slider "Off".
3. Raise the throttle slider until the the car starts running.
4. Click "Set Start Boost" at the throttle level.   
5. Set the throttle slider "Off".
6. Turn on the "Enable Boost&Limit" check button.
7. Raise the throttle slider a little.
8. Check that the car starts running.
9. Adjust "Start Boost Time" for smooth acceleration.

### Calibrate the Throttle Feel
Purpose: Improved throttle sensitivity
1. Turn off the "Enable Boost&Limit" check button.
2. Set the throttle slider "Off".
3. Raise the throttle slider until the car moves.
4. Reduce the throttle slider at the minimum value that the car keeps running.
5. Click "Set Lower Limit" at the throttle level.
6. If you want to reduce the maximum speed, set the Upper Limit.
7. Turn on the "Enable Boost&Limit" check button.
8. Raise the throttle slider a little.
9. Check that the car keeps running.

### Calibrate the Throttle Steering Boost
Purpose: Improved torque when cornering
1. Turn off the "Enable Boost&Limit" check button.
2. Set the throttle slider "Off".
3. Set the Steerling slide max.
4. Raise the throttle slider until the car moves.
5. Reduce the throttle slider at the minimum value that the car keeps running.
6. Click "Set Steering Boost" at the throttle level.
7. Turn on the "Enable Boost&Limit" check button.
8. Set the Steerling slide at center.
9. Raise the throttle slider a little.
10. Set the Steerling slide max (right side).
11. Check that the car keeps running.
12. Set the Steerling slide min (left side).
13. Check that the car keeps running.

### Calibrate the Steering Feel
Purpose: Improved control of small steering angles
1. Adjust "Steering Feel" slider.
2. Move Steering slider from left to right.
3. Check the steering feeling.

### Calibrate the Steering Balance
Purpose: Make left and right turns the same level
1. Set "Steering level" to about -0.8. (left side)
2. Run the car and check turn level.
3. Set "Steering level" to about +0.8.(right side)
4. Check the balance and adjust "Steering Balance" level


