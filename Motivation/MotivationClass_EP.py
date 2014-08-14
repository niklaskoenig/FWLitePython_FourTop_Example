print 'Starting: MotivationClass'
import ROOT,math,sys
from DataFormats.FWLite import Events,Handle
from ROOT import TLorentzVector
from array import array

class Motivation_EP(object):
	def __init__(self,evtsTT, evtsTTTT,postfixTT,postfixTTTT):
		self.evtsTT = evtsTT
		self.evtsTTTT = evtsTTTT
		self.postfixTT = postfixTT
		self.postfixTTTT = postfixTTTT

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


		##### Defining variables
		self.numbersignalevents = 0
		self.numbercuts = 100

		self.max_muonpt = 0
		
		self.max_jetpt = 0
		self.deltajetpt = 0

		self.max_H_T = 0
		self.deltaH_T = 0
		
		##### Defining lists
      		self.listmuonptpreselectionTT = []
		
		self.listmuonptvaluesTT = []
		self.listeffmuonptTT = []

      		self.listmuonptpreselectionTTTT = []
		self.listmuonptvaluesTTTT = []
		self.listeffmuonptTTTT = []
		self.listpurmuonpt = []
		self.listmuonptEP = []

		self.listmuonptvaluesTT_err = []
		self.listeffmuonptTTTT_err = []
		self.listpurmuonpt_err = []
		self.listmuonptEP_err = []


      		self.listjetptpreselectionTT = []
		
		self.listjetptvaluesTT = []
		self.listeffjetptTT = []

      		self.listjetptpreselectionTTTT = []
		self.listjetptvaluesTTTT = []
		self.listeffjetptTTTT = []
		self.listpurjetpt = []
		self.listjetptEP = []

		self.listjetptvaluesTT_err = []
		self.listeffjetptTTTT_err = []
		self.listpurjetpt_err = []
		self.listjetptEP_err = []

		self.listH_T_preselectionTT = []
		self.listH_T_preselectionTTTT = []
		self.listH_Tvalues = []
		self.listeff_H_T_TT = []
		self.listeff_H_T_TTTT = []
		self.listpur_H_T = []
		self.listEP_H_T = []

		self.listH_Tvalues_err = []
		self.listeff_H_T_TTTT_err = []
		self.listpur_H_T_err = []
		self.listEP_H_T_err = []

		
		

	##### Adressing every single event in events



		for i,event in enumerate(self.evtsTT):			
  			

      			if i%10000 == 0 or i == 1 or i == 0:				
        			print "processed ",i+1," events"
			#if i==1000:
				#break	

			##### Count events
			self.numbersignalevents+=1

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
			
			self.H_T_TT = 0
				
			for muonTT in muonsTT:
				self.listmuonptpreselectionTT.append(muonTT.pt())
				self.H_T_TT += muonTT.pt()
				if muonTT.pt() <= self.max_muonpt:
					self.max_muonpt += 0
				else: 
					self.max_muonpt = muonTT.pt()

			for jetTT in jetsTT:
				self.H_T_TT += jetTT.pt()
				self.listjetptpreselectionTT.append(jetTT.pt())
				if jetTT.pt() <= self.max_jetpt:
					self.max_jetpt += 0
				else: 
					self.max_jetpt = jetTT.pt()
			self.max_jetpt = 200
			self.max_H_T = 1000
			
			self.listH_T_preselectionTT.append(self.H_T_TT)
					
					
		print 'Maximales muPt: ', self.max_muonpt
		print 'Maximales JetPt: ', self.max_jetpt




		for i,event in enumerate(self.evtsTTTT):			
  			

      			if i%10000 == 0 or i == 1 or i == 0:				
        			print "processed ",i+1," events"
			#if i==1000:
				#break	



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
			
			self.H_T_TTTT = 0
				
			for muonTTTT in muonsTTTT:
				self.H_T_TTTT += muonTTTT.pt()
				self.listmuonptpreselectionTTTT.append(muonTTTT.pt())

			for jetTTTT in jetsTTTT:
				self.H_T_TTTT += jetTTTT.pt()
				self.listjetptpreselectionTTTT.append(jetTTTT.pt())
				
			self.listH_T_preselectionTTTT.append(self.H_T_TTTT)

		
		print 'Zweiter Durchlaiuf abgeschlossen'



		##### Calculating efficiency, purity
		print 'Starting calculation of efficiency and purity'
		for i in range(0,self.numbercuts-1):					#####: Generates x-axis 
			self.deltapt = self.max_muonpt/(self.numbercuts)*(1+i)
			self.listmuonptvaluesTT.append(self.deltapt)

			self.deltajetpt = self.max_jetpt/(self.numbercuts)*(1+i)
			self.listjetptvaluesTT.append(self.deltajetpt)

			self.deltaH_T = self.max_H_T/(self.numbercuts)*(1+i)
			self.listH_Tvalues.append(self.deltaH_T)

		

		for i in range(0,self.numbercuts-1):						###### Generates list of muon and efficiency: Result saved in list 'self.listeffmuonptTT'
			self.listmuonptpostselectionTT = []
			self.listmuonptpostselectionTTTT = []

			for j in range(0, len(self.listmuonptpreselectionTT)-1):							
				if self.listmuonptpreselectionTT[j] >= self.max_muonpt/(self.numbercuts)*(1+i):			
					self.listmuonptpostselectionTT.append(self.listmuonptpreselectionTT[j])
				if len(self.listmuonptpostselectionTT) == 0:
					self.listmuonptpostselectionTT.append(1)


			for k in range(0, len(self.listmuonptpreselectionTTTT)-1):
				if self.listmuonptpreselectionTTTT[k] >= self.max_muonpt/(self.numbercuts)*(1+i):							
					self.listmuonptpostselectionTTTT.append(self.listmuonptpreselectionTTTT[k])
				if len(self.listmuonptpostselectionTTTT) == 0:
					self.listmuonptpostselectionTTTT.append(1)

			self.listeffmuonptTT.append(float(len(self.listmuonptpostselectionTT))/float(len(self.listmuonptpreselectionTT)))	
			self.listeffmuonptTTTT.append(float(len(self.listmuonptpostselectionTTTT))/float(len(self.listmuonptpreselectionTTTT)))
			self.listpurmuonpt.append(float(len(self.listmuonptpostselectionTTTT))/(float(len(self.listmuonptpostselectionTTTT))+float(len(self.listmuonptpostselectionTT)))) 
			self.listmuonptEP.append(self.listpurmuonpt[i]*self.listeffmuonptTTTT[i])

			self.listmuonptvaluesTT_err.append(0.)
			self.listeffmuonptTTTT_err.append(math.sqrt(  math.pow( 1./(float(len(self.listmuonptpreselectionTTTT))) ,2) +  math.pow( ( float(len(self.listmuonptpostselectionTTTT)) )/( math.pow( float(len(self.listmuonptpreselectionTTTT)) ,2) ) ,2)  )) 
			self.listpurmuonpt_err.append(  pow( ((1.)/(float(len(self.listmuonptpostselectionTTTT))))/(pow( 1. + (float(len(self.listmuonptpostselectionTT)))/(float(len(self.listmuonptpostselectionTTTT))) ,2)) ,2) + pow( ((float(len(self.listmuonptpostselectionTT)))/(pow(float(len(self.listmuonptpostselectionTTTT)),2)))/(pow( 1.+ (float(len(self.listmuonptpostselectionTT)))/(float(len(self.listmuonptpostselectionTTTT))) ,2)) ,2) )
 			self.listmuonptEP_err.append(pow(self.listpurmuonpt[i]*self.listpurmuonpt_err[i],2)+pow(self.listeffmuonptTTTT[i]*self.listeffmuonptTTTT_err[i],2))
 

			#the same procedure for jets.pt

			self.listjetptpostselectionTT = []
			self.listjetptpostselectionTTTT = []

			for j in range(0, len(self.listjetptpreselectionTT)-1):				
				if self.listjetptpreselectionTT[j] >= self.max_jetpt/(self.numbercuts)*(1+i):			
					self.listjetptpostselectionTT.append(self.listjetptpreselectionTT[j])
				if len(self.listjetptpostselectionTT) == 0:
					self.listjetptpostselectionTT.append(1)

			for k in range(0, len(self.listjetptpreselectionTTTT)-1):
				if self.listjetptpreselectionTTTT[k] >= self.max_jetpt/(self.numbercuts)*(1+i):							
					self.listjetptpostselectionTTTT.append(self.listjetptpreselectionTTTT[k]) 
				if len(self.listjetptpostselectionTTTT) == 0:
					self.listjetptpostselectionTTTT.append(1)

			self.listeffjetptTT.append(float(len(self.listjetptpostselectionTT))/len(self.listjetptpreselectionTT))
			self.listeffjetptTTTT.append(float(len(self.listjetptpostselectionTTTT))/len(self.listjetptpreselectionTTTT))
			self.listpurjetpt.append(float(len(self.listjetptpostselectionTTTT))/(float(len(self.listjetptpostselectionTTTT))+float(len(self.listjetptpostselectionTT)))) 
			self.listjetptEP.append(self.listpurjetpt[i]*self.listeffjetptTTTT[i])

			self.listjetptvaluesTT_err.append(0.)
			self.listeffjetptTTTT_err.append(math.sqrt(  math.pow( 1./(float(len(self.listjetptpreselectionTTTT))) ,2) +  math.pow( ( float(len(self.listjetptpostselectionTTTT)) )/( math.pow( float(len(self.listjetptpreselectionTTTT)) ,2) ) ,2)  )) 			
			self.listpurjetpt_err.append(  pow( ((1.)/(float(len(self.listjetptpostselectionTTTT))))/(pow( 1. + (float(len(self.listjetptpostselectionTT)))/(float(len(self.listjetptpostselectionTTTT))) ,2)) ,2) + pow( ((float(len(self.listjetptpostselectionTT)))/(pow(float(len(self.listjetptpostselectionTTTT)),2)))/(pow( 1.+ (float(len(self.listjetptpostselectionTT)))/(float(len(self.listjetptpostselectionTTTT))) ,2)) ,2) ) 
			self.listjetptEP_err.append(pow(self.listpurjetpt[i]*self.listpurjetpt_err[i],2)+pow(self.listeffjetptTTTT[i]*self.listeffjetptTTTT_err[i],2))


			#the same procedure for H_T

			self.listH_T_postselectionTT = []
			self.listH_T_postselectionTTTT = []

			for j in range(0, len(self.listH_T_preselectionTT)-1):				
				if self.listH_T_preselectionTT[j] >= self.max_H_T/(self.numbercuts)*(1+i):			
					self.listH_T_postselectionTT.append(self.listH_T_preselectionTT[j])
				if len(self.listH_T_postselectionTT) == 0:
					self.listH_T_postselectionTT.append(1)

			for k in range(0, len(self.listH_T_preselectionTTTT)-1):
				if self.listH_T_preselectionTTTT[k] >= self.max_H_T/(self.numbercuts)*(1+i):							
					self.listH_T_postselectionTTTT.append(self.listH_T_preselectionTTTT[k])
				if len(self.listH_T_postselectionTTTT) == 0:
					self.listH_T_postselectionTTTT.append(1) 

			self.listeff_H_T_TT.append(float(len(self.listH_T_postselectionTT))/len(self.listH_T_preselectionTT))
			self.listeff_H_T_TTTT.append(float(len(self.listH_T_postselectionTTTT))/len(self.listH_T_preselectionTTTT))
			self.listpur_H_T.append(float(len(self.listH_T_postselectionTTTT))/(float(len(self.listH_T_postselectionTTTT))+float(len(self.listH_T_postselectionTT)))) 
			self.listEP_H_T.append(self.listpur_H_T[i]*self.listeff_H_T_TTTT[i])

			self.listH_Tvalues_err.append(0.)
			self.listeff_H_T_TTTT_err.append(math.sqrt(  math.pow( 1./(float(len(self.listH_T_preselectionTTTT))) ,2) +  math.pow( ( float(len(self.listH_T_postselectionTTTT)) )/( math.pow( float(len(self.listH_T_preselectionTTTT)) ,2) ) ,2)  )) 			
			self.listpur_H_T_err.append(  pow( ((1.)/(float(len(self.listH_T_postselectionTTTT))))/(pow( 1. + (float(len(self.listH_T_postselectionTT)))/(float(len(self.listH_T_postselectionTTTT))) ,2)) ,2) + pow( ((float(len(self.listH_T_postselectionTT)))/(pow(float(len(self.listH_T_postselectionTTTT)),2)))/(pow( 1.+ (float(len(self.listH_T_postselectionTT)))/(float(len(self.listH_T_postselectionTTTT))) ,2)) ,2) ) 
			self.listEP_H_T_err.append(pow(self.listpur_H_T[i]*self.listpur_H_T_err[i],2)+pow(self.listeff_H_T_TTTT[i]*self.listeff_H_T_TTTT_err[i],2))


		
		
	def savingdata(self):
		print "Writing resultes in files"
		result_H_T_eff_pur = open("result_H_T_eff_pur.txt", "w")
		print >> result_H_T_eff_pur, self.listH_Tvalues, self.listEP_H_T
                

	def plotdata(self):
		x_muonptTT = array('d',self.listmuonptvaluesTT)
		y_muonptEP = array('d',self.listmuonptEP)
		y_muonptEff = array('d',self.listeffmuonptTTTT)
		y_muonptPur = array('d',self.listpurmuonpt)
		err_x_muonptTT = array('d',self.listmuonptvaluesTT_err)
		err_y_muonptEP = array('d',self.listmuonptEP_err)
		err_y_muonptEff = array('d',self.listeffmuonptTTTT_err)
		err_y_muonptPur = array('d',self.listpurmuonpt_err)
		
		self.c1 = ROOT.TCanvas("c1") 
		self.Graph_muon_EP = ROOT.TGraphErrors(len(self.listmuonptvaluesTT),x_muonptTT,y_muonptEP, err_x_muonptTT, err_y_muonptEP)
		self.Graph_muon_Eff = ROOT.TGraphErrors(len(self.listmuonptvaluesTT),x_muonptTT,y_muonptEff, err_x_muonptTT, err_y_muonptEff)
		self.Graph_muon_Pur = ROOT.TGraphErrors(len(self.listmuonptvaluesTT),x_muonptTT,y_muonptPur, err_x_muonptTT, err_y_muonptPur)
		#self.Graph_muon_EP.GetYaxis().SetRange(0,2)
		self.Graph_muon_Eff.SetMarkerColor(ROOT.kBlue)
		self.Graph_muon_Pur.SetMarkerColor(ROOT.kRed)

		self.leg_1 = ROOT.TLegend(0.7,0.77,0.85,0.55)
		self.leg_1.SetFillColor(0)
		self.leg_1.AddEntry(self.Graph_muon_Eff,"Efficiency #epsilon","l")
		self.leg_1.AddEntry(self.Graph_muon_Pur,"Purity P","l")
		self.leg_1.AddEntry(self.Graph_muon_EP,"#epsilon*P","l")
		self.leg_1.SetTextSize(0.037)
		self.leg_1.SetBorderSize(0)
		
		self.Graph_muon_Eff.Draw("AL*P")
		self.Graph_muon_Pur.Draw("sameL*")
		self.Graph_muon_EP.Draw("sameL*")
		self.leg_1.Draw("same")

		
		x_jetptTT = array('d',self.listjetptvaluesTT)
		y_jetptEP = array('d',self.listjetptEP)
		y_jetptEff = array('d',self.listeffjetptTTTT)
		y_jetptPur = array('d',self.listpurjetpt)
		err_x_jetptTT = array('d',self.listjetptvaluesTT_err)
		err_y_jetptEP = array('d',self.listjetptEP_err)
		err_y_jetptEff = array('d',self.listeffjetptTTTT_err)
		err_y_jetptPur = array('d',self.listpurjetpt_err)
		
		self.c2 = ROOT.TCanvas("c2") 
		self.Graph_jet_EP = ROOT.TGraphErrors(len(self.listjetptvaluesTT),x_jetptTT,y_jetptEP, err_x_jetptTT, err_y_jetptEP)
		self.Graph_jet_Eff = ROOT.TGraphErrors(len(self.listjetptvaluesTT),x_jetptTT,y_jetptEff, err_x_jetptTT, err_y_jetptEff)
		self.Graph_jet_Pur = ROOT.TGraphErrors(len(self.listjetptvaluesTT),x_jetptTT,y_jetptPur, err_x_jetptTT, err_y_jetptPur)
		#self.Graph_jet_EP.GetYaxis().SetRange(0,2)
		self.Graph_jet_Eff.SetMarkerColor(ROOT.kBlue)
		self.Graph_jet_Pur.SetMarkerColor(ROOT.kRed)

		self.leg_2 = ROOT.TLegend(0.7,0.77,0.85,0.55)
		self.leg_2.SetFillColor(0)
		self.leg_2.AddEntry(self.Graph_jet_Eff,"Efficiency #epsilon","l")
		self.leg_2.AddEntry(self.Graph_jet_Pur,"Purity P","l")
		self.leg_2.AddEntry(self.Graph_jet_EP,"#epsilon*P","l")
		self.leg_2.SetTextSize(0.037)
		self.leg_2.SetBorderSize(0)
		
		self.Graph_jet_Eff.Draw("AL*P")
		self.Graph_jet_Pur.Draw("sameL*")
		self.Graph_jet_EP.Draw("sameL*")
		self.leg_2.Draw("same")




		x_H_T_TT = array('d',self.listH_Tvalues)
		y_H_T_EP = array('d',self.listEP_H_T)
		y_H_T_Eff = array('d',self.listeff_H_T_TTTT)
		y_H_T_Pur = array('d',self.listpur_H_T)
		err_x_H_T_TT = array('d',self.listH_Tvalues_err)
		err_y_H_T_EP = array('d',self.listEP_H_T_err)
		err_y_H_T_Eff = array('d',self.listeff_H_T_TTTT_err)
		err_y_H_T_Pur = array('d',self.listpur_H_T_err)
		

		self.c3 = ROOT.TCanvas("c3") 
		self.Graph_H_T_EP = ROOT.TGraphErrors(len(self.listH_Tvalues),x_H_T_TT,y_H_T_EP, err_x_H_T_TT, err_y_H_T_EP)
		self.Graph_H_T_Eff = ROOT.TGraphErrors(len(self.listH_Tvalues),x_H_T_TT,y_H_T_Eff, err_x_H_T_TT, err_y_H_T_Eff)
		self.Graph_H_T_Pur = ROOT.TGraphErrors(len(self.listH_Tvalues),x_H_T_TT,y_H_T_Pur, err_x_H_T_TT, err_y_H_T_Pur)
		self.Graph_H_T_Eff.SetMarkerColor(ROOT.kBlue)
		self.Graph_H_T_Pur.SetMarkerColor(ROOT.kRed)

		self.leg_3 = ROOT.TLegend(0.7,0.77,0.85,0.55)
		self.leg_3.SetFillColor(0)
		self.leg_3.AddEntry(self.Graph_H_T_Eff,"Efficiency #epsilon","l")
		self.leg_3.AddEntry(self.Graph_H_T_Pur,"Purity P","l")
		self.leg_3.AddEntry(self.Graph_H_T_EP,"#epsilon*P","l")
		self.leg_3.SetTextSize(0.037)
		self.leg_3.SetBorderSize(0)
		
		self.Graph_H_T_Eff.Draw("AL*P")
		self.Graph_H_T_Pur.Draw("sameL*")
		self.Graph_H_T_EP.Draw("sameL*")
		self.leg_3.Draw("same")



			







