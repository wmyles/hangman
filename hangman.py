#hangman game


# if you want to choose randomly from a list of words
 #word_list = ["Python", "Java", "computer", "hacker", "painter"]
  #  random_number = random.randint(0, 4)
   # word = word_list[random_number]
def hangman(word):# function accepts variable name word as param
    wrong=0 # amount of wrong characters thy guessed
    stages=["", # list filled with strings use to draw hanman, when we print this it will appear
            "________       ",
            "|              ",
            "|        |     ",
            "|        O     ",
            "|       /|\    ",
            "|       / \    "
            ]
    rletters=list(word)# list containg each character in variable word that keeps track of letters to be guessed
    board=["_"]* len(word)# list of strings used to keep track of the hins you display to player two
    Win=False #^so an underscore for every letter
    print("Welcome to Hangman")
    while wrong < len(stages)-1 : #saying that hangman drawing is not made(remember that  we subtract 1 because wrong starts counting from 1 but index starts from 0)
#when wrong is more than STRINGS  in hangman game is over we subtract one because of below/propertis of lists
        print("\n") #stage lists count from zero its a list so u have to compnesate while wrong starts from 0
        msg="guess a letter"#above prints a blank space
        char=input(msg)
        if char in rletters:#if guess is charact we need to update list
            cind=rletters.index(char)# use index method to get first index of the letter player two guessed
            board[cind]=char# use the index returned by method above and set it equal to the guess to have the board be updated
            rletters[cind]='$' # index only returns the first index  in which the letter occurs
             #thus if letter appears twice it wont work because itll stop at first
                  # get around this by replacing that letter with a dollar sign so it wont be read/recongized
        else:
            wrong+=1
        print((" ".join(board))) #print the scoreboard
        counter=wrong + 1
        print("\n".join(stages[0:counter]))
#printing hangman is tricky "\n" is blank space, so joining stages pritns the entire hangman
#however, we need to slice it to the point in which the game is now
# we can use variable e that we set to wrong, wrong is where we are at in the game
# we add one to wrong because the end slice does not get included in the result
        if "_" not in board: # if no underscores then the game is won!
            print("you win!")
            print(" ".join(board))
            Win=True
            break 
    if not Win:
        print("\n".join(stages[0: wrong])) #print the full hangman
        print("you lose! it was {}.".format(word)) #use format to input word that was not gessed
hangman("cat")
