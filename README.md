# PythonPingTracker
 Python tools to track ping over a custom amount of time and display the data.

## Installation
 Developed with Python version 3.7.5
 Use ```$pip install -r requirements.txt``` to install dependencies.

## Usage
### Ping
 ```$python pingLogger.py [-h] [-H HOST] [-f FILE]```
 
 Use Ctrl+C to halt pinging and save data to the desired file.

 #### optional arguments:
  
  -H HOST, --host HOST  Alternate host to ping
  
  -f FILE, --file FILE  Log output file
### Display Data
 ```$python displayJsonData.py [-h] -f FILE```

 #### optional arguments:
  -f FILE, --file FILE  Log file to read data from
