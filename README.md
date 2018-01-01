# Air Hockey

[![Join the chat at https://gitter.im/AirHockey55/Lobby](https://badges.gitter.im/AirHockey55/Lobby.svg)](https://gitter.im/AirHockey55/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg "Made with Python")

## About Air Hockey
This is a two player game. There are two paddles and a puck. The left-paddle (Player 1) can be moved using WASD keys and the right-paddle (Player 2)can be moved by the arrow keys. The puck hits the upper and lower boundaries and gets reflected and if it goes inside the goal, it is point for the other one.

## Screenshots

>StartScreen
![StartScreen](/assets/Shot1.png)

>Gameplay
![Gameplay](/assets/Shot2.png)

>PauseScreen
![PauseScreen](/assets/Shot3.png)

>EndScreen
![EndScreen](/assets/Shot4.png)


P.S. The game has a branch `powerup_unstable` which contains powerups which appear randomly in the game and gives advantage to a player over the other.

## Prerequisite

Python2 is the default language needed for playing this game,to check which version of Python you have, type the following in terminal:
```
python --version
```

For more info, visit [Pygame download page](http://www.pygame.org/download.shtml)

## Run


### Linux

Run the AirHockey executable present in `linux-build/dist/AirHockey/AirHockey`
or `python2 main.py` while you are in the AirHockey directory

### Clone the repository.

1. Create the branch on your local machine and switch in this branch :
```
git branch [name_of_your_new_branch]
git checkout [name_of_your_branch]
```
2. Open the directory, open properties for "Install_Dependencies.desktop", toggle "Allow executing file as program" and launch it. This is only required for the first time launch.

NOTE: The administrative permission is required to place the AHlogo.png file into the usr/share/icons directory and install the pygame module.

3. Open properties for run.desktop, toggle "Allow executing file as program" and click Play.

## GamePlay Help

1. Click on player 1 or player 2 to enter name.

2. Choose each player's paddle color at the title screen.

3. To start playing, click on the difficulty level.

4. Each game comprises of three rounds, and the player who wins two (or more) rounds is the winner.

5. During playtime, game can be paused anytime by pressing SpaceBar or clicking the pause icon on the screen.


Enjoy The Game!
