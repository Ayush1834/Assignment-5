rows=int(input("Enter the number of rows"))
m=65
for i in range (rows):
    for j in range(i+1):
        if m>90:
            m=65
            print(chr(m),end='')
            m+=1
            print()
        print()
