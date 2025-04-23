prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

# Fibonacci with for loop
# for fibo in range(18):
    # newFibo = prev1 + prev2
    # print(newFibo)
    # prev2 = prev1
    # prev1 = newFibo
    
# Fibonacci with recursion
# count = 2

# def fibonacci(prev1, prev2):
    # global count
    # if count <= 19:
        # newFibo = prev1 + prev2
        # print(newFibo)
        # prev2 = prev1
        # prev1 = newFibo
        # count += 1
        # fibonacci(prev1, prev2)
    # else:
        # return
        
# fibonacci(1,0)

# finding the nth FIbo number with recursion
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)
        
print(F(19))