def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near
  
def lose1():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)
      
# checks whether the numbers are consecutive
def check(seq):
    i = 1
    while i<len(seq):
        if (seq[i]-seq[i-1])!= 1:
            return False
        i = i + 1
    return True
  
# starts the game
def Begin():
    seq= []
    last = 0
    while True:
        print ("Enter 'F' to play the first ")
        print("Enter 'S' to play the second ")
        chance = input(' ')
        if chance == "F" :
            while True:
                if last == 20:
                    lose1()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you want to enter?")
                    ele = int(input(''))
                    if ele > 0 and ele <= 3:
                        comp = 4 - ele
                    else:
                        print ("Wrong input \n Disqualified.")
                        lose1()
                    i, j = 1, 1
                    print ("Enter values")
                    while i <= ele:
                        seq.append(int(input(' ')))
                        i = i + 1
                    last = seq[-1] 
                    if check(seq) == True: 
                        if last == 21:
                            lose1()  
                        else:
                            while j <= comp:
                                seq.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            print (seq)
                            last = seq[-1]
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose1()
                          
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    seq.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (seq)
                if seq[-1] == 20:
                    lose1()
                      
                else:
                    print ("\nYour turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    
                    ele = int(input(' '))
                    if(ele <=3):
                        i = 1
                        print ("Enter your values")
                        while i <= ele:
                            seq.append(int(input(' ')))
                            i = i + 1
                        last = seq[-1]
                        if check(seq) == True:
                            near = nearestMultiple(last)
                            comp = near - last
                            if comp == 4:
                                comp = 3
                            else:
                                comp = comp
                        else:
                            print ("\nYou did not input consecutive integers.")
                            lose1()
                    else:
                        print("Wrong input\n Disqualified")
                        lose1()
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON GAME!")
            exit(0)
              
        else:
            print ("wrong choice")
                          
          
game = True    
while game == True:
        print ("Here player2 is COMPUTER")
        print("Do you want to play the 21 number game? (Yes / No)")
        ans = input('')
        if ans =='Yes':
            Begin();
        else:
            print ("Do you want quit the game?(yes / no)")
            quitting= input('> ')
            if quitting == "yes":
                print ("You are quitting the game...")
                exit(0)
            elif quitting== "no":
                print ("Continue the game")
            else:
                print ("Wrong choice")
                 
