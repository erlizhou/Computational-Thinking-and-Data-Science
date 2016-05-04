# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    delays = [300, 150, 75, 0]
    for delay in delays:
    	total = []
    	for i in range(numTrials):
    		patient = TreatedPatient([ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005) for j in range(100)], 2000)
    		for x in range(delay):
    			patient.update()
    		patient.addPrescription('guttagonol')
    		for x in range(149):
    			patient.update()
    		total.append(patient.update())

    	pylab.xlabel('Virus population size')
    	pylab.ylabel('Frequencies')
    	pylab.title('Virus Population Histograms')
    	pylab.legend()
    	pylab.hist(total)
    	pylab.show()


# simulationDelayedTreatment(100)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [300, 150, 75, 0]
    for delay in delays:
    	total = []
    	for i in range(numTrials):
    		patient = TreatedPatient([ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005) for j in range(100)], 1000)
    		for x in range(150):
    			patient.update()
    		patient.addPrescription('guttagonol')
    		for x in range(delay):
    			patient.update()
    		patient.addPrescription('grimpex')
    		for x in range(149):
    			patient.update()
    		total.append(patient.update())

    	pylab.xlabel('Virus population size')
    	pylab.ylabel('Frequencies')
    	pylab.title('Virus Population Histograms')
    	pylab.legend()
    	pylab.hist(total)
    	pylab.show()

simulationTwoDrugsDelayedTreatment(100)