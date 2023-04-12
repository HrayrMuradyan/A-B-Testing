"""
  Run this file at first, in order to see what is it printng. Instead of the print() use the respective log level
"""
############################### LOGGER
from abc import ABC, abstractmethod
from logs import *
logger = logging.getLogger("MAB Application")
logger.setLevel(logging.DEBUG) # this on you need for you tests.

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)



class Bandit(ABC):
    ##==== DO NOT REMOVE ANYTHING FROM THIS CLASS ====##

    @abstractmethod
    def __init__(self, p):
        self.p = p
        self.p_estimate = 0.
        self.N = 0

    @abstractmethod
    def __repr__(self):
        return f'A bandit with {self.p} win rate.'

    @abstractmethod
    def pull(self):
        return np.random.random() < self.p

    @abstractmethod
    def update(self, x):
        self.N += 1
        self.p_estimate = ((self.N - 1)*self.p_estimate + x) / self.N

    @abstractmethod
    def experiment(self):
        pass

    @abstractmethod
    def plot1(self): # you name it
        # Visualize the performance of each bandit
        pass


    @abstractmethod
    def report(self):
        # store the data in csv
        # print the average reward: using logging package
        # print average regret: using logging package
        pass

#--------------------------------------#





class EpsilonGreedy(Bandit):
    pass
    
        
        
#--------------------------------------#

class ThompsonSampling(Bandit):
    pass




def comparison(): # this may be stored in utils.py if you decide to build a package
    # think of a way to compare the performances of the two algorithms VISUALLY and 
    pass

if __name__=='__main__':
   
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
