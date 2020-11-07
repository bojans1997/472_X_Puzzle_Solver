import UCSNodes as nodes
class UCSBoard:
    def generateBoard(self, puzzleList, rowsCount, colsCount):
        global rows
        global cols

        rows = rowsCount
        cols = colsCount

        print("Rows gb are {}" .format(rows))
        print("Cols gb are {}" .format(cols))

        for i in range (rows*cols):
            newNode = nodes.UCSNodes()
            
            print(i)
        
    def __init__(self, rows, cols, puzzleList):
        self.generateBoard(puzzleList, rows, cols)


