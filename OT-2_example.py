#!/usr/bin/python3
# -*- coding=utf-8 -*-

#===================================
# @Filename: OT-2_example.py
# @Author: Longwei Zhang
# @Create Time: 2023-12-04 00:25:43
# @Email: lz539@georgetown.edu
# @Description: 
#===================================

from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Simple OT-2 Protocol',
    'author': 'Your Name',
    'description': 'A simple Opentrons OT-2 protocol',
    'apiLevel': '2.11',
}

def run(protocol: protocol_api.ProtocolContext):
    # Add tips
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')

    # Load a sample plate
    sample_plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

    # Load a pipette
    pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tips])

    # Perform a simple liquid transfer
    pipette.pick_up_tip()

    for source_well, destination_well in zip(sample_plate.wells()[:6], sample_plate.wells()[6:12]):
        pipette.transfer(100, source_well, destination_well, new_tip='never')

    pipette.drop_tip()

