from coco_functions import F1



class Function():

    def __init__(self, function):
        self.function = function
        
        

    def __call__(self, x_vector):
        return self.function(x_vector)


a = Function(F1(1))

print(a)
print(a((2,3)))