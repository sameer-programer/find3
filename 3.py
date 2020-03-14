# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x=int(input("enter a number"))
count=0
while x!=0:
    r=x%10
    if r==3:
        count=count+1
    x=x//10
print(count)
    