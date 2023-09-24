
# import only system from os
from os import system, name
from os.path import exists
import json
  
# import sleep to show output for some time period
from time import sleep

from functools import reduce
# Constants
# Count for completion
complete = {
    "hyruleBass": 15,
    "heartyBass": 15,
    "opal": 45,
    "tail": 45,
    "acorn": 30,
    "beetle": 15,
    "honey": 16,
    "darner": 2,
    "rushroom": 55,
    "silentPrincess": 19,
    "amber": 10,
    "flint": 11,
    "luminous": 10,
    "cricket": 10,
    "frog": 5,
    "firefly": 5,
    "sunshroom": 3,
    "spring": 15,
    "shaft": 8,
    "core3": 3,
    "core5": 5,
    "octaballoon": 1,
    "faroshHorn": 4,
    "faroshClaw": 2,
    "faroshFang": 1,
    "faroshScale": 3,
    "naydraHorn": 4,
    "naydraClaw": 2,
    "naydraFang": 1,
    "naydraScale": 1,
    "dinraalHorn": 4,
    "dinraalClaw": 2,
    "dinraalFang": 1,
    "dinraalScale": 2,
    "eliteBokoblin": 1,
    "eliteMoblin": 1,
    "eliteLizalfos": 1,
    "eliteLynel": 1,
    "eliteFarosh": 1,
    "eliteNaydra": 1,
    "eliteDinraal": 1,
    "eliteWindblight": 1,
    "eliteThunderblight": 1,
    "eliteWaterblight": 1,
    "eliteFireblight": 1,
    "eliteGanon": 1,
    "eliteBeast": 1,
    "eliteKohga": 1,
    "exMolduking": 1,
    "exTalus": 1,
    "guardianSmall": 1,
    "guardianSkywatcher": 1,
    "guardianStalker": 1,
    "blupee": 1,
    "stalhorse": 1,
    "kilton": 1,
    "heroine": 1,
    "heroineSword": 1,
    "weaponDuplexBow": 1,
    "weaponWindcleaver": 1,
    "weaponAncientShortSword": 1,
    "weaponAncientBattleAxe": 1,
    "weaponFrostspear": 1,
    "weaponFireRod": 1,
    "weaponMoblinClub": 1,
    "weaponTravelerSword": 1,
}
searchKeys = {
    "hyrulebass": "hyruleBass",
    "heartybass": "heartyBass",
    "opals":"opal",
    "lizalfostails": "tail",
    "acorns": "acorn",
    "beetles": "beetle",
    "courserbeehoney": "honey",
    "colddarners": "darner",
    "rushrooms": "rushroom",
    "silentprincess": "silentPrincess",
    "ambers": "amber",
    "sunshrooms": "sunshroom",
    "flints": "flint",
    "frogs": "frog",
    "crickets": "cricket",
    "fireflyfireflies": "firefly",
    "luminousstone": "luminous",
    "ancientspring": "spring",
    "ancientshaft": "shaft",
    "ancientcorestasiscore3": "core3",
    "ancientcore5": "core5",
    "octaballoon": "octaballoon",
    "elitesilverbokoblin": "eliteBokoblin",
    "elitesilvermoblin": "eliteMoblin",
    "elitesilverlizalfos": "eliteLizalfos",
    "elitesilverlynel": "eliteLynel",
    "elitefaroshdragon": "eliteFarosh",
    "elitenaydradragon": "eliteNaydra",
    "elitedinraaldragon": "eliteDinraal",
    "elitewindblightganon": "eliteWindblight",
    "elitethunderblightganon": "eliteThunderblight",
    "elitewaterblightganon": "eliteWaterblight",
    "elitefireblightganon": "eliteFireblight",
    "elitecalamityganon": "eliteGanon",
    "elitedarkbeastganon": "eliteBeast",
    "elitekohgamasterkohga": "eliteKohga",
    "eliteexmolduking": "exMolduking",
    "eliteexigneotalustitan": "exTalus",
    "guardianstalkerwalking": "guardianStalker",
    "guardiansmallscout": "guardianSmall",
    "guardianflyingskywatcher": "guardianSkywatcher",
    "blupee": "blupee",
    "stalhorse": "stalhorse",
    "weaponyigaswordwindcleaver": "weaponWindcleaver",
    "weaponancientswordshortsword": "weaponAncientShortSword",
    "weaponancientbattleaxe": "weaponAncientBattleAxe",
    "weaponfrostspear": "weaponFrostspear",
    "weaponfirerod": "weaponFireRod",
    "weaponmoblinclub": "weaponMoblinClub",
    "weapontravelersword": "weaponTravelerSword",
    "weaponduplexbowyiga": "weaponDuplexBow",
    "kilton": "kilton",
    "eighthheroine": "heroine",
    "heroineswordbigsword": "heroineSword",
}

