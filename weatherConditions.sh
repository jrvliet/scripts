#!/usr/bin/env bash

# Runs the weather command and outputs status to .weather file
output="/home/jacob/scripts/status"
current=$(weather fips3539380)
temp=$(weather fips3539380 | awk '/Temperature/ {print $2}')
humid=$(weather fips3539380 | awk '/Relative/ {print $3}')
wind=$(weather fips3539380 | awk '/Wind/ {print $8}')
if [ "$wind" = "" ]; then
    wind=0
fi
sky=$(weather fips3539380 | awk '/Sky/' | awk -F':' '{print $2}')
printf '%sF, %s, %smph, %s' $temp $humid $wind $sky > $output

