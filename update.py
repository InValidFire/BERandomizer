import subprocess, sys, time
print("Starting update script")
try:
    subprocess.run('git pull',shell=True)
    subprocess.run('git checkout origin/master .',shell=True)
    print("Update Complete! Restarting!")
    time.sleep(3)
    subprocess.run('cls',shell=True)
    subprocess.run(['python','start.py'],shell=True)
    sys.exit()
except:
    print("Update failed. Try downloading manually. :c")