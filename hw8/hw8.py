#Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    try: 
        file1 = open(fname, 'r')
        lines = file1.readlines()
        return lines
    except: 
        return -1 
    #You MUST use a try-except block to prevent an error
    #if the file doesn’t exist 

# print(get_data_list('smallfile.csv'))
# print(get_data_list('fakefile.notreal'))



#Part 2: hw8_index
#==========================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#==========================================
def hw8_index(row1_str):    
    try: 
        row_list = row1_str.split(",")
        hw8_index = row_list.index('hw8 Grade')
        return hw8_index
    except: 
        return -1  
    
# print(hw8_index("hw1 Grade,hw2 Grade,hw3 Grade,hw4 Grade,hw5 Grade,hw6 Grade,hw7 Grade,hw8 Grade,hw9 Grade\n"))
# print(hw8_index("HW8 grade,HW8 Graid,hw8 Grade,HW 8grade,Homework8 grade\n"))
# print(hw8_index('This,file,exists,,\n'))


#Part 3: alter_grade
#==========================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#==========================================
def alter_grade(row_str,idx):

    row_list = row_str.split(",")
    row_list[idx] = '40'
    altered_str = ",".join(row_list)
    return altered_str

print(alter_grade("30,20,0,0,\n",2))
print(alter_grade("5,2,5,6,0,0,minutes,\n",1))
print(alter_grade("Bulbasaur,Charmander,Squirtle,Weedle,Pidgey\n",3))

#Part 4: haxx
#==========================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file doesn't exist
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):
    try: 
        data_list = get_data_list(fname)
        column_index = hw8_index(data_list[0])
        if column_index == -1: 
            return False 
        f = open(fname, 'w')
        for row in data_list: 
            if "Ishika Nimmagadda" in row: 
                row_str_altered = alter_grade(row, column_index)
                f.write(row_str_altered)
            else: 
                f.write(row)
        
        f.close()    
        return True 
    except: 
        return False 
    
print(haxx('fakefile.notreal'))
print(haxx('smallfile.csv'))
print(haxx('grades1.csv'))
print(haxx('grades2.csv'))
print(haxx('grades3.csv'))
            
