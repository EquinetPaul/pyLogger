# pyLogger
Simple Python Logger

## How To Use
- Import pyLogs.py in your folder
- Open pyLogs.py and configure it (True or False)
```sh
display_time = True
display_date_time = True
```
- In your Python file you want to get logs, import the lib
```sh
import pyLogs as l
```
- Enjoy!

## Features
- Different type of logs
- Display Date and/or Time

## Parameters
```sh
l("Message to Log", "LogType")
```
#### LogType
- Default (d)
- Succes (s)
- Success2 (s2)
- Warning (w)
- Error (e)
- TITLE (e)

## Exemple
### main.py
```sh
import pyLogs as l

l.l("Default", "d")
l.l("Success!", "s")
l.l("Success 2!", "s2")
l.l("Warning!", "w")
l.l("Error!", "e")
l.l("TITLE", "t")
```
### Result
![result](https://www.zupimages.net/up/22/11/namx.png)

### Why?
Better and more beautiful than a simple print (and with date and color!!!)
### To Do
- Save logs into files (done)
