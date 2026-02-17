def pattern(l):
    a=11
    a1,a2,a3,a4,a5,a6,a7,a8,a9=l
    for i in range(a):
        for j in range(a):
                if i==1 and j==1:
                    print(a1,end=" ")
                elif i==5 and j==1:
                    print(a4,end=" ")
                elif i==9 and j==1:
                    print(a7,end=" ")
                elif i==1 and j==5:
                    print(a2,end=" ")
                elif i==5 and j==5:
                    print(a5,end=" ")
                elif i==9 and j==5: 
                    print(a8,end=" ")
                elif i==1 and j==9:
                    print(a3,end=" ")
                elif i==5 and j==9:
                    print(a6,end=" ")
                elif i==9 and j==9:
                    print(a9,end=" ")

                elif i==3 or i==7 or j==3 or j==7:
                    print("*",end=" ")
            
                # else:
                
                else:
                    print(" ",end=" ")
        print()
l=["-","-","-","-","-","-","-","-","-"]
j=0
print("                .   TIC TAC GAME   .     ")

print()
print(" -------------: : Game is going to Start  : :-------------")
print()
print(" -------------- Enter the number from 1 - 9 -----------------")

while True:
    if j%2==0:
        print()
        print("       ----   Turn of the person A   ---")
        
        k=int(input("Enter the position:  "))
        if l[k-1]=="-":


        
            if k==1:
                l[0]="X"
            elif k==2:
                l[1]="X"
            elif k==3:
                l[2]="X"
            elif k==4:
                l[3]="X"
            elif k==5:
                l[4]="X"
            elif k==6:
                l[5]="X"
            elif k==7:
                l[6]="X"
            elif k==8:
                l[7]="X"
            else:
                l[8]="X"
        else:
            print()
            print("Already changed try again")
            j-=1
        j+=1
        
        pattern(l)
        if l[0]==l[1]==l[2]=="X":
            print("Winner:A")
            break
        elif l[0]==l[3]==l[6]=="X":
            print("Winner:A")
            break
        elif l[1]==l[4]==l[7]=="X":
            print("Winner:A")
            break
        elif l[2]==l[5]==l[8]=="X":
            print("Winner:A")
            break
        elif l[3]==l[4]==l[5]=="X":
            print("Winner:A")
            break
        elif l[6]==l[7]==l[8]=="X":
            print("Winner:A")
            break
        elif l[0]==l[4]==l[8]=="X":
            print("Winner:A")
            break
        elif l[2]==l[4]==l[6]=="X":
            print("Winner:A")
            break
        elif l[0]!="-" and l[1]!="-" and l[2]!="-" and l[3]!="-" and l[4]!="-" and l[5]!="-" and l[6]!="-" and l[7]!="-" and l[8]!="-":
            break
    else:
        print()
        print("    ----   Turn of the person B   ---")
        k=int(input("Enter the position:  "))
        

        if l[k-1]=="-":
        
            if k==1:
                l[0]="O"
            elif k==2:
                l[1]="O"
            elif k==3:
                l[2]="O"
            elif k==4:
                l[3]="O"
            elif k==5:
                l[4]="O"
            elif k==6:
                l[5]="O"
            elif k==7:
                l[6]="O"
            elif k==8:
                l[7]="O"
            else:
                l[8]="O"
        else:
            print()
            print("Already changed try again")
            j-=1
        j+=1
        pattern(l)
        if l[0]==l[1]==l[2]=="O":
            print("Winner:B")
            break
        elif l[0]==l[3]==l[6]=="O":
            print("Winner:B")
            break
        elif l[1]==l[4]==l[7]=="O":
            print("Winner:B")
            break
        elif l[2]==l[5]==l[8]=="O":
            print("Winner:B")
            break
        elif l[3]==l[4]==l[5]=="O":
            print("Winner:B")
            break
        elif l[6]==l[7]==l[8]=="O":
            print("Winner:B")
            break
        elif l[0]==l[4]==l[8]=="O":
            print("Winner:B")
            break
        elif l[2]==l[4]==l[6]=="O":
            print("Winner:B")
            break
        elif l[0]!="-" and l[1]!="-" and l[2]!="-" and l[3]!="-" and l[4]!="-" and l[5]!="-" and l[6]!="-" and l[7]!="-" and l[8]!="-":
            break
            

