# Yarn Ninja

Team: Abiram Nair (anair29), Bardia Attar (battar), Bikramjit Singh (bsingh96), Darryl Lee (dlee688)

---

**Instructions to set up environment and run the game**
The game is built in a python3 environment using pygame for the game controls and features.

The user must ensure that they have PyCharm IDE (Community Edition), pip ( can be downloaded by going to the following link:
https://pip.pypa.io/en/stable/cli/pip_install/), and Python3 installed on their device.
The source code will be submitted as a ZIP file, after unzipping the folder, the user must open the project in pycharm.

The project requires installation of pygame which can be downloaded by:

- Going into the python interpreter settings and installing the package by searching
  or
- python3 -m pip install -U pygame --user (Documentation: https://www.pygame.org/wiki/GettingStarted)

**Once the prerequisites are met, the user can then go ahead and run the Main.py file from the project. This will open a window and the user can begin playing the game.**

**You may also run the Main.exe file to begin playing the game.**

**The entry point in case Main.exe does not work is Main.py if using an IDE.**

---

**Game Controls and Game Play**

The player can use the arrow keys (up,down,left, and right) to navigate the ninja in the desired direction.

Please note, when the ninja is in movement, you cannot stop until you hit a wall or other objects (i.e. gates, buttons).
You cannot change directions mid-movement.

Each movement decrements the "move counter" on the top right of the screen. The player should aim to reach the red block of yarn before
the move counter reaches 0. If the move counter reaches 0, the player has used all their moves, and the game will end. The game will restart at the failed
level.

The game has 6 levels. Once Level 6 is completed, the game will go back to the home screen.

---

Interactable Objects:

Green Portal: Entering a green portal will transport the player to another green portal.
Purple Portal: Entering a purple portal will transport the player to a designated spot on the grid (i.e. not to another purple portal). The
designated spot is constant.

Red/Purple buttons: Hitting one of these buttons will open a gate of the same colour.

Yarn Block: The red yarn block represents the goal. If the player comes in contact with the Yarn Block, the player has successfully completed the level.
A message will be shown on screen to show level completion, and then load the next level shortly after.

---

Enemy:

There are two types of enemies: Horizontal Slimes and Vertical Slimes. These slimes will patrol an area in the maze. If the player comes in
contact with an enemy, the game will end, and the level will reset.
