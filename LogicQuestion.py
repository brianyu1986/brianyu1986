def printTriangle(number):
   for i in range(1, number+1):
       tempStr = ""                    # Initialize String for every line
       tempStr += " " * (number-i)     # Count and add-in the space for each line
       tempStr += "* "*i               # Count and add-in * and space for each line
       print(tempStr)                  # Print the result for each line


def sortNum(num_list):
   # Initialize empty list for odd and even number
   num_odd = []
   num_even = []

   # Use a for loop to classify each number
   for num in num_list:
       # Use if statement to differentiated even number and odd number
       if int(num) % 2 == 0:
           num_even.append(num)
       else:
           num_odd.append(num)

   num_even = sorted(num_even)                 # Sort even number list
   num_odd = sorted(num_odd, reverse=True)     # Sort and reverse odd number list

   # Combine two number list together and put odd number in front of even number
   num_odd.extend(num_even)               
  
   # Return and join the number list to string
   return ''.join(num_odd)
