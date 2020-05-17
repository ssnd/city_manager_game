# A small city manager game.

## Description

Welcome to the City Manager Game! 
In this game you can create new buildings, roads and earn money 
from the things you have built. 
Every 5 seconds you will earn money from your belongings. 
You can build new things using the money you earn. 
Have fun! 


## Installation
:exclamation: **Prerequisites**: python 3.6 and pip.  
To install the game, please run
`./build.sh`

## Run
Use this command to run the game:  
`./game.py`


## :memo: Notes on the game architecture and the design patterns used.
The game has two main scenes available. The scenes are managed 
by the `GameManager` class. The welcome screen scene displays 
a message describing the gameplay. The `GameManager` also initializes
the `Mouse` and `GameSaver` classes that are responsible
 for controlling the mouse clicks and reading, writing and saving
  the game state to a 
 .pickle file respectively. 
 
The `Mouse` has two dfferent states: `FreeMoving` and `BuildingBlocks`.
When a tile on `ControlPanel` is selected, the state is changed
from `FreeMoving` to `BuildingBlocks`  until a block is built on the 
`TileGrid`. After that, the `Mouse` state is changed back to the 
`FreeMoving` state.
 
The initialized instances of the 
`Mouse` and `GameSaver` classes are then passed to all the other classes 
needing them.

The main game scene is managed by the `GameRenderer` class.
It initializes the `Wallet`, `TileGrid`, `ControlPanel` 
and `ScheduledEventsHandler` classes.  
- The `Wallet` manages the money available. There are methods for 
spending and adding money as well as a property 
to return the amount of money available.  
- The `TileGrid` is basically a map displaying the built tiles.
It is built using the builder pattern to be able to build 
tiles of different sizes and types efficiently. The `BlockBuilder` and 
`BlockDirector` classes are available in the `builders/` folder.
- The `ControlPanel` displays the tiles available to be built and,
when some tile is selected, it can be then built on the `TileGrid`.
The `ControlPanel` also displays the money available and a Reset 
Button to clear the `TileGrid`.
- Once in 5 seconds, a custom user event is fired that is adding 
the income to the user's wallet based on the things he has built. 
The `ScheduledEventsHandler` is responsible for this behaviour.
