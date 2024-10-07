class Adventurer: 
    def __init__(self, name, level, strength, speed, power): 
        self.name = name 
        self.level = level
        self.strength = strength
        self.speed = speed 
        self.power = power 
        self.HP = level * 6 
        self.hidden = False 
        
    def __repr__(self): 
        string = self.name + " - HP: " + str(self.HP)
        return string
    
    
    def attack(self,target): 
        if target.hidden == True: 
            string = self.name + " can't see " + target.name
            print(string)
        else: 
            damage_amount = self.strength + 4
            string = self.name + " attacks " + target.name + " for " + str(damage_amount) + " damage"
            target.HP = target.HP - damage_amount
            print(string)

# thog = Adventurer("Thog",3,5,1,2)
# print(repr(thog))
# goku = Adventurer("Goku",20,10,7,9001)
# print(goku)
# print(thog.attack(goku))
# print(str(goku))
# print(goku.HP)
# goku.hidden = True
# print(thog.attack(goku))
# print(goku.attack(thog))
# print(thog)
# print(goku.attack(thog))
# print(thog.HP)


class Fighter(Adventurer): 
    def __init__(self, name, level, strength, speed, power): 
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 12 
        self.hidden = False 
    
        
    def attack(self,target): 
        if target.hidden == True: 
            string = self.name + " can't see " + target.name
            return string
        else: 
            damage = 2 * self.strength + 6
            target.HP = target.HP - damage
            string = self.name + " attacks " + target.name + " for " + str(damage) + " damage"
            return string 
        
class Thief(Adventurer): 
    def __init__(self, name, level, strength, speed, power): 
        super().__init__(name, level, strength, speed, power)
        self.HP = level * 8
        self.hidden = True 
     
    def attack(self,target): 
        if self.hidden == False: 
            super().attack(target)
        elif self.hidden == True and target.hidden == True and self.speed < target.speed: 
                string = self.name + " can't see " + target.name
                print(string)
        else: 
            damage = (self.speed + self.level) * 5 
            self.hidden = False 
            target.hidden = False 
            target.HP = target.HP - damage
            string = self.name + " attacks " + target.name + " for " + str(damage) + " damage"
            return string 

class Wizard(Adventurer): 
    def __init__(self, name, level, strength, speed, power): 
        super().__init__(name, level, strength, speed, power)
        self.hidden = True 
        self.fireballs_left = power
    
    def attack(self,target): 
        if self.fireballs_left == 0: 
            super().attack(target)
        else: 
            self.hidden = False 
            damage = self.level * 3 
            target.HP = target.HP - damage
            target.hidden = False
            self.fireballs_left = self.fireballs_left - 1
            string = self.name + " casts fireball on " + target.name + " for " + str(damage) + " damage"
            print(string)

# albus = Wizard("Dumbledore",15,4,6,2)
# smeagol = Thief("Gollum",12,1,4,1)
# bruce = Thief("Batman",10,4,5,1)

# print(albus)
# print(smeagol)
# print(bruce)
# print(albus.attack(smeagol))
# print(albus)
# print(smeagol.attack(albus))
# print(smeagol)

def duel(adv1, adv2): 
    while adv1.HP > 0 and adv2.HP > 0:
        print(adv1)
        print(adv2)
        
        adv1.attack(adv2)
        if adv2.HP <= 0: 
            print(adv1)
            print(adv2)
            string = adv1.name + " wins!"
            print(string)
            return True 
    
        adv2.attack(adv1)
        if adv1.HP <= 0: 
            print(adv1)
            print(adv2)
            string = adv2.name + " wins!"
            print(string)
            return False
    
    if adv2.HP <= 0 and adv1.HP <= 0: 
        print(adv1)
        print(adv2)
        string = "Everyone loses"
        print(string)
        return False

     
albus = Wizard("Dumbledore",15,4,6,2)
smeagol = Thief("Gollum",12,1,4,1)
bruce = Thief("Batman",10,4,5,1)
durden = Fighter("Tyler",6,3,2,1)
jack = Thief("Jack",7,2,5,1)
will = Thief("Will",8,3,4,2)
elizabeth = Thief("Elizabeth",5,3,3,2)
sean_bean = Fighter("Boromir",5,5,3,1)
orc1 = Fighter("Orc",1,5,1,1)
orc2 = Fighter("Orc",1,5,1,1)
orc3 = Fighter("Orc",1,5,1,1)
orc4 = Fighter("Orc",1,5,1,1)

# print(albus)
# print(smeagol)
# print(bruce)
# print(duel(albus,smeagol))
# print(duel(bruce,albus))
# print(duel(durden,durden))
# print(duel(will,jack))
# print(duel(jack,will))
# print(jack.hidden)
# print(elizabeth.hidden)
# print(duel(jack,elizabeth))
# print(duel(orc1,sean_bean))
# print(duel(orc2,sean_bean))
# print(duel(orc3,sean_bean))
# print(duel(orc4,sean_bean))
# print(duel(sean_bean,orc1))



def tournament(adv_list): 
    if len(adv_list) == 0: 
        return None
    
    if len(adv_list) == 1: 
        return adv_list[0]
    
            
    while len(adv_list) > 1:  
        sorted_adv_list = sorted(adv_list, key=lambda adv: adv.HP, reverse=True)
        second_highest = sorted_adv_list[1]
        highest = sorted_adv_list[0]
        
        winner = duel(second_highest, highest)
        
        if winner == highest: 
            adv_list.remove(highest)
        else: 
            adv_list.remove(second_highest)
            
    return adv_list[0]

print(tournament([]))
mario = Wizard("Mario",8,4,4,2)
link = Fighter("Link",7,4,2,1)
fox = Thief("Fox",9,2,4,2)
ness = Wizard("Ness",6,1,1,4)
smashls = [mario,link,fox,ness]
#winner = tournament(smashls)

jaina = Wizard("Jaina",15,1,2,6)
frisk = Fighter("Frisk",1,1,1,1)
madeline = Thief("Madeline",4,1,10,1)
gandalf = Wizard("Gandalf",19,4,3,1)
arthur = Fighter("Arthur",3,4,4,4)
wesley = Thief("Wesley",14,4,5,1)
winner = tournament([jaina,frisk,madeline,gandalf,arthur,wesley])




