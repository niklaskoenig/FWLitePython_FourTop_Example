import ROOT # provides ROOT
import math # provides fabs
from DataFormats.FWLite import Events,Handle # cmssw 
##### collections
genPartsLabel  = "genParticles"
genPartsHandle = Handle("vector<reco::GenParticle>")
##
##### histos

genmuLeptonsPtHist = ROOT.TH1D("genmuLeptonsPtHist","p_T(#mu)",40,0,200)
genmuLeptonsPtHistCutoff = ROOT.TH1D("genmuLeptonsPtHistCutoff","p_T(#mu)",40,25,200)

##
#### input
events = Events([
	'dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms//store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/146A413C-CA0A-E211-B5F3-002590147CA2.root',
	'dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/2C53DD3D-9F0A-E211-9C6B-001E67396E0A.root',
	'dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/38B000AD-A80A-E211-97A0-001E67398011.root',
	'dcap://grid-dcap-extern.physik.rwth-aachen.de/pnfs/physik.rwth-aachen.de/cms/store/mc/Summer12_DR53X/TTTT_TuneZ2star_8TeV-madgraph-tauola/AODSIM/PU_S10_START53_V7A-v1/00000/6224DA2F-CC0A-E211-A4DE-002590200A88.root'
	]) #part of /TTTT_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM 
maxEvents = 1000
###
##### event processing
for i,event in enumerate(events):
  if i >= maxEvents:
    break
  event.getByLabel(genPartsLabel,genPartsHandle)
  genParts = genPartsHandle.product()
  for part in genParts:
    if part.status() == 3 and math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) and 24 and math.fabs(part.eta()) < 2.1 and math.fabs(part.pt()) > 30 : # selecting only taus with status 3 (matrix element particles)
      	genmuLeptonsPtHistCutoff.Fill(part.pt())
    if part.status() == 3 and math.fabs(part.pdgId()) == 13 and math.fabs(part.mother().pdgId()) == 24: # selecting only taus with status 3 (matrix element particles)
      	genmuLeptonsPtHist.Fill(part.pt())

  if i%100 == 0:
    print "processed ",i+1," events"
##
##### saving hists to files
genmuLeptonsPtHist.SaveAs(genmuLeptonsPtHist.GetName()+'.root')
genmuLeptonsPtHistCutoff.SaveAs(genmuLeptonsPtHistCutoff.GetName()+'.root')





