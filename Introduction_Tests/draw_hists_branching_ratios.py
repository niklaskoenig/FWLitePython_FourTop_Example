##### drawing hist in ROOT: W Decay Branching Ratios
import ROOT
file_Count = ROOT.TFile("HistCountEvents.root")
hist_Count = file_Count.Get
hist_Count = file_Count.Get("HistCountEvents")
cv_Count = ROOT.TCanvas("cc")
hist_Count.SetFillColor(ROOT.kAzure-8)
hist_Count.GetXaxis().SetLabelSize(0)
hist_Count.DrawNormalized()
