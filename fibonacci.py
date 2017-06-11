#!/usr/bin/python

import sys
import math

initialValue = float(sys.argv[1])
laterValue = float(sys.argv[2])

delta = initialValue - laterValue

fibonacciFirstLevel = laterValue  + (delta * 0.236) 
fibonacciSecondLevel = laterValue  + (delta * 0.382) 
fibonacciThirdLevel = laterValue  + (delta * 0.618) 
fibonacciFinalLevel = laterValue + delta

print " "
print fibonacciFirstLevel
print " "
print fibonacciSecondLevel
print " "
print fibonacciThirdLevel
print " "
print fibonacciFinalLevel



