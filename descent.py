# Layers of Descent - text adventure game with combat system
# Copyright (C) 2024 Layers of Descent Development Team
#
# This file is part of Layers of Descent.
#
# Layers of Descent is free software: however you cannot redistribute it, but it can
# be modified. Redistribution/sale of this software/product is against the law
# and be playing/editing/owning this software you consent to all of these terms and 
# conditions. This software is under the terms of the GNU General Public License as published by
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
    #such as a fight engine.            #
    #Enjoy!                             #
    #####################################
TESTPERMS = str (input ("Do you have the test key?")
if TESTPERMS == "BRAM BARBER IS LACKING":
    print("yes, yes he is")
    TESTSWORD = 1
    TESTARMOUR = 1
else:
    TESTSWORD = 0
    TESTARMOUR = 0

import hashlib

NOTICE = """Layers of Descent Copyright (C) 2024 LoD Development Team
This program comes with ABSOLUTELY NO WARRANTY; for details type "W".
This is free software, and the code can be modified. However, this code
cannot be redistributed and those who make retistribute/sell this product
are breaking the law; type "L" for details."""

CREDITS = """Layers of Descent Credits

MyBrianHurt5 - concept and code
estella144 - concept and code
isTopaz - concept, music and Terms and Conditions

WARRANTY = """15. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
"""

CONDITIONS_1 = """4. Conveying Verbatim Copies.

You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.
"""

CONDITIONS_2 = """5. Conveying Modified Source Versions.

You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.
"""

CONDITIONS_3 = """    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.
"""

CONDITIONS_4 = """6. Conveying Non-Source Forms.

You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge."""

CONDITIONS_5 = """    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d."""

CONDITIONS_6 = """  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

"Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.
"""

CONDITIONS_7 = """If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying."""

CONDITIONS = [CONDITIONS_1, CONDITIONS_2, CONDITIONS_3, CONDITIONS_4,
              CONDITIONS_5, CONDITIONS_6, CONDITIONS_7]

#variables
Item1 = 0.0
base_hp=20
RoomHeals=0
hp=20
GOLD=0
player_attack=1
player_defense=1
player_magic=1
kills=0
choice="x"
#definitions

def end_cs():
    input("It is defeated...")
    input("It is all finally over...")
    input("The door opens. You run...")
    input("...")
    input("...")
    input("...")
    input("You reach the top, and you see, at last...")
    input("THE LIGHT...")
    input("There is a strange feeling...")
    input("Suddenly, you fall over!")
    input("As you lie on the soft earth, you think your last thoughts...")
    input("You have come so far...")
    input("It all ends now...")
    input("You feel tired...")
    input("You close your eyes.")
    input("You Win!")

def codex():
    """Prints a comprehensive manual"""
    print("CODEX CAVERNA\n\nWelcome to the Codex of Caverna. An indespensible guide to these deadly tunnels.\nThis is not the only codex you will find down here, but I hope it will serve you well.\nGood luck...")
    codex_choice = input("Select a chapter:\na) Journal\nb) Monsters\nc) Items\n d) Abilities\ne) Exit").lower()
    while codex_choice != "e":
        if codex_choice == "a":
            print("Error! This codex chapter has not been added yet.")
            print("Create an issue on GitHub: github.com/estella144/layers-of-descent/issues/new")
            print("[Error 0x20]")
        elif codex_choice == "b":
            print("Error! This codex chapter has not been added yet.")
            print("Create an issue on GitHub: github.com/estella144/layers-of-descent/issues/new")
            print("[Error 0x20]")
        if codex_choice == "c":
            print("Error! This codex chapter has not been added yet.")
            print("Create an issue on GitHub: github.com/estella144/layers-of-descent/issues/new")
            print("[Error 0x20]")
        if codex_choice == "d":
            print("Error! This codex chapter has not been added yet.")
            print("Create an issue on GitHub: github.com/estella144/layers-of-descent/issues/new")
            print("[Error 0x20]")
        codex_choice = ""
    print("Exiting Codex...")
    input()


def fight(enemy_attack,enemy_defense,enemy_name,EnSt,EnWk,EnDd,reward,Esc):#basis for a simple customisable fight
    global player_attack
    global player_defense
    global player_magic
    global hp
    global base_hp
    global GOLD
    global kills
    print(str(enemy_name)+str(EnSt)) #enemy approaches

    while True:
        print("")

        if enemy_defense<=0:
        # Enemy dead
            kills += 1
            GOLD += reward
            print(f"You Win! Reward: {reward} gold")
            print("You now have", GOLD, "GOLD")
            print("Fight end")
            print("")
            break
        if enemy_defense<=enemy_defense/4:
        # Enemy weak
            print(str(enemy_name)+str(EnWk))

        # Enemy attack
        print(enemy_name, "strikes")
        hp -= (enemy_attack/player_defense)
        print("Your HP:","%.1f" %(hp,))
        print(f"{enemy_name}'s' DF: {enemy_defense}")
        print("Do you:\na)Hit\nb)Heal\nc)Run")
        action=input()
        if action=="a" or action=="A":#attacks
            print("you attack!")
            enemy_defense -= player_attack
        elif action=="b" or action=="B":#heals
            print("There is a flash of light! You have been healed!")
            hp += player_magic
            if hp > base_hp:
                hp = base_hp
                print("You are now at full health!")
            print(str(hp))
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
            print("Invalid choice")

def RoomDecide(Rm,Rn): #decides what to do in the room
    global GOLD
    global hp
    global base_hp
    global choice
    global RoomHeals

    while choice != "a":
        print("\na) Look\nb)Check Stats\nc)Heal\nd)Open Codex\ne)Move\n")
        choice = input()
        while (choice != "a" or choice != "A" :
            if choice == "a":
                print("The descent continues...")
            elif choice == "b":
                print("You have:\n",player_attack,"At\n",player_defense,"Df\n",player_magic,"Mg\n",hp, "Hp\n",GOLD,"GOLD\n\nYour Max Hp is",base_hp,"\nYou are in room",Rn,Rm)
            elif choice == "d":
                codex()
            elif choice == "c":
                if RoomHeals<0:
                    if hp == base_hp:
                        print("You are already at full health")
                    else:
                        hp=hp+player_magic
                        RoomHeals=RoomHeals-1
                        print("There is a bright flash of light\nYou now have",hp,"\nYour Max hp is",base_hp,"\nYou can only heal once per room")
                        print("You have",RoomHeals,"heal(s) left for this room")
                else:
                    print("You have used all your healing spells for this room")
            elif choice == "e":
                print("Not implemented yet")

print(NOTICE)
print()
print("Welcome to Layers of Descent ^TM^ version 0.1 [0c917f5].")
print("Press enter to continue...")
print("[C=Credits] [W=Warranty] [L=Conditions]")

while True:
    choice = input("").lower()
    if hashlib.sha256(bytes(choice, "utf-8")).hexdigest() == '151b01cf3ebced87a1b70c62adc9fe6f1b1da49c20bdce0d4f5dc47b3f8021ef':
        end_cs()
        break
    elif choice not in ("c", "w", "l"):
        break
    elif choice == "c":
        print(CREDITS)
    elif choice == "w":
        print(WARRANTY)
    elif choice == "l":
        for i in CONDITIONS:
            print(i)
            input("[ENTER=Next page]")

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

# Choose weapon

while True:

    print("You find yourself in a dark room. On the floor are:")
    print("A: 1 SWORD (At 3 Df 2 Mg 3) \nB: 1 AXE (At 3 Df 3 Mg 2) \nC: 1 STAFF (At 2 Df 3 Mg 3)")
    Item1 = input()

    if Item1 == "A" or Item1 == "a":
        print("You pick up the SWORD. Your STATS are \nAt 3 Df 2 Mg 3 \nyou feel SKILLED")
        player_attack=3.0
        player_defense=2.0
        player_magic=3.0
        break

    if Item1 == "B" or Item1 == "b":
        print("You pick up the AXE. Your STATS are \nAt 3 Df 3 Mg 2 \nyou feel POWERFUL")
        player_attack=3.0
        player_defense=3.0
        player_magic=2.0
        break

    if Item1 == "C" or Item1 == "c":
        print("You pick up the STAFF. Your STATS are \nAt 2 Df 3 Mg 3")
        print("You feel a MENACING presence watching you")
        player_attack=2.0
        player_defense=3.0
        player_magic=3.0
        break

    else:
        print("Invalid choice: " + str(Item1))

input("[ENTER=Continue]")
if TESTSWORD= 1:
    player_attack=1000.0
if TESTARMOUR= 1:
    player_defense=1000.0 
print("You step into the first room...")
input("[ENTER=Continue]")

fight(5,5,"Goblint"," jumps out!\nIt's a monster! Use your skills to survive this attack!"," is shedding everywhere. It looks weak!","Dust explodes everywhere!",5,1)
RoomDecide("Beginnner room.",1)
print ("The room is dimly lit by torches. There are some barrels to your left, a stone panel to your right and a door directly ahead.") 
Lever_0_1_1 = 0
Open_0_1_1 = 0
Exit_0_1_1 = 0
Exit_0_1_2 = 0
while Exit_0_1_1 == 0:
    Action_0_1_1=input ("Do you:\na) Search the barrels\nb) Inspect the panel\nc) Try the door\nd)Wait")
    if (Action_0_1_1== "a" or Action_0_1_1== "A"):
        print("The barrels lie on the floor, slowly rotting")
        while True:
            Action_0_1_2 =input ("Do you:\na) Try to open the barrels\nb) Try to break the barrels \nc) Leave the barrels")
            if (Action_0_1_2== "a" or Action_0_1_2== "A"):
                if (Lever_0_1_1== 0):
                    print ("The barrels are heavy with rot, but the lid is tightly secured")
                elif (Lever_0_1_1== 1):
                    print ("The barrels are in ruins. There is no lid to open.")
            if (Action_0_1_2== "b" or Action_0_1_2== "B"):
                if (Lever_0_1_1== 0):
                    print ("You smash the barrels open. You collect a loose LEVER from inside")
                elif (Lever_0_1_1== 1):
                    print ("The barrels are in ruins. There is nothing inside.")
            if (Action_0_1_2== "c" or Action_0_1_2== "C"):
                break 

