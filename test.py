#!/usr/bin/python3

#### Monkeys.py ############
# Author: SG Langer Aug 2024
#
# Purpose: demonstrate the power of 
#	probability to non-math types
#
# Ext. depedencies
###########################
import random
import enchant
import os, sys
import datetime
import configparser as CP

def init():
#############################
# Purpose: read props file 
# for init Vars
##########################
  mod ="monkey:init: "

  startPath = os.path.abspath(os.getcwd())
  propPath = startPath + '/monkeys.prop'
  print (propPath)
  
  try:
    config=CP.RawConfigParser()
    config.read(propPath)
    a = config.items('init')
    #print (a)
    maxWords = a[0][1]
    maxLen = a[1][1]
    wordList = a[2][1]
  except:
    print (mod, 'could not read props, exiting')
    sys.exit()

  return maxWords,  maxLen,  wordList
  
  
## main
os.system('clear')

maxLen, maxWords, wordList = init ()
print (maxWords, maxLen, wordList)

