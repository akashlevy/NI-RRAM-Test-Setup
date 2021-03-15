# NI-Skywater-Test-Setup

LabVIEW code for testing tsmc40r chip


## TSMC-recommended values

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

## Chips

Chip 1: Breakout Board Chip, status: unsure if working, looks like the wire bonds are shorted...
Chip 2: Prototyping Chip, status: some cells over-SET, working otherwise, nothing formed past 2512 as far as known
Chip 3: FORMed all, programmed with first set of inputs (HRS: 70-90kOhm)... was somewhat working, but then we tried to push to 500kOhm and shorted a bunch of cells. Lesson learned: don't push past 100kOhm.
Chip 4: FORMed every 8 cells, programmed with a simple debug vector, working but cell HRS is 70-90kOhm
Chip 5: FORMed every 8 cells, programmed with a simple debug vector, HRS is >100kOhm, working
Chip 6: FORMed all, programmed with first set of inputs (HRS: >100kOhm), working!!! But now shorted
Chip 7: FORMed all, programmed with second batch of inputs (HRS: >100kOhm), TODO: reexamine
Chip 8: FORMed all, programmed with a simple debug vector (same as 4), we think the sense amp might be broken
Chip 9: prototyping
Chip 10: unused
