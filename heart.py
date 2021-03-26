#!/usr/bin/env python3

import os
from time import sleep

with open('heart.txt', 'r') as f:
    data = f.readlines()
    #for i in range(2):
    while True:
        for line in data:
            print(line)
            sleep(0.5)
        
