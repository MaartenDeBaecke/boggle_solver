import math
import time

board = [ #remove input board to use this board
    "M", "A", "N", "O",
    "A", "K", "P", "S",
    "N", "E", "U", "T",
    "T", "L", "R", "O"
]

letters = {
    0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G",
    7 : "H", 8 : "I", 9 : "J", 10 : "K", 11 : "L", 12 : "M", 13 : "N",
    14 : "O", 15 : "P", 16 : "Q", 17 : "R", 18 : "S", 19 : "T", 20 : "U",
    21 : "V", 22 : "W", 23 : "X", 24 : "Y", 25 : "Z"
}

Adictionary, Bdictionary, Cdictionary, Ddictionary, Edictionary, Fdictionary, Gdictionary, Hdictionary, Idictionary, Jdictionary, Kdictionary, Ldictionary, Mdictionary, Ndictionary, Odictionary, Pdictionary, Qdictionary, Rdictionary, Sdictionary, Tdictionary, Udictionary, Vdictionary, Wdictionary, Xdictionary, Ydictionary, Zdictionary = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()

dictionaries = {
    "A" : Adictionary, "B" : Bdictionary, "C" : Cdictionary, "D" : Ddictionary,
    "E" : Edictionary, "F" : Fdictionary, "G" : Gdictionary, "H" : Hdictionary,
    "I" : Idictionary, "J" : Jdictionary, "K" : Kdictionary, "L" : Ldictionary,
    "M" : Mdictionary, "N" : Ndictionary, "O" : Odictionary, "P" : Pdictionary,
    "Q" : Qdictionary, "R" : Rdictionary, "S" : Sdictionary, "T" : Tdictionary,
    "U" : Udictionary, "V" : Vdictionary, "W" : Wdictionary, "X" : Xdictionary,
    "Y" : Ydictionary, "Z" : Zdictionary
}

def get_dictionaries(): #all words from Adictionary.txt will be sorted in Adictionary, Bdictionary.txt in Bdictionary...
    for x in range(len(letters)):
        with open("short_dict/" + letters[x] +"words.txt") as f:
            for word in f:
                word = word.strip().upper()
                dictionary = dictionaries[letters[x]]
                dictionary.add(word)

    return Adictionary, Bdictionary, Cdictionary, Ddictionary, Edictionary, Fdictionary, Gdictionary, Hdictionary, Idictionary, Jdictionary, Kdictionary, Ldictionary, Mdictionary, Ndictionary, Odictionary, Pdictionary, Qdictionary, Rdictionary, Sdictionary, Tdictionary, Udictionary, Vdictionary, Wdictionary, Xdictionary, Ydictionary, Zdictionary

def get_dimensions(): #get the length/width of the board
    n = int(math.sqrt(len(board)))
    return n

def define_pieces(): #give each board item a piece type (corner1, side4, center...)
    # ['corner1', 'side1', 'side1', 'corner2',
    #  'side2', 'center', 'center', 'side3',
    #  'side2', 'center', 'center', 'side3',
    #  'corner3', 'side4', 'side4', 'corner4']
    pieces = []
    piece = ""

    for index in range(len(board)):
        if (index == 0):
            piece = "corner1"
        elif (index == n-1 ):
            piece = "corner2"
        elif (index == (n*n-n)):
            piece = "corner3"
        elif (index == (n*n-1)):
            piece = "corner4"
        elif (index < n-1):
            piece = "side1"
        elif (index % n == 0):
            piece = "side2"
        elif ((index + 1) % n == 0):
            piece = "side3"
        elif (n*n -n < index and index < n*n-1):
            piece = "side4"
        else:
            piece = "center"

        pieces.append(piece)
    return pieces

def get_options(i): #gets neighbours of specific piece
    piece = pieces[i]

    option = {}
    if(piece == "corner1"):
        options = {
            0 : 1,
            1 : n,
            2 : n+1
        }
    elif(piece == "corner2"):
        options = {
            0 : n-2,
            1 : 2*n-2,
            2 : 2*n-1
        }
    elif(piece == "corner3"):
        options = {
            0 : n*n-2*n,
            1 : n*n-2*n+1,
            2 : n*n-n+1
        }
    elif(piece == "corner4"):
        options = {
            0 : n*n-2,
            1 : n*n-n-1,
            2 : n*n-n-2
        }
    elif(piece == "side1"):
        options = {
            0 : i-1,
            1 : i+1,
            2 : i+n,
            3 : i+n-1,
            4 : i+n+1
        }
    elif(piece == "side2"):
        options = {
            0 : i-n,
            1 : i+n,
            2 : i-n+1,
            3 : i+1,
            4 : i+n+1
        }
    elif(piece == "side3"):
        options = {
            0 : i-n,
            1 : i+n,
            2 : i-n-1,
            3 : i-1,
            4 : i+n-1
        }
    elif(piece == "side4"):
        options = {
            0 : i-1,
            1 : i+1,
            2 : i-n,
            3 : i-n-1,
            4 : i-n+1
        }
    elif(piece == "center"):
        options = {
            0 : i-n-1,
            1 : i-n,
            2 : i-n+1,
            3 : i-1,
            4 : i+1,
            5 : i+n-1,
            6 : i+n,
            7 : i+n+1
        }
    return options

def find_duplicate(path): #returns true if path contains duplicate
    count = {}
    for s in path:
      if s in count:
        count[s] += 1
      else:
        count[s] = 1

    for key in count:
      if count[key] > 1:
        return True
    else:
        return False

def find_next_char(current_word, option, options, path): #finds next char for given lettercombination
    new_word = current_word + board[int(options[option])]
    path.append(str(options[option]))

    dictionary = dictionaries[current_word[0]]

    if len(new_word) > 2: #len of word needs to me at least 3
        if new_word in dictionary: #if new_word is an existing word, add to words
            if new_word not in words:
                if (find_duplicate(path) == False):
                    words.add(new_word)
                    print(new_word)

    if (any(item.startswith(new_word) for item in dictionary)):
        index = int(path[-1])
        options = get_options(index)
        for x in range(len(options)):
            find_next_char(new_word, x, options, path)
        path.pop()
    else:
        path.pop()


def find_word(index): #find all words starting with board[index] letter
    options = get_options(index)

    current_word = board[index] #stores possible words
    path = [str(index)] #stores the index of every letter (to later check for duplicates -> the same letter can't be used twice)

    for x in range(len(options)):
        find_next_char(current_word, x, options, path)




board_input = input("Type your board here: ")
start = time.time()
board = list(board_input.upper())
n = get_dimensions()

print("Your board: \n")
for b in range(0, n*n, n):
    x = b
    y = b + n
    print(board[x:y])
print("\nFound words: \n")

Adictionary, Bdictionary, Cdictionary, Ddictionary, Edictionary, Fdictionary, Gdictionary, Hdictionary, Idictionary, Jdictionary, Kdictionary, Ldictionary, Mdictionary, Ndictionary, Odictionary, Pdictionary, Qdictionary, Rdictionary, Sdictionary, Tdictionary, Udictionary, Vdictionary, Wdictionary, Xdictionary, Ydictionary, Zdictionary = get_dictionaries()
pieces = define_pieces()
words = set()
for i in range(len(board)):
    find_word(i)
end = time.time()

print("--------------------------------")
print("Found " + str(len(words)) + " Words in " + (str(end - start))[:-10] + "seconds")
