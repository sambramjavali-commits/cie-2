import sys
def largest(a, b, c):
    
  
    if a<b and a>c:
        print("a is largest")
    elif b<c and b>c:    
        print("b is largest")
    else:
        print("c is largest")

if __name__ =="__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
largest(a, b, c)

