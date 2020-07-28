import FWCore.ParameterSet.Config as cms

from RecoVertex.BeamSpotProducer.BeamSpot_cfi import *

from L1Trigger.TrackFindingTracklet.Tracklet_cfi import *

from SimTracker.TrackTriggerAssociation.TrackTriggerAssociator_cff import *

# prompt hybrid emulation
TTTrackAssociatorFromPixelDigis.TTTracks = cms.VInputTag(cms.InputTag("TTTracksFromTrackletEmulation", "Level1TTTracks") )

L1HybridTracks = cms.Sequence(offlineBeamSpot*TTTracksFromTrackletEmulation)
L1HybridTracksWithAssociators = cms.Sequence(offlineBeamSpot*TTTracksFromTrackletEmulation*TrackTriggerAssociatorTracks)

# extended hybrid emulation
TTTrackAssociatorFromPixelDigisExtended = TTTrackAssociatorFromPixelDigis.clone(
    TTTracks = cms.VInputTag(cms.InputTag("TTTracksFromExtendedTrackletEmulation", "Level1TTTracks") )
)

L1ExtendedHybridTracks = cms.Sequence(offlineBeamSpot*TTTracksFromExtendedTrackletEmulation)
L1ExtendedHybridTracksWithAssociators = cms.Sequence(offlineBeamSpot*TTTracksFromExtendedTrackletEmulation*TTTrackAssociatorFromPixelDigisExtended)

# both (prompt + extended) hybrid emulation 
L1PromptExtendedHybridTracks = cms.Sequence(offlineBeamSpot*TTTracksFromTrackletEmulation*TTTracksFromExtendedTrackletEmulation)
L1PromptExtendedHybridTracksWithAssociators = cms.Sequence(offlineBeamSpot*TTTracksFromTrackletEmulation*TrackTriggerAssociatorTracks*TTTracksFromExtendedTrackletEmulation*TTTrackAssociatorFromPixelDigisExtended)

# extended hybrid emulation
TTTrackAssociatorFromPixelDigisWithQuality = TTTrackAssociatorFromPixelDigis.clone(
    TTTracks = cms.VInputTag(cms.InputTag("TTTracksFromTrackletEmulationWithQuality", "Level1TTTracks") )
)

L1HybridTracksWithQuality = cms.Sequence(offlineBeamSpot*TTTracksTrackletEmulationWithQuality)
L1HybridTracksWithAssociatorsWithQuality = cms.Sequence(offlineBeamSpot*TTTracksTrackletEmulationWithQuality*TTTrackAssociatorFromPixelDigisWithQuality)
