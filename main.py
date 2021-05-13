from ck12func import *
import os

list_of_txt = []
test = os.getcwd()
for file in os.listdir(test):
    if file.endswith(".txt"):
        list_of_txt.append(file)

for item in list_of_txt:
    readTxt(item,0)
