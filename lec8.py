'''

lec 8
functions

'''

#def my_function(a, b):
   # result = a+ b
    #return result 
    
#print(my_function(1,2))
 
def cal_plus(input1, input2=0): #default value assigned 
    #return input1 + input2
    print(input1)
    print(input2)
    result = input1+input2
   
    return result

#print (cal_plus(input2=1,input1=3)) keyword argument 
print(cal_plus(2))

'''
input1 is a local parameter and does 
not exist outside the function

#print(input1)

ERROR: input1 is not defined outside of the 
function

'''
 
def cal_plus(input1, input2=0): 
    return input1 + input2
    print(input1)
    print(input2)
    result = input1+input2
   
    #return result
print(cal_plus(2,1))


def cal_abs(a):
    
    if type(a)is str:
        return('wrong data type')
    
    elif a > 0:
        return a
    
    else:
        return -a
        
#print(cal_abs(-5678))

def call_sigma(m,n):
    result = 0
    
    for i in range(1,6):
        result = result +i
        
    return result
        
print (call_sigma(5,3))

def call_pi(m,n):
    result = 1
    
    for i in range (n,m +1):
        
        result = result * i
        
    return result
        
#print (call_pi(10,3))

def cal_f(m): 
    if m ==0:
        return 1
    else: 
        return m * cal_f(m-1)
        
    #print(cal_f(5))

def cal_p(m,n):
    return cal_f(m)/calf(m-n)
    
print(cal_p(5,3))
