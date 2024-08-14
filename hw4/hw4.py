# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()
    
    for i in range(97,122):
        for j in range(97,122):
            for k in range(97,122):
                for l in range(97,122):
                    password = chr(i) + chr(j) + chr(k) + chr(l)
    #TODO: Try all possible four letter passwords, not just 'pwnd'
    #password = 'pwnd'
                    if decrypt(data,password):
                        return password


# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================
def is_prime(number): 
    sqri = int(number ** .5)
    for i in range(2, sqri+1):
        if (number/i).is_integer():
            return False 
        
    return True 

# print(is_prime(9))
# print(is_prime(11))
# print(is_prime(13))
# print(is_prime(547120117))


def count_primes(low, high):
    count = 0
    if (low > high): 
        return 0 
    else: 
        for i in range(low,high + 1): 
            if i == 1: 
                continue
            if is_prime(i): 
                print(str(i) + " is prime")
                count = count + 1
        
    return count

# print(count_primes(1, 20))
# print(count_primes(547120100, 547120200))
# print(count_primes(79, 97))
# print(count_primes(3201814, 200))
# print(count_primes(37, 37))

# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================
def population(small, middle, big):
    week = 1 

    
    while (week != 101 and small >= 10 and middle >= 10 and big >= 10): 
        changebig = (-0.1 * big) + (0.0002 * middle * big)
        changemedium = (-.05 * middle) + (.0001 * small * middle) - (.00025* middle * big)
        changesmall = (.1*small) - (.0002 * small * middle)

        small = small + changesmall
        big = big + changebig
        middle = middle + changemedium
        
        print ("Week " + str(week) + " Small: " + str(small) + " Middle: " + str(middle) + " Big: " + str(big))
        week = week + 1
    return week - 1

# print(population(800, 600, 1000))
# print(population(20,30000,10))
# print(population(400, 1000, 9))
# print(population(1200,400,300))


# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')

# print(find_password('encrypted1.txt'))
# print(find_password('encrypted2.txt'))
# print(find_password('encrypted3.txt'))
# print(find_password('encrypted4.txt'))

