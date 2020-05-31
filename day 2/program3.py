for r in range(1,9):
    for c in range(1,9):
        if(r+c==9 or r==c):
            print('*',end="")
        else:
            print(" ",end="")
    print()
