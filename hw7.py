def collatz(n):
    seq = [n]
    if n == 1 and len(seq) <= 1: 
        return seq
    if n % 2 == 0: 
        new = n//2
        seq = [n] + collatz(new)
    else:
        new = n * 3 + 1
        seq = [n] + collatz(new)
    return seq 

# print(collatz(5))  
# print(collatz(1))  
# print(collatz(123))  

def find_min(num_list): 
    if len(num_list) == 1: 
        min = num_list[0]
        return min
    min = num_list[0]
    if find_min(num_list[1:]) > min: 
        return min
    else: 
        min  = find_min(num_list[1:])
    return min
 
print(find_min([8]))  
print(find_min([0, 2, -5, -2, 5, -1, 4, 0, -5, -1]))
print(find_min([30, 40, 20, 34, 32, 34, 48, 43, 21]))  
        