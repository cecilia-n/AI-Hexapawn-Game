import copy


"""
Returns the next best move, according to  Minimax function. Arguments include: board, which is a list of strings, boardSize which is size of the board, pawnColor, which is either black or white and movesAhead, how far our Minimax function can search to be best goal
"""
def hexapawn(board, boardSize, pawnColor, movesAhead):
  
  print("Board (as input):", board)
  board = listOfStringsToBoard(board,pawnColor) #change to Board, then at end list of strings
  print("Board (after transform):", board)
  best_score, best_board = miniMax(board, depth = 0, max_depth = movesAhead) #dictionary of pawnColor's best moves
  print("Best Score:", best_score)
  print("Best Board:")
  printBoard(best_board)

  return boardToListOfStrings(best_board) 
  

"""
Gets the list of strings representation of board and returns a representation of the board as a dictionary. Arguments include: listOfStrings, which is the original board representation of the board as a list of strings, and color, which is either black or white
"""
def listOfStringsToBoard(listOfStrings, color):
  board = {"w": [], "b": []}
  for rowIndex in range(len(listOfStrings)):
    # print("Row Index:", rowIndex)
    rowString = listOfStrings[rowIndex]
    # print("Row String:", rowString)
    for columnIndex in range(len(rowString)):
      piece = rowString[columnIndex]
      location = {"row":rowIndex, "column": columnIndex}
      if piece == "w":
        board["w"].append(location)
      if piece == "b":
        board["b"].append(location)
  board["size"] = rowIndex + 1
  board["turn"] = color #current turns color
      
  return board

"""Returns the best score and best board of either black or white (depending on turn) chosen by the miniMax search Algorithm. Board is represented as a dictionary, from the starting board, depth of search starts at 0 and the max depth is 5
"""
def miniMax(board, depth = 0, max_depth = 5):
  nextMovesOfPieces = getMovesOfPieces(board) #copy of board where move has happened
  #look at possible moves (moves you can do)
  movedBoardScores = []
  for movedBoard in nextMovesOfPieces:
    #pick best score
    #to get scores use board eval for each board
    score = boardEval(movedBoard) #if it's at max depth or at 10 or -10
    winner = getWinner(movedBoard)
    # if there's not a win
    if winner == "No Winner":
      # do minimax algorithmn until max depth
      if depth < max_depth:
        scored, _ = miniMax(movedBoard, depth = depth + 1, max_depth = max_depth)
        #If minimax run, better than boardEval, used
    movedBoardScores.append((score, movedBoard)) #want list of scores and board together
  # print("Moved Board List:", movedBoardScores)
  #Pick best score
  movedBoardScores.sort(key = lambda x:x[0]) #for each tuple, value in this list, we just want to pay attention to score, beggining of tuple
  if board["turn"] == "b":
    # the lowest score in all of nextMovesOfPieces (i.e. in all of
    # movedBoardScores)
    bestScore  = movedBoardScores[0]
    return bestScore
  if board["turn"] == "w":
    # the highest score in all of nextMovesOfPieces (i.e. in all of
    # movedBoardScores)
    bestScore  = movedBoardScores[-1]
    return bestScore
  
        

# starts at new starting point where not a win
#pick best score for the player's turns
  #white wants max, black wants minimizing
#at end, out of recursive, just static board 
# black wants negative numbers, white wants positive numbers
#general movements, one space at a time, one ahead if empty, diagonal if another pawn (opponents pawn)
#white pawns always start at top of the board, and the black pawns always start at the bottom of the board

"""
Given location on board, function tells what piece is on board (w,b, or -). Location would be the the row and column and the board would be represented as a dictionary.
"""
def lookAtLocation(location,
                   board):  #given location, what piece it is (w, b, or hyphen)
    # print(location)
    # print(board)
    whitePieces = board["w"]
    #print("White Pieces:", whitePieces)
    for piece in whitePieces:  #is location in white pieces?
        if piece == location:
            return "w"
    blackPieces = board["b"]
    for piece in blackPieces:
        if piece == location:
            return "b"
    if piece != "b" and "w":  #if don't find in either list, then "-"
        return "-"
  
