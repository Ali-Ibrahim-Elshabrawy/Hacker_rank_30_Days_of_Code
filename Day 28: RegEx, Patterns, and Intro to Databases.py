#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    res = []
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1].split('@')
        res.append([firstName,emailID[1]])
    for i in range(N):
        if res[i][1] == 'gmail.com':
            names.append(res[i][0])
        else:
            continue
    names.sort()
    print(*names,sep = '\n')
