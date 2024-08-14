def sound(weight):
    if(weight < 13): 
        return "Yip"
    if(weight >= 13 and weight <=30): 
        return "Ruff"
    if(weight >= 31 and weight <=70):
        return "Bark"
    if (weight > 70): 
        return "Boof"

print(sound(13))
print(sound(12))
print(sound(50))
print(sound(10000))

def choice(text,option1,option2,option3):
    print(text)
    print()
    print("1. " + option1)
    print("2. " + option2)
    print("3. " + option3)
    userinput = input("Choose 1, 2, or 3:")
    while (userinput != '1' and userinput != '2' and userinput != '3'): 
        print ("Invalid Input")
        userinput = input("Choose 1, 2, or 3:")
    return userinput

# print(choice("You have no idea how to approach this problem.",
#        "Go to office hours",
#        "Send an email to the TAs",
#        "Post the problem online, there's no way I'll be caught")
# )


def adventure(): 
    state = 1
    state1choice = choice("You sneak into the dragon's lair, with your comrades Wizard McBlastyFace and Steve the Bard. The dragon is fast asleep.", 
           "Tickle the dragon on the nose.", "Tell your team to start stealing things", "Tell your team to prepare for battle.")
    
    if state == 1:
        if state1choice == "1":
            print ("False")
            return False
        elif state1choice == "2": 
            state = 2
        elif state1choice == "3":
            state = 3
            
    if state == 2: 
        state2choice = choice("State 2", 
           "", "", "")
        if state2choice == "1": 
            print ("True")
            return True 
        elif state2choice == "2": 
            state = 4
        elif state2choice == "3": 
            state = 4
    
    if state == 3: 
        state3choice = choice("State 3", 
           "", "", "")
        if state3choice == "1": 
            print ("False")
            return False 
        elif state3choice == "2": 
            state = 4
        elif state3choice == "3": 
            state = 5
    
    if state == 4: 
        state4choice = choice("State 4", 
           "", "", "")
        if state4choice == "1": 
            print ("True")
            return True
        elif state4choice == "2": 
            state = 5
        elif state4choice == "3": 
            print ("False")
            return False 
    
    if state == 5: 
        state5choice = choice("State 5", 
           "", "", "")
        if state5choice == "1": 
            print ("True")
            return True 
        elif state5choice == "2": 
            print ("False")
            return False
        elif state5choice == "3": 
            print ("True")
            return True
        
    
adventure() 
  