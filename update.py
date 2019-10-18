import subprocess, sys, time
print("Starting update script")
subprocess.run('git checkout origin/master .',shell=True)
subprocess.run('git reset --hard origin/master .',shell=True)
subprocess.run('git pull',shell=True)
print("Update Complete! Restarting!")
time.sleep(3)
subprocess.run('cls',shell=True)
subprocess.run(['python','start.py'],shell=True)