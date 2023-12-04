#!/usr/bin/python3
# -*- coding=utf-8 -*-

#===================================
# @Filename: OT-2_protocal.py
# @Author: Longwei Zhang
# @Create Time: 2023-11-30 15:03:05
# @Email: lz539@georgetown.edu
# @Description: 
#===================================

from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Cell Plating',
    'author': 'Longwei Zhang',
    'description': 'transfer trypsinized cells in a deep-well reservoir to 384 well plates.',
    'apiLevel': '2.11',
}
def run(protocol: protocol_api.ProtocolContext):
    # Define labware
    source = protocol.load_labware('nest_96_wellplate_2ml_deep', '1')
    #destination = protocol.load_labware('corning_384_wellplate_112ul_flat', '2')
    destination = protocol.load_labware('nest_96_wellplate_2ml_deep', '2')
    pipette = protocol.load_instrument('p300_multi',mount='right', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '3')])

    # Perform the transfer
    pipette.pick_up_tip()

    # Define transfer parameters
    # for i in range(0,13):
    #     source_well = source.columns()[i]
    #     dest_well_1 = destination.columns()[i][0:8]
    #     dest_well_2 = destination.columns()[i][9:16]
    #     for s,d in zip(source_well,dest_well_1):
    #         pipette.transfer(10,s,d,mix_before=(3,50),new_tip='never')
    #     for s,d in zip(source_well, dest_well_2):
    #         pipette.transfer(10,s,d, mix_before=(3, 50), new_tip='never')
    s = source.wells()[0:6]
    d = destination.wells()[0:6]
    for a,b in zip(s,d):
        pipette.transfer(10, s, d, new_tip='never')
    pipette.drop_tip()