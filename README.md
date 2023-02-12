## 🏓 This is simple ping-pong game for two players
### Description
You have three scenes:
* Start menu
* Play scene
* Restart menu

#### Start menu
In the start menu, you can choose a maximum score for the game. 
If you set an invalid value or leave it empty, the game will have no limit and will be infinite.

#### Play scene
In the play scene you can play for two players (left player and right player).
For moving right paddle use UP/DOWN arrows.
For moving left paddle use W/S keys.
If you close play scene using X button, then winner will be setup according to score.

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