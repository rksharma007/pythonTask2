#Python program for Fibonacci Series

def fibonacci(num):
    num1 = 0
    num2 = 1
    temp = 0

    for i in range(num):
        print(temp, end=' ');
        num1 = num2;
        num2 = temp;
        temp = num1 + num2;

num = int(input('Enter number of terms in Fibonacci series: '))
fibonacci(num)
