# Opentrons

Python and json scripts for Opentrons OT-2 in drug response experiment.

- [Opentrons GitHub](https://github.com/Opentrons/opentrons)
- [Design](https://designer.opentrons.com)

The project is designed for Drug Synergy Response Experiment. The protocol file are set on the ProtocolDesign website.

## CherryPick

## SynergyMatrix

### Materials
15 mL conical rack NEST 2mL Deepwell reservoirs (for serial dilution preparation) 

384 well plate (needs definition created) 300 ul Tips 

- Reagents
  - 10mM stock of each compound
  - 60µM velcade (positive control)
  - DMSO 
  - HBSS
- Supplies
  - Basins
  - 384 well drug plate
  - 8 channel pipette
  - tips

### Procedure

#### Dilution
- Prepare 10mM stock
- Prepare HBSS + DMSO
  - 5.928ml HBSS + 72µl DMSO
  - 29.64ml HBSS + 360µl DMSO
- Prepare serial dilutions

The calculates below are for six 1:2 dilutions beginning at 10µM (120µM to 10µM), plus DMSO control.
Dilutions are made at 12x (25µl of cells/media + 2.5µl of each drug)

| Start Conc. | Final Conc. | Vol. HBSS+DMSO | Vol. Prev | Note      |
|:------------|:-----------:|:---------------|:----------|:----------|
| 120         |     10      | 1976µl         | 24µl      | HBSS Only |
| 60          |      5      | 1000µl         | 1000µl    | HBSS DMSO |
| 30          |     2.5     | 1000µl         | 1000µl    | HBSS DMSO |
| 15          |    1.25     | 1000µl         | 1000µl    | HBSS DMSO |
| 7.5         |    0.625    | 1000µl         | 1000µl    | HBSS DMSO |
| 3.75        |   0.3175    | 1000µl         | 1000µl    | HBSS DMSO |
| 0           |      0      | 1000µl         | 0         | HBSS DMSO |

The file SynergyMatrix_Dilution.json is set for the step. The file can be import to [design](https://designer.opentrons.com) website to set the parameters and change the step settings.

The initial state and the final state of the drugs conc. are given in the json file.

## PlateStamp