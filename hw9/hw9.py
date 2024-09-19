def first_words(fname): 
    file1 = open(fname, 'r')
    first_words = []
    lines = file1.readlines()
    for line in lines: 
        splitline = line.split(" ")
        first_words.append(splitline[0])
    return first_words

# print(first_words('short1.txt'))
# print(first_words('short2.txt'))

def next_words(fname): 
    file1 = open(fname, 'r')
    dic = {}
    for word in file1.split(" "): 
        
        
    
    

        