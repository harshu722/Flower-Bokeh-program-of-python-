given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
output = {}  
# Using loop for constructing output list  
for i in given_list:  
    if i % 2 == 0:
        output[i] = i ** 3  
print("Output List using for loop:", output)  
