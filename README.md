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

# Run results for multi-processing version
* 8 cores (eg monkeys) doing 1M words each, 20 seconds
	* came up with "A sea of feces"

# next Steps
* ??

