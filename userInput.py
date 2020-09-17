from pip._vendor.distlib.compat import raw_input

ROWS = 0
COLUMNS = 0
ROW_LIST = []
GRID = []
ERROR = "Invalid Input for START or END points!"


def createGrid():
    ROWS = int(input("Enter number of rows of the grid: "))
    COLUMNS = int(input("Enter number of columns of the grid: "))

    for r in range(ROWS):
        for c in range(COLUMNS):
            ele = int(input('Enter elements for row (%d , %d): ' % (r, c)))
            ROW_LIST.append(ele)
        GRID.append(ROW_LIST[:])
        ROW_LIST.clear()

        dims = (r + 1, c + 1)
    print(GRID)
    return GRID, dims


def getlocation(r, c):
    coord = tuple(int(x.strip()) for x in raw_input().split(','))
    # validation

    if 0 <= coord[0] <= r and 0 <= coord[1] <= c:
        return coord

    print(coord, ERROR)
    exit()


def getStartEnd(dims):
    (r, c) = dims
    print('dims', r, c)
    print("Enter start point co-ordinates (x,y):")
    START = getlocation(r, c)

    print("Enter end point co-ordinates (x,y):")
    END = getlocation(r, c)

    return START, END

