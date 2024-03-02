# Tic-Tac-Toe Bot
Assignment for an Artificial Intelligence course. Comprises of 4 bots:
- A simple bot that plays random moves every single time.
- A slightly more complicated bot that checks if there is a winning move and plays it; otherwise, it plays a random move.
- An even more complicated bot that check if there is a winning move, then checks if the other player has a winning move (and blocks if there exists such a move), or plays a random move if the other two conditions are not satisfied.
- A bot which is uses the minimax algorithm to decide what the best move for each turn is.

The interface for the game has been created using [pygame](https://www.pygame.org/docs/). All of the code for the bots is present in the bot.py file, the UI in the main.py file, the player in the player.py file and the board in the board.py file.

## Usage (only tested for Linux):
Clone the repo locally:

	git clone https://github.com/thetrashed/tic-tac-toe.git

Create a virtual environement (recommended) in the clone repo, for example using `virtualenv`:

	virtualenv ./.venv
	
Activate the virtual environment by doing the following:

	source ./.venv/bin/activate
	
Install the required libraries:

	pip install -r requirements.txt
	
Run the program:

	python src/main.py

## References
These resources helped me along the way:
- Tutorial: https://thesharperdev.com/coding-the-perfect-tic-tac-toe-bot/
- Finding the indices of a certain value in a 2d array: https://stackoverflow.com/questions/27175400/
- Mouse detection in pygame: https://stackoverflow.com/questions/10990137/
- Making a grid in pygame: https://stackoverflow.com/questions/33963361/
- Pygame documentation: https://www.pygame.org/docs/
