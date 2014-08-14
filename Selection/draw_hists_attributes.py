##### drawing hists in ROOT:
import ROOT
file_muon_pt_2T = ROOT.TFile("muon_pt_TestHist_2T.root")
file_muon_eta_2T = ROOT.TFile("muon_eta_TestHist_2T.root")
file_muon_numbervalidhitstracker_2T = ROOT.TFile("muon_numbervalidhitstracker_TestHist_2T.root")
file_muon_pt_4T = ROOT.TFile("muon_pt_TestHist_4T.root")
file_muon_eta_4T = ROOT.TFile("muon_eta_TestHist_4T.root")
file_muon_numbervalidhitstracker_4T = ROOT.TFile("muon_numbervalidhitstracker_TestHist_4T.root")
file_jet_pt_2T = ROOT.TFile("jet_pt_TestHist_2T.root")
file_jet_eta_2T = ROOT.TFile("jet_eta_TestHist_2T.root")
file_jet_pt_4T = ROOT.TFile("jet_pt_TestHist_4T.root")
file_jet_eta_4T = ROOT.TFile("jet_eta_TestHist_4T.root")
file_H_T_mu_jet_TestHist_2T = ROOT.TFile("H_T_mu_jet_TestHist_2T.root")
file_H_T_mu_jet_TestHist_4T = ROOT.TFile("H_T_mu_jet_TestHist_4T.root")



hist_muon_pt_2T = file_muon_pt_2T.Get("muon_pt_TestHist_2T")
hist_muon_eta_2T = file_muon_eta_2T.Get("muon_eta_TestHist_2T")
hist_muon_numbervalidhitstracker_2T = file_muon_numbervalidhitstracker_2T.Get("muon_numbervalidhitstracker_TestHist_2T")
hist_jet_pt_2T = file_jet_pt_2T.Get("jet_pt_TestHist_2T")
hist_jet_eta_2T = file_jet_eta_2T.Get("jet_eta_TestHist_2T")


hist_muon_pt_4T = file_muon_pt_4T.Get("muon_pt_TestHist_4T")
hist_muon_eta_4T = file_muon_eta_4T.Get("muon_eta_TestHist_4T")
hist_muon_numbervalidhitstracker_4T = file_muon_numbervalidhitstracker_4T.Get("muon_numbervalidhitstracker_TestHist_4T")
hist_jet_pt_4T = file_jet_pt_4T.Get("jet_pt_TestHist_4T")
hist_jet_eta_4T = file_jet_eta_4T.Get("jet_eta_TestHist_4T")

hist_H_T_mu_jet_TestHist_2T = file_H_T_mu_jet_TestHist_2T.Get("H_T_mu_jet_TestHist_2T")
hist_H_T_mu_jet_TestHist_4T = file_H_T_mu_jet_TestHist_4T.Get("H_T_mu_jet_TestHist_4T")

leg_1 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_1.SetFillColor(0)
leg_1.AddEntry(hist_muon_pt_2T,"Muon: p_T(tt)","l")
leg_1.AddEntry(hist_muon_pt_4T,"Muon: p_T(tttt)","l")
leg_1.SetTextSize(0.037)
leg_1.SetBorderSize(0)

leg_2 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_2.SetFillColor(0)
leg_2.AddEntry(hist_muon_eta_2T,"Muon: #eta(tt)","l")
leg_2.AddEntry(hist_muon_eta_4T,"Muon: #eta(tttt)","l")
leg_2.SetTextSize(0.037)
leg_2.SetBorderSize(0)

leg_3 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_3.SetFillColor(0)
leg_3.AddEntry(hist_muon_numbervalidhitstracker_2T,"Muon: Number Valid Hits on Tracker(tt)","l")
leg_3.AddEntry(hist_muon_numbervalidhitstracker_4T,"Muon: Number Valid Hits on Tracker(tttt)","l")
leg_3.SetTextSize(0.037)
leg_3.SetBorderSize(0)


