def run():
  import os
  if os.path.exists("System/boot/setup.bool"):
    import System.login as sys_login
    sys_login.run()
  else:
    import PyWin_base.entry as pywin_entry
    pywin_entry.user("XQFC")
    open("System/boot/setup.bool", "x")
    run()