from random import randint

def encrypt(msg,key):
    col = len(msg)
    row = key
    mat = [['' for _ in range(col)] for _ in range(row)]
    dir,row = 1,0

    for i in range(0,col):
        mat[row][i] = msg[i]
        row += dir
        
        if(row == 0 or row == key-1):
            dir *= -1
    cipher = ''
    for i in range(0,key):
        for j in range(0,col):
            if(mat[i][j] != ''):              
                cipher += mat[i][j]
    return cipher
        
def decrypt(cip,key):
    col=len(cip)
    row = key
    mat =[['' for _ in range(col)] for _ in range(row)]

    dir , row = 1,0
    for i in range (0,col):
        mat[row][i] = '*'
        row += dir
    
        if (row == 0 or row == key-1):
            dir *= -1
    u=0
    for i in range(0,key):
        for j in range(0,col):
        
            if mat[i][j] == '*':
                mat[i][j] = cip[u]
                u +=1 
    dir , row = 1,0
    planT = ''
    for i in range (0,col):
        planT += mat[row][i] 
        row += dir
        if (row == 0 or row == key-1):
            dir *= -1
    return planT

msg = input("Enter a message: ")
key = randint(2,5)
cipher = encrypt(msg,key)
print("Cipher Text:", cipher)
planT = decrypt(cipher,key)
print("Decrypted text: ", planT)