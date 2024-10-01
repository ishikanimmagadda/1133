

class Complex: 
    def __init__(self, real, imag): 
        self.real = real
        self.imag = imag
    
    def get_real(self): 
        return self.real
    
    def get_imag(self): 
        return self.imag
    
    def set_real(self,new_real): 
        self.real = new_real
    
    def set_imag(self,new_imag): 
        self.imag = new_imag
        
    def __str__(self):
        final = str(self.real) + " + " + str(self.imag) + "i"
        return final
    
    def __add__(self, other): 
        return Complex(self.real + other.real, self.imag + other.imag)
        
    def __mul__(self, other): 
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (other.real * self.imag)
        return Complex(real, imag)
    
    def __eq__(self,other): 
        if (self.real == other.real) and (self.imag == other.imag):
            return True 
        else: 
            return False
    
    
# x = Complex(2.7,3)
# y = Complex(-4,0)
# z = Complex(0,-1.5)

# print(x.real)       	# 2.7
# print(x.get_real()) 	# 2.7
# print(y.get_imag()) 	# 0

# x.set_real(6)
# z.set_imag(-2.5)

# print(x.real)       	# 6
# print(x.get_real()) 	# 6
# print(z.get_imag()) 	# -2.5

# print(x)            	# 6 + 3i
# print(y)            	# -4 + 0i
# print(z)            	# 0 + -2.5i
# print(x+y)          	# 2 + 3i
# print(z+y+x)        	# 2 + 0.5i
# print(y*z)          	# 0.0 + 10.0i
# print(x*z)          	# 7.5 + -15.0i
# print(x*y+x*z)      	# -16.5 + -27.0i
# print(x*(y+z))      	# -16.5 + -27.0i
# print(x == y)       	# False
# print(x*y+x*z == x*(y+z))   # True

class Employee: 
    def __init__(self, stringdata): 
        data = stringdata.split(",")
        self.name =  data[0]
        self.position = data[1]
        self.salary = float(data[2])
        self.seniority = float(data[3])
        self.value = float(data[4]) 
        
    def __str__(self): 
        return self.name + ", " + self.position

    def net_value(self): 
        val = self.value - self.salary
        return val
    
    def __lt__(self, other): 
        if self.value - self.salary < other.value - other.salary: 
            return True 
        else: 
            return False
        
    

# emp1 = Employee('Milton,Underling,310423.01,5.0,22.99\n')
# emp2 = Employee('Bill,Boss,403567.34,5.0,519.35\n')

# print(emp1.name)            # Milton
# print(emp1.position)        # Underling
# print(emp1.salary)          # 310423.01
# print(emp1.seniority)       # 5.0
# print(emp1.value)           # 22.99
# print(emp1)                 # Milton, Underling
# print(emp1.net_value())     # -310400.02
# print(emp2.net_value())     # -403047.99
# print(emp1 < emp2)          # False
# print(emp2 < emp1)          # True


class Branch: 
    def __init__(self, fname): 
        file1 = open(fname, 'r')
        lines = file1.readlines()
        self.team = []
        for i, line in enumerate(lines): 
            if i == 0:     
                location = line.split(",")
                self.location = location[1]
            if i == 1: 
                upkeep = line.split(",")
                self.upkeep = upkeep[1]
            if i > 2: 
                emp = Employee(line)
                self.team.append(emp)
    
    def __str__(self): 
        location = self.location
        employee_strings = ""
        for emp in self.team:
            employee_strings += str(emp) + "\n"
        return location + "\n" + employee_strings
    
    def profit(self): 
        sum = 0
        for emp in self.team: 
            sum = sum + emp.net_value()
        return sum - float(self.upkeep)
            
    def __lt__(self, other): 
        if self.profit() < other.profit(): 
            return True 
        else: 
            return False 
    
    def cut(self,num): 
        self.team.sort(key=lambda emp:emp.net_value())
        self.team = self.team[num:]
        return self.team
        
        
# branch2 = Branch('branch2.csv')
# print(branch2.location)         #Pawnee
# print(branch2.upkeep)           #98229.98
# print()
# print(branch2)
# print(branch2.profit())
# branch2.cut(7)
# print(branch2)


# print()
# print(branch2.profit())         #12577.81
# branch1 = Branch('branch1.csv')
# print(branch1.upkeep)           #57867.07
# ##
# print()
# print(branch1)
# ####                Scranton
# ####                Dwight, Efficiency Evolution Specialist
# ####                Jim, Data Innovation Specialist
# ####                Pam, Operational Analytics Technician
# ####                Ryan, Data Evolution Consultant
# ####                Stanley, Efficiency Logistics Technician
# ####                Michael, Enterprise Communications Technician
# ####                Kevin, Operational Services Technician
# ####                Meredith, Data Evolution Technician
# ####                Angela, Enterprise Communications Consultant
# ####                Oscar, Creative Innovation Coordinator
# ####                Phyllis, Enterprise Analytics Technician
# branch1.cut(8)
# ##
# print()
# print(branch1)
# ####                Scranton
# ####                Pam, Operational Analytics Technician
# ####                Michael, Enterprise Communications Technician
# ####                Stanley, Efficiency Logistics Technician

class Company: 
    def __init__(self, name, branches): 
        self.name = name 
        self.branches = branches
    
    def __str__(self):
        branch_str = ""
        for branch in self.branches: 
            branch_str += str(branch) + "\n"
            
        return self.name + "\n" + "\n" + branch_str
    
    def synergize(self): 
        profit_margins = [] 
        for branch in self.branches: 
            profit_margins.append(branch.profit())
            
        min_profit = min(profit_margins)
        index = profit_margins.index(min_profit)
        final_branch = self.branches[index]
        num_employees_to_cut = len(final_branch.team)
        return final_branch.cut(num_employees_to_cut//2)
          
        
    

# b1 = Branch('branch1.csv')
# b2 = Branch('branch2.csv')
# b3 = Branch('branch3.csv')
# b4 = Branch('branch4.csv')
# hs = Company('Synergistic Management Solutions',[b1,b2,b3,b4])
# print(hs.name)           #Synergistic Management Solutions

# print()
# print(hs)


# print()
# hs.synergize()
# print()

# print(hs)

# print()
# hs.synergize()
# print()

# print(hs)

# print()
# hs.synergize()
# print()






  
            
        
