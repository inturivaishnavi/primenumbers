# Declare the variables
lower=int(input("enter the lower interval:"))
upper=int(input("enter the upper interval:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
    
 
