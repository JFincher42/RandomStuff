import random

#random.randint(1, 100)


ones=0
twos=0
threes=0
fours=0
fives=0
sixes=0
hotdice=True

#print(*roll)

print("Welcome to Farkle")
playernum=input("How many will be playing? ")

playerarray=[""]*int(playernum)

score=[0]*int(playernum)

for i in range(0,int(playernum)):
  player=input("What is Player "+str(i+1)+"'s name? ")
  playerarray[i]=player
  
print ("\nThe Players are: ")
print(*playerarray)
print("")
print("Alright lets get started!")
gameRun=True


#for t in range (0,int(playernum)):
t=0
while gameRun:
  
  
  hotdice=True
  while hotdice:
    roll=[""]*6
    for i in range(0,6):
      roll[i]=random.randint(1, 6)
    print(playerarray[t]+" its your turn\nYou got:")
    print("a:"+str(roll[0])+", b:"+str(roll[1])+", c:"+str(roll[2])+", d:"+str(roll[3])+", e:"+str(roll[4])+", f:"+str(roll[5]))

    a0=input("would you like to reroll die 'a'")
    if a0=="yes":
      roll[0]=random.randint(1, 6)
      print("You got a "+str(roll[0]))
  
    a1=input("would you like to reroll die 'b'")
    if a1=="yes":
      roll[1]=random.randint(1, 6)
      print("You got a "+str(roll[1]))

    a2=input("would you like to reroll die 'c'")
    if a2=="yes":
      roll[2]=random.randint(1, 6)
      print("You got a "+str(roll[2]))
    
    a3=input("would you like to reroll die 'd'")
    if a3=="yes":
      roll[3]=random.randint(1, 6)
      print("You got a "+str(roll[3]))

    a4=input("would you like to reroll die 'e'")
    if a4=="yes":
      roll[4]=random.randint(1, 6)
      print("You got a "+str(roll[4]))

    a5=input("would you like to reroll die 'f'")
    if a5=="yes":
      roll[5]=random.randint(1, 6)
      print("You got a "+str(roll[5]))
  
    print("\nyour final roll is: ")
    print("a:"+str(roll[0])+", b:"+str(roll[1])+", c:"+str(roll[2])+", d:"+str(roll[3])+", e:"+str(roll[4])+", f:"+str(roll[5]))
  
    if a0=="no" and a1=="no" and a2=="no" and a3=="no" and a4=="no" and a5=="no":
      print("\nnice hot dice you got there, time to roll again!")
      hotdice=True
    
    elif a0=="yes" or a1=="yes" or a2=="yes" or a3=="yes" or a4=="yes" or a5=="yes":
      print("\nno hot dice this time\n")
      hotdice=False
  
    for r in range (0,6):
      if roll[r]==1:
        ones+=1
      elif roll[r]==2:
        twos+=1
      elif roll[r]==3:
        threes+=1
      elif roll[r]==4:
        fours+=1  
      elif roll[r]==5:
        fives+=1
      elif roll[r]==6:
        sixes+=1
      
    score[t]+=ones*100
    score[t]+=fives*50
  
    if ones>=3 and ones!=6:
      score[t]+=1000
      if ones==6:
        score[t]+=2000

    if twos>=3 and twos!=6:
      score[t]+=200
      if twos==6:
        score[t]+=400
      
    if threes>=3 and threes!=6:
      score[t]+=300
      if fours==6:
        score[t]+=600

    if fours>=3 and fours!=6:
      score[t]+=400
      if fours==6:
        score[t]+=800

    if fives>=3 and fives!=6:
     score[t]+=500
     if fives==6:
        score[t]+=1000
      
    if sixes>=3 and sixes!=6:
      score[t]+=600
      if sixes==6:
        score[t]+=1200
        
    print("Final Score for your turn: "+str(score[t]))
    
    ones=0
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0
    
    if score[t]>=1000:
      print(playerarray[t]+" you  got 1000 points and won the game \nCongrats")
      gameRun=False
    
  if t+1 < int(playernum):
    t =+ 1
  elif t+1 >= int(playernum):
    t=0
  elif hotdice == True:
    t=+0
