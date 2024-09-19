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

             
            
print(next_words('short1.txt'))
#print(next_words('short2.txt'))
    
        
        
    
    

        