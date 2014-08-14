import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from MotivationClass_EP import Motivation_EP

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

##### Run Motivation
mot = Motivation_EP(events_TT, events_TTTT, "_Test_TT", "_Test_TTTT")
mot.loop()
mot.savingdata()
mot.plotdata()

##### Print some results

print 'End of run'
