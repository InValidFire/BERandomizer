import subprocess, sys, time
print("Starting update script")
try:
    subprocess.run('git checkout origin/update .',shell=True)
    print("Update Complete! Restarting!")
    time.sleep(3)
    subprocess.run(['python start.py'],shell=True)
    sys.exit()
except:
    print("Update failed. Try downloading manually. :c")