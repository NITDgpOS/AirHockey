# Air Hockey

## About Air Hockey
This is a two player game. There are two paddles and a puck. The left-paddle (Player 1) can be moved using WASD keys and the right-paddle (Player 2) can be moved by the arrow keys. The puck hits the upper and lower boundaries and gets reflected and if it goes past the paddle, it is point for the other one.

## Screenshots

>StartScreen
![StartScreen](/img/Shot1.png)

>Gameplay
![Gameplay](/img/Shot2.png)

## Prerequisite

Python2 is the default language needed for playing this game,to check which version of Python you have, type the following in terminal:
```
python --version
```
## Installing Pygame

```
sudo apt-get install python-pip
pip install --upgrade pip
```
```
pip install pygame
```
If this does not work, then
```
sudo -H pip install pygame
```

For more info, visit [Pygame download page](http://www.pygame.org/download.shtml)

## Run

### Linux

Run the AirHockey executable present in linux-build/dist/AirHockey/AirHockey

### Clone the repository.

2. Create the branch on your local machine and switch in this branch :
```
git branch [name_of_your_new_branch]
git checkout [name_of_your_branch]
```
3. Open the directory, open properties for "set_icon.desktop", toggle "Allow executing file as program" and launch it. This is only required for the first time launch.

NOTE: The administrative permission is required to place the AHlogo.png file into the usr/share/icons directory.

4. Open properties for run.desktop, toggle "Allow executing file as program" and click Play.

## Enjoy The Game
