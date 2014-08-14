import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from MotivationClass import Motivation

##### Reading in files from 'TTJetsMCdilep.txt'
TTJetsFiles = open('TTJetsMCdilep.txt')
files=TTJetsFiles.readlines()
TTJetsFiles=[]
for f in files:
  TTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events = Events(TTJetsFiles)
#maxEvents = 10			


##### Run Selection
mot = Motivation(events, "_TestHist_2T")
mot.loop()

##### Saving Data to Histograms
mot.savinghists()

##### Print some results
print 'Number of events is ',mot.numbersignalevents
print 'End of run'

