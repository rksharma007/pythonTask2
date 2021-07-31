#Python program to print all positive numbers in list

List = []
j = 0
n = int(input("Enter the number of integers in list: "))

print("Enter %d elements: "%n)

for i in range(1, n + 1):
    value = int(input())
    List.append(value)

print("\nPositive Numbers in this list are : ")
while(j < n):
    if(List[j] >= 0):
        print(List[j], end = '   ')
    j = j + 1

