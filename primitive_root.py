def gen_mod(b,p):
    temp=[]
    for i in range(1,p):
        temp.append((b**i) % p)
    return temp
   

p=int(input("Enter the prime number : "))
arr = []
print(f"Primitive roots of {p} are: ")
print("   B\t\t\t\tMods")
print("_______________________________________________________")
roots= []
for i in range (p):
    arr.append(gen_mod(i,p))
    if(len(set(arr[i])) == (p - 1)):
        print(f"B = {i} | {arr[i]}")
        roots.append(i)
print(f"Roots = {roots}")