# Global Variables
part = ""
notes = list()
data = {}
for k in complete:
    data[k] = 0
output = ""
hide_help = False
expand_cat = False
  
# Functions
# Clear screen
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Print Help
def help():
    print("\033[0mAvailable Commands:")
    print("\033[93m  [o]k    <material | picture>")
    print("  [p]art  <Co | ShGe | ShSc | ShSp | ShScSp | Sh>")
    print("  [h]orn  <[n]aydra | [d]inraal | [f]arosh>")
    print("  [c]law  <[n]aydra | [d]inraal | [f]arosh>")
    print("  [f]ang  <[n]aydra | [d]inraal | [f]arosh>")
    print("  [s]cale <[n]aydra | [d]inraal | [f]arosh>")
    print("  [n]ote  <something>")
    print("  expand  to expand completed categories")
    print("  core    to add a core")
    print("  hide    to hide help (uhide to show)")
    print("  reset   to reset run (not reversible)")
    print("  exit    to quit")
    print("")
    print("\033[90m  Add \"u\" in front of the command to undo. Example: \"uo spring\" unchecks the completion of 15 springs")
    print("  Material/Pictures support auto-search. For example: \"o boko\" checks silver bokoblin picture")
    print("  Progress is auto saved")
    print("\033[20A")
    
def cell(text, key):
    if(data[key] >= complete[key]):
        return "\033[92m"+text
    elif(data[key] != 0):
        return "\033[93m"+text
    else:
        return "\033[0m"+text
    
def dragon_cell(text, key):
    formatted_text = "[  "+text+"   "+str(data[key])+"/"+str(complete[key])+"  ]"
    return cell(formatted_text, key)

def farosh_horn_cell():
    if data["faroshHorn"]<10:
       return cell("[  Horn      "+str(data["faroshHorn"])+"  ]", "faroshHorn")
    else:
       return cell("[  Horn     "+str(data["faroshHorn"])+"  ]", "faroshHorn")

def core_cell(text, key):
    return cell("[Core:"+text+" "+str(data[key])+"/"+str(complete[key])+"]", key)
    
def check_all_complete(keys):
    for k in keys:
        if data[k] < complete[k]:
            return False
    return True

def check_all_complete_starts_with(key):
    for k in data:
        if k.startswith(key) and data[k] < complete[k]:
            return False
    return True

