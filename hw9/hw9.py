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
    final_dic = {}
    
    with open(fname, 'r') as file1:
        # Reading the whole content and splitting by space
        words = file1.read().split()
        #print(words)
        
        for i in range(len(words)):
            current_word = words[i]
            
            # If the current word is not the last word
            if i < len(words) - 1:
                next_word = words[i + 1]
            else:
                next_word = "."
            
            # If the word is already in the dictionary, append to the list
            if current_word in final_dic:
                final_dic[current_word].append(next_word)
            else:
                final_dic[current_word] = [next_word]
    
    return final_dic

             
            
#print(next_words('short1.txt'))
#print(next_words('short2.txt'))
import random
def fanfic(fname): 
    file1 = open(fname, 'r')
    for i in range(0,10): 
        final = " "
        first_word = random.choice(first_words(fname))
        final = final + first_word 
        dict = next_words(fname)
        next_word = " "
        while(next_word != "."):
            val_list = dict[first_word]
            next_word = random.choice(val_list)
            final = final + " " + next_word
            first_word = next_word
        print(final)
        
print(fanfic('short1.txt'))
#print(fanfic('short2.txt'))

        
    
        
        
    
    

        