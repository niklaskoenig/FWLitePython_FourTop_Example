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

events_TT = Events(TTJetsFiles)

##### Reading in files from 'TTTT_TuneZ2star_8TeV-madgraph-tauola.txt'
TTTTJetsFiles = open('TTTT_TuneZ2star_8TeV-madgraph-tauola_mini.txt')
files=TTTTJetsFiles.readlines()
TTTTJetsFiles=[]
for f in files:
  TTTTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events_TTTT = Events(TTJetsFiles)
