## Day 1 - Assignment; # Exercise 20.8
# Q 3 

# Alice in Wonderland
import pandas as pd
from urllib2 import urlopen


aliceTxt = urlopen('http://www.gutenberg.org/cache/epub/11/pg11.txt').read()
aliceTxtLines = str(aliceTxt.split("\n"))
aliceTxtLower = aliceTxtLines.lower()
aliceTxtLower = aliceTxtLower.replace('"', '')
aliceTxtLower = aliceTxtLower.replace("'", "")
aliceTxtLower = aliceTxtLower.replace(']', '')
aliceTxtLower = aliceTxtLower.replace('(', '')
aliceTxtLower = aliceTxtLower.replace(')', '')
aliceTxtLower = aliceTxtLower.replace('#', '')
aliceTxtLower = aliceTxtLower.replace('$', '')
aliceTxtLower = aliceTxtLower.replace('-', '')
aliceTxtLower = aliceTxtLower.replace('--', '')
aliceTxtLower = aliceTxtLower.replace(',', '')
aliceTxtLower = aliceTxtLower.replace('.', '')
aliceTxtLower = aliceTxtLower.replace('!', '')
wordList = {}
for word in aliceTxtLower.split():
    if word not in wordList:
        wordList[word] = 1
    else:
        wordList[word] += 1
print wordList
alice_df = pd.DataFrame(wordList.items(), columns = ['Word', 'Count'])
alice_df = alice_df.sort("Word")
print(alice_df)
# Write to file
alice_df.to_csv('C:\\Users\\Z062892\\Desktop\\Diwali\\Training\\UCBerkeley\\Day1 - Aug 29\\alice_words.csv', 
                header = None, index = None, sep = ',', mode = 'a')

# How many times does the word "alice" occur in the book
print("The word alice occurs : " + str(wordList['alice']) + " times in the whole book")   # 313 times

# What is the longest word in Alice in Wonderland? How many characters does it have?
alice_df.Word[alice_df.Word.str.len() == alice_df.Word.str.len().max()]  # importantunimportantunimportantimportant
alice_df.Word.str.len().max() # length is 40
