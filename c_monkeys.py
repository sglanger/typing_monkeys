#!/usr/bin/python3

#### c_Monkey.py ############
# Author: SG Langer Aug 2024
#
# Purpose: demonstrate the power of 
#	probability to non-math types. This
#   us a nulti-processor version
# Ext. depedencies:
#   monkeys.prop
###########################
import random  
import enchant  
import os  
import datetime  
import configparser as CP  
  
class MonkeySimulator:  
    def __init__(self):  
        """Read properties file for initialization variables."""  
        mod = "monkey:init: "   
        self.letter_list = []  
        self.len_list = 0  
        self.dict_real = enchant.Dict("en_US")  
   
        start_path = os.path.abspath(os.getcwd())  
        prop_path = os.path.join(start_path, 'monkeys.prop')  
  
        try:  
            config = CP.RawConfigParser()  
            config.read(prop_path)  
            a = config.items('init')  
            self.max_words = int(a[1][1])  
            self.max_len = int(a[0][1])  
            self.word_list = a[2][1].split(',')[1:-1]  
        except Exception as e:  
            print(mod, 'could not read props, exiting:', e)  
            os._exit(1)  
            
        return
  
    def make_list(self):  
        """Create a statistically valid array of the English alphabet."""  
        mod = "monkey:makeList: "  
        self.letter_list = (  
            ['a'] * 820 + ['b'] * 150 + ['c'] * 280 + ['d'] * 430 +  
            ['e'] * 1270 + ['f'] * 220 + ['g'] * 200 + ['h'] * 610 +  
            ['i'] * 700 + ['j'] * 15 + ['k'] * 77 + ['l'] * 400 +  
            ['m'] * 240 + ['n'] * 670 + ['o'] * 750 + ['p'] * 190 +  
            ['q'] * 9 + ['r'] * 600 + ['s'] * 630 + ['t'] * 910 +  
            ['u'] * 280 + ['v'] * 98 + ['w'] * 240 + ['y'] * 200 + ['z'] * 7  
        )  
        random.shuffle(self.letter_list)  
        self.len_list = len(self.letter_list)  
        return
  
    def make_word(self, num_letters):  
        """Generate a random word of specified length."""  
        mod = 'monkey:makeWord: '  
        word = ''.join(random.choice(self.letter_list) for _ in range(num_letters))  
        return word  
  
    def run(self):  
        """Main method to execute the monkey simulation."""  
        mod = "monkey:makeList: "  
        os.system('clear')  
        start_time = datetime.datetime.now()  
    
        self.make_list()    
        with open("rawText.txt", 'w') as raw:  
            for _ in range(self.max_words):  
                word = self.make_word(random.randrange(1, self.max_len))  
                raw.write(word + '\n')  
  
        with open("rawText.txt", 'r') as raw, open("filterText.txt", 'w') as filtered:  
            lines = raw.readlines()  
            for line in lines:  
                word = line.strip()  
                if len(word) > 2 or word in self.word_list:  
                    if self.dict_real.check(word):  
                        filtered.write(word + '\n')  
  
        print('Monkeys are tired.')  
        print("Trials are ", self.max_words)  
        print('ended   ', datetime.datetime.now())  
        print('started ', start_time)  
        print('Results in filterText.txt')  

###### Main 
# Example of how to use the class  
if __name__ == "__main__":  
    mod = "c_monkey:main: "  
    simulator = MonkeySimulator()  
    simulator.run()  
