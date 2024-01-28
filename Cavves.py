
    #####################################
    #Willkommen in meinem Spiel.        #
    #This is a text based adventure game#
    #that includes some unique features #
    #such as a FIGHT engine.            #
    #Enjoy!                             #
    #####################################


#variables
Item1 = 0.0 
BaseHp=20
RoomHeals=0
Hp=20
GOLD=0
At=1
Df=1
Mg=1
KILLS=0
Choice="x"
#definitions
def CODEX():#prints a comprehensive manual
    print ("CODEX")
def FIGHT(EnAt,EnDf,EnNm,EnSt,EnWk,EnDd,EnGl,Esc):#basis for a simple customisable fight
    global At
    global Df
    global Mg
    global Hp
    global BaseHp
    global GOLD
    global KILLS
    print(str(EnNm)+str(EnSt)) #enemy approaches

    while True: 
        print("")
        if EnDf<1:#enemy death
            KILLS=KILLS+1
            print("You Win!")
            GOLD=GOLD+EnGl
            print("You have", GOLD,"GOLD")
            print("Fight end")
            print("")
            break
        if EnDf<3:#enemy weak
            print(str(EnNm)+str(EnWk))
        print(EnNm+" strikes")#enemy attack
        Hp=Hp-(EnAt/Df)
        print ("Hp=","%.1f" %(Hp,))
        action=input("Do you:\na)hit\nb)magic\nc)run")#selects action
        if action=="a" or action=="A":#attacks
            print("you attack!")
            EnDf=EnDf-At
        elif action=="b" or action=="B":#heals
            print("there is a flash of light")
            Hp=Hp+Mg
            if Hp>BaseHp:
                Hp=BaseHp
                print ("You are at full health")
            print(str(Hp))
        elif action=="c" or action=="C":#escapes
            if Esc==1:
                print("You dive out the way!")
                print("")
                print("Fight end")
                print("")
                break
            else:
                print("You cannot escape!")
        else:
            print("err")
def RoomDecide(Rm,Rn):#decides what to do in the room
    global GOLD
    global Hp
    global BaseHp
    global Choice
    global RoomHeals
    while Choice != "a" or Choice != "A":
        Choice=input("\na)explore the room\nb)check stats\nc)heal\nd)CODEX")
        if Choice== "a" or Choice=="A":
            print("")
        if Choice== "b" or Choice=="B":
            print("You have:\n",At,"At\n",Df,"Df\n",Mg,"Mg\n",Hp, "Hp\n",GOLD,"GOLD\n\nYour Max Hp is",BaseHp,"\nYou are in room",Rn,Rm)
        if Choice== "d" or Choice=="D":
            CODEX
        if Choice== "c" or Choice=="C":
            if RoomHeals>0:
                print("There is a bright flash of light\nYou have",Hp,"\nYour Max Hp is",BaseHp,"\nYou can only heal once per room")
                Hp=Hp+Mg
                RoomHeals=RoomHeals-1
                print("You have",RoomHeals,"heals left for this room")
            else:
                print("You have used all your healing spells for this room")
            
            

#end of defenitions        
        
#story begins
print ("Welcome to my tunnels of deadly deception ^TM^.\nPress enter to continue...")
input("")

print ("You will face many dangerous challenges as you travel deeper into the tunnels.") 
input("")

print ("If you are defeated by the trials, you will never return to the surface...") 
input("")

print ("Good luck!")
input("")

print ("") 

print ("") 

while True : 

    print ("You find yourself in a dark room. On the floor are:") #select weapon

    Item1= input("A: 1 SWORD (At 3 Df 2 Mg 3 \nB: 1 AXE (At 3 Df 3 Mg 2 \nC: 1 STAFF (At 2 Df 3 Mg 3") 

    if Item1 == "A" or Item1 == "a": 

        print("You pick up the SWORD. Your STATS are \nAt 3 Df 2 Mg 3 \nyou feel SKILLED") 

        At=3.0 

        Df=2.0

        Mg=3.0 

        break  

    if Item1 == "B" or Item1 == "b": 

        print("You pick up the AXE. Your STATS are \nAt 3 Df 3 Mg 2 \nyou feel POWERFUL") 

        At=3.0 

        Df=3.0 

        Mg=2.0 

        break 

    if Item1 == "C" or Item1 == "c": 

        print("You pick up the STAFF. Your STATS are \nAt 2 Df 3 Mg 3") 

        print("You feel a MENACING presence watching you") 

        At=2.0 

        Df=3.0 

        Mg=3.0 

        break 

    else: 

        print("err") 
input("")

print("You step into the first room...") 
input("")

FIGHT(5,5,"Goblint"," jumps out!\nIt's a monster! Use your skills to survive this attack!"," is shedding everwhere.","Dust explodes everwhere.",5,1)#starts a FIGHT. Text is customisable.
RoomDecide("Beginnner room.",1)
print(KILLS)

