# Hero's Inventory
# Eric Broadbent
#11/18
import os
def hud():
    print("stats: ",player_stats)
    print("inventory: ",inventory)
    print("equiped:",equiped)
                
import random
player_health = 100
player_armor = 1250
player_atack = 250
player_money = 0
max_inventory = 10
equiped = []

inventory = ["rusty sword","leather armor","Wood shield","small healing potion"]
player_stats = ["health",player_health,"armor",player_armor,
                "atack",player_atack,"money",player_money]
print("as you set out on your journey you have the following")
print("player stats")
print (player_stats)
print()
print("Your items include:")
for item in inventory:
    print(item)
    
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You have", len(inventory), "/",max_inventory," items in your possession.")
print("so you can pick up ",max_inventory-len(inventory), " more items"  )
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("you get attacked and take damage")
player_stats[1]  -= 22
input("\nPress the enter key to continue.")
os.system('cls')
hud()

input("\nyou have taken some damage on your journey \n"+
      "your health is at " +str(player_stats[1]) +"\n"+
      "you need to use your healing potion \nPress the enter key to continue.")

if "small healing potion" in inventory:
     print("You will live to fight another day. by using the healing potion")
     player_stats[1] += 20
     print(player_stats)
     print()
     inventory.remove("small healing potion")
     for item in inventory:
        print(item)
input("\nPress the enter key to continue.")
os.system('cls')
hud()

for i in range(len(inventory)):
    print(str(i),inventory[i])
print("lets equipt some armor")
index = int(input("\nEnter the index number for an armor item in your inventory you wish to equip "))
while index >len(inventory)-1 or index <0:
    print("that numbe is out of range")
    index = int(input("\nEnter the index number for an armor item in inventory: "))
print("you equip your ",  inventory[index])
equiped.append(inventory[index])
inventory.remove(inventory[index])
if "leather armor" in equiped:
    player_stats[3] +=1000
if "Wood shield" in equiped:
    player_stats[3] +=500
input("\nPress the enter key to continue.")
os.system('cls')
hud()

start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])
print()
input("\nPress the enter key to continue.")
os.system('cls')
hud()

chest_items = ["gold", "gems","elven sword", "bow", "crossbow", "boots" , "hat"]
chest = []
for i in range (3):
    item = random.choice(chest_items)
    chest.append(item)
print("You find a chest which contains:")
print(chest)
print()
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print()
print(inventory)
print()
print("convert tresure to gold")
if "gold" in inventory:
    player_stats[7]+=100
    inventory.remove("gold")
if "gems" in inventory:
    player_stats[7]+=1000
    inventory.remove("gems")
print("player stats")
print (player_stats)
print()
print(inventory)

input("\nPress the enter key to continue.")
os.system('cls')
hud()

if player_stats[7] > 100:
    print("You want trade your sword for a crossbow. so you sell your sword for 20 gold and buy a crossbow for 100 gold")
    player_stats[7]+=20
    player_stats[7]-=100
    print (player_stats)
    inventory[0] = "crossbow"
    print("Your inventory is now:")
    print(inventory)
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You trade in the last 2 items from your inventory for a new item.")
inventory[len(inventory)-2:len(inventory)] = ["orb of future telling"]
print("Your inventory is now:")
print()
print(inventory)
print()
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("In a great battle, your shield is destroyed.")
for i in range(len(inventory)):
    if inventory[i] == "Wood shield":
        del inventory[i]
for i in range(len(equiped)):
    if equiped[i] == "Wood shield":
        del equiped[i]
    
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("Your first 2 items in your inventory are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
os.system('cls')

input("\nPress the enter key to Exit.")





