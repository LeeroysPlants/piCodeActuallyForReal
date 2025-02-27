#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import PCF8591 as ADC  # Import PCF8591 module
import time  # for delay in print statement
#WATER LEVEL SHOULD BE IN Ain1 in the converter thingy

def main(args):
    ADC.setup(0x48)  # idk tutorial made me do it
    try:
        while True:  # Continuously read and print
            print(ADC.read(1))  # assumes water level is in Ain1
            time.sleep(0.2)  # Delay of 0.2 seconds
    except KeyboardInterrupt:
        print("Exit")  # Exit on CTRL+C

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
