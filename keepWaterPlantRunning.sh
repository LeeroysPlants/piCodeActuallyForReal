#!/bin/bash

if pgrep -f "checkToWaterPlant.sh" > /dev/null; then
	echo "was running"
else
	echo "was not running, starting it"
	/home/noah/ssp2/checkToWaterPlant.sh
fi
	
