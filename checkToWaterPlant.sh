#!/bin/bash
PATH=....
source ~/env/bin/activate
while true; do
	python ~/ssp2/waterPlant.py
	/usr/bin/sleep 5
done

#chron job to check if this is running, starts it if its not 
