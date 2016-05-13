def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

#print fibs(10)



def square(x):
    'Calculate the square of the number x'
    return x*x

#print square.__doc__
#help(square)


def print_params(*params):
    print params

#print_params('test')
#print_params(1,2,3)

def print_params_1(**params):
    print params

#print_params_1(x=1,y=2,z=3)

def print_params_2(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar

#print_params_2(1,2,3,5,6,7,foo=1,bar=2)


def add(x,y):return x+y

params=(1,2)
print add(*params)

def with_start(**kwds):
    print kwds['name'],'is',kwds['age'],'years old'

def without_start(kwds):
    print kwds['name'],'is',kwds['age'],'years old'

args={'name':'Yun','age':24}

with_start(**args)
without_start(args)










