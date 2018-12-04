# ZPY
### Multiplayer Python Implementation of Chinese Trick Taking Card Game
### Project Description 
**Name: Zhao Peng You (ZPY), English Name: Finding Friends**   
ZPY is an online multiplayer card game where users can play this same-name strategic Chinese Trick Taking game. The card game is similar to Hearts, but with an emphasis on secrecy and creating allies between the “Dictator” team and the “Opposition” team. Each team has their own win-objective and players aim to individual rounds in order to rack up points.

Click for a complete set of [Rules](https://www.zhao-pengyou.com/)   

### How To Install Any Needed Libraries
1. Make sure you have [Python3](https://www.python.org/downloads/) Installed.
2. Download and Unzip the Files
3. All other Libaries (sockets, tkinter, etc...) are already installed and do not need redownload.

### How to Run The Project
1. Open Terminal and cd into the root folder
2. First run the server file:
```
python3 zpy_server.py
```
3. Then, in 4 separate terminal windows, run the client files. Each file represents an individual player:
```
python3 zpy.py
```
4. To exit out of the program, Ctrl+C on Terminal. 
5. To rerun the files, in both the zpy_server.py and zpy.py files, change the PORT numbers to another 5-digit number 0-65535.

NOTE: If running on separate computers, change the HOST value to the IP address of the host computer.

### Shortcut Commands That Exist
No shortcut commands exist at this time.
