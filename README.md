# ne204_lab1

## Goals
* deplete an HPGe
* readout HPGe signal
* create pulse height spectrum
* develop calibration routine
    * energy and energy resolution
* develop configurable shaping filter
    * trapezoidal is a good starting point
    * evaluate filter with ballistic deficit and noise contributions in mind
    * estimate fano factor ?
* how does sampling rate impact energy resolution?

## configs
Using CAMIS.json, with following changes
* Sample length set to 50,000 (based on 200 us pulse length from scope, and conversion to clock cycles set at 250 Mhz)
* Pre-trigger delay set to 500 (after a few iterations, seemed like a good value)
* Invert Signal set to False
* Various changes to Trigger threshold value
* TODO: check scope to see what voltage range should be (0, 1, 2, currently set at 1 or 1.9 V)
* want pre-trigger long enough such that baseline isn't



## test7.h5
* 60 second measurement (177 events)
* 170 trigger threshold


## test0.h5
* 120 trigger threshold
* 60 second measurement (2223 events)

## samples and digitizers
* send input analog signals to ADCs which samples at 350 MSPS
* digitized outputs buffered
* once done thrown into digital buffer

## constant triggering issue?
* too high countrate will be too fast for GBit ethernet we are communicating over - fails at some point
* threw a bunch of data at it, then needs some time distribution to reset and try again


## triggering
* read through manual!
* moving window trigger - does integration over preconfigured range, if exceeds threshold then triggers
* FIP - Jordanov - finitie impulse response
* trap filter in camis config


## digital shaping
* energy is pulse height
* convert impulse into something we can measure with trapezoidal filter
* corect for exponential tailing then make trapezoidal filter
* Jordanov filtering paper
* applying 3 filters
* will fix pileup - separate them
