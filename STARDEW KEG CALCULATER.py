shedsize = int(input("enter shed size(1 = big, 2 = normal): "))
craftedkeg = int(input("enter the amount of kegs you already have crafted: "))
kegneeded = 0
copper = 0
coppercost=0
iron = 0
ironcost=0
coal = 0
coalcost = 0
total = 0

if shedsize == 1:
    kegneeded = 137

else:
    kegneeded = 67
kegneeded = kegneeded-craftedkeg
resin = kegneeded
copper = kegneeded * 5
wood = kegneeded * 30
woodcost = wood * 50
coppercost = copper * 150
iron = kegneeded * 5
ironcost = iron * 250
coal = kegneeded
coalcost = coal * 250
total = coppercost + coalcost + ironcost + woodcost

print(f" you need {kegneeded} kegs, {copper} copper ore costing {coppercost}g, {iron} iron ore costing {ironcost}g, {wood} wood costing {woodcost}g, with a total cost of {total}")