def print_upper():

    print("\033[0m=========================== Hundo Checklist ===========================")
    print("Part Combination:\033[96m", part, "\033[0m")
    
    # Quest Material
    if (not expand_cat) and check_all_complete(["core3", "core5", "spring", "shaft", "amber", "flint", "luminous", "frog", "darner", "firefly", "cricket", "sunshroom", "rushroom", "octaballoon"]):
        print("\033[92m--- Quest Materials Complete ----------------------------------------\033[0m")
    else:
        print("")
        print(core_cell("Stasis", "core3"), core_cell("Sword ", "core5"), cell("[Spring      15 ]", "spring"), cell("[Shaft       8  ]", "shaft"))
        print(cell("[Amber       10 ]", "amber"),       cell("[Flint       11 ]", "flint"),   cell("[Luminous    10 ]", "luminous"), cell("[Frog        5  ]", "frog"))
        print(cell("[Octaballoon  1 ]", "octaballoon"), cell("[Firefly      5 ]", "firefly"), cell("[Cricket     10 ]", "cricket"),  cell("[Sunshroom   3  ]", "sunshroom"))
        print(cell("[Rushroom    55 ]", "rushroom"),    cell("[Cold Darner  2 ]", "darner"))

    # Quest Pictures
    if (not expand_cat) and check_all_complete(["guardianSmall", "guardianStalker", "guardianSkywatcher", "stalhorse", "blupee", "kilton", "heroine", "heroineSword"]):
        print("\033[92m--- Enemy/Creature Pictures Complete ----------------------------------\033[0m")
    else:
        print("")
        print(cell("[Guardian Scout ]", "guardianSmall"), cell("[Stalker        ]", "guardianStalker"), cell("[Skywatcher     ]", "guardianSkywatcher"), cell("[Eighth Heroine ]", "heroine"))
        print(cell("[Stalhorse      ]", "stalhorse"),     cell("[Blupee         ]", "blupee"),          cell("[Kilton         ]", "kilton"),             cell("[Heroine Sword  ]", "heroineSword"))
        
    # Weapon Connoisseur
    if (not expand_cat) and check_all_complete_starts_with("weapon"):
        print("\033[92m--- Weapon Connoisseur Complete ---------------------------------------\033[0m")
    else:
        print("")
        print(cell("[Traveler Sword ]", "weaponTravelerSword"), cell("[Fire Rod       ]", "weaponFireRod"), cell("[Moblin Club    ]", "weaponMoblinClub"), cell("[Duplex Bow     ]", "weaponDuplexBow"))
        print(cell("[Windcleaver    ]", "weaponWindcleaver"), cell("[Battle Axe +   ]", "weaponAncientBattleAxe"), cell("[Frostspear     ]", "weaponFrostspear"), cell("[Ancient Sword  ]", "weaponAncientShortSword"))
    
    # Elite pictures
    if (not expand_cat) and check_all_complete_starts_with("elite") and check_all_complete_starts_with("ex"):
        print("\033[92m--- Elite Enemy Pictures Complete -------------------------------------\033[0m")
    else:
        print("")
        print(cell("[Silver Bokoblin]", "eliteBokoblin"), cell("[ Thunderblight ]","eliteThunderblight"), cell("[  Farosh       ]", "eliteFarosh"),  cell("[EX Molduking   ]", "exMolduking"))
        print(cell("[Silver Moblin  ]", "eliteMoblin"),   cell("[ Waterblight   ]","eliteWaterblight"),   cell("[  Naydra       ]", "eliteNaydra"),  cell("[EX Talus Titan ]", "exTalus"))
        print(cell("[Silver Lizalfos]", "eliteLizalfos"), cell("[ Fireblight    ]","eliteFireblight"),    cell("[  Dinraal      ]", "eliteDinraal"), cell("[EX Windblight  ]", "eliteWindblight"))
        print(cell("[Silver Lynel   ]", "eliteLynel"),    cell("[ Calamity      ]","eliteGanon"))
        print(cell("[Master Kohga   ]", "eliteKohga"),    cell("[ Dark Beast    ]","eliteBeast"))
        
    # Upgrade material
    if (not expand_cat) and check_all_complete(["hyruleBass", "heartyBass", "opal", "tail", "acorn", "beetle", "honey", "silentPrincess"]):
        print("\033[92m--- Upgrade Material (Non-Dragon) Complete ----------------------------\033[0m")
    else:
        print("")
        print(cell("[Hyrule Bass 15 ]", "hyruleBass"), cell("[Hearty Bass 15 ]", "heartyBass"), cell("[Opal       45  ]", "opal"),  cell("[Lizal Tail 45  ]", "tail"))
        print(cell("[Acorn       30 ]", "acorn"),      cell("[Beetle      15 ]", "beetle"),     cell("[Honey      16  ]", "honey"), cell("[Princess   19  ]", "silentPrincess"))
    
    #Dragon
    if (not expand_cat) and check_all_complete_starts_with("farosh") and check_all_complete_starts_with("naydra") and check_all_complete_starts_with("dinraal"):
        print("\033[92m--- Dragon Parts Complete ---------------------------------------------\033[0m")
    else:
        print("")
        print("\033[0m     Farosh            Naydra            Dinraal")
        print(farosh_horn_cell(),                  dragon_cell("Horn ", "naydraHorn"),  dragon_cell("Horn ", "dinraalHorn"))
        print(dragon_cell("Claw ", "faroshClaw"),  dragon_cell("Claw ", "naydraClaw"),  dragon_cell("Claw ", "dinraalClaw"))
        print(dragon_cell("Fang ", "faroshFang"),  dragon_cell("Fang ", "naydraFang"),  dragon_cell("Fang ", "dinraalFang"))
        print(dragon_cell("Scale", "faroshScale"), dragon_cell("Scale", "naydraScale"), dragon_cell("Scale", "dinraalScale"))
    print("\033[0m-------------------------------- Notes --------------------------------")
    if(len(notes) == 0):
        print("(None)")
    else:
        for i, n in enumerate(notes):
            print("[", i,"]", n)
    print("=======================================================================")
  
  