#   # iterate through the list of strings
#   # look at each element (row string)
#   # in each element, iterate through that string
#   # that can tell us where the 'w' and 'b's are
#   # (and where the empty spaces are)
#   print(listOfStrings)
"""
Given a board represented as a dictionary, return the original board represented as a list of strings. The argument board is the board represented as a dictionary.
"""
def boardToListOfStrings(board):
    listOfStrings = []
    for rowIndex in range(board["size"]):  #since board size number
        rowString = ""
        for columnIndex in range(
                board["size"]):  #go through column, add to rowString
            location = {"row": rowIndex, "column": columnIndex}
            piece = lookAtLocation(location, board)
            rowString += piece
        listOfStrings.append(rowString)  #append rowstring to every row
    return listOfStrings

    #print(board["size"])

"""
  Given a board, says who the winner is: "b", "w", or "No Winner"
"""
def getWinner(board):
  whitePieces = board["w"]
  blackPieces = board["b"]
  #A player's pawn has advanced to the other end of the board.
    #black at row 0 
    #white at board["size"]
  for blackPiece in blackPieces:
    # print("blackPiece:", blackPiece)
    if blackPiece["row"] == 0:
      return "b"
  for whitePiece in whitePieces:
    if whitePiece["row"] == board["size"]-1: #since rows one less than size
      return "w"

  # The opponent has no pawns remaining on the board.
    #len(whitePieces) == 0, black won
    #len(blackPieces) == 0, white won
  if len(whitePieces) == 0:
    return "b"
  if len(blackPieces) == 0:
    return "w"
    
  # It is the opponent's turn to move a pawn but is unable to do so
    #A pawn may be moved one square forward to an empty square
      #check each piece, black, look row-1 if dash
      #similar for white, row + 1 if theres a dash
  allBlackPiecesStill = True
  for blackPiece in blackPieces: #if all black pieces don't move, then white wins
    # print("Black Piece:", blackPiece)
    currColumn = blackPiece["column"] 
    currRow = blackPiece["row"] -1
    lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
    if lookUpDash == "-":
      allBlackPiecesStill = False

    # print("Black Piece:", blackPiece)
    currColumn = blackPiece["column"] + 1
    currRow = blackPiece["row"] -1
    lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
    if lookUpDash == "w":
      allBlackPiecesStill = False

    currColumn1 = blackPiece["column"] - 1
    currRow1 = blackPiece["row"] -1
    lookUpDash = lookAtLocation({"row":currRow1, "column":currColumn1}, board)
    if lookUpDash == "w":
      allBlackPiecesStill = False
  #if black can't move and blacks turn!     
  if allBlackPiecesStill == True and board["turn"] == "b":
    return "w" #check all pieces before say winner
    #  A pawn may be moved one square diagonally forward to a square occupied by an opponent's pawn. The opponent's pawn is then removed.
      #For black, next column, row-1 or last column, row-1
        #check if there's a white piece 
  allWhitePiecesStill = True
  for whitePiece in whitePieces: #if all black pieces don't move, then white wins
    # print("White Piece:", whitePiece)
    currColumn = whitePiece["column"] 
    currRow = whitePiece["row"] + 1
    lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
    if lookUpDash == "-":
      allWhitePiecesStill = False

    # print("White Piece:", whitePiece)
    currColumn = whitePiece["column"] - 1
    currRow = whitePiece["row"] + 1
    lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
    if lookUpDash == "b":
      allWhitePiecesStill = False

    currColumn1 = blackPiece["column"] + 1
    currRow1 = blackPiece["row"] + 1
    lookUpDash = lookAtLocation({"row":currRow1, "column":currColumn1}, board)
    if lookUpDash == "b":
      allWhitePiecesStill = False
      
  if allWhitePiecesStill == True and board["turn"] == "w":
    return "b"
  
  return "No Winner"

