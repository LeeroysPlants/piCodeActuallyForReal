#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  postTest.py
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
#  Assumes server runnign on localhost port 3000

import requests
def main(args):
    print("omg python code")
    url = 'http://localhost:3000/data'
    obj = {'soilMoisture': '13'}
    x = requests.post(url, obj)
    print("post sent?")
    print(x.text)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
