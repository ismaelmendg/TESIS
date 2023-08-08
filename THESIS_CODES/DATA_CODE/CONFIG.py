# Algoritm configuration for data acquisition
# Developed by Ismael Mendoza
# 24/09/2022

import random
import numpy as np
from itertools import repeat
# TIMING CONSTANTS:
# *****************

updateRate= 0.9


ExperimentConfigureTime=0
fixationCrossTime=0
cueTime= 1.5
timeout =3
taskTime =3
resultTime=2
restTime=1
fixationTime = 2

detectionThresholdLH = 0.9  #0.5
detectionThresholdRH = 0.6 #0.6
detectionThresholdBH = 0.75

n_LH = 1
n_RH = 1
n_BH = 1

LH_array = list(repeat(1, n_LH))
RH_array = list(repeat(-1, n_RH))
BH_array = list(repeat(2, n_BH))
total = len(LH_array) + len(RH_array) + len(BH_array)
trials = np.zeros(total)
all_arrays = LH_array + RH_array + BH_array

for i in range(0, total, 1):
    trials[i] = random.sample(all_arrays, 1)[0]
    all_arrays.remove(trials[i])

#  NOTES:
# ********
# Class (+1): extension (right)
# Class (-1): flexion (left)
# Class (+2): Both hands
