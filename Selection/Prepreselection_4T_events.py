import ROOT # provides ROOT
import math # provides fabs
from DataFormats.FWLite import Events,Handle # cmssw 
##### collections
genPartsLabel  = "genParticles"
genPartsHandle = Handle("vector<reco::GenParticle>")

##### histos
HistBR = ROOT.TH1D("HistBR","W Decay Branching Ratio",5,0,5)
##
##### Reading in files from 'TTTT_TuneZ2star_8TeV-madgraph-tauola.txt'
TTJetsFiles = open('TTTT_TuneZ2star_8TeV-madgraph-tauola.txt')
files=TTJetsFiles.readlines()
TTJetsFiles=[]
for f in files:
  TTJetsFiles.append ('dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms'+f.rstrip('\n'))

events = Events(TTJetsFiles)
#maxEvents = 1000

dimuonic = 0.
numbersignalevents = 0

###
##### event processing
for i,event in enumerate(events):
 	#if i >= maxEvents:
		#break
	numbersignalevents +=1
	event.getByLabel(genPartsLabel,genPartsHandle)
	genParts = genPartsHandle.product()
	Counter_e = 0
	Counter_mu = 0
	Counter_tau = 0
	Counter_leptonic = 0
	for part in genParts:
		if part.status() == 3 and math.fabs(part.pdgId()) == 15 and math.fabs(part.mother().pdgId()) == 24: # selecting only taus with status 3 (matrix element particles)
			Counter_tau = Counter_tau + 1
		elif part.status() == 3 and math.fabs(part.pdgId()) == 11 and math.fabs(part.mother().pdgId()) == 24:
			Counter_e = Counter_e + 1
		elif part.status() == 3 and math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24:
			Counter_mu = Counter_mu + 1
	Counter_leptonic = Counter_e + Counter_mu + Counter_tau

	if Counter_mu == 2 and Counter_leptonic==2:
		dimuonic += 1
	HistBR.Fill(Counter_e + Counter_mu + Counter_tau)
 	if i%10000 == 0:
    		print "processed ",i+1," events"
##
##### saving hists to files
HistBR.SaveAs(HistBR.GetName()+'.root')

##### Print some results
print 'Number of events is ', numbersignalevents
print 'Number of dimuonic events is ', dimuonic
print 'Braching Ratio dileptonic events ', dimuonic/numbersignalevents 
print 'End of run'

