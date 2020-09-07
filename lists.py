guests = ['Laura Les', 'Dorian Electra', 'Catherine Slater']
for x in range(0, 3):
    print(guests[x] + " would you like to attend my dinner party?")

print("\n" + guests[2] + " won't be able to make it.\nWe will be inviting Ayesha Erotica instead.\n")
del guests[2]
guests.append("Ayesha Erotica")
for x in range(0, 3):
    print(guests[x] + " would you like to attend my dinner party?")

print("\nWell look at that! We found a bigger dinner table!\n")
guests.insert(0, "That Kid")
guests.insert(2, "Osquinn")
guests.append("Hisoka Morrow")

for x in range(len(guests)):
    print(guests[x] + " would you like to attend my dinner party?")

print("\nOopsie daisies. The table won't make it in time. Unfortunately, we only have room for two people!\n")
for x in range(5, 1, -1):
    popped = guests.pop(x)
    print("Sorry " + popped + ", we don't have space at the table for you.")
print()

print("We are still inviting "+ str(len(guests)) + " guests!")

for x in range(1, -1, -1):
    print(guests[x] + " you guys can still attend the dinner party.")
    del guests[x]
print(guests)
