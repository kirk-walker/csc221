''' Table Printer practice project

Author: Kirk
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    
    colWidths = [0] * len(tableData)
    
    
    for y in range(len(tableData)):
        for x in tableData[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    for x in range(len(tableData[0])) :
        for y in range(len(tableData)) :
            print(tableData[y][x].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)