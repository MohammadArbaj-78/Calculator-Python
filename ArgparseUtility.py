
# import argparse

import argparse

parser=argparse.ArgumentParser()                               # create argument object by argumentparser
parser.add_argument("name")                                    # positional argument
parser.add_argument("num", type=int)                           # Type argument
parser.add_argument("--mode",choices=["easy", "medium", "hard"])           # choice argument
parser.add_argument('-a','--action', action='store_true')                  # flag boolean argument
parser.add_argument('-o','--output',help='output file',default='out.txt')  # optional and default argument

args=parser.parse_args()               # datatype me convert karti hai and error detect karti hai and arguments ko object me store karti hai

# ham mulple argument bana sakte hai or cli me de sakte hai

print('Cli Utility of Arbaj')                # print text

print('youe name :',args.name)               # print positional argument
print('tupe argument :',args.num)            # print type argument
print('optonal argument :',args.output)      # print optional argument
print('boolean argument :',args.action)      # boolean argument
print("Selected mode:", args.mode)           # print choice argument
if args.action:                              # check condition boolean argument  
    print("Verbose mode ON!")                # true print on
else:
    print("Verbose mode OFF")                # false print of
