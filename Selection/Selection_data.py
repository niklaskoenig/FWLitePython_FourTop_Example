import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from SelectionClass import Selection_DATA

##### Reading in files from 'SingleMu_SoftJetSkim.txt'
print 'Reading DATA1-files'
DATA1JetsFiles = open('SingleMu_SoftJetSkim.txt')
files=DATA1JetsFiles.readlines()
DATA1JetsFiles=[]
for f in files:
  DATA1JetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events_DATA1 = Events(DATA1JetsFiles)


##### Reading in files from 'SingleMuRunB.txt'
print 'Reading DATA2-files'
DATA2JetsFiles = open('SingleMuRunB.txt')
files=DATA2JetsFiles.readlines()
DATA2JetsFiles=[]
for f in files:
  DATA2JetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events_DATA2 = Events(DATA2JetsFiles)


