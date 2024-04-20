'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    '''
    found = False
    
    for i in range(len(wordlist)):
        if wordlist[i] == word:
            found = True
    return found
    

def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    '''
    row = ''
    i = 0
    
    while i < len(board[row_index]):
        row = row + board[row_index][i]
        i = i + 1

    return row

def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    '''
    column_string = ''

    for row in board:
        column_string += row[column_index]

    return column_string

    '''column = ''
    i = 0
    
    for char in range(len(board)):
            column = board[i][column_index] + board[i + 1][column_index]

    return column'''

def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''

    for column_index in range(len(board[0])):
        column_str = make_str_from_column(board, column_index)
        if word in column_str:
            return True

    return False

def board_contains_word(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    for col_index in range(len(board[0])):
        if word in make_str_from_column(board, col_index):
            return True
    return False

def word_score(word):
    ''' (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    '''

    score = 0
    while len(word):
        if len(word) <= 3:
            return 0
        elif 3 < len(word) < 6:
            return score + 1 * len(word)
        elif 7 < len(word) < 9:
            return score + 2 * len(word)
        elif len(word) > 10:
            return score + 3 * len(word)
    return score

def update_score(player_info, word):
    ''' ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    score = 0
    while len(word):
        if len(word) <= 3:
            return 0 + player_info[1]
        elif 3 < len(word) < 6:
            return (score + 1 * len(word)) + player_info[1]
        elif 7 < len(word) < 9:
            return (score + 2 * len(word)) + player_info[1]
        elif len(word) > 10:
            return (score + 3 * len(word)) + player_info[1]
    return score

    

def num_words_on_board(board, words):
    ''' (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    score = 0

    for word in words:
        if board_contains_word(board, word):
            score = score + 1
    return score


def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''

    words = []

    for line in words_file:
        word = line.strip()
        words.append(word)

    return words


def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''

    board = []

    for line in board_file:
        row = list(line.strip())
        board.append(row)

    return board

