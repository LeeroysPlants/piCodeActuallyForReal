#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  waterPlant.py
#  
#  Copyright 2025  <noah@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time  # for delay in print statement
import requests
from gpiozero import Motor
from time import sleep

def main(args):
    
    
    url = 'http://localhost:3000/doesPiNeedToWaterPlant'
    response = requests.get(url); 
    print(response.text); 
    #pump = Motor(forward=17, backward=27)  # Using Raspberry Pi GPIO pin numbers
    #pump.forward(speed=1)  # Set pump speed, range is 0 to 1
    #sleep(5)   
    #pump.stop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
