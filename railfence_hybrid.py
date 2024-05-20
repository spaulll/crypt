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
    return caesarCipher(cipher, key)
        
def decrypt(cip,key):
    cip = caesarCipher(cip, -key)
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

#caesarCipher
def caesarCipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

msg = input("Enter a message: ")
key = randint(2,5)
cipher = encrypt(msg, key)
print("Cipher Text:", cipher)
planT = decrypt(cipher, key)
print("Decrypted text:", planT)