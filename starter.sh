#!/bin/bash
trap ctrl_c INT

while :
do
    python3 app.py & python3 display.py & python3 buttonReader.py & python3 gpio_reader.py
done


