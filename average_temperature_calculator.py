'''
Average Temperature Calculator
>Ask user for how many days one wants to calculate the average
>input each day temperature
'''
days = int(input("How many day's you want an average? "))

counter = 1
temperatures = []

while counter <= days:
    tmp = int(input(f"Enter {counter}st day highest temprature:"))
    temperatures.append(tmp)
    counter += 1
average = sum(temperatures)/len(temperatures)
print(f"average temperature value is:{average}")

'''
Caculate how many days were above average
'''
dy = 0
for i in temperatures:
    if i > average:
        dy += 1

print(f"Total {dy} days were above avrage temperature!!")