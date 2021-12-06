filename = "pt1.txt"
in_nums = open(filename).readline().rstrip().split(",")

in_boards = []
with open(filename) as file:
    next(file)
    next(file)
    board = []
    for line in file:
        if line != "\n":
            board.append(" ".join(line.split()).split())
        else:
            in_boards.append(board)
            board = []
    in_boards.append(board)

test_nums = ("7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1").split(",")
test_boards = [
    # board 1
    [
        ("22 13 17 11 0").split(" "),
        ("8 2 23 4 24").split(" "),
        ("21 9 14 16 7").split(" "),
        ("6 10 3 18 5").split(" "),
        ("1 12 20 15 19").split(" "),
    ],
    # board 2
    [
        ("3 15 0 2 22").split(" "),
        ("9 18 13 17 5").split(" "),
        ("19 8 7 25 23").split(" "),
        ("20 11 10 24 4").split(" "),
        ("14 21 16 12 6").split(" "),
    ],
    # board 3
    [
        ("14 21 17 24 4").split(" "),
        ("10 16 15 9 19").split(" "),
        ("18 8 23 26 20").split(" "),
        ("22 11 13 6 5").split(" "),
        ("2 0 12 3 7").split(" "),
    ]
]

# Initializes appropriate data structures for bingo
def init_bingo(boards):
    bingo_boards = []
    for board in boards:
        bingo_board = []
        for row in board:
            bingo_board.append({i : False for i in row})
        bingo_boards.append(bingo_board)
    return bingo_boards

# Convert bingo board back to matrix
def conv_board(board):
    c_board = []
    for row in board:
        c_row = []
        for num in row:
            c_row.append(num)
        c_board.append(c_row)
    return c_board
        
def transpose_board(board):
    t_board = []
    # Convert bingo board back to matrix
    c_board = conv_board(board)

    # Transpose matrix
    for i in range(len(c_board[0])):
        t_row = {}
        for j in range(len(c_board)):
            num = c_board[j][i]
            t_row[num] = board[j][num]
        t_board.append(t_row)
            
    return t_board

# Debug print
def print_board(board):
    print("\n")
    for row in board:
        print(row)

def check_board(board):
    # Check rows first
    for row in board:
        if check_bingo(row):
            return True
    t_board = transpose_board(board)
    for col in t_board:
        if check_bingo(col):
            return True
    return False

def check_bingo(nums):
    for k in nums:
        if nums[k] != True:
            return False
    return True

def sum_board(board):
    ret = 0
    for row in board:
        for num in row:
            if not row[num]:
                ret += int(num, 10)
    return ret

# Plays Bingo, basically
def play_bingo(boards, nums):
    n = len(boards)
    winners = []
    for num in nums:
        garb = []
        # Check number against all boards
        for i, board in enumerate(boards):
            for row in board:
               # Mark number
               if num in row:
                   row[num] = True
            # Check if board wins
            if check_board(board):
                board_sum = sum_board(board)
                winners.append((int(num), board_sum))
                garb.append(board)
        # Remove any winners
        while len(garb) > 0:
            board = garb.pop()
            boards.remove(board)
    # Last winning board
    return winners[-1][0] * winners[-1][1]

if __name__ == "__main__":
    boards = init_bingo(in_boards)
    ans = play_bingo(boards, in_nums)
    print("Answer:", ans)

    
   