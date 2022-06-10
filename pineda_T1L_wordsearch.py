'''
Pineda, Brixter Sien M.
2020-02919
BS CS 
'''
import mysql.connector
import random

#this function will get random set of words from the file
def getRandomWords():
    words = []
    fileHandle = open("WordsToSearch.txt", "r")#open the file which stores the words
    for word in fileHandle: #this loop is to store all the words from the file to a list
        word = word.strip("$\n")
        words.append(word)
    fileHandle.close()

    count = 0
    randomWords = []
    while count < numItems: #numItems is the number of items/words that will be inputted in the gameboard
        randWord = random.choice(words).upper().replace("'", '').split() #get random word
        if randWord[0] not in randomWords: #to prevent a word being selected twice
            randomWords.append(randWord[0])
            count = count + 1

    return randomWords

#function for creating a blank matrix
def createGrid():
    grid = []
    for row in range(numRow):
        column = []
        for col in range(numCol):
            column.extend("_")
        grid.append(column)

    return grid

#Function for Placing the random words on the matrix
def setPosition():
    randWords.clear()
    randWords.extend(getRandomWords())
    grid = createGrid()
    directions = ['vertical', 'horizontal', 'diagonal_down', 'diagonal_up']

    for item in randWords:
        direction = random.choice(directions)
        item_length = len(item)
        findItems.extend(item.split())
        placed = False
        while not placed:
            # the following if statement check what direction was selected
            # then assign the movement in the maxtrix (x,y) that letters from a word will have
            if (direction == 'vertical'):
                x_step = 0
                y_step = 1
            if (direction == 'horizontal'):
                x_step = 1
                y_step = 0
            if (direction == 'diagonal_down'):
                x_step = 1
                y_step = 1
            if (direction == 'diagonal_up'):
                x_step = 1
                y_step = -1

            # assigning the position(x,y) of the first letter of the word
            y_position = random.randrange(numCol)
            x_position = random.randrange(numRow)

            # the following will check if the tiles will be enough for the word, if not the while loop will restart
            if (x_step < 0 and y_position < item_length):
                continue
            if (x_step > 0 and y_position > numCol - item_length):
                continue
            if (y_step < 0 and x_position < item_length):
                continue
            if (y_step > 0 and x_position > numRow - item_length):
                continue

            # current position of the first letter
            current_column = y_position
            current_row = x_position
            fail = False
            for letter in item:
                # check if the the tile is empty or has the same value as the letter to be placed
                if grid[current_row][current_column] == letter or grid[current_row][current_column] == '_':
                    current_row += y_step
                    current_column += x_step
                else:

                    fail = True
                    break

            if not fail: #if fail is false we will now place the letters of the word in the matrix
                #position of the first letter
                current_column = y_position
                current_row = x_position
                for letter in item: #place the letters on the matrix/grid
                    grid[current_row][current_column] = letter
                    current_row += y_step
                    current_column += x_step

                placed = True
    return grid

#function that will fill random letter in each blank tile of the matrix
def fill_letter(grid):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(numRow):
        for col in range(numCol):
            if grid[row][col] == "_":
                randomLetter = random.choice(LETTERS)
                grid[row][col] = randomLetter

#Function that will print tha matrix when called
def printGrid(grid):
    fill_letter(grid);
    for r in range(numRow):
        print( "\t" +  ' '.join(grid[r]))

#function for the Menu
def startMenu():

    while True:
        print("\nSTART MENU:")
        print("\t[1]Start Game")
        print("\t[2]How to play")
        print("\t[3]Exit")
        choice = input("Choice:\t")

        if choice == '1':
            return False #exitGame=False
        elif choice == '2': #Show the instruction
            print("\n\n================INSTRUCTION:==================")
            print("The main goal of this game is to find the five(5) hidden words in the matrix. \nThe 10x10 matrix consist a letter each tile.")
            print("A hidden word may be arranged VERTICALLY, HORIZONTALLY, or DIAGONALLY. \nHere is an example a matrix(5X5) to show the orientation of words:\n")
            print("C A T - -")
            print("- O - - -")
            print("D - W - T")
            print("O - - A -")
            print("G - R - -")

            print("\n\nIf you found a word, choose the option 1 from the menu that will be shown below the matrix."
                  + "\nYou can then type the word that you have found. "
                  + "\nYou will only be given THREE(3) chances to retry if ever you type a wrong word.")

            print("\nTIP: All words are ICT related")
            print("Also if you go back to the START MENU, you CAN'T continue the previous game.")
            print("\n==============================================")

            while True: #Option to go back to Menu
                back = input("\nGo Back (Y):\t")
                if (back.upper() == "Y"): #check if the input is Y
                    print("\n")
                    break
                else:
                    print("Invalid Input\n")
            continue

        elif choice == '3':
            return True #exitGame=True

        else:
            print("Invalid Input\n")
            continue #Options will show again

        break #stop the loop

#Function that will print the options for the game
def inGameMenu():
    print("[1] Type the word I found")
    print("[2] Go back to Menu")
    print("[3] Quit/Exit")
    choice = input("Choice:\t")
    print()
    return choice



findItems =[]
randWords = []
numCol = 10
numRow = 10
numItems = 5

print("\n=======WORDSEARCH GAME=========")
exitGame = startMenu()
print()
while not exitGame:
    print("\nFind the 5 hidden words.....")
    remNumItems = numItems  #remaining number of words that haven't been found
    foundItems = []
    lives = 3  #limit of the number of mistakes
    board = setPosition() #get the matrix
    items = randWords  #list of the hidden words
    newGame = False
    while not newGame:



        printGrid(board) #print matrix
        print()
        choice = inGameMenu()


        if choice == '1': #check if the player chose to type a word from the option
            foundWord = input("Word found:\t")

            if foundWord.upper() in foundItems:
                print("Already found the inputted word")
            elif foundWord.upper() in items:
                remNumItems = remNumItems-1
                foundItems.extend(foundWord.upper().split())
                items.remove(foundWord.upper())
                if remNumItems == 0:  # check if all items are found
                    print("CONGRATS YOU HAVE FOUND ALL THE HIDDEN WORDS!!\n")
                    exitGame = startMenu()  # show the start menu
                    break
                else:
                    print("You found one,", remNumItems, " more!")
            else:
                lives = lives - 1
                if lives == 0:  # check if the player lose
                    print("SORRY YOU DON'T HAVE ANY REMAINING LIFE. YOU LOSE\n")
                    exitGame = startMenu()
                    break
                else:
                    print("Sorry the inputted word is not one of the hidden words")
                    print(str(lives) + " life remaining")

            print()
        elif choice == '2': #check if the player chose to go back to the start menu
            exitGame = startMenu()
            newGame = True

        elif choice == '3': #exit the program
            exitGame = True
            newGame = True

        else:
            print("Invalid Input\n\n")


print("\n=========THANK YOU!!!===========")




