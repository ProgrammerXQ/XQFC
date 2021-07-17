def run():
  from colors import color
  print(color("XQFC Online", "green"))
  while True:
    import getpass, os, base64
    if os.path.exists("users/autologin.txt"):
      users = {}
      f = open("users/autologin.txt", "r")
      i = 1
      os.system("clear")
      for user in f.readlines():
        print(color(str(i) + ". " + user, "black", "white"))
        users[i] = user
        i += 1
      print(color("q. login manually", "black", "white"))
      val = input("Autologin user: ")
      if val != "q":
        username = users[int(val)]
        password = base64.b64decode(open(f"users/{username}.user", "r").read())
        os.system("clear")
        break
      else:
        username = input("XQFC Login: ")
        if os.path.exists(f"users/{username}.user"):
          password = getpass.unix_getpass("Password: ")
          truePass = base64.b64decode(open(f"users/{username}.user", "r").read()).decode("utf-8")
        if password == truePass:
          break
    username = input("XQFC Login: ")
    if os.path.exists(f"users/{username}.user"):
      password = getpass.unix_getpass("Password: ")
      truePass = base64.b64decode(open(f"users/{username}.user", "r").read()).decode("utf-8")
      if password == truePass:
        break
  import System.terminal as system
  system.runas(username, password)