"""
 Given a certain color (black or white), movements can be done on the board
"""
def movePiece(color, dir, pieceIndex, board):
  #make new board with piece in new location, if don't, movements do movements on new board with another movement already made before instead of original

  newBoard = copy.deepcopy(board) #don't want the original board to change

  # print("original board state:")
  # printBoard(board)

  if color == "b":
    # print("the color piece that we're moving is black")
    newBoard["turn"] = "w"
    if dir == "up":
      newBoard[color][pieceIndex]["row"] -= 1 
    if dir == "diag_right":
      newBoard[color][pieceIndex]["row"] -= 1 
      newBoard[color][pieceIndex]["column"] += 1 

      currRow = newBoard[color][pieceIndex]["row"]
      currColumn = newBoard[color][pieceIndex]["column"]
      # print("direction is diag_right")
      newBoard = removePiece("w", {"row":currRow, "column": currColumn}, newBoard)

    if dir == "diag_left":
      newBoard[color][pieceIndex]["row"] -= 1 
      newBoard[color][pieceIndex]["column"] -= 1 

      currRow = newBoard[color][pieceIndex]["row"]
      currColumn = newBoard[color][pieceIndex]["column"]
      # print("direction is diag_left")
      newBoard = removePiece("w", {"row":currRow, "column": currColumn}, newBoard)
      

  if color == "w":
    # print("the color piece that we're moving is white")
    newBoard["turn"] = "b"
    if dir == "down":
      newBoard[color][pieceIndex]["row"] += 1 
    if dir == "diag_right":
      newBoard[color][pieceIndex]["row"] += 1 
      newBoard[color][pieceIndex]["column"] += 1 

      currRow = newBoard[color][pieceIndex]["row"]
      currColumn = newBoard[color][pieceIndex]["column"]
      
      newBoard = removePiece("b", {"row":currRow, "column": currColumn}, newBoard)

    if dir == "diag_left":
      newBoard[color][pieceIndex]["row"] += 1 
      newBoard[color][pieceIndex]["column"] -= 1

      currRow = newBoard[color][pieceIndex]["row"]
      currColumn = newBoard[color][pieceIndex]["column"]
      newBoard = removePiece("b", {"row":currRow, "column": currColumn}, newBoard)
  return newBoard

"""
Given color and location of pawn piece, remove the piece from the board
"""
def removePiece(color, location, board):
  # print()
  # print("color:", color)
  # print("location:", location)
  # print()
  # printBoard(board)
  # print()
  # whitePieces = board["w"]
  # print("whitePieces:", whitePieces)
  newBoard = copy.deepcopy(board)
  # printBoard(board)
  # print()
  # print(newBoard)
  # print()
  # print(location)
  # print(color)
  newBoard[color].remove(location)
  return newBoard

