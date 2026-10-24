#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Orginal List:", L)

#variable to store the sum of 
# the list
count = 0 

# Finding the sum
for i in L:
    count+= i

    # divide the total elements by
    # number of elements
    avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()

# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])

