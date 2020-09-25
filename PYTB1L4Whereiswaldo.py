import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
stoelnum = 1
print(people)
for index in range(len (people)):
    if (people [index]) == "Waldo":  
        print("hij is op stoel " + str(stoelnum))
    else:
        stoelnum = stoelnum + 1