"""
Returns each possible move of each piece in a list called NextMoves
"""
def getMovesOfPieces(board): 
  nextMoves = []
  whitePieces = board["w"]
  blackPieces = board["b"]
  #similar to get winner
  #black and white are able to go up one square or diagonally
  #Use look at location since we have a board?
  #do we use parts of getWinner since some pieces can't move since blocked?
  if board["turn"] == "b":
    for blackPieceIndex in range(len(blackPieces)): #get numbers/index while looping to keep track of pieces/ update easier
      blackPiece = blackPieces[blackPieceIndex]
      # print("Black Piece:", blackPiece)
      currColumn = blackPiece["column"] 
      currRow = blackPiece["row"] -1
      lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
      if lookUpDash == "-":
        nextMoves.append(movePiece("b", "up", blackPieceIndex, board))
        #replace "-" with "b"

      currColumn = blackPiece["column"] + 1
      currRow = blackPiece["row"] -1
      # print("column", currColumn)
      # print("row", currRow)
      lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
      if lookUpDash == "w":
        nextMoves.append(movePiece("b", "diag_right", blackPieceIndex, board))
        # print("Next Moves Black (Diag_Right):", nextMoves)
        

      currColumn1 = blackPiece["column"] - 1
      currRow1 = blackPiece["row"] -1
      lookUpDash = lookAtLocation({"row":currRow1, "column":currColumn1}, board)
      if lookUpDash == "w":
          #change piece location
          nextMoves.append(movePiece("b", "diag_left", blackPieceIndex, board))

  if board["turn"] == "w":
    for whitePieceIndex in range(len(whitePieces)):
      whitePiece = whitePieces[whitePieceIndex] 
      currColumn = whitePiece["column"] 
      currRow = whitePiece["row"] + 1
      lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
      if lookUpDash == "-":
        #change location
        nextMoves.append(movePiece("w", "down", whitePieceIndex, board))

      currColumn = whitePiece["column"] - 1
      currRow = whitePiece["row"] + 1
      lookUpDash = lookAtLocation({"row":currRow, "column":currColumn}, board)
      if lookUpDash == "b":
          #change location
        nextMoves.append(movePiece("w", "diag_left", whitePieceIndex, board))

      currColumn1 = whitePiece["column"] + 1
      currRow1 = whitePiece["row"] + 1
      lookUpDash = lookAtLocation({"row":currRow1, "column":currColumn1}, board)
      if lookUpDash == "b":
          nextMoves.append(movePiece("w", "diag_right", whitePieceIndex, board))
  return nextMoves      
    
    


# {
#   "size": 3,
#   "w": [
#     {"row": 0, "column": 0},
#     {"row": 0, "column": 1},
#     {"row": 0, "column": 2}
#   ],
#   "b": [
#     {"row": 2, "column": 0},
#     {"row": 2, "column": 1},
#     {"row": 2, "column": 2}
#   ]
# }
#


# www
# ---
# bbb
"""
Prints board in a more visual format
"""
def printBoard(board):
    #convert list of strings
    #print out string
    listOfStrings = boardToListOfStrings(board)
    for string in listOfStrings:
        print(string)

"""
For a particular color,  pieces of
that color that have a clear path ahead of them to the
end of the board are counted
"""
def clearPath(color, board):

  #if dash in front, then count the clear paths
  #clear path until another piece or end of board
  pieces = board[color]
  # print("Color Pieces:", pieces)
  clearPathCount = 0
  if color == "w":
    #look down board
    for piece in pieces: 
      allSpacesEmpty = True
      #for each piece, all pieces ahead empty

      #also want to keep checking spaces ahead
      #want to update pathinFront until the end of board
      # print("piece:", piece) #repeated over and over
      row = piece["row"]
      # print("Row:", row)
      column = piece["column"]
      # print("Column", column)

      for rowIndex in range(row+1, board["size"]):
        pathinFront = {"row": rowIndex, "column": column} #still want row and column key
        # print("Path in Front", pathinFront)
        pieceinFront = lookAtLocation(pathinFront, board)
        # print("Piece in Front:", pieceinFront)
        if pieceinFront != "-":
          allSpacesEmpty = False
          # we want to keep track of each piece that there's an empty space ahead
      if allSpacesEmpty == True: #outside for loop since we just want to count each piece
          clearPathCount += 1  #update clearPathCount values
            #incerament when white piece has clear path to the end of the end of the board instead of incrementing when there's a dash in the front
            # print("Clear Path Count:", clearPathCount)
    return clearPathCount  #finishes for loop then returns whole thing

    #in front of white
  if color == "b":
    #look up board
    for piece in pieces: 
      allSpacesEmpty = True
      #for each piece, all pieces ahead empty

      #also want to keep checking spaces ahead
      #want to update pathinFront until the end of board
      # print("piece:", piece)
      row = piece["row"]
      # print("Row:", row)
      column = piece["column"]
      # print("Column", column)
      
      #want to look at row before, b goes up
      #range function wants lower, then higher (go forwards), but we can change it
      #range arg, start, stop, how far to go in what direction
      #-1 tells it to stop after 0
      for rowIndex in range(row-1, -1, -1):
        pathinFront = {"row": rowIndex, "column": column} #still want row and column key
        # print("Path in Front", pathinFront)
        pieceinFront = lookAtLocation(pathinFront, board)
        # print("Piece in Front:", pieceinFront)
        if pieceinFront != "-":
          allSpacesEmpty = False
          # we want to keep track of each piece that there's an empty space ahead
      if allSpacesEmpty == True: #outside for loop since we just want to count each piece
          clearPathCount += 1  #update clearPathCount values
            #increment when white piece has clear path to the end of the end of the board instead of incrementing when there's a dash in the front
          # print("Clear Path Count:", clearPathCount)
    return clearPathCount
        
