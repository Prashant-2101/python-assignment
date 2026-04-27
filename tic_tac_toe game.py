li=[1,2,3,4,5,6,7,8,9]
player="X"
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
flag=0
selected=[]
while True:
    print("\n\t\tTIC TAC TOE")
    print(f"\n\t\t {li[0]} | {li[1]} | {li[2]}")
    print("\t\t----------")
    print(f"\t\t {li[3]} | {li[4]} | {li[5]}")
    print("\t\t----------")
    print(f"\t\t {li[6]} | {li[7]} | {li[8]}")
    if flag==1:
        print("\n\t\tGAME OVER")
        break
    if len(selected)==9:
        print("\n\t\tMATCH TIE")
        break
    print(f"\n\t\tPLAYER {player} TURN: ",end="")
    try:
        ch = int(input(""))
    except:
        print("\n\t\tInvalid input! Enter number 1-9")
        continue
    if ch not in selected and ch in li:
        selected.append(ch)
        li[ch-1]=player
        for i,j,k in wins:
            if li[i]==li[j]== li[k] and li[i] in ["X","O"]:
                print(f"\n\t\tPLAYER {player} WINS")
                flag=1
                break
        if flag==1:
            continue
        if player=="X":
            player = "O"
        else:
            player="X"
    else:
        print("\n\t\tAlready selected value\n\t\tTry again")

