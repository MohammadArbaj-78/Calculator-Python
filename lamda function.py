
# lamda function

sum= lambda a:a*a        # are synonems function by labda keyword and assign sum variable

ans=sum(2)               # and call lambda function
print(ans)               # print answer

# function pass function

def new(f,v):            # are simple function pass function
    return 2*f(v)        # and return pass function value into 2

print(new(lambda x:x*x,2))        # call new function and pass lambda function
print(new(sum,2))                 # call new function and pass sum function   