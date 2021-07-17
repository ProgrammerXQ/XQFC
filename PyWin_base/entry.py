def user(os):
  while True:
    username = input(f"New {os} username: ")
    if username == input(f"Confirm {os} username: "):
      import getpass
      password = getpass.unix_getpass("New Password: ")
      if password == getpass.unix_getpass("Confrim Password: "):
        import os
        if os.path.exists(f"/users/{username}.user"):
          os.remove(f"users/{username}.user")
        os.mkdir(f"users/{username}")
        f = open(f"users/{username}.user", "ab")
        import base64
        f.write(base64.b64encode(password.encode("utf-8")))
        break
      else:
        print("Passwords don't match")