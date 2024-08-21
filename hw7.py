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

print(collatz(5))  
print(collatz(1))  
print(collatz(123))  