#Static Board Eval
# The function returns a +10 if the board is such that white wins.  It returns a -10 if black wins.
# (TIEBREAKER)If neither side has won, the function returns the number of white pawns with clear paths in front of them minus the number of black pawns with clear paths in front of them PLUS the result of counting the number of white pawns on the board and subtracting the number of black pawns.  "Clear path" means that a pawn has no other pawns of either color between it and the opposite end of the board as it moves straight ahead.  "Clear path" does not consider what may be ahead of a pawn on a diagonal.  Assume that your board evaluation function can determine if either player is unable to make a move, without having to extend the search.

"""
Static Board Evaluation
"""
def boardEval(board):
  #if white,
  #count how many white pieces
  #if black,
  #count how many black pieces
  #find length of list of whitePieces and blackPieces
  whitePieces = board["w"]
  # print("White Pieces:", whitePieces)
  blackPieces = board["b"]
  winner = getWinner(board)
  if whitePieces:
    countWhite = len(whitePieces)
  if blackPieces:
    countBlack = len(blackPieces)

  # The function rerurns a +10 if the board is such that white wins.
  if winner == "w":
    return 10
  #It returns a -10 if black wins.
  elif winner == "b": #elif, then condition
    return -10
  # (TIEBREAKER)If neither side has won, the function returns the number of white pawns with clear paths in front of them minus the number of black pawns with clear paths in front of them PLUS the result of counting the number of white pawns on the board and subtracting the number of black pawns.
  else: #else, nothing else to check
    clearPathWhite = clearPath("w", board)
    # print("Clear Path White:", clearPathWhite)
    clearPathBlack = clearPath("b", board)

    tieValue = clearPathWhite - clearPathBlack 
    tieValue = (
      tieValue +
      (len(whitePieces) - len(blackPieces))
    )
    # print("Tie Value:", tieValue)
    #to see black or white, can find length of whitePieces and blackPieces
    return tieValue  
  

# ======= TEST INPUTS =======
listOfStringsExample = ["www", "---", "bbb"]
boardExample = {
    "size": 3,
    "turn": "w",
    "w": [{
        "row": 0,
        "column": 0
    }, {
        "row": 0,
        "column": 1
    }, {
        "row": 0,
        "column": 2
    }],
    "b": [{
        "row": 2,
        "column": 0
    }, {
        "row": 2,
        "column": 1
    }, {
        "row": 2,
        "column": 2
    }]
}
boardExample2 = listOfStringsToBoard([
  "w-----",
  "-w-w--",
  "---b--",
  "------",
  "-b----",
  "-----b"
], "w")
boardExample3 = listOfStringsToBoard([
  "------",
  "-w-w--",
  "---b--",
  "------",
  "-b----",
  "w----b"
], "w")
boardExample4 = listOfStringsToBoard([
  "------",
  "--ww-b",
  "---b--",
  "------",
  "-b----",
  "w-----"
], "b")
boardExample5 = listOfStringsToBoard([
  "-w-",
  "w-w",
  "b--"
], "w")
boardExample6 = listOfStringsToBoard([
  "---",
  "wbw",
  "b--"
], "w")
boardExample7 = listOfStringsToBoard([
  "---",
  "wb-",
  "b--"
], "w")
boardExample8 = listOfStringsToBoard([
  "-w-",
  "wbw",
  "b-b"
], "b")

# # ======= TEST boardToListOfStrings =======
# print("boardToListOfStrings:", boardToListOfStrings(boardExample))

