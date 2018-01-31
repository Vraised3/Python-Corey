nums = [1, 2, 3, 4, 5]
##############################For Loops######################
for num in nums:
    if(num == 3):
        print('Found')
        continue  # Similar to C++
    print(num)
print('\n')

for num in nums:
    for letter in 'abc':
        print(num, letter)
print('\n')

# For Running Through a loop a certain number of times
for i in range(10):  # Starts at 0 by default
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

x = 0
while True: # Infinite loop
    if x == 5: # If no Break statement Ctrl-C will give a keyboard interrupt
        break
    x += 1
    print(x)
