{
    
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) #taking d as input
        m=int(input()) # taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        
if __name__=='__main__':
    main()
}

def mean(d,m):
    sum1=m*3
    mean=int((sum1+d)/4)
    return mean