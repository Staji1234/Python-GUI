import re

filename = input("Enter your file name(.txt format) :") + ".txt"
p = input("Enter the word you want to search : ")
with open(filename, 'r') as f:
  lines = f.read()
  
  print(lines)
  print("\n *********Output********\n")
  for line in lines.split("."):
        if re.match("(.*\s)"+p+"(\s.*)", line, re.DOTALL):
            print(line+".")
     


    
