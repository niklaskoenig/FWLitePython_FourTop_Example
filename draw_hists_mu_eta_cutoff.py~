##### drawing hists in ROOT:
import ROOT
file_muLeptons = ROOT.TFile("genmuLeptonsEtaHist.root")
file_muLeptonsCutoff = ROOT.TFile("genmuLeptonsEtaHistCutoff.root")
hist_muLeptons = file_muLeptons.Get("genmuLeptonsEtaHist")
hist_muLeptonsCutoff = file_muLeptonsCutoff.Get("genmuLeptonsEtaHistCutoff")
leg_L = ROOT.TLegend(0.7,0.77,0.85,0.55)
leg_L.SetFillColor(0)
leg_L.AddEntry(hist_muLeptons,"#eta","l")
leg_L.AddEntry(hist_muLeptonsCutoff,"#eta (cutoff)","l")
leg_L.SetTextSize(0.037)
hist_muLeptons.SetLineColor(ROOT.kRed)
hist_muLeptonsCutoff.SetLineColor(ROOT.kGreen)
cv_Leptons = ROOT.TCanvas("cL")
hist_muLeptons.DrawNormalized("")
hist_muLeptonsCutoff.DrawNormalized("sames")
leg_L.Draw("sames")

