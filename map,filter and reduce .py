
# map function

lis = [7,8,7,9,0]            # are list of numbers

def square(a):               # square function
    return a+a               # return square value

sr=list(map(square,lis))     # map function arguments are function or list
print(sr)                    # print result in list


# filter function

lis = [7,8,7,9,0]            # are list of numbers

greater=list(filter(lambda a:a<8,lis))     # filter function arguments are function or list

print('lessthen value to 8 : ',greater)    # print result valuse used by filter function

# reduce fucntion

from functools import reduce       # to use reduce function import reduce

lis=[1,2,3,5,6,7,8,9]              # list of numbers

def sum(a):                      # function to addition of values
    return a+2

add=reduce(sum,lis)                # reduce function arguments function applies on iterable

print(add)                         # and print all list values sum