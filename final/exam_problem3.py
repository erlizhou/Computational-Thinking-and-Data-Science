import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
MINRABBITPOP = 10
MINFOXPOP = 10

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    prob = 1.0 - (CURRENTRABBITPOP * 1.0) / MAXRABBITPOP
    counter = 0
    if CURRENTRABBITPOP < MINRABBITPOP:
    	pass
    else:
    	for i in range(CURRENTRABBITPOP):
    		if random.random() < prob:
    			counter += 1
    	CURRENTRABBITPOP = min(CURRENTRABBITPOP + counter, MAXRABBITPOP)
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    prob = CURRENTRABBITPOP * 1.0 / MAXRABBITPOP
    counterrabbit = 0
    counterfox = 0
    if CURRENTFOXPOP < MINFOXPOP:
    	pass
    else:
    	for i in range(CURRENTFOXPOP):
    		if random.random() < prob:
    			counterrabbit += 1
    			if random.random() < 1.0 / 3:
    				counterfox += 1
    		else:
    			if random.random() < 0.9:
    				counterfox -= 1
    	CURRENTRABBITPOP = max(CURRENTRABBITPOP - counterrabbit, MINRABBITPOP)
    	CURRENTFOXPOP = max(CURRENTFOXPOP + counterfox, MINFOXPOP)
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = ()
    fox_populations = ()
    for i in range(numSteps):
    	rabbitGrowth()
    	foxGrowth()
    	rabbit_populations += (CURRENTRABBITPOP,)
    	fox_populations += (CURRENTFOXPOP,)
    return rabbit_populations, fox_populations

rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(200)
pylab.plot(rabbitPopulationOverTime, '-b')
pylab.plot(foxPopulationOverTime, '-r')
pylab.show()
coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))
pylab.show()
coeff1 = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff1, range(len(foxPopulationOverTime))))
pylab.show()