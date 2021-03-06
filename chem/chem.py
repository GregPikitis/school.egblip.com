#!/usr/bin/env python3
# Emelia Blankenship
# Block 5 Chem Honors
# Element Diversity Project
import colorama
import os
import sys
import time

from colorama import Fore, Back, Style

def cls(): # Clear the screen depending on system and configuration
    global inIdle
    if inIdle == False:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print ("-"*40)

print('Running in IDLE' if 'idlelib.run' in sys.modules else 'Not running in IDLE')
if 'idlelib.run' in sys.modules: # Check if running in idle or not, and set a variable for use in CLS
    inIdle = True
else:
    inIdle = False 
    
time.sleep(.5)
cls()

start = '\033[1m'
end = '\033[0;0m'

colorama.init()
cls()
while True:
    print(Fore.CYAN+"Element Diversity Project")
    print("Emelia Blankenship"+Style.RESET_ALL)
    print()
    print(Fore.YELLOW+"MOLYBDENUM (Mo):"+Style.RESET_ALL)
    print(Fore.GREEN+"1. Basic Information\n2. Similar Elements (properties, ions, isotopes, group or period)\n3. Concerning Electrons\n"+Style.RESET_ALL)
    print()
    print(Fore.YELLOW+"ARSENIC (As):"+Style.RESET_ALL)
    print(Fore.GREEN+"4. Basic Information\n5. Similar Elements (properties, ions, isotopes, group or period)\n6. Electron Info"+Style.RESET_ALL)
    print()
    print(Fore.RED+"q to quit"+Style.RESET_ALL)
    print()
    choice = input("Which option would you like to expand? (Please input the number)\n")
    cls()
    print()
    if choice == '1':
        print(Fore.YELLOW+"BASIC INFO - MOLYBDENUM"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Name: "+Style.RESET_ALL+Fore.WHITE+"Molybdenum (Mo)"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Classification: "+Style.RESET_ALL+Fore.WHITE+"Metal"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Family: "+Style.RESET_ALL+Fore.WHITE+"Transition Metal")
        print(Fore.MAGENTA+"Atomic Number: "+Style.RESET_ALL+Fore.WHITE+"42")
        print(Fore.MAGENTA+"Atomic Mass: "+Style.RESET_ALL+Fore.WHITE+"95.96")
        print()
        print(Fore.MAGENTA+"Neutral Atoms:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Protons - "+Style.RESET_ALL,end,Fore.WHITE+"42"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Electrons - "+Style.RESET_ALL,end,Fore.WHITE+"42"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Neutrons - "+Style.RESET_ALL,end,Fore.WHITE+"54"+Style.RESET_ALL)
        print()
        input("Press enter to return.")
        cls()
        
    elif choice == '2':
        print(Fore.YELLOW+"SIMILAR ELEMENTS - MOLYBDENUM"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Common Isotopes:"+Style.RESET_ALL)
        print(Fore.WHITE+"\u2089\u2082","\t","\u2089\u2087")
        print(" Mo","\t"," Mo")
        print("\u2074\u00B2","\t","\u2074\u00B2"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Common Ion: "+Style.RESET_ALL+Fore.WHITE+"Mo\u00B3\u207A")
        print("This is different from a neutral atom because it has 39 electrons instead of the neutral 42. This means it has a positive 3 charge. Mo creates this ion because it has 3 valence electrons and would rather lose the 3 than gain 5 to have 8 valence electrons."+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Element with Similar Properties: "+Style.RESET_ALL+Fore.WHITE+"Niobium (Nb)")
        print("Nb has similar properties to Molybdenum because both elements are metals, and must share those properties. They are also both part of the same block on the periodic table."+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Similar Elements Based on Periodic Table:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Larger Atomic Radius:",end,"\nRb has a larger atomic radius because it is placed left of Mo, meaning it has less protons pulling on the energy levels and electrons, so the distance from the nucleus to the last energy level is farther."+Style.RESET_ALL)
        print()
        print(Fore.WHITE,start,"Larger Ionization Energy:",end,"\nCr is above Mo on the periodic table meaning it has a higher ionization energy because it has less energy levels. Having less energy levels means it requires more energy to remove electrons because having less energy levels means that the energy levels are closer to the nucleus and have more pull on them from the protons, making it require more energy to remove electrons from the energy levels."+Style.RESET_ALL)
        print()
        print(Fore.WHITE,start,"Larger Electronegativity:"+end+"\nPd has a larger electronegativity because it is placed to the right of Mo on the periodic table, meaning that it has more protons. Having more protons causes more of a pull on the electrons, and a bigger desire to gain electrons."+Style.RESET_ALL)
        print()
        input(Fore.WHITE+"Press enter to return."+Style.RESET_ALL)
        cls()
        
    elif choice == '3':
        print(Fore.YELLOW+"ELECTRON INFORMATION - MOLYBDENUM"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Electron Config:"+Style.RESET_ALL+Fore.WHITE+"1s\u00B22s\u00b22p\u20763s\u00B23p\u20764s\u00B23d\u00B9\u20704p\u20765s\u00B24d\u2074"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Energy Level Electron Amount:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"1st Energy Level-",end,"2 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"2nd Energy Level-",end,"8 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"3rd Energy Level-",end,"18 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"4th Energy Level-",end,"12 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"5th Energy Level-",end,"2 electrons"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Total Sublevels: "+Style.RESET_ALL+Fore.WHITE+"10"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Highest Energy Level: "+Style.RESET_ALL+Fore.WHITE+"5"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Valence Electrons: "+Style.RESET_ALL+Fore.WHITE+"2"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Dot Diagram:"+Style.RESET_ALL)
        print(" \u2022\u2022 ")
        print(" Mo ")
        print()
        print(Fore.MAGENTA+"Orbital Diargram: "+Style.RESET_ALL)
        print("| 4p\u2076 | 5s\u00B2 | 4d\u2074 |")
        print("| [\u21C5] | [\u21C5] | [\u2191] |")
        print("| [\u21C5] |     | [\u2191] |")
        print("| [\u21C5] |     | [\u2191] |")
        print("|     |     | [\u2191] |")
        print("|     |     | [ ] |")
        print()
        print(Fore.MAGENTA+"Partially Occupied Orbitals: "+Style.RESET_ALL+Fore.WHITE+"4"+Style.RESET_ALL)
        print()
        input("Press enter to return.")
        cls()
        
    elif choice == '4':
        print(Fore.YELLOW+"BASIC INFO - ARSENIC"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Name: "+Style.RESET_ALL+Fore.WHITE+"Arsenic (As)"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Classification: "+Style.RESET_ALL+Fore.WHITE+"Semimetal"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Family: "+Style.RESET_ALL+Fore.WHITE+"Metalloid")
        print(Fore.MAGENTA+"Atomic Number: "+Style.RESET_ALL+Fore.WHITE+"33")
        print(Fore.MAGENTA+"Atomic Mass: "+Style.RESET_ALL+Fore.WHITE+"74.92")
        print()
        print(Fore.MAGENTA+"Neutral Atoms:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Protons - ",end,Style.RESET_ALL+Fore.WHITE+"33"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Electrons - ",end,Style.RESET_ALL+Fore.WHITE+"33"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Neutrons - ",end,Style.RESET_ALL+Fore.WHITE+"42"+Style.RESET_ALL)
        print()
        input("Press enter to return.")
        cls()
        
    elif choice == '5':
        print(Fore.YELLOW+"SIMILAR ELEMENTS - ARSENIC"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Common Isotopes:"+Style.RESET_ALL)
        print(Fore.WHITE+"\u2076\u2078","\t","\u2077\u2076")
        print(" As","\t"," As")
        print("\u2083\u2083","\t","\u2083\u2083"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Common Ion: "+Style.RESET_ALL+Fore.WHITE+"As\u207B\u00B3")
        print("This is different from a neutral atom because it has 3 more electrons, making the atom negative, a anion. This is so because As has 5 valence electrons, and it is easier to gain the 3 than lose the 5 it already has."+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Element with Similar Properties: "+Style.RESET_ALL+Fore.WHITE+"Phosphorus (P)")
        print("Phosphorus has similar properties to Arsenic because they are both part of the same block, and group on the periodic table, meaning there are similarities in their electron config and in their valence electrons."+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Similar Elements Based on Periodic Table:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"Larger atomic radius:",end,"\nK has a larger atomic radius because it is placed left of As, meaning it has less protons pulling on the energy levels and electrons, so the distance from the nucleus to the last energy level is farther."+Style.RESET_ALL)
        print()
        print(Fore.WHITE,start,"Larger Ionization Energy:",end,"\nN is above As on the periodic table meaning it has a higher ionization energy because it has less energy levels. Having less energy levels means that N requires more energy to remove electrons because having less energy levels means that the energy levels are closer to the nucleus and have more pull on them from the protons, making it require more energy to remove electrons from the energy levels."+Style.RESET_ALL)
        print()
        print(Fore.WHITE,start,"Larger Electronegativity:",end,"\nSe has a larger electronegativity because it is placed to the right of As on the periodic table, meaning that it has more protons. Having more protons causes more of a pull on the electrons, and a bigger desire to gain electrons because of the pull."+Style.RESET_ALL)
        print()
        input(Fore.WHITE+"Press enter to return."+Style.RESET_ALL)
        cls()
        
    elif choice == '6':
        print(Fore.YELLOW+"ELECTRON INFORMATION - ARSENIC"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Electron Config:"+Style.RESET_ALL+Fore.WHITE+"1s\u00B22s\u00b22p\u20763s\u00B23p\u20764s\u00B23d\u00B9\u20704p\u00B3"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Energy Level Electron Amount:"+Style.RESET_ALL)
        print(Fore.WHITE,start,"1st Energy Level-",end,"2 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"2nd Energy Level-",end,"8 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"3rd Energy Level-",end,"18 electrons"+Style.RESET_ALL)
        print(Fore.WHITE,start,"4th Energy Level-",end,"5 electrons"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Total Sublevels: "+Style.RESET_ALL+Fore.WHITE+"8"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Highest Energy Level: "+Style.RESET_ALL+Fore.WHITE+"4"+Style.RESET_ALL)
        print(Fore.MAGENTA+"Valence Electrons: "+Style.RESET_ALL+Fore.WHITE+"5"+Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+"Dot Diagram:"+Style.RESET_ALL)
        print(" \u2022\u2022 ")
        print("\u2022As\u2022")
        print(" \u2022")
        print()
        print(Fore.MAGENTA+"Orbital Diargram: "+Style.RESET_ALL)
        print("| 4s\u00B2 | 3d\u00B9\u2070 | 4p\u00B3 |")
        print("| [\u21C5] | [\u21C5]  | [\u2191] |")
        print("|     | [\u21C5]  | [\u2191] |")
        print("|     | [\u21C5]  | [\u2191] |")
        print("|     | [\u21C5]  |     |")
        print("|     | [\u21C5]  |     |")
        print()
        print(Fore.MAGENTA+"Partially Occupied Orbitals: "+Style.RESET_ALL+Fore.WHITE+"3"+Style.RESET_ALL)
        print()
        input("Press enter to return.")
        cls()
    elif choice == 'q':
              break
    else:
        input(Fore.RED+"This is not a valid input. Press enter to return to menu.\n"+Style.RESET_ALL)
        cls()
        print()
        
