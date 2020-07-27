#ifndef L1Trigger_TrackFindingTracklet_interface_Quality_h
#define L1Trigger_TrackFindingTracklet_interface_Quality_h

#include <iostream>
#include <set>
#include <vector>
#include <memory>
#include <string>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "PhysicsTools/ONNXRuntime/interface/ONNXRuntime.h"

#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"
#include "DataFormats/L1TrackTrigger/interface/TTTypes.h"


class Quality{
  public:
    Quality();
    Quality(string Algorithm,
            string ONNXmodel,
            string ONNXInputName,
            string ONNXOutputName,
            vector<string> in_features,
            );

    Quality(string Algorithm,
            float maxZ0,
            float maxEta, 
            float chi2dofMax,
            float bendchi2Max,
            float minPt,
            int nStubsmin
            );

    ~Quality() = default;

    vector<float> Feature_Transform();
    
    void Prediction();

    void Set_Cut_Parameters();
    void Set_ONNX_Model();



  private:
    string Algorithm_ = "None";
    string ONNXmodel_;
    string ONNXInputName_;
    string ONNXOutputName_;
    vector<string> in_features_;
    float maxZ0_ = 15;
    float maxEta_ = 2.4; 
    float chi2dofMax_ = 40;
    float bendchi2Max_ = 2.4;
    float minPt_ = 2.0;
    int nStubsmin_ = 4;
    
  };
#endif