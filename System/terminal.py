def runas(username, password):
  from colors import color
  import os
  print(color(f"Logged in as {username}.", "green"))
  global sudo
  sudo = False
  try:
    if path != "yep":pass
  except:
    path = f"users/{username}/"
  def run(text):
    sudo = False
    if os.path.exists("System/boot/sudo.bool"):
      sudo = True
    args = text.split()
    try:
      command = args[0].lower()
    except: command = "none"
    args.pop(0)
    if command == "power":
      if not sudo:
        print(color("Error: Attempted to run admin command, Are you root?", "red"))
      else:
        if args[0] == "shutdown":
          try:
            import time
            time.sleep(int(args[1]))
          except: pass
          exit(8)
        elif args[0] == "restart":
          print("Failed to restart")
    elif command == "clear":
      os.system("clear")
    elif command == "term":
      out = ""
      for i in range(len(args)):
        if i == 0:
          out = args[i]
        else:
          out += " " + args[i]
      os.system(out)
    elif command == "none":
      pass
    elif command == "sudo":
      import getpass
      if getpass.unix_getpass("Sudo password: ") == password.decode("utf-8"):
        out = ""
        for i in range(len(args)):
          if i == 0:
            out = args[i]
          else:
            out += " " + args[i]
        if os.path.exists("System/boot/sudo.bool"):
          os.remove("System/boot/sudo.bool")
        open("System/boot/sudo.bool", "x")
        run(out)
    elif command == "usermod":
      if not sudo:
        print(color("Error: Attempt to run an admin command, Are you root?"))
      else:
        if args[0] == "autologin":
          open("users/autologin.txt", "a").write(f"\n{args[2]}")
        elif command == "rm-autologin":
          f = open("users/autologin.txt", "a")
          lines = f.readlines()
          f.close()

          f = open("users/autologin.txt", "w")
          for line in lines:
            if line.strip("\n") != args[1]:
              f.write(line)
    elif command == "echo":
      i = 0
      out = 0
      for c in args:
        if i == 0:
          out = args[i]
        else:
          out += " " + args[i]
        i += 1
      print(out)
    elif command == "mkdir":
      os.mkdir(path + "/" + args[0])
    elif command == "ls" or command == "dir":
      print(os.listdir(path))
    elif command == "cd":
      out = ""
      if args[0][0] == "/":
        path = args[0]
      elif args[0] == "..":
        for p in range(len(path.split("/"))):
          if p == 0:
            path = path.split("/")[p]
          elif p < len(path.split("/")):
            path += "/" + path.split("/")[p]
      path = out
    else:
      print(color(f"Error: command '{command}' not found.", "red"))
    sudo = False
  while True:
    raw = input(f"{path} >>>")
    if "&" in raw:
      for command in raw.split("&"):
        run(command)
    else:
      run(raw)