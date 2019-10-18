---
YamlDesc: CONTENT-ARTICLE
Title: Python Execute OS Commands
MetaDescription: Python Execute OS Commands,subprocess example code, tutorials
MetaKeywords: python functions, function with parameters, function with return value example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: os-commands
---

# Python Execute OS Command
* Python provides ways to execute OS commands
* Using "OS" Module "system" function
* Using the "subprocess.call"

## OS Module
### Using os.system 
# Executing OS command using the OS Module  
```
import os
# String to store the OS command
OScommand = "echo Tinitiate.com"

# Run the OS command using system function
os.system(OScommand)
```


## SubProcess Module
### Using subprocess.call
* The OS Command is passed as a list, with an argument shell=true,
```
# Executing OS command SubProcess Module
import subprocess
subprocess.call(['echo','Hello Tinitiate'], shell=True)
```

### Using subprocess.Popen
* The **Popen** function can be used to capture the Standard Error 
  and Standard output.
```
# Capture Standard Out and Standard Error in SDOut and SDErr variables
(SDOut,SDErr) = subprocess.Popen(['echo','Hello World!'],stdout=subprocess.PIPE, shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)
# Intentionally Generate Error, Attempt to view a file that dons not exist
(SDOut,SDErr) = subprocess.Popen(['cat','Hello World!.txt'],stdout=subprocess.PIPE, shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)
```

### Check Return Code with subprocess.Popen to 
```
command = subprocess.Popen('echo', shell=True)
command.wait()
print(command.returncode)
```