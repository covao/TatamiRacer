# How to Calibrate TatamiRacer

## Start TatamiRacaer Test Tool  
Lunch "TatamiRacer Test" shortcut or enter following command from terminal.
~~~
cd ~/mycar
python tatamiracer_test.py
~~~

<img src="../img/tatamiracer_test.jpg" alt="" title="" width="640" height="">

## TatamiRacer Controller
TatamiRacer controller enhance motor start torque and feeling.
This is a block diagram that controls throttle and steering.
<img src="../img/TatamiRacer_Controller.jpg" alt="" title="" width="640" height="">


## Calibrate Servo PWM
1. Turn off the "Enable Servo Limit" check button.
2. Adjust center position by "Servo PWM" slider.
3. Click "Set Servo Center" button.
4. Check running straight by "Motor PWM" slider.
5. Adjust Servo Limit
6. Click "Set Servo Limit" button
7. Turn on "Enable Servo Limit"

## Calibrate Throttle Start Boost
1. Turn off the "Enable Boost&Limit" check button.
2. Set the throttle slider "Off".
3. Raise the throttle slider until the the car starts running.
4. Click "Set Start Boost" at the throttle level.   
5. Set the throttle slider "Off".
6. Turn on the "Enable Boost&Limit" check button.
7. Raise the throttle slider a little.
8. Check that the car starts running.
9. Adjust "Start Boost Time" for smooth acceleration.

## Calibrate the Throttle Feel
1. Turn off the "Enable Boost&Limit" check button.
2. Set the throttle slider "Off".
3. Raise the throttle slider until the car moves.
4. Reduce the throttle slider at the minimum value that the car keeps running.
5. Click "Set Lower Limit" at the throttle level.
6. If you want to reduce the maximum speed, set the Upper Limit.
7. Turn on the "Enable Boost&Limit" check button.
8. Raise the throttle slider a little.
9. Check that the car keeps running.

## Calibrate Throttle Steering Boost for Car Turns
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

## Calibrate Steering





