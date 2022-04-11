import sys
from subprocess import *
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

ssh = ["ssh", host]
handle = Popen(ssh, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
handle.communicate(input=password)[0]
