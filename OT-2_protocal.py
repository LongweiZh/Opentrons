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
    reservoir = protocol.load_labware('nest_96_wellplate_2ml_deep', '1')
    plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', '2')
    pipette = protocol.load_instrument('p300', 'left', tip_racks=[protocol.load_labware('opentrons_96_tiprack_300ul', '3')])

    # Define transfer parameters
    source_well = 'A1'  # Update this with the actual well containing trypsinized cells
    destination_start_well = 'A1'  # Update this with the starting well in the 384-well plate
    transfer_volume = 50  # Adjust the volume as needed

    # Perform the transfer
    pipette.pick_up_tip()

    for dest_well in plate_384.wells(destination_start_well, length=8):
        pipette.transfer(transfer_volume, reservoir.wells(source_well), dest_well, new_tip='never')

    pipette.drop_tip()