def search(keys):
    current_list = list()
    for sk in searchKeys:
        current_list.append(sk)
        
    for k in keys:
        k_lower = k.lower()
        new_list = list()
        for c in current_list:
            if k_lower in c:
                new_list.append(c)
        if len(new_list) <= 1:
            return new_list
        current_list = new_list
    return current_list

def save_to_file():
    part_file = open("part", "w")
    part_file.write(part)
    part_file.close()
    notes_file = open("notes", "w")
    notes_file.write(json.dumps(notes))
    notes_file.close()
    data_file = open("data", "w")
    data_file.write(json.dumps(data))
    data_file.close()

# Initialize
if(exists("part")):
    part_file = open("part", "r")
    part = part_file.read()
    part_file.close()

if(exists("notes")):
    notes_file = open("notes", "r")
    notes = json.load(notes_file)
    notes_file.close()
    
if(exists("data")):
    data_file = open("data", "r")
    data = json.load(data_file)
    data_file.close()

# Main Loop
while(True):
    save_to_file()
    clear()
    print_upper()
    print("")
    print("")
    print(output)
    if not hide_help:
        help()
    else:
        print("\033[3A")
    command = input("\033[0m> "),
    args = command[0].split()
    if(len(args) < 1):
        output = ""
        continue
    
    if(command[0] == "exit"):
        break
    elif(command[0] == "reset"):
        for k in data:
            data[k] = 0
        notes = list()
        output="\033[92mResetted"
        part=""
    elif(args[0] == "o" or args[0] == "ok" or args[0] == "uo" or args[0] == "uok"):
        # search
        search_result = search(args[1:])
        if(len(search_result) == 0):
            output="\033[91mSearch failed: "+str(args[1:])
        elif(len(search_result) > 1):
            mapped_keys = list(map(lambda k: searchKeys[k], search_result))
            output="\033[91mFound too many results: "+str(mapped_keys)
        else:
            found_key = searchKeys[search_result[0]]
            if(args[0] == "o" or args[0] == "ok"):
                data[found_key] = complete[found_key]
                output="\033[92mMarked as complete: "+ str(found_key)
            else:
                data[found_key] = 0
                output="\033[92mmarked as incomplete: "+str(found_key)
            
    elif(args[0] == "p" or args[0] == "part"):
        if(len(args) < 2):
            part = ""
        elif (args[1] == "Co"):
            part = "Core"
        elif (args[1] == "ShGe"):
            part = "Shaft + Gear"
        elif (args[1] == "ShSc"):
            part = "Shaft + Screw"
        elif (args[1] == "ShScSp" or args[1] == "ShSpSc"):
            part = "Shaft + Screw + Spring"
        elif (args[1] == "ShSp"):
            part = "Shaft + Spring"
        elif (args[1] == "Sh"):
            part = "Shaft Only"
        else:
            output="\033[91mUnknown Part Combination: "+args[1]
            continue
            
        if(args[1] != "Co"):
            data["shaft"] = complete["shaft"]
        else:
            data["core3"] = complete["core5"]
            data["core5"] = complete["core5"]
        if("Sp" in args[1]):
            data["spring"] = complete["spring"]
        
        if(args[1] == "Co" or args[1] == "ShGe" or args[1] == "ShScSp" or args[1] == "ShSpSc"):
            data["eliteBokoblin"] = 1
            data["eliteMoblin"] = 1
            data["eliteLizalfos"] = 1
            data["eliteLynel"] = 1
            data["eliteFarosh"]= 1
            data["eliteNaydra"]= 1
            data["eliteDinraal"]= 1
            data["eliteWindblight"]= 1
            data["eliteThunderblight"]= 1
            data["eliteWaterblight"]= 1
            data["eliteFireblight"]= 1
            data["eliteGanon"]= 1
            data["eliteBeast"]= 1
            data["eliteKohga"]= 1
            data["exMolduking"]= 1
            data["exTalus"]= 1
        
        output="\033[92mSet part combination as: "+ part
    elif (args[0] == "h" or args[0] == "horn" or args[0] == "uh" or args[0] == "uhorn"
          or args[0] == "c" or args[0] == "claw" or args[0] == "uc" or args[0] == "uclaw"
          or args[0] == "f" or args[0] == "fang" or args[0] == "uf" or args[0] == "ufang"
          or args[0] == "s" or args[0] == "scale" or args[0] == "us" or args[0] == "uscale"):
        if(len(args) < 2):
            output="\033[91mPlease specify which dragon"
            continue
        dragon = ""
        if(args[1] == "f" or args[1] == "farosh"):
            dragon = "farosh"
        elif(args[1] == "n" or args[1] == "naydra"):
            dragon = "naydra"
        elif(args[1] == "d" or args[1] == "dinraal"):
            dragon = "dinraal"
        else:
            output="\033[91mUnknown dragon: "+args[1]
            continue

        if(args[0][0] == "h" or (args[0][0:2] == "uh")):
            dragon+="Horn"      
        elif(args[0][0] == "c" or (args[0][0:2] == "uc")):
            dragon+="Claw"  
        elif(args[0][0] == "f" or (args[0][0:2] == "uf")):
            dragon+="Fang"
        elif(args[0][0] == "s" or (args[0][0:2] == "us")):
            dragon+="Scale"    

        if(args[0][0] == "u"):
            if(data[dragon] <=0 ):
                output="\033[91mCannot decrease dragon part count below 0"
            else:
                data[dragon] -= 1
                output="\033[92mDecremented count for: "+ dragon
        else:
            data[dragon]+=1
            output="\033[92mIncremented count for: "+ dragon
    elif(args[0] == "n" or args[0] == "note"):
        if(len(args) < 2):
            output="\033[91mPlease specify note content"
            continue
            
        content = reduce(lambda acc, n: acc+" "+n, args[1:])
        notes.append(content)
        output="\033[92mAdded Note"
    elif(args[0] == "un" or args[0] == "unote"):
        if(len(args) < 2):
            output="\033[91mPlease specify note index to remove"
            continue
        try:
            index = int(args[1])
            if(index < 0 or index >= len(notes)):
                output="\033[91mNote index out of bounds"
                continue
            notes.pop(index)
            output="\033[92mRemoved note"  
        except ValueError:
            output="\033[91mInvalid index: "+args[1]
            continue
            
    elif(args[0] == "hide"):
        hide_help = True
    elif(args[0] == "uhide"):
        hide_help = False
    elif(args[0] == "core"):
        data["core3"]+=1
        data["core5"]+=1
    elif(args[0] == "expand"):
        expand_cat = True
    elif(args[0] == "uexpand"):
        expand_cat= False
    else:
        output="\033[91mUnknown Command"
    
clear()
    
    