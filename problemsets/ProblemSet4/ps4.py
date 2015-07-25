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
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    delays = [300, 150, 75, 0]
    res = []

    for delay in delays:
        for i in range(numTrials):
            virusList = []
            virusPop = 0
            for n in range(numViruses):
                virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            my_patient = TreatedPatient(virusList, maxPop)

            for step in range(delay + 150):
                if step == delay:
                    my_patient.addPrescription('guttagonol')
                virusPop = my_patient.update()
            res.append(virusPop)

    toPlot = []
    for i in range(0, len(res), numTrials):
        toPlot.append(res[i:i + numTrials])

    for i, j in enumerate(delays):
        pylab.subplot(2, 2, i + 1)
        pylab.hist(toPlot[i])
    pylab.show()

simulationDelayedTreatment(100)



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
    