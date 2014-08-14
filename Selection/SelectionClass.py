print 'Starting: SelectionClass'
import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector

class Selection_MC(object):
	def __init__(self,evtsTT, evtsTTTT,postfixTT,postfixTTTT):
		self.evtsTT = evtsTT
		self.evtsTTTT = evtsTTTT
		self.postfixTT = postfixTT
		self.postfixTTTT = postfixTTTT


	def SelectionLoop_TT(self):
		print 'Starting SelectionLoop_TT()'

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
		self.cutprocessTT = ROOT.TH1D("cutprocess"+self.postfixTT,"Cut Process for TT events",5,0,5)
		self.NumberMuonsPerEventTT = ROOT.TH1D("NumberMuonsPerEvent"+self.postfixTT,"Number of Selected Muons per TT-Event",4,0,4)
		self.JetsPtPreSelectionTT = ROOT.TH1D("JetsPtPreSelection"+self.postfixTT,"Jets momentum pre-selection (TT)",100,0,100)
		self.NumberJetsPreSelectionTT = ROOT.TH1D("NumberJetsPreSelection"+self.postfixTT,"Number jets/event MC (TT)",8,0,8)
		self.NumberBJetsPreSelectionTT = ROOT.TH1D("NumberBJetsPreSelection"+self.postfixTT,"Number Bjets/event MC (TT)",8,0,8)


		##### Defining variables
		self.numbersignaleventsTT = 0
		self.numbertriggerTT = 0
		self.numbertotalmuonsTT = 0
		#self.numbertotalselectedmuons = 0
		self.numberdimuoneventsTT = 0
		self.numberselectedjeteventsTT = 0


		##### Defining lists
		
 
		##### Adressing every single event in eventsTT
		for i,event in enumerate(self.evtsTT):			
  			##### Test routine:
			if i%10000 == 0 or i == 1 or i == 0:				
        			print "processed ",i+1," events"
			#if i==1000:
				#break	

			##### Count number of background events:
			self.numbersignaleventsTT += 1						#number signal events AFTER preselection
			self.cutprocessTT.Fill(0)

			##### Create Product of event
			event.getByLabel(muonsRecoLabel,muonsRecoHandle)
      			event.getByLabel(jetsLabel,jetsHandle)
			event.getByLabel((TrigResultslabel,"","HLT"),TrigResultshandle)
			event.getByLabel(vtxRecoLabel,vtxRecoHandle)
			event.getByLabel(METLabel,METHandle)

			muonsTT = muonsRecoHandle.product()
      			jetsTT = jetsHandle.product()
			TrigResultsTT = TrigResultshandle.product()
      			TriggerNamesTT = event.object().triggerNames(TrigResultsTT)
			vtxsTT = vtxRecoHandle.product()
			METsTT = METHandle.product()

			##### Set Trigger
			availTriggerMuTT = (" ".join([ tr for tr in TriggerNamesTT.triggerNames() if "HLT_IsoMu24_eta2p1_v" in tr])).strip() ##### Trigger-Auswahl

      			if not TrigResultsTT[TriggerNamesTT.triggerIndex(availTriggerMuTT)].accept():
        			continue

			self.numbertriggerTT += 1
			self.cutprocessTT.Fill(1)

			##### Defining lists to count particles per event
			self.listmuonsTT = []
			self.listcombjetsTT = []
			self.listjetsTT = []
			self.listbjetsTT = []
	
			##### Defining Muons			
      			for muonTT in muonsTT:
        			if muonTT.pt() > 30 and muonTT.isGlobalMuon():
          				self.listmuonsTT.append(muonTT)

			self.numbertotalmuonsTT += len(self.listmuonsTT)
			self.NumberMuonsPerEventTT.Fill(len(self.listmuonsTT))


			##### Defining Jets
      			for jetTT in jetsTT:
        			self.JetsPtPreSelectionTT.Fill(jetTT.pt())
        			if math.fabs(jetTT.eta()) < 2.4:
          				self.listcombjetsTT.append(jetTT)
          				if jetTT.pt() > 40:
            					self.listjetsTT.append(jetTT)
            					if jetTT.bDiscriminator("combinedSecondaryVertexBJetTags") > 0.5:
              						self.listbjetsTT.append(jetTT)

			self.NumberJetsPreSelectionTT.Fill(len(self.listjetsTT))
			self.NumberBJetsPreSelectionTT.Fill(len(self.listbjetsTT))

			
			if len(self.listmuonsTT) >= 2:
				self.numberdimuoneventsTT += 1
				self.cutprocessTT.Fill(2)
				
				if len(self.listjetsTT) >= 5:
					self.numberselectedjeteventsTT +=1
			

	def SelectionLoop_TTTT(self):
		print 'Starting SelectionLoop_TTTT()'

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
		self.cutprocessTTTT = ROOT.TH1D("cutprocess"+self.postfixTTTT,"Cut Process for TTTT events",5,0,5)
		self.NumberMuonsPerEvenTTTTT = ROOT.TH1D("NumberMuonsPerEvent"+self.postfixTTTT,"Number of Selected Muons per TTTT-Event",4,0,4)
		self.JetsPtPreSelectionTTTT = ROOT.TH1D("JetsPtPreSelection"+self.postfixTTTT,"Jets momentum pre-selection (TTTT)",100,0,100)
		self.NumberJetsPreSelectionTTTT = ROOT.TH1D("NumberJetsPreSelection"+self.postfixTTTT,"Number jets/event MC (TTTT)",18,0,18)
		self.NumberBJetsPreSelectionTTTT = ROOT.TH1D("NumberBJetsPreSelection"+self.postfixTTTT,"Number Bjets/event MC (TTTT)",8,0,8)


		##### Defining variables
		self.numbersignaleventsTTTT = 0
		self.numbertriggerTTTT = 0
		self.numbertotalmuonsTTTT = 0
		#self.numbertotalselectedmuons = 0
		self.numberdimuoneventsTTTT = 0
		self.numberselectedjeteventsTTTT = 0


		##### Defining lists
		
 
		##### Adressing every single event in eventsTTTT
		for i,event in enumerate(self.evtsTTTT):			
  			##### Test routine:
			if i%10000 == 0 or i == 1 or i == 0:				
        			print "processed ",i+1," events"
			#if i==1000:
				#break	

			##### Count number of background events:
			self.numbersignaleventsTTTT += 1						#number signal events AFTER preselection
			self.cutprocessTTTT.Fill(0)

			##### Create Product of event
			event.getByLabel(muonsRecoLabel,muonsRecoHandle)
      			event.getByLabel(jetsLabel,jetsHandle)
			event.getByLabel((TrigResultslabel,"","HLT"),TrigResultshandle)
			event.getByLabel(vtxRecoLabel,vtxRecoHandle)
			event.getByLabel(METLabel,METHandle)

			muonsTTTT = muonsRecoHandle.product()
      			jetsTTTT = jetsHandle.product()
			TrigResultsTTTT = TrigResultshandle.product()
      			TriggerNamesTTTT = event.object().triggerNames(TrigResultsTTTT)
			vtxsTTTT = vtxRecoHandle.product()
			METsTTTT = METHandle.product()

			##### Set Trigger
			availTriggerMuTTTT = (" ".join([ tr for tr in TriggerNamesTTTT.triggerNames() if "HLT_IsoMu24_eta2p1_v" in tr])).strip() ##### Trigger-Auswahl

      			if not TrigResultsTTTT[TriggerNamesTTTT.triggerIndex(availTriggerMuTTTT)].accept():
        			continue

			self.numbertriggerTTTT += 1
			self.cutprocessTTTT.Fill(1)

			##### Defining lists to count particles per event
			self.listmuonsTTTT = []
			self.listcombjetsTTTT = []
			self.listjetsTTTT = []
			self.listbjetsTTTT = []
	
			##### Defining Muons			
      			for muonTTTT in muonsTTTT:
        			if muonTTTT.pt() > 30 and muonTTTT.isGlobalMuon():
          				self.listmuonsTTTT.append(muonTTTT)

			self.numbertotalmuonsTTTT += len(self.listmuonsTTTT)
			self.NumberMuonsPerEvenTTTTT.Fill(len(self.listmuonsTTTT))


			##### Defining Jets
      			for jeTTTTT in jetsTTTT:
        			self.JetsPtPreSelectionTTTT.Fill(jeTTTTT.pt())
        			if math.fabs(jeTTTTT.eta()) < 2.4:
          				self.listcombjetsTTTT.append(jeTTTTT)
          				if jeTTTTT.pt() > 40:
            					self.listjetsTTTT.append(jeTTTTT)
            					if jeTTTTT.bDiscriminator("combinedSecondaryVertexBJeTTTTags") > 0.5:
              						self.listbjetsTTTT.append(jeTTTTT)

			self.NumberJetsPreSelectionTTTT.Fill(len(self.listjetsTTTT))
			self.NumberBJetsPreSelectionTTTT.Fill(len(self.listbjetsTTTT))

			
			if len(self.listmuonsTTTT) >= 2:
				self.numberdimuoneventsTTTT += 1
				self.cutprocessTTTT.Fill(2)
				
				if len(self.listjetsTTTT) >= 5:
					self.numberselectedjeteventsTTTT +=1
			
			



	def SavingHists(self):
		print "Starting Saving Data to Histograms"
		
		self.cutprocessTT.SaveAs(self.cutprocessTT.GetName()+'.root')
		self.NumberMuonsPerEventTT.SaveAs(self.NumberMuonsPerEventTT.GetName()+'.root')
		self.JetsPtPreSelectionTT.SaveAs(self.JetsPtPreSelectionTT.GetName()+'.root')
		self.NumberJetsPreSelectionTT.SaveAs(self.NumberJetsPreSelectionTT.GetName()+'.root')
		self.NumberBJetsPreSelectionTT.SaveAs(self.NumberBJetsPreSelectionTT.GetName()+'.root')
		self.cutprocessTTTT.SaveAs(self.cutprocessTTTT.GetName()+'.root')
		self.NumberMuonsPerEvenTTTTT.SaveAs(self.NumberMuonsPerEvenTTTTT.GetName()+'.root')
		self.JetsPtPreSelectionTTTT.SaveAs(self.JetsPtPreSelectionTTTT.GetName()+'.root')
		self.NumberJetsPreSelectionTTTT.SaveAs(self.NumberJetsPreSelectionTTTT.GetName()+'.root')
		self.NumberBJetsPreSelectionTTTT.SaveAs(self.NumberBJetsPreSelectionTTTT.GetName()+'.root')





		
