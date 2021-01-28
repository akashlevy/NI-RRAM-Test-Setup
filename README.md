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
P0.0-P0.5: wl_addr[0:5]
P0.6-P0.7: bl_ext_[0:1]
P1.1-P1.7: sl_addr[0:6]
P2.0: sl_dec_en
P2.1: wl_dec_en
P2.2: sl_ext





