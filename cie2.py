import sys

def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
c = (sys.argv[3])  
print("Largest number is:", largest(a, b, c))