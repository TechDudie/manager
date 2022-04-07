import random
import sys
import os
import time
usage = "Usage: main.py [name] [file] [length]|load [file]"
def clear():
  os.system("clear")
def longest(arr): 
  count = 0
  for i in arr:
    if len(i) > count:
      count = len(i)
      string = i
  return string
def form(key, value, name, values):
  return ("| {:<" + str(name) + "} | {:<" + str(values) + "} |").format(key, value)
def table(table):
  names = list(table.keys())
  name = len(longest(names))
  values = list(table.values())
  value = len(longest(values))
  if name < 4:
    name = 4
  if value < 8:
    value = 8
  print("+" + "-" * (name + 2) + "+" + "-" * (value + 2) + "+")
  print(form("Name", "Password", name, value))
  print("+" + "-" * (name + 2) + "+" + "-" * (value + 2) + "+")
  x = 0
  for pwd in values:
    print(form(names[x], pwd, name, value)) 
    x += 1
  print("+" + "-" * (name + 2) + "+" + "-" * (value + 2) + "+")
load = False
try:
  name = sys.argv[1]
  file = sys.argv[2]
  length = int(sys.argv[3])
except:
  load = False
  if sys.argv[1] == "load":
    load = True
    try:
      file = sys.argv[2]
    except:
      print(usage)
      exit()
  if not load:
    print(usage)
    exit();
if not load:
  string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789@#$&*()'\"%-+/;:,._^[]{}|~\<>!?"
  password = "".join(random.sample(string, length))
  print("Password: {}\nStored as {} in {}\nWill be cleared in 3 seconds.".format(password, file, name))
  time.sleep(3)
  clear()
  try:
    file_h = open(file, "a")
    file_h.write("{}={}".format(name, password))
    file_h.close()
  except:
    print(usage)
    print("File not found. Aborting...")
    exit()
else:
  try:
    file_h = open(file)
  except:
    print("So you want me to read something that doesn't exist?")
    exit()
  cont = file_h.read()
  cont_arr = cont.split("\n")
  passdict = {}
  for i in cont_arr:
    try:
      passdict[i.split("=")[0]] = i.split("=")[1]
    except:
      print("Invalid file format. Did you make this file yourself?")
      exit()
  table(passdict)
