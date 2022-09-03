import random,time
##board = ['','','','',
##         '','','','',
##         '','','','',
##         '','','','']
##
##board = [ 1, 2, 3, 4,
##          3, 4, 2, 1,
##          2, 3, 1,'',
##          4, 1, 4,'']
##
##board = [ 4, 3, 2, 1,
##          3, 2, 1, 4,
##          2, 4, 3, 1,
##         '','','','']

##board = [ 1, 2,'','',
##          3,'', 2, 1,
##         '', 3, 1, 2,
##          2, 1, 4,'']

board = ['', 2,'','',
          3,'', 2, 1,
         '', 3,'', 2,
          2,'', 4,'']

def checkRow(rowNumP): #availNumsP = list of available numbers
    availNums = [1,2,3,4]
    for i in range(rowNumP*4,rowNumP*4+4):
        if board[i] in availNums:
            availNums.remove(board[i])
    
    return availNums

def checkCol(colNumP):
    availNums = [1,2,3,4]
    for i in range(colNumP,colNumP+13,4):
        if board[i] in availNums:
            availNums.remove(board[i])

    return availNums

def getNums(rowNumsP,colNumsP):
    if len(rowNumsP)>len(colNumsP):
        numsAvail = rowNumsP
        for num in rowNumsP:
            if num not in colNumsP:
                numsAvail.remove(num)
    else:
        numsAvail = colNumsP
        for num in colNumsP:
            if num not in rowNumsP:
                numsAvail.remove(num)
    return numsAvail

def getEmptySquares():
    for i in range(len(board)):
        if board[i]=='':
            emptySquares.append(i)
    #return emptySquares

def resetBoard():
    for i in emptySquares:
        board[i]=''

def checkBoard():
    #check Rows
    for rowNum in range(4):
        rowNumsAvail = checkRow(rowNum)
        if len(rowNumsAvail)>0: return 'incorrect'     
    #check Columms
    for colNum in range(4):
        colNumsAvail = checkCol(colNum)
        if len(colNumsAvail)>0: return 'incorrect'
        
    return 'correct'

#hold and remember index numbers of empty squares (board[i]=='')
emptySquares = []; getEmptySquares()
while checkBoard()=='incorrect':
    resetBoard()
    for i in emptySquares: #loop thru indices w/ ''
        rowNum = i // 4
        colNum = i%4
        rowNumsAvail = checkRow(rowNum)
        if len(rowNumsAvail)>1:
            colNumsAvail = checkCol(colNum)
            availNums = getNums(rowNumsAvail,colNumsAvail)
            if len(availNums)>1:
                index_r = random.randint(0,len(availNums)-1)
                board[i]=availNums[index_r]
            elif len(availNums)==1:
                board[i]=availNums[0]
        elif len(rowNumsAvail)==1:
            board[i]=rowNumsAvail[0]
    #print board
    for i in range(len(board)):
        if i%4==0 and i>0: print('\n'+str(board[i]),end=' ')
        else: print(board[i],end=' ')
    time.sleep(1); print('\n')

#print board                      
##for i in range(len(board)):
##    if i%4==0 and i>0: print('\n'+str(board[i]),end=' ')
##    else: print(board[i],end=' ')    
    
