# typing_monkeys
* Purpose: for demoing statistics of random word creations
* Author: sg langer Aug 2024

# HOw to install
* have python3 on your system
* clone the repo in the usual way
* make sure enchated is installed
	* if not use "pip install pyenchant"
	
	
# How to run
* edit properties file  to taste for: max number of Words, max word length, number of CPU cores avail
* after run, compare the raw vs filtered .TXT files

# Run results for single task version
* 100,000 words, 3 seconds, did not shuffle wordList, no sentences
* 1 Billion words, 620 minutes, list shuffled, multiple sentences (eg "Hes  a ten", "Eaten a wee son", "a foe in a tea cup")

# next Steps
* Time permitting setup a 2nd version that multi-processes
	* __convert current monkeys.py to a class
	* write a new Main that uses multi-process to call class N times
	* track the PIDs of above
	* when all PIDs finish, assemble the final fiteredTexts into one big one

