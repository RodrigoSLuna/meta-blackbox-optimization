import numpy as np

from abc import ABC, abstractmethod
class Optimizer(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def next_point(self, dimension, domain):
        pass

    @abstractmethod
    def reset(self):
        pass

class RandomSearchOptimizer(Optimizer):

    def __init__(self):
        pass

    def next_point(self, dimension, domain, hf):
        new_x = (domain[1] - domain[0]) * np.random.random_sample(dimension) + domain[0]
        return new_x

    def reset(self):
        pass

class MetamodelOptimizer(Optimizer):

    def __init__(self, representation, points_strategy, nb_points, hist_strategy, hist_init, size_hf, best_point_strategy):
        self.representation = representation
        self.points_strategy = points_strategy
        self.nb_points = nb_points
        self.hist_strategy = hist_strategy
        self.hist_init = hist_init
        self.size_hf = size_hf
        self.best_point_strategy = best_point_strategy

    def next_point(self, dimension, domain, hf):

        #1) CHOOSE METAPOINTS AND CURR_HIST
        selected_points  = self.select_points(dimension, domain)
        selected_history = self.select_history(hf)

        #2) Meta-evaluate points in meta-model
        evaluations = self.representation.predict(selected_points, selected_history)

        #3) Get the next point (x_t+1)
        new_x = self.best_meta_point(selected_points, evaluations)

        return new_x

    def reset(self):
        pass   

    def select_points(self, dimension, domain):
        if self.points_strategy == "random":
            return (domain[1] - domain[0]) * np.random.random_sample((self.nb_points, dimension)) + domain[0] 

    def select_history(self, hf):
        #Init:
        if hf == []:
            return self.init_history()
        else:
            if self.hist_strategy == "random":
                hf = np.array(hf)
                idx = np.random.choice(len(hf), self.size_hf)
                return hf[idx]

    def init_history(self):
        if self.hist_init == "random":
            return np.array([(0,0,0)]*self.size_hf)


    def best_meta_point(self, selected_points, evaluations):
        if self.best_point_strategy == "random":
            index = np.random.randint(0, len(selected_points))
            return selected_points[index]


# class Meta_Random_Search_Optimizer(Optimizer):

#     def __init__(self):
#         pass

#     def meta_points(self):
#         pass

#     def hf(self):
#         pass

#     def predictions(self, meta_points, curr_hf):
#         pass

#     def best_point(self, meta_points, meta_evaluations):
#         pass

#     def update(self, info):
#         pass

# class R2andom_Search_Optimizer(Optimizer):
    
#     def __init__(self, max_steps=1000, verbose=0):
#         self.max_steps = max_steps
#         self.verbose = verbose
    
#     def optimize(self, f):

#         #Init best values and steps:
#         best_x = [None] * f.dimension 
#         best_y = 99999.0
#         steps = []

#         #Define Iterator:
#         if self.verbose == 1:
#             print("kkk")
#             #iterator = tqdm(range(self.max_steps))
#         else:
#             iterator = range(self.max_steps)
        
#         #Iteration:
#         for step in iterator:

#             #Choose random x and evaluate it:
#             new_x = (f.domain[1] - f.domain[0]) * np.random.random_sample(f.dimension) + f.domain[0]
#             new_y = f(new_x)/1000

#             #Check if it is an improvement:
#             if new_y < best_y: 
#                 best_y = new_y
#                 best_x = new_x
#                 steps.append([best_x, best_y, step])

#                 #Check if it is a solution:
#                 if round(best_y, 5) == round(f.fopt/1000, 5):
#                     return np.array(steps), True

#         return np.array(steps), False

# class Meta_Search_Optimizer:
    
#     '''Meta Search Optimizer
       
#        @init:
#        max_steps = max number of iterations
#        verbose = True shows progress bar
       
#        @optimize:
#            *input:
#                f = function to be optimized
#                warning: 
#                    - f.opt = optimal value
#                    - f.domain = interval to search, e.g. [-5, 5]
#                    - f.dimension = dimension of the function
#            *output:
#                (best_x, number of steps) if optimal point was found else (None, -1)
#     '''
    
#     def __init__(self, meta_model, init_hf_strategy="zero", best_meta_point_strategy="lowest", 
#                  hf_strategy="random", nb_samples=10, size_hf=5, max_steps=1000, verbose=1, 
#                  train=False, output_file = ""):
#         self.meta_model = meta_model
#         self.init_hf_strategy = init_hf_strategy
#         self.best_meta_point_strategy = best_meta_point_strategy
#         self.hf_strategy = hf_strategy
#         self.nb_samples = nb_samples
#         self.size_hf = size_hf
#         self.max_steps = max_steps
#         self.verbose = verbose

#         self.train = train
#         self.output_file = "train_data/" + output_file

        
#     def init_hf(self):
#         if self.init_hf_strategy == "zero":
#             return np.array([(0,0,0)]*self.size_hf)
        
#     def best_meta_point(self, meta_points, meta_evaluations, hf):
#         if self.best_meta_point_strategy == "lowest":
#             meta_evaluations = meta_evaluations.reshape(self.nb_samples)
#             indexes = np.argsort(meta_evaluations)
#             hf = np.array(hf)
#             if hf.size == 0:
#                 return meta_points[indexes[0]]
#             for idx in indexes:
#                 if meta_points[idx] not in hf[:, 0:2]:
#                     return meta_points[idx]
#             return meta_points[indexes[0]]
#         if self.best_meta_point_strategy == "random":
#             index = np.random.randint(0, len(meta_points))
#             return meta_points[index]
        
#     def optimize(self, f):
        
#         #Init best values:
#         best_x = [None] * f.dimension 
#         best_y = 99999.0
#         steps = []
        
#         #Init history
#         hf = []
#         curr_hf = self.init_hf()

#         #Init train data:
#         train_data = []
        
#         #Define Iterator:
#         if self.verbose == 1:
#             iterator = tqdm(range(self.max_steps))
#         else:
#             iterator = range(self.max_steps)
        
#         #Iteration:
#         for step in iterator:
            
#             #1) Select n random points to be evaluated by meta-model
#             meta_points = (f.domain[1] - f.domain[0]) * np.random.random_sample((self.nb_samples, f.dimension)) + f.domain[0]
            
#             #2) Meta-evaluate points in meta-model
#             meta_evaluations = self.meta_model.predict(meta_points, curr_hf)
            
#             #3) Get the next point (x_t+1)
#             new_x = self.best_meta_point(meta_points, meta_evaluations, hf)

#             #4) Evaluate this point in function
#             new_y = f(new_x)/1000

#             #Check if want to store train data:
#             if self.train:
#                 train_data.append([new_x, hf, new_y])
            
#             #Check if it is an improvement:
#             if new_y < best_y: 
#                 best_y = new_y
#                 best_x = new_x
#                 steps.append([best_x, best_y, step])
                
#                 #Check if it is a solution:
#                 if round(best_y, 5) == round(f.fopt/1000, 5):
#                     if self.train: np.save(self.output_file, np.array(train_data)) 
#                     return np.array(steps), True

#             #5) Add this info in your history
#             info = (new_x[0], new_x[1], new_y)  #TODO: here it's only 2D problem!
#             hf.append(info)

#             #6) Select next current history
#             curr_hf = self.select_hf(hf)
            
#         if self.train: np.save(self.output_file, np.array(train_data))
#         return np.array(steps), False
            
#     def select_hf(self, hf):

#         if self.hf_strategy == "gagne":
            
#             if len(hf) < self.size_hf:
#                 choices = np.random.choice(len(hf), self.size_hf)
#                 curr_pop = np.array([hf[i] for i in choices])
#                 return curr_pop
#             else:
#                 #50% top:
#                 top50 = sorted(range(len(hf)), key=lambda i: hf[i], reverse=True)[-self.size_hf//2:]

#                 #50% random:
#                 random50 = [random.randint(0, len(hf)-1) for i in range(self.size_hf//2)]

#                 all_indexes = sorted(top50 + random50)
#                 curr_pop = [(hf[ind][0], hf[ind][1], hf[ind][2]) for ind in all_indexes]

#                 return np.array(curr_pop)

#         elif self.hf_strategy == "random":
#             hf = np.array(hf)
#             idx = np.random.choice(len(hf), self.size_hf)
#             return hf[idx]