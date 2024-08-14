def length_contract(dist, speed): 
    c = (3 * (10**8))
    final_dist = dist * ((1-((speed**2)/ (c**2))) ** .5)
    return final_dist

# print(length_contract(100, 150000000))
# print(length_contract(30000, 0))
# print(length_contract(0, 200000000))
# print(length_contract(4.37, 297000000))
# print(length_contract(1000000, 299999999))

def parsectometers(parsec): 
    meters = (3.086 * (10**16)) * parsec
    return meters

def secondstoyear(seconds): 
    year = seconds/31557600
    return year

def bessel_run(speed): 
    meters = parsectometers(12)
    distance = length_contract(meters, speed)
    timeinseconds = distance / speed
    time = secondstoyear(timeinseconds)
    
    print(time)
    return time

# print(bessel_run(200000000))
# print(bessel_run(88))
# print(bessel_run(299999999))
# print(bessel_run(150000000) + bessel_run(100000000))
    
def helper1():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

def helper2(): 
    helper1()
    helper1()
    helper1()
    helper1()
    helper1()

def print_100():
    helper2()
    helper2()
    helper2()
    helper2()

print_100()
  