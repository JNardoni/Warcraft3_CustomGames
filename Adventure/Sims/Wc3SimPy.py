
import json
from enum import Enum

class SimType(Enum):
    SingleTarget = 0

#Sim Info
sims = 1
simType = SimType.SingleTarget.value

#Game Info
attSpdAgi = .02

#Hero Info
Hero = "Paladin"
level = 3
items = ["","","","","",""]

#Boss Stats
armor = 5
magicRes = 25

class attr(Enum):
    Strength = 0
    Agility = 1
    Intelligence = 2

if __name__ == "__main__":

    # Opening JSON file
    f = open('heroes.json',)
  
    # returns JSON object as a dictionary
    data = json.load(f)
  
    Str = data[Hero]["Strength"]
    Agi = data[Hero]["Agility"]
    Int = data[Hero]["Intelligence"]
    StrGn = data[Hero]["Str/Lvl"]
    AgiGn = data[Hero]["Agi/Lvl"]
    IntGn = data[Hero]["Int/Lvl"]
    AttSpd = data[Hero]["Att Spd"]

    DmgHigh = data[Hero]["Dmg High"]
    DmgLow = data[Hero]["Dmg Low"]


    print(data['Paladin']['Strength'])
  
    # Closing file
    f.close()