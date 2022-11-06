#!/bin/python3

punct_list = [",", ".", "!", "?"]
line = input()
for c in punct_list:
    new_line = line.replace(c, "")
    line = new_line
print(line.lower())
