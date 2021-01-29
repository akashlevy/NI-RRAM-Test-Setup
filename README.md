# NI-Skywater-Test-Setup

LabVIEW code for testing tsmc40r chip


|         	| WL-range  	| WL-default 	| BL-range 	| BL-default 	| SL-range 	| SL-default 	|
|---------	|-----------	|------------	|----------	|------------	|----------	|------------	|
| Forming 	| 0.9~2.4V  	| 1.3V       	| 2.0~4.0V 	| 3.2V       	| 0        	| 0          	|
| SET     	| 0.9V~2.4V 	| 2.2V       	| 0.9~2.4V 	| 1.9V       	| 0        	| 0          	|
| RESET   	| 0.9~3.0V  	| 2.6V       	| 0        	| 0          	| 0.9~2.4V 	| 1.5V       	|
| Read    	| 0.9~1.3V  	| 1.1V       	| 0.1~0.3V 	| 0.2V       	| 0        	| 0          	|


## Program-Verify

## Addressing Scheme

```
< MSB.................LSB >
{wl_addr}|{wl_ext_sel}|{sl_addr[6:0]}|sl_ext_sel
```

Note that wl_ext_sel and sl_ext_sel need to be decoded programmatically to determine which wl_ext_[0:3] or bl_ext[0:1] should be high.

## Pinmap

AI4: sl_shunt_meas
AO0-AO3: wl_ext_[0:3]
DIO 0-5: wl_addr[0:5]
DIO 6-12: sl_addr[0:6]
DIO 13: wl_dec_en
DIO 14: sl_dec_en
DIO 15: sl_ext
PDC 0-1: bl_ext[0:1]

## Done and TODOs

Done with:
- Address Split.vi
- BER.vi
- BL Disable.vi
- BL Source.vi
- Close.vi
- Decode Disable.vi
- Decode Enable.vi
- Globals.vi
- Increment 2D Array Element.vi
- Iterator.vi
- Measure Current.vi
- Read.vi
- Set Address.vi
- Setup.vi (delete if not used!)
- Static Pattern.vi


TODO:
- Draw Checkerboard.vi: adapt for 1T1R only and 1D array outputs
- Dynamic Form.vi
- Dynamic RESET.vi
- Dynamic SET.vi
- RESET.vi
- RRAM.vi: cleanup and finish the other VIs
- Target Resistance.vi
