import sys
import subprocess
host = sys.argv[1]
try:
  print("Connecting to " + host + "using password...")
  password = sys.argv[2]
except:
  print("Password not given. Searching in connections.txt...")
  save = open("connections.txt").read().split("\n")
  for i in save:
    if i.split("=")[0] == host:
      password = i.split("=")[1]
      print("Password found.")
      break
  try:
    password = password
  except:
    print("Password not found. Aborting...")
    exit()
