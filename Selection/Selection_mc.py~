import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from SelectionClass import Selection_MC

##### Reading in files from 'TTJetsMCdilep.txt'
print 'Reading TT-files'
TTJetsFiles = open('TTJetsMCdilep.txt')
files=TTJetsFiles.readlines()
TTJetsFiles=[]
for f in files:
  TTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events_TT = Events(TTJetsFiles)

##### Reading in files from 'TTTT_TuneZ2star_8TeV-madgraph-tauola.txt'
print 'Reading TTTT-files'
TTTTJetsFiles = open('TTTT_TuneZ2star_8TeV-madgraph-tauola_mini.txt')
files=TTTTJetsFiles.readlines()
TTTTJetsFiles=[]
for f in files:
  TTTTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events_TTTT = Events(TTTTJetsFiles)



##### Run Selection
selection = Selection_MC(events_TT, events_TTTT, "_Test_TT", "_Test_TTTT")
selection.SelectionLoop_TT()
selection.SelectionLoop_TTTT()


##### Saving Data to Histograms
selection.SavingHists()

##### Print some results
print 'Number of events (TT) is ',selection.numbersignaleventsTT		
print 'Number of dimuon events (TT) is ',selection.numberdimuoneventsTT
print 'Number of selected jet events (TT) is' ,selection.numberselectedjeteventsTT
print 'Efficienty (TT)', float(selection.numberselectedjeteventsTT)/float(selection.numbersignaleventsTT)		

print 'Number of events (TTTT) is ',selection.numbersignaleventsTTTT		
print 'Number of dimuon events (TTTT) is ',selection.numberdimuoneventsTTTT
print 'Number of selected jet events (TTTT) is' ,selection.numberselectedjeteventsTTTT
print 'Efficienty (TTTT)', float(selection.numberselectedjeteventsTTTT)/float(selection.numbersignaleventsTTTT)		



print 'End of run'

