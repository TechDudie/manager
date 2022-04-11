import sys
import subprocess

def run(host, cmd):
  stdout, stderr = subprocess.Popen(f"ssh {host} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  return [stdout, stderr]

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

while True:
  command = input()
  print(run(host, command)[0])
