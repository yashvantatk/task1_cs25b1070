#!/bin/bash

BATTERY=$((RANDOM % 101))
echo "Current Battery Level: ${BATTERY}%"

if [ "$BATTERY" -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi

if ping -c 1 google.com &> /dev/null; then
    echo "All systems operational!"
else
    echo "Communication failure!"
    exit 1
fi
