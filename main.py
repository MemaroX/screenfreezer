import keyboard  # Import keyboard library for detecting keypress events 
import subprocess  # Import subprocess module for running system commands
import time
while True:
  time.sleep(1)
  if keyboard.is_pressed('x'):
    break
    # Break out of infinite loop when 'X' is pressed
print("PC has been stunned.")
process = subprocess.Popen(["systemctl", "stop", "lightdm"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, error = process.communicate()
if error != b"":
  print(error)
else:
  print("System stopped successfully.")
  #In this example, we use `systemctl` to stop the Light Display Manager (LDM), which is responsible for managing graphical sessions on Linux systems like Ubuntu and Fedora. By stopping LDM, we effectively freeze the system until it is restarted or shut down manually.
