# Explanation:
# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
# You must implement it using Class
# Sample Input:
# x: 10
# n: 2
# Sample Output:
# 100


# Method 1:



class Maths1:
    def power(self, x, n):
        print(x**n)


x = int(input("Enter the first number: "))
n = int(input("Enter the Second number: "))

m = Maths1()
m.power(x,n)


# Method 2:

class Maths:
    x = int(input("Enter the first number: "))
    n = int(input("Enter the Second number: "))

    def power1 (self):
        print(f"the Power of {Maths.x} and {Maths.n} is {Maths.x**Maths.n}")


m1 = Maths()
m1.power1()

#Method 3:

class Maths2:
    def __init__(self, x, n):
        self.x = x
        self.n = n 

    def power2(self):
        return (f"the Power of {self.x} and {self.n} is {self.x**self.n}")

m2 = Maths2(10,2)
print(m2.power2())

