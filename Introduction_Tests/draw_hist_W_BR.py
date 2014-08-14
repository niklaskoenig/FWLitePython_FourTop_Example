##### drawing hist in ROOT: W Decay Branching Ratios
import ROOT
file_Count = ROOT.TFile("HistCountEvents.root")
hist_Count = file_Count.Get
hist_Count = file_Count.Get("HistCountEvents")
hist_Count.SetFillColor(ROOT.kBlue)
cv_Count = ROOT.TCanvas("cc")
hist_Count.Draw()
hist_Count.SetFillColor(ROOT.kBlue-8)
hist_Count.Draw()
hist_Count.SetFillColor(ROOT.kAzure-8)
hist_Count.Draw()
