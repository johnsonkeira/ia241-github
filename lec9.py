'''

lec 9 
define a class

'''
#def report_maker(input):
    
#    return input

import lec8
print(lec8.cal_abs(-9))

import numpy 

print(numpy)

class car:          # define a class 
    maker = 'toyota'        # define an attribute 
    
#    def report_maker (self):
        
#        return self.maker 
    def __init__(self, input_model):
        self.model = input_model
    
    def report (self):
        return self.maker, self.model
        
        
my_camry = car ('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

my_highlander = car('highlander')
print(my_highlander.maker)
print(my_highlander.model)
print(my_highlander.report())

my_camry.maker = 'Ford'
print(my_camry.report())