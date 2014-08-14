import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from SelectionClass import Selection

##### Reading in files from 'TTTT_TuneZ2star_8TeV-madgraph-tauola.txt'
TTJetsFiles = open('TTTT_TuneZ2star_8TeV-madgraph-tauola.txt')
files=TTJetsFiles.readlines()
TTJetsFiles=[]
for f in files:
  TTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events = Events(TTJetsFiles)
#maxEvents = 1000			


##### Run Selection
exampleSelection = Selection(events, "_TestHist")
exampleSelection.selectionloop()

##### Saving Data to Histograms
exampleSelection.savinghists()

##### Print some results
print 'Number of events is ',exampleSelection.numbersignalevents
print 'muonsEvts ',exampleSelection.numberselectedmuonevents
print 'End of run'
