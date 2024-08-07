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
import os
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


def makeList():
######################
# Purpose: make a statistically valid
#	array of the english alphabet
# Refs:
#  https://stackoverflow.com/questions/14992521/python-weighted-random
#  https://en.wikipedia.org/wiki/Letter_frequency
#####################
  mod = "monkey:makeList: "
  global list, lenList
  list = ['a'] * 820 + ['b'] * 150 + ['c'] * 280 + ['d'] * 430 + \
    ['e'] * 1270 + ['f'] * 220 + ['g'] * 200 + ['h'] * 610 + ['i'] * 700 \
    + ['j'] * 15 + ['k'] *  77 + ['l'] * 400 + ['m'] * 240 + ['n'] * 670 \
    + ['o'] * 750 + ['p'] * 190 + ['q'] * 9 + ['r'] * 600 + ['s'] * 630 \
    + ['t'] * 910 + ['u'] * 280 + ['v'] * 98 + ['w'] * 240 + ['y'] * 200 + ['z'] * 7

  random.shuffle(list)  
  lenList =  len(list)
  #print (list)
  return 

def makeWord (numLetters):
#######################
# Purpose: loop over numLetters
#   to make a random word
#######################
  mod = 'monkey:makeWord: '
  i = 0
  word = ""
  
  #print (mod , numLetters)
  while i < numLetters :
    spot = random.randrange(0, lenList)
    word = word + list[spot]
    #print (word)
    i = i+1
    
  return  word 

########################## main
# Purpose: write random words to file, compare to a dict 
# of real words, then write those hits to a 2nd file
#
# Refs
#  https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
#####################
mod = "monkey:main: "
os.system('clear')

#### Init block for running the monkeys
maxWordLen, numWords, wordList = init()
raw = open ("rawText.txt", 'w')
i = 0
startTime = datetime.datetime.now()

makeList() 
while i < numWords :
  word = makeWord(random.randrange(1, maxWordLen))
  raw.write(word + '\n')
  i = i+1

raw.close()

# Now compare raw file to dict
raw = open ("rawText.txt", 'r')
filtered = open ("filterText.txt", 'w')
dictReal = enchant.Dict("en_US")

Lines = raw.readlines()
for line in Lines:
  word = line.strip()
  # for some obscure reason the Enchant version thinks all single letter and most 2 letter
  # strings are valid words
  if len(word) > 2 or word in wordList :
    if dictReal.check(word) :
      filtered.write(word + '\n')  

raw.close()
filtered.close()

# show finished product
print ('Monkeys are tired.')
print ("Trials are ", numWords)
print ('ended   ', datetime.datetime.now())
print ('started ', startTime)
print (' Results ---- ')
os.system('cat filterText.txt')


