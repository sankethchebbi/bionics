import numpy as np
import serial

# establish serial connection with bionic arm
ser = serial.Serial('COM3', 9600)

# function to control bionic arm movement based on EEG sensor input
def control_arm(eeg_data):
    # threshold for arm movement
    threshold = 0.5
    # check if EEG sensor input is above threshold
    if eeg_data > threshold:
        # send command to bionic arm to move
        ser.write(b'1')
    else:
        # send command to bionic arm to stop moving
        ser.write(b'0')
