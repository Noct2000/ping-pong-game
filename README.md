## 🏓 This is simple ping-pong game for two players
### Description
You have three scenes:
* Start menu
* Playground
* Restart menu

#### Start menu
In the start menu you can choose max score game. 
If you set invalid value or leave it is empty game will be infinite.

#### Playground
In the playground you can play for two players (left player and right player).
For moving right paddle use UP/DOWN arrows.
For moving left paddle use W/S keys.
If you close playground using X button, then winner will be setup according to score.

#### Restart menu
Restart menu consists text about winner and two options: Restart and Exit.
Also, for exit from game you can use X button.

### Technologies
This game wrote on python using pygame

#### Required
* Python 3.7.9
* pygame 2.1.2
* pyinstaller 5.8.0

### How to Run
* clone repository
* go to the project dir
* run `python main.py`

### How to Build into exe
* clone repository
* go to the project dir
* run `./setup.cmd` fow windows and `./setup` for linux.

Your exe-file will be in the `dist/ping-pong-game.exe`