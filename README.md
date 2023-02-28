# PyBoard

### What is PyBoard?

PyBoard is a personal project I've wanted to work on for a while: a framework to streamline the development of simple board games using Python.

This project is nothing but a challenge to myself born from my love of programming. However, my hope is that it serves as a fun example of proper software architecture, object oriented design and clean code for anyone interested.

The idea of PyBoard is to provide a set of base classes (some of them abstract) that can lead to fully functional board games with as little programming as possible.

The exact development process is detailed below, but an effort has been made to minimize the work needed to develop a new game. Common methods between games (and when possible full classes) are already developed and are general enough to accommodate any board game inside the scope, while all the game-specific methods have been isolated.

The PyBoard project also includes demos of some games already developed. The demos serve two main purposes:

- On one side, they are examples. The framework can be too abstract without examples of its usage, so these pre-developed games are meant to ease the development of new games.
- On the other side, they are stress tests for the framework. The only way to verify that the design can accommodate any board game inside the scope is to try to develop them.

The third secret reason is that I wanted to develop some games using the framework.

### How does the framework work?

Each game consists of three main classes:

- **Board**: The board is the game itself, it holds a matrix to represent the board status at any given time and methods to update it (which means to make a move) and manage the game logic.
- **Config**: Structured data where the initial parameters of the game are stored.
- **Agent**: An AI of the game to play against.

To develop a new game, one must only extend these classes, fill in the required abstract methods and, if necessary, declare new configuration properties. By looking at the documentation and the available demos it should be intuitive enough how the to-be-implemented methods are meant to perform.

On top of that, the development of a GUI for the game has also been streamlined as part of the project, and the process to do so can be found in the documentation.

### What is the scope of the project?

Tough question. As I said in the beginning, this project is a challenge to myself, so the final goal is that this project is in a state I'm happy with. As such, if I think of some sort of enhancement to the project, I'll add it to my to-do list.

However, there is a scope defined so that this project doesn't get out of hand. The kind of game I want this framework to accommodate is whatever game fits this criteria:

- The game is a board game that can be represented with a matrix of tiles.
- The game is turn based.
- All the players share the same information about the game status (players can't withhold information from other players).

I think that this can lead to a variety of games while restricting the framework enough so that I don't need to define each class so abstract that I might as well not define them.

Aside from the code, the repository itself is also part of the scope of the project. I want everything to be well documented and organized, I haven't worked much with git prior to this project so I want to tackle this part of it as a learning process.

### What is the status of the project?

While the following list is too general and not set in stone, as I will add whatever feature I find useful to it as the project goes on, it should help make a picture of what is already in place, what is planned, and what isn't even considered:

Developing the framework:
- [x] Base Config class implemented
- [x] Base Board class implemented
- [x] Framework design tested by developing a sample game (TicTacToe)
- [x] Base Agent class implemented
- [x] Agent design tested by developing an agent for sample game (TicTacToe)
- [ ] Base GUI element classes defined
- [ ] GUI design tested by developing a GUI for sample game (TicTacToe)


Enhancing the code:
- [x] Error handling implemented
- [ ] Documentation comments written


Repository:
- [x] README file
- [ ] Classes documented in a wiki
- [ ] Class diagrams provided for better understanding of software architecture


Games/demos:
- [ ] TicTacToe
 - [x] Game logic
 - [x] Easy agent
 - [x] Console demo
 - [ ] Agent of all difficulties
 - [ ] GUI demo
- [ ] Chess
 - [ ] Game logic
 - [ ] Easy agent
 - [ ] Console demo
 - [ ] Agent of all difficulties
 - [ ] GUI demo
- [ ] Connect 4
 - [ ] Game logic
 - [ ] Easy agent
 - [ ] Console demo
 - [ ] Agent of all difficulties
 - [ ] GUI demo
- [ ] ...

### That's all!

Just wanted to say thanks if you're this far. This is a passion project and it means much that you showed interest in it. Feedback is always appreciated!