leg_4 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_4.SetFillColor(0)
leg_4.AddEntry(hist_jet_pt_2T,"Jet: p_T(tt)","l")
leg_4.AddEntry(hist_jet_pt_4T,"Jet: p_T(tttt)","l")
leg_4.SetTextSize(0.037)
leg_4.SetBorderSize(0)

leg_5 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_5.SetFillColor(0)
leg_5.AddEntry(hist_jet_eta_2T,"Jet: #eta(tt)","l")
leg_5.AddEntry(hist_jet_eta_4T,"Jet: #eta(tttt)","l")
leg_5.SetTextSize(0.037)
leg_5.SetBorderSize(0)

leg_6 = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_6.SetFillColor(0)
leg_6.AddEntry(hist_H_T_mu_jet_TestHist_2T,"H_T(tt)","l")
leg_6.AddEntry(hist_H_T_mu_jet_TestHist_4T,"H_T(tttt)","l")
leg_6.SetTextSize(0.037)
leg_6.SetBorderSize(0)

hist_muon_pt_2T.SetLineColor(ROOT.kBlue)
hist_muon_eta_2T.SetLineColor(ROOT.kBlue) 
hist_muon_numbervalidhitstracker_2T.SetLineColor(ROOT.kBlue) 
hist_jet_pt_2T.SetLineColor(ROOT.kBlue) 
hist_jet_eta_2T.SetLineColor(ROOT.kBlue) 

hist_muon_pt_4T.SetLineColor(ROOT.kRed) 
hist_muon_eta_4T.SetLineColor(ROOT.kRed) 
hist_muon_numbervalidhitstracker_4T.SetLineColor(ROOT.kRed) 
hist_jet_pt_4T.SetLineColor(ROOT.kRed) 
hist_jet_eta_4T.SetLineColor(ROOT.kRed) 

hist_H_T_mu_jet_TestHist_2T.SetLineColor(ROOT.kBlue) 
hist_H_T_mu_jet_TestHist_4T.SetLineColor(ROOT.kRed) 

cv_muon_pt = ROOT.TCanvas("c_m_pt")
hist_muon_pt_2T.Sumw2()
hist_muon_pt_4T.Sumw2()
hist_muon_pt_2T.DrawNormalized("E")
hist_muon_pt_4T.DrawNormalized("sames,E")
leg_1.Draw("sames")

cv_muon_eta = ROOT.TCanvas("c_m_eta")
hist_muon_eta_2T.Sumw2()
hist_muon_eta_4T.Sumw2()
hist_muon_eta_2T.DrawNormalized("E")
hist_muon_eta_4T.DrawNormalized("sames,E")
leg_2.Draw("sames")

cv_muon_numbervalidhitstracker = ROOT.TCanvas("c_m_nvht")
hist_muon_numbervalidhitstracker_2T.Sumw2()
hist_muon_numbervalidhitstracker_4T.Sumw2()
hist_muon_numbervalidhitstracker_2T.DrawNormalized("E")
hist_muon_numbervalidhitstracker_4T.DrawNormalized("sames,E")
leg_3.Draw("sames")

cv_jet_pt = ROOT.TCanvas("c_j_pt")
hist_jet_pt_2T.Sumw2()
hist_jet_pt_4T.Sumw2()
hist_jet_pt_2T.DrawNormalized("E")
hist_jet_pt_4T.DrawNormalized("sames,E")
leg_4.Draw("sames")

cv_jet_eta = ROOT.TCanvas("c_j_eta")
hist_jet_eta_2T.Sumw2()
hist_jet_eta_4T.Sumw2()
hist_jet_eta_2T.DrawNormalized("E")
hist_jet_eta_4T.DrawNormalized("sames,E")
leg_5.Draw("sames")


cv_H_T = ROOT.TCanvas("c_H_T")
hist_H_T_mu_jet_TestHist_2T.Sumw2()
hist_H_T_mu_jet_TestHist_4T.Sumw2()
hist_H_T_mu_jet_TestHist_2T.DrawNormalized("E")
hist_H_T_mu_jet_TestHist_4T.DrawNormalized("sames,E")
leg_5.Draw("sames")