# #boardexample the value of board

# # ======= TEST listOfStringsToBoard =======

# print(listOfStringsToBoard(listOfStringsExample, 'w'))

# # ======= TEST lookAtLocation =======
# locationExample = {"row": 0, "column": 0}
# print(lookAtLocation(locationExample, boardExample))
# print()

# # this should return 'w'

# locationExample = {"row": 2, "column": 1}
# print(lookAtLocation(locationExample, boardExample))
# print()

# # this should return 'b'

# locationExample = {"row": 1, "column": 2}
# print(lookAtLocation(locationExample, boardExample))
# print()
# # this should return '-'

# locationExample = {"row": 4, "column": 2}
# print(lookAtLocation(locationExample, boardExample))
#returns none

# ======= TEST boardEval =======
# printBoard(boardExample)
# print(boardEval(boardExample))

# printBoard(boardExample2)
# print(boardEval(boardExample2))

# printBoard(boardExample3)
# print(boardEval(boardExample3))

# printBoard(boardExample4)
# print(boardEval(boardExample4))
# print()

# printBoard(boardExample5)
# print(boardEval(boardExample5))
# print()

# printBoard(boardExample6)
# print(boardEval(boardExample6))
# print()

# printBoard(boardExample7)
# print(boardEval(boardExample7))
# print()

# printBoard(boardExample8)
# print(boardEval(boardExample8))

# # ======= TEST printBoard =======
# printBoard(boardExample)

# # ======= TEST clearPath =======
# # print("clearPath for white on board:")
# # printBoard(boardExample)
# # print(clearPath("w", boardExample)) #want to print result, print statements inside run first, then result
# # this should be 0

# #to see clearPath run more clearly, comment print statements inside of def clearPath
# # print(clearPath("w", boardExample2))
# # # should be 1

# print("clearPath for black on board:")
# printBoard(boardExample2)
# print(clearPath("b", boardExample2))
# # # should be 1

# # ======= TEST getWinner =======
# printBoard(boardExample)
# print(getWinner(boardExample))

# printBoard(boardExample3)
# print(getWinner(boardExample3))

# printBoard(boardExample4)
# print(getWinner(boardExample4))

# printBoard(boardExample5)
# print(getWinner(boardExample5))

# printBoard(boardExample6)
# print(getWinner(boardExample6))

# printBoard(boardExample7)
# print(getWinner(boardExample7))

# printBoard(boardExample8)
# print(getWinner(boardExample8))

# # # ======= TEST movePiece =======
# printBoard(boardExample)
# print()
# print("Move Piece:")
# printBoard(movePiece("b", "up", 1, boardExample))
# print()
# newBoard = movePiece("b", "up", 2, boardExample)
# printBoard(newBoard)
# print()
# printBoard(movePiece("b", "diag_left", 2, newBoard))

# # # # ======= TEST getMovesOfPieces =======
# print("Original board:")
# print()
# printBoard(boardExample8)
# print()
# next_moves = getMovesOfPieces(boardExample8)
# print("Next moves:")
# print()
# for next_move in next_moves:
#   printBoard(next_move)
#   print()


# # # # # ======= TEST miniMax =======
# print("input board:")
# printBoard(boardExample)
# best_score1, best_board1 = miniMax(boardExample, depth = 0, max_depth = 10) #return a tuple, can have variable name for each tuple
# print()
# print("best score for white's first move:", best_score1)
# print("\nbest board for white's first move:")
# printBoard(best_board1)
# print()
# print("What should black's next move be?")
# print("Here's the current board state:")
# print(best_board1)
# best_score2, best_board2 = miniMax(best_board1, depth = 0, max_depth = 10) 
# print()
# print("best score for black's first move:", best_score2)
# print("\nbest board for black's first move:")
# printBoard(best_board2)
# print()
# #black does minimax, board is now best_board1 of white


# # # # ======= TEST hexapawn =======
print(hexapawn(["www","---","bbb"],3,'w',2))