# i % 2 == 0 : print () 

def evenOdd(n):
    for i in range(n):
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")


print(evenOdd(10))