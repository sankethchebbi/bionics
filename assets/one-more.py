import serial
import time
import pyeeg
from pymindwave import pyeeg

# create connection with the MindWave headset
headset = pyeeg.MindWaveMobile()

# connect to the headset
headset.connect()

# establish serial connection with bionic arm
ser = serial.Serial('COM3', 9600)

# function to control bionic arm movement based on EEG sensor input
def control_arm():
    while True:
        # check if headset is connected
        if headset.status == "connected":
            # get EEG data
            eeg_data = headset.attention
            # threshold for arm movement
            threshold = 50
            # check if EEG sensor input is above threshold
            if eeg_data > threshold:
                # send command to bionic arm to move
                ser.write(b'1')
            else:
                # send command to bionic arm to stop moving
                ser.write(b'0')
        # if headset is not connected, try to connect again
        else:
            headset.connect()
            time.sleep(1)
