import subprocess
#Change path name to include double slashes otherwise Python interprets it as Unicode.
#This opens Teams.
subprocess.Popen('C:\\Users\\Theunis\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"')

#This opens Zoom.
subprocess.Popen("C:\\Users\\Theunis\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

#This opens Chrome and Firefox.
subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

#This opens Outlook.
subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")