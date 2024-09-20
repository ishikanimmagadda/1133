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
        
#print(fanfic('short1.txt'))
#print(fanfic('short2.txt'))

        
    
        
        
def total_txt_size(directory): 
    final = 0
    for key, value in directory.items(): 
        if type(value) == int:
            if ".txt" in key:
                final = final + value
        else: 
            final = final + total_txt_size(directory[key]) 
    return final

root1 = {'time_travel':{'micro_black_holes.zip':100,
                        'quantum_realm.pdf':150,
                        'magic.txt':200},
         'space_travel':{'tesseract.java':400,
                         'magic.txt':100,
                         'warp_drive.py':300,
                         'mass_relay.txt':100}}
print(total_txt_size(root1))

root2 = {}
print(total_txt_size(root2))

root3 = {'labs':{'lab1.txt':223,
                'lab2.txt':251,
                'lab3.txt':317,},
        'hws':{},
        'plans':{'vacation.txt':636,
                 'evil':{'world_domination.txt':766}},
        'resume.txt':607,
        'cat.jpg':607}
print(total_txt_size(root3))
            
root4 = {'a':{'b':{'c':{'d':{'e':{'f.c':10}},'g.txt':12}}}}
print(total_txt_size(root4))

    

        