import subprocess, sys
print("Starting update script")
try:
    subprocess.run('git checkout .',shell=True)
    print("Update Complete!")
    subprocess.run(['python','start.py'],shell=True)
    sys.exit()
except:
    print("Update failed. :c")