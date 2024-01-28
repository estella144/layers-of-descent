# Layers of Descent - text adventure game with combat system
# Copyright (C) 2024 Layers of Descent Development Team
#
# This file is part of Layers of Descent.
#
# Layers of Descent is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
player_attack=1
player_defense=1
Mg=1
KILLS=0
Choice="x"
#definitions

def codex():
    """Prints a comprehensive manual"""
    print("CODEX")

def FIGHT(EnAt,EnDf,EnNm,EnSt,EnWk,EnDd,EnGl,Esc):#basis for a simple customisable fight
    global player_attack
    global player_defense
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
        Hp=Hp-(EnAt/player_defense)
        print ("Hp=","%.1f" %(Hp,))
        action=input("Do you:\na)hit\nb)magic\nc)run")#selects action
        if action=="a" or action=="A":#attacks
            print("you attack!")
            EnDf=EnDf-player_attack
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
def RoomDecide(Rm,Rn): #decides what to do in the room
    global GOLD
    global Hp
    global BaseHp
    global Choice
    global RoomHeals
    while Choice != "a":
        Choice=input("\na)explore the room\nb)check stats\nc)heal\nd)CODEX").lower()
        if Choice== "a":
            print("")
        if Choice== "b":
            print("You have:\n",player_attack,"At\n",player_defense,"Df\n",Mg,"Mg\n",Hp, "Hp\n",GOLD,"GOLD\n\nYour Max Hp is",BaseHp,"\nYou are in room",Rn,Rm)
        if Choice== "d":
            codex()
        if Choice== "c":
            if RoomHeals>0:
                if Hp == BaseHp:
                    print("You are already at full health")
                else:
                    Hp=Hp+Mg
                    RoomHeals=RoomHeals-1
                    print("There is a bright flash of light\nYou now have",Hp,"\nYour Max Hp is",BaseHp,"\nYou can only heal once per room")
                    print("You have",RoomHeals,"heal(s) left for this room")
            else:
                print("You have used all your healing spells for this room")



#end of defenitions

#story begins
print("Welcome to Layers of Descent ^TM^.\nPress enter to continue...")
input("")

print("You will face many dangerous challenges as you travel deeper into the tunnels.")
print("[ENTER=Continue]")
input("")

print("If you are defeated by the trials, you will never return to the surface...")
print("[ENTER=Continue]")
input("")

print("Good luck!")
print("[ENTER=Continue]")
input("")

print("")

print("")

while True:

    print("You find yourself in a dark room. On the floor are:") #select weapon
    Item1 = input("A: 1 SWORD (At 3 Df 2 Mg 3) \nB: 1 AXE (At 3 Df 3 Mg 2) \nC: 1 STAFF (At 2 Df 3 Mg 3)")

    if Item1 == "A" or Item1 == "a":
        print("You pick up the SWORD. Your STATS are \nAt 3 Df 2 Mg 3 \nyou feel SKILLED")
        player_attack=3.0
        player_defense=2.0
        Mg=3.0
        break

    if Item1 == "B" or Item1 == "b":
        print("You pick up the AXE. Your STATS are \nAt 3 Df 3 Mg 2 \nyou feel POWERFUL")
        player_attack=3.0
        player_defense=3.0
        Mg=2.0
        break

    if Item1 == "C" or Item1 == "c":
        print("You pick up the STAFF. Your STATS are \nAt 2 Df 3 Mg 3")
        print("You feel a MENACING presence watching you")
        player_attack=2.0
        player_defense=3.0
        Mg=3.0
        break

    else:
        print("Invalid choice: " + str(Item1))

input("")

print("You step into the first room...")
input("")

FIGHT(5,5,"Goblint"," jumps out!\nIt's a monster! Use your skills to survive this attack!"," is shedding everwhere.","Dust explodes everwhere.",5,1)#starts a FIGHT. Text is customisable.
RoomDecide("Beginnner room.",1)
print(KILLS)
