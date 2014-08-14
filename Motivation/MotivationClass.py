print 'Starting: MotivationClass'
import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector

class Motivation(object):
	def __init__(self,evts,postfix):
		self.evts = evts
		self.postfix = postfix

	def loop(self):
		print 'Starting loop()'
		##### Objects which will be analysed
		jetsLabel = "selectedPatJetsPFlow"
		jetsHandle = Handle("vector<pat::Jet>")
		muonsRecoLabel = "selectedPatMuonsPFlow"
		muonsRecoHandle = Handle("vector<pat::Muon>")
		TrigResultslabel=("TriggerResults")
		TrigResultshandle=Handle("edm::TriggerResults") 
		vtxRecoHandle = Handle("vector<reco::Vertex>")
		vtxRecoLabel = "offlinePrimaryVertices"
		METLabel = "patMETsPFlow"
		METHandle = Handle("vector<pat::MET>")

		##### Defining Histogramms
		self.muon_pt = ROOT.TH1D("muon_pt"+self.postfix,"p_T(#mu)",200,0,200)
		self.muon_eta = ROOT.TH1D("muon_eta"+self.postfix,"#eta(#mu)",100,-3,3)
		self.muon_numbervalidhitstracker = ROOT.TH1D("muon_numbervalidhitstracker"+self.postfix,"# of valid hits in tracker",100,0,30)
		self.muon_chi2 = ROOT.TH1D("muon_chi2"+self.postfix,"chi^2(#mu)",100,0,20)
		self.jet_pt = ROOT.TH1D("jet_pt"+self.postfix,"p_T(Jet)",200,0,200)
		self.jet_eta = ROOT.TH1D("jet_eta"+self.postfix,"#eta(Jet)",100,-3,3)
		self.H_T_mu_jet = ROOT.TH1D("H_T_mu_jet"+self.postfix,"H_T",200,0,2000)
		self.MET = ROOT.TH1D("MET"+self.postfix,"MET",200,0,2000)
		
		##### Defining variables
		self.numbersignalevents = 0

		##### Adressing every single event in events
		for i,event in enumerate(self.evts):
  			

      			if i%10000 == 0 or i == 1 or i == 0:				
        			print "processed ",i+1," events"
			#if i==10:
				#break	

			self.H_T = 0
			##### Count events
			self.numbersignalevents+=1

			##### Create Product of event
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
				self.muon_pt.Fill(muon.pt())
				self.muon_eta.Fill(muon.eta())
				self.muon_numbervalidhitstracker.Fill(muon.numberOfValidHits())
				#self.muon_chi2.Fill(muon.normChi2())
				self.H_T += muon.pt()


			for jet in jets:
				self.jet_pt.Fill(jet.pt())
				self.jet_eta.Fill(jet.eta())
				self.H_T += jet.pt()
			
			self.H_T_mu_jet.Fill(self.H_T)

	def savinghists(self):
		print "Starting Saving Data to Histograms"
		self.muon_pt.SaveAs(self.muon_pt.GetName()+'.root')				
		self.muon_eta.SaveAs(self.muon_eta.GetName()+'.root')	
		self.muon_numbervalidhitstracker.SaveAs(self.muon_numbervalidhitstracker.GetName()+'.root')	
		#self.muon_chi2.SaveAs(self.muon_chi2.GetName()+'.root')
		self.jet_pt.SaveAs(self.jet_pt.GetName()+'.root')				
		self.jet_eta.SaveAs(self.jet_eta.GetName()+'.root')
		self.H_T_mu_jet.SaveAs(self.H_T_mu_jet.GetName()+'.root')
		self.MET.SaveAs(self.EP_MET.GetName()+'.root')



			







