##### drawing hists in ROOT:
import ROOT
file_muon_pt_2T = ROOT.TFile("muon_pt_TestHist_2T.root")
file_muon_eta_2T = ROOT.TFile("muon_eta_TestHist_2T.root")
file_muon_numbervalidhitstracker_2T = ROOT.TFile("muon_numbervalidhitstracker_TestHist_2T.root")
file_muon_pt_4T = ROOT.TFile("muon_pt_TestHist_4T.root")
file_muon_eta_4T = ROOT.TFile("muon_eta_TestHist_4T.root")
file_muon_numbervalidhitstracker_4T = ROOT.TFile("muon_numbervalidhitstracker_TestHist_4T.root")
file_jet_pt_2T = ROOT.TFILE("jet_pt_TestHist_2T.root")
file_jet_eta_2T = ROOT.TFILE("jet_eta_TestHist_2T.root")
file_jet_pt_4T = ROOT.TFILE("jet_pt_TestHist_4T.root")
file_jet_eta_4T = ROOT.TFILE("jet_eta_TestHist_4T.root")

hist_muon_pt = file_eLeptons.Get("geneLeptonsEtaHist")
hist_muon_eta = file_muLeptons.Get("genmuLeptonsEtaHist")
hist_muon_numbervalidhitstracker = file_tauLeptons.Get("gentauLeptonsEtaHist")
hist_jet_pt = file_uHadrons.Get("genuHadronsEtaHist")
hist_jet_eta = file_cHadrons.Get("gencHadronsEtaHist")

leg_cL = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_cL.SetFillColor(0)
leg_cL.AddEntry(hist_eLeptons,"e","l")
leg_cL.AddEntry(hist_muLeptons,"#mu","l")
leg_cL.AddEntry(hist_tauLeptons,"#tau","l")
leg_cL.SetTextSize(0.037)
leg_cH = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_cH.AddEntry(hist_uHadrons,"u","l")
leg_cH.AddEntry(hist_cHadrons,"c","l")
leg_cH.SetTextSize(0.037)
hist_eLeptons.SetLineColor(ROOT.kBlue)
hist_muLeptons.SetLineColor(ROOT.kRed)
hist_tauLeptons.SetLineColor(ROOT.kGreen)
hist_uHadrons.SetLineColor(ROOT.kBlue)
hist_cHadrons.SetLineColor(ROOT.kRed)





cv_Leptons = ROOT.TCanvas("cL")
hist_tauLeptons.SetAxisRange(0, 85, "Y")
hist_tauLeptons.Draw("")
hist_eLeptons.Draw("sames")
hist_muLeptons.Draw("sames")
leg_cL.Draw("sames")


cv_Leptons_n = ROOT.TCanvas("cL_n")
hist_tauLeptons.DrawNormalized("")
hist_muLeptons.DrawNormalized("sames")
hist_eLeptons.DrawNormalized("sames")
leg_cL.Draw("sames")


cv_Hadrons = ROOT.TCanvas("cH")
hist_uHadrons.SetAxisRange(0, 260, "Y")
hist_uHadrons.Draw("")
hist_cHadrons.Draw("sames")
leg_cH.Draw("sames")


cv_Hadrons_n = ROOT.TCanvas("cH_n")
hist_uHadrons.DrawNormalized("")
hist_cHadrons.DrawNormalized("sames")
leg_cH.Draw("sames")
