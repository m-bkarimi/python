def countdown(n:int) -> int:

    while n>=0:
        yield n
        n = n-1
             
if __name__=='__main__':
    for i in countdown(5.0):
        print(i)
