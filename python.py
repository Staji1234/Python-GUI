import re
import webbrowser
import sys
import time
#c = webbrowser.get('Google')
filename = input("Enter your file name(.txt format):") + ".txt"
#input the file name 
p = input("Enter the word you want to search: ")
#input the word you want to search

fo = open('output.html','wb')

with open(filename, 'r') as f:
  lines = f.read()
  #read the file line by line
  print("\n *********Output********\n")
  for line in lines.split("."):
      if (re.match("(?i).*\s"+p+"\s.*", line,re.DOTALL)):
              print(line+".")
              

#webbrowser.open_new_tab('output.html')
#c.open_new_tab('http://docs.python.org')


