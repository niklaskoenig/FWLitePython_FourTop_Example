import ROOT # provides ROOT
import math # provides fabs
from DataFormats.FWLite import Events,Handle # cmssw 
from ROOT import TLorentzVector

##### collections
jetsLabel = "selectedPatJetsPFlow"
jetsHandle = Handle("vector<pat::Jet>")
muonsRecoLabel = "selectedPatMuonsPFlow"
muonsRecoHandle = Handle("vector<pat::Muon>")
TrigResultslabel=("TriggerResults")
TrigResultshandle=Handle("edm::TriggerResults") 
vtxRecoHandle = Handle("vector<reco::Vertex>")
vtxRecoLabel = "offlinePrimaryVertices"
##
##### histos
genMuonsPtHist = ROOT.TH1D("genMuonsPtHist","genMuonsPtHist",200,0,200)
##
#### input
events = Events([
	'dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms///store/user/fhohle/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/BScSkim_TTJets_fullLep_2014-06-02_11-12-02/6eea63ca40c7f36421b750ebc0e3ead7/TTTT_TuneZ2star_8TeV-madgraph-tauola_patTuple_TTJets_FullLeptMGDecays_8TeV-madgraph-tauola__Summer12_DR53X-PU_S10_START53_V7C-v2__AODSIM_10_1_2AV.root'])
maxEvents = 1000
###
##### event processing
for i,event in enumerate(events):
 	if i >= maxEvents:
    		break
	numberofmuons = 0
	numberofjets = 0
	event.getByLabel(muonsRecoLabel,muonsRecoHandle)
      	event.getByLabel(jetsLabel,jetsHandle)
	event.getByLabel((TrigResultslabel,"","HLT"),TrigResultshandle)		
	event.getByLabel(vtxRecoLabel,vtxRecoHandle)

	muons = muonsRecoHandle.product()
      	jets = jetsHandle.product()
	TrigResults=TrigResultshandle.product()
      	TriggerNames=event.object().triggerNames(TrigResults)
	vtxs = vtxRecoHandle.product()
	##### Set Trigger
	availTriggerMu=(" ".join([ tr for tr in TriggerNames.triggerNames() if "HLT_IsoMu24_eta2p1_v" in tr])).strip() ##### Trigger-Auswahl

      	if not TrigResults[TriggerNames.triggerIndex(availTriggerMu)].accept():
        	continue	

	for muon in muons:
		numberofmuons += 1
	
	for jet in jets:
		numberofjets += 1

	if numberofmuons >=1 and numberofjets >=1:
		break

  	if i%100 == 0:
    		print "processed ",i+1," events"
##
##### saving hists to files
genMuonsPtHist.SaveAs(genMuonsPtHist.GetName()+'.root')

