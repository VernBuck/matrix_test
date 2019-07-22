# Matrix Stack Library
# Vernon Buck
# you should modify the routines below to complete the assignment

#makes stack and appends matrix
def gtInitialize():
    global stack
    stack = []
    matrix = [[0]*4 for x in range(4)] 
    for x in range(4):
        matrix[x][x] = 1 
    stack.append(matrix)
    return stack;

#helper method for multiplication completed
#4x4 multiplication
def gtMultiplication(matrixA, matrixB):
    solution = [[0]*4 for x in range(4)] 
    for x in range(4):
        solution[x][x] = 0 
    
    a = 0
    b = 0
    c = 0
    d = 0
    
    #iterates through all matrix indicies and puts it into solution
    for x in range(4):
        for y in range (4):
            for z in range(4):
                solution[x][y] += matrixA[a][b]*matrixB[c][d]
                b = b + 1
                c = c + 1
            b = 0
            c = 0
            d = d + 1
        a = a + 1
        b = 0
        c = 0
        d = 0
    return solution
    

#pushes top value
def gtPushMatrix():
    duplicate = stack[0]
    stack.append(duplicate)
    pass

#pops top value
def gtPopMatrix():
    
    if len(stack) == 1:
        println("cannot pop the matrix stack")
    else:
        stack.pop(0)
    pass

#performs translate by creating new matrix to multiply with the stack
def gtTranslate(x, y, z):
    translateMatrix = [[0]*4 for p in range(4)] 
    for p in range(4):
        translateMatrix[p][p] = 1 
    translateMatrix[0][3] = x
    translateMatrix[1][3] = y 
    translateMatrix[2][3] = z
    translateMatrix[3][3] = 1
    stack[0] = gtMultiplication(stack[0], translateMatrix)
    return stack

#performs scale by creating new matrix to multiply with the stack
def gtScale(x, y, z):
    scaleMatrix = [[0]*4 for p in range(4)] 
    scaleMatrix[0][0] = x
    scaleMatrix[1][1] = y 
    scaleMatrix[2][2] = z
    scaleMatrix[3][3] = 1
    stack[0] = gtMultiplication(stack[0], scaleMatrix)
    return stack

#rotates matrix by using the radian value to create a rotation matrix to multiply with identity
def gtRotateX(theta):

    radian = radians(theta)
    
    #matrix X
    rotateMatrixX = [[0]*4 for p in range(4)] 
    rotateMatrixX[0][0] = 1
    rotateMatrixX[1][1] = cos(radian) 
    rotateMatrixX[1][2] = -sin(radian) 
    rotateMatrixX[2][1] = sin(radian)
    rotateMatrixX[2][2] = cos(radian) 
    rotateMatrixX[3][3] = 1
    
    solution = gtMultiplication(rotateMatrixX, stack[0])
    stack[0] = solution
    return stack    

#rotates matrix by using the radian value to create a rotation matrix to multiply with identity
def gtRotateY(theta):
    #matrix Y
    radian = radians(theta)    

    rotateMatrixY = [[0]*4 for p in range(4)] 
    rotateMatrixY[0][0] = cos(radian)
    rotateMatrixY[0][2] = sin(radian)  
    rotateMatrixY[1][1] = 1
    rotateMatrixY[2][0] = -sin(radian)
    rotateMatrixY[2][2] = cos(radian) 
    rotateMatrixY[3][3] = 1
    
    solution = gtMultiplication(rotateMatrixY, stack[0])
    stack[0] = solution
    return stack

#rotates matrix by using the radian value to create a rotation matrix to multiply with identity
def gtRotateZ(theta):
     #matrix Z
    radian = radians(theta)  
     
    rotateMatrixZ = [[0]*4 for p in range(4)] 
    rotateMatrixZ[0][0] = cos(radian)
    rotateMatrixZ[0][1] = -sin(radian)  
    rotateMatrixZ[1][0] = sin(radian)
    rotateMatrixZ[1][1] = cos(radian)
    rotateMatrixZ[2][2] = 1 
    rotateMatrixZ[3][3] = 1
    
    solution = gtMultiplication(rotateMatrixZ, stack[0])
    stack[0] = solution
    return stack


def gtGetMatrix():
    pass

#prints the matrix line by line
def print_ctm():
    for x in stack[0]:
        for item in x:
            print item,
        print ""
    println (" ")
    pass   