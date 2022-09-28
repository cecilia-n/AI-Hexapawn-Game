# AI-Hexapawn-Game
Extending the definition of hexapawn to include any similar game 
involving n white pawns, n black pawns, and a n x n board. 

Constructed a Python function (and all supporting functions) which takes as input a representation of 
the state of a hexapawn game (i.e., a board position), an integer representing the size of 
the board, an indication as to which player is to move next, and an integer representing 
the number of moves to look ahead. This function returns as output the best next move 
that the designated player can make from that given board position. The output should be 
represented as a hexapawn board position in the same format that is used for the input 
board position.

My function selected the best next move by using MiniMax search. I used a static board evaluation function.
