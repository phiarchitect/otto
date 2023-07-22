---
title: Engine and OBD Diagnostic Codes<
pageTitle: Engine and OBD Diagnostic Codes<
created: 23.202.130420
tags: [volvo,cars,740,745,760,765,780,940,945,960,965,s90,v90,maintenance,repairs,obd,diagnostic codes]
source: https://www.volvoclub.org.uk/faq/EngineOBDCodes.html
author: 
---

# Engine and OBD Diagnostic Codes<
source: [](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html)

> Volvo Engine and OBD Diagnostic Codes<


![Volvo Owners Club Logo](Engine%20and%20OBD%20Diagnostic%20Codes/voc_logo_new.jpg)

  

[VOC Home](https://www.volvoclub.org.uk/index.shtml)  |  [FAQ Home](https://www.volvoclub.org.uk/faq/FAQSummary1.html)

**Engine and OBD Diagnostic Codes [PDF](https://www.volvoclub.org.uk/faq/FAQPDFVersions/EngineOBDCodes.pdf)**

[Fuel Injection and Ignition Diagnostic Procedures in LH-Jetronic 2.4+, Regina, and EZK 116/REX 1](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#FuelInjectionandIgnitionDiagnosticCodesi)

Fault Code Tables:Bosch [LH2.4 Fuel Injection Fault Codes](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#LH24FuelInjectionFault)

Fault Code Tables: Bosch [Motronic 1.8 Fuel Injection Fault Codes](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#LH24FuelInjectionFault)

Fault Code Tables: Bosch/Regina [EZK 116 and Rex Ignition Fault Codes](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#EZK116IgnitionFaultCodes)

Fault Code Tables: Regina [Regina Fuel Injection Fault Codes](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#ReginaFuelInjectionFaultCodes)

For code tables for ABS brakes, see [ABS Diagnostic Code Retrieval](https://www.volvoclub.org.uk/faq/BrakesABS.html#ABSDiagnosticCodeRetrieval)

Other Diagnostic Code Tables and Notes:

[Cruise Control Onboard Diagnostic Codes](https://www.volvoclub.org.uk/faq/CruiseControl.html#CruiseControlOnboardDiagnosticCodes)

[ECC Climate Unit Diagnostic Codes](https://www.volvoclub.org.uk/faq/HeatingAirConditioning.html#ECCClimateUnitDiagnosticCodes)

[Power Seat Diagnostic Trouble Codes](https://www.volvoclub.org.uk/faq/InteriorSeats.html#PowerSeatDiagnosticTroubleCodes)

[SRS Airbag Diagnostic Trouble Codes](https://www.volvoclub.org.uk/faq/ElectricalSRS.html#SRSOnboardDiagnosticCodesPre1992)

[OBD-II Scanners and Tools for 960/90 Cars](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#OBDIIScanners)

[Fuel Injection and Ignition Diagnostic Procedures in Earlier Bosch LH-Jetronic 2.2: EZK 102/115/117/118 for B280/B200/B230FT](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#Bosch22Codes)

___

**Note: For further information about specific symptoms, fuel injection and ignition components, and sensors, see the relevent [FAQ files](https://www.volvoclub.org.uk/faq/FAQSummary1.html).**

___

**Abbreviations**:

AMM = Air Mass Meter

ECT = Engine Coolant Temperature sensor

ECU = Engine Control Unit computer (either fuel injection or ignition)

FI = Fuel Injection

FPR = Fuel Pressure Regulator

IAC = Idle Air Control solenoid valve

TB = Throttle Body

TPS = Throttle Position Sensor

VSS = Vehicle Speed Sensor

**General Notes on On-Board Diagnostics in Volvo RWD Cars**.

Volvo started using self-diagnostics on its Bosch LH 2.4 engine management systems in 1988 on 700 series non-turbo cars and in Regina-equipped cars. Earlier Bosch LH 2.2 and Turbo cars until 1990 had very limited self-diagnostic capability using an [LED tester](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#Bosch22Codes). In LH 2.4 cars, If a system fault occurs, then the "check engine" lamp will illuminate, signifying the presence of a fault code. For every model year using LH2.4 up to and including the '95s (except 200 series DLs and GLs), you can flash out fault codes, as well as perform input and output testing, through the OBD-I diagnostic connector unit simply by inserting a little self-contained probe and pressing a button. You do not need a special scan tool to read codes. As electronic systems were added to more Volvo models, more socket options and even more diagnostic connectors were added.

Unfortunately, you cannot use a generic code reader on any of these OBD-I cars: you have to manually extract the codes from the systems as noted below. 1996+ cars have the entirely different OBD-II system which requires a computerized code scanner to read codes through a special data link.

![](Engine%20and%20OBD%20Diagnostic%20Codes/DiagnosticUnit.gif)

The diagnostic connector units for OBD-I systems are small black rectangular boxes mounted in front of the left-side(driver-side in LHD countries) shock tower. Earlier cars have only one unit ("A"); later cars have two ("A" and "B"). Diagnostic connector "A" contains the test terminal probe (the wire mounted on the side of the box in the picture) used in both A and B along with the test button and the LED readout lamp. In diagnostic connector A, socket 1 is for the [electronic transmission](https://www.volvoclub.org.uk/faq/TransmissionAutoAW30.html#OnBoardDiagnostiCodesforAW3040SeriesAutomaticTransmissions) (if your 960 or 90-series car has the AW30/40), socket 2 for [fuel injection](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#LH24FuelInjectionFault) or Motronic, socket 3 for [ABS](https://www.volvoclub.org.uk/faq/BrakesABS.html#ABSDiagnosticCodeRetrieval), socket 6 for [ignition](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#EZK116IgnitionFaultCodes) and socket 7 for the instrument cluster. If the 1992+ car is so equipped with connector B, socket 1 is for the [climate control](https://www.volvoclub.org.uk/faq/HeatingAirConditioning.html#ECCClimateUnitDiagnosticCodes), socket 2 for [cruise control](https://www.volvoclub.org.uk/faq/CruiseControl.html#CruiseControlOnboardDiagnosticCodes), socket 5 for the [SRS](https://www.volvoclub.org.uk/faq/ElectricalSRS.html#SRSOnboardDiagnosticCodesPre1992) and socket 6 for the [memory seats](https://www.volvoclub.org.uk/faq/InteriorSeats.html#PowerSeatDiagnosticTroubleCodes).

For later 1996+ OBD-II equipped cars, the diagnostic connector was changed to an electronic data link and moved from under the hood to in front of the shifter in the console. As a result, you need a computerized scan tool to do everything from checking for codes to resetting the maintenance light. Maintenance light resetting, by the way, was returned to a push-button method in the very late '90s.

Note that 200 series DLs and GLs have self-diagnostic capability only for fuel and ignition control. All other systems except 1990-93 SRS require a proprietary tool. For '90 to '93 models with air bags, just jump a terminal to ground to get codes out of the system.

**Can't Obtain an OBD Code?** **Malfunctioning OBD Code Reader?**

\[Inquiry\] I tried obtaining a fuel injection diagnostic code and can't even get 1-1-1.

\[Response: Chris Herbst\] I have run into a LOT of Volvo products with bad diagnostic readout units, usually caused by corrosion. While it is possible that there is no signal TO the diagnostic unit, it is just as likely that either the connection in the terminal, or the connection TO the unit from the ECU computer, is bad. You should try cleaning those connections, and if necessary you can jiggle the connections until you DO get proper readings. I've never had it where I wasn't able to at least read codes and reset the computer, although sometimes it was when I was squeezing the connections into the diagnostic readout unit, or jiggling them around. While your problem could be the ECU, more likely it is corrosion or a bad connection, especially if the engine is operable. \[Chris Mullet\] When I could not get the LED to illuminate, it turned out that the LED itself was burned out. I picked up another one off a wrecked car and it got me back into business.

If you have an ohm meter to test continuity, you can pop the unit open and check out the LED, resistor, button contact, etc. Be careful as there are a couple tiny springs that can go flying when you open it up. \[Doug Bennett\] Remove the unit from the fender wall. The there is a plastic cover that covers the button. There are two small tabs, facing inward. Depress these with a small screwdriver, and carefully swivel the plastic cover away. The button will now come out. BE CAREFUL NOT TO LOSE/DROP THE TWO SMALL SPRINGS ON EACH LEG OF THE BUTTON! Luckily, I had a magnet handy. On both the bottom of the button and down in the test unit itself, are the contacts. Mine were filthy. 15 seconds with a Dremel, reassemble, and all is well!

**Does the OBD Code Pinpoint All Problems?** \[Editor\] Absolutely not: the earlier OBD-I systems are quite crude and provide a hint only. Coolant temperature and knock sensors, for example, can fail without any OBD codes being set and the only real test is further diagnostics.

___

**Fuel Injection and Ignition Diagnostic Procedures in Bosch LH-Jetronic 2.4+, Regina, and EZK 116/REX 1**

The following section describes the onboard diagnostic codes for the Bosch LH2.4 and Regina fuel injection and EZK 116/Rex1 ignition systems used on later 1988+ 2XX, 7XX, and 9XX Volvo cars.  If you have the Bosch LH2.2 or earlier systems, you do NOT have OBD capabilities and will have to diagnose sensor and performance problems using traditional manual techniques.

The later fuel injection and ignition systems incorporate a built-in diagnostic subsystem that is able to test various sensors and fuel injection or ignition components and report the results.  This diagnostic system is located behind the driver's side strut tower in the engine compartment with a readout box with several functional modes.  940 cars have two boxes: "A" and "B"; the former is used for engine diagnostics and [ABS](https://www.volvoclub.org.uk/faq/BrakesABS.html#ABSDiagnosticCodeRetrieval); the latter for SRS and [cruise control](https://www.volvoclub.org.uk/faq/CruiseControl.html#CruiseControlOnboardDiagnosticCodes).  If fault codes related to the emission system are registered, the "Check Engine" lamp on the instrument panel is lit. The test cable is mounted to the side of A.

There are three OBD diagnostic test modes (DTM):

1.  DTM 1. The fuel injection ECU continually checks the following when the car is being driven: ECU internal functions; oxygen sensor and mixture; ECT sensor; AMM; battery voltage; TPS; rpm sensor signal from the ignition ECU; speedometer signal; knock signal from the ignition ECU (except B230F and B204FT); IAC valve. The ignition ECU continually checks its own functions; the knock sensor; fuel system load signal; rpm sensor; ECT sensor; and EGR controller and temperature sensor signals. A fault in any of these causes a trouble code in DTM Mode 1. If it is emission related, then the "check engine" lamp is illuminated on the dash.
2.  DTM 2. The ECU control module, activated through the diagnostic test box button by pressing it twice, tests specific signals from sensors when it is activated with the test box button: TPS in full load or idle positions; engine speed signal from ignition ECU; air conditioning control and compressor OK; engine speed compensation for auto tranny OK. The diagnostic box responds with a flashing code if it receives the signal when the sensor is activated.
3.  DTM 3. This mode, when it is activated through the diagnostic test box button by pressing it three times, tests the signals to various control components: engine fan half and full speed; injectors; IAC valve; carbon filter solenoid; cold start valve. Whether the component is operating is ascertained by listening or feeling it.

To operate the diagnostic system, open the A box cover and insert the end of the test cable mounted on the side of the box into either socket 2 for LH 2.4/Motronic 1.8/Regina fuel injection diagnostics and component or sensor tests or socket 6 for EZK 116 ignition or California EGR diagnostics.  Place the ignition key in the ignition lock and note where key position II "KPII" is on the switch. To operate the system:

**1\. Diagnostic Test Mode 1: Fault Code Retrieval**

-   Place the cable into socket 2 (LH2.4/Regina/Motronic 1.8fuel injection test) or 6 (EZK116 or REX1 ignition test) as above
-   Turn the ignition ON to KPII without starting the engine
-   Select Mode 1 by pressing the button once and holding for more than 1 second but less than 3 seconds
-   The LED lamp will flash in successive series of three digits followed by a three-second pause.  If there are no fault codes stored, it will flash 1-1-1 indicating the fuel injection system is operating correctly. (If nothing flashes, see [No Code](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#NoOBDCode).)
-   Count the successive flashes and record the fault code.
-   Press the button again.
-   Record the fault code.  If it is the same as the previous one, then no additional codes are stored.  Repeat until all the codes stored are retrieved (maximum of three.)
-   Refer to Table 1 for the interpretation of fault codes from the LH2.4 Fuel injection System and Table 2 for codes from the EZK 116 Ignition System.
-   Move the cable into socket 6 (for ignition codes from EZK116 or REX1) or socket 2 (for fuel injection codes from LH2.4/Regina) and repeat the above.

2\. **Erasing Fault Codes.**  After you have retrieved all the Fault Codes in step 1 above, you should erase the system memory.

-   Repeat step 1 above and read the fault codes again
-   Press and hold the button for more than five seconds, then release it.
-   When the LED lights, press the button again for more than five seconds and release.  If the LED goes off, then the memory is cleared.
-   To test that memory is cleared, press the button again for >1 second and <3 seconds.  If code 1-1-1 is returned, then the memory is cleared.
-   Repeat step 1 above with the other cable position mode (2 or 6) to erase FI or ignition codes.
-   If you cannot erase the code, yet you feel the problem has been fixed, then turn the ignition off and disconnect the battery ground for a few seconds.  This will clear all the codes.  After starting the engine, if the code does not reappear, then you've fixed the problem.  If you obtain another code, then you've still got the fault.

**3\. Diagnostic Test Mode 2: System Sensor Signal Test**. This tests whether signals are received from certain sensors and switches. If they are, then a code flashes so indicating it.

-   For vehicles equipped with air conditioning, turn the a/c control to "on."
-   Turn the ignition ON to KPII and install the cable into socket 6 for ignition-related tests.
-   Press the button two times for >1 and <3 seconds each.  The LED lamp should flash rapidly. (If nothing flashes, see [No Code](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#NoOBDCode).)
-   Check the throttle position switch by turning the throttle pivot wheel slightly from within the engine compartment.  The LED should go out and then flash code 3-3-4 which indicates proper operation of the TPS. If no code is flashed and the lamp keeps flashing, the TPS is faulty.
-   After the tests, the LED should keep flashing.
-   Remove the ignition coil center lead and crank the starter motor; the engine will not start but it will turn over.  The LED should go out, then flash 1-4-1 for the RPM sensor. If no code is flashed and the lamp keeps flashing, the RPM sensor is faulty. Reinstall the coil lead and turn the ignition key ON to KPII.
-   Install the cable into socket 2 for fuel injection-related tests.
-   Press the button two times for >1 and <3 seconds each.  The LED lamp should flash.
-   Activate the following sensors.  If the LED diagnostic code shown (**note: this is not a fault code**) is present then the sensor or component is OK:
    -   TPS OK in full load position (when throttle is moved from full load)    3-3-3
    -   TPS OK in idle position (when throttle is moved from idle)     3-3-2
    -   RPM sensor signal from ignition OK   3-3-1
    -   A/C control on/off OK (when a/c switch is depressed or released)    1-1-4
    -   A/C compressor start OK     1-3-4
    -   Engine idle speed compensation for automatic tran OK 1-2-4 (depress the brake pedal, move the selector to **D** and then to **N**.)
-   Exit Mode 2 by switching off the ignition.

**4\. Diagnostic Test Mode 3:  Injection System Component Activation Test**

-   Turn the ignition ON to KPII and install the cable into socket 2 for fuel-injection-related tests.
-   Press the button three times for one second each time (waiting between >1 and <3 seconds before pressing again)
-   The diagnostic unit then sequentially tests the following components: engine coolant fan (if equipped), fuel injectors, idle air control solenoid valve, carbon filter solenoid valve (if equipped), cold start valve, radio suppression relay and fuel pump. No code is produced: you have to listen or feel each in turn to make sure it is operating.
-   Exit by switching off the ignition.

**5.  Diagnostic Test Mode 3:  EGR System Component Activation Test** (if so equipped)

-   Turn the ignition ON to KPII and install the cable into socket 6 to test the EGR system controller.
-   Press the button three times for one second each time (waiting between >1 and <3 seconds before pressing again)
-   The diagnostic unit then tests the EGR system controller which you can hear or feel. No code is produced.
-   Exit by switching off the ignition.

Table 1: **Bosch LH2.4 and Motronic 1.8 Fuel Injection Fault Codes** (\* denotes Check Engine lamp goes on). Where the Motronic 1.8 codes are different from LH 2.4, the **differences are shown in blue italic.** Read these from socket 2. See [Table 3](https://www.volvoclub.org.uk/faq/EngineOBDCodes.html#ReginaFuelInjectionFaultCodes) below for Regina fuel injection codes.

Table 2: **EZK 116 and Regina Rex Ignition Fault Codes** (\* denotes Check Engine lamp goes on)  
(REX 1 ignition system codes are shown in italic.) Read these from socket 6:

Table 3: **Regina Fuel Injection Fault Codes.** Read these from socket 2:

___

**OBD-II Scanners and Tools for 960/90 Cars**. Here are sources of OBD-II scanners and PC-based scantools for 960 and 90-series cars using OBD-II protocols:

-   [Freediag](http://freediag.sourceforge.net/): Freediag is a suite of vehicle diagnostic protocols and an OBD II (mostly) compliant Scan Tool, currently for Linux platforms.
-   [Automotive Electronics Services](http://www.aeswave.com/): Suppliers of a variety of electronics and scan tools, including adapters and software for PDAs and laptops
-   [OBD Auto Diagnostics](http://www.obddiagnostics.com/): Makers of a simple interface box to read codes on a laptop.
-   [OBDII Vehicle Scan Tool](http://www.obd-2.com/): Software interface and OBDII manager for Windows
-   [OBDScan](http://www.ghg.net/dharrison/obdscan.html): Interface and software for Windows laptops or Palm PDA.

Other information, buying guides, and links are found at:

-   [AutoTap](http://www.obdii.com/): Buying guides and basic information on OBD-II

\[Tip\] I purchased a $99.00 OBDII code scanner for the '96 and newer 960's from   [http://www.ghg.net/dharrison/obdscan.html](http://www.ghg.net/dharrison/obdscan.html)  I received a ISO9141-compatible device that connects between the OBDII connector on the car and the serial port on a PC. It arrived today and I installed the software on my laptop (3 diskettes) and took the unit out to my '96 960 wagon. I connected it up to the 960's OBDII port and started the program on my laptop. When I turned on the ignition, the scanner successfully connected to the ECU and they started communicating.  At first, it appeared that although it was telling me that the MIL lamp was not on and that I had no trouble codes set, it did not provide a list of parameters that I could monitor in real time...  The instructions mentioned that some cars start the OBDII communications with the transmission ECU, and that’s what appears to have happened here.  There is an on-screen button you can toggle to "Change ECU's". Once I toggled this button, the engine ECU came on-line.  I'm very pleased that for $99.00 I now have a tool that can monitor a number of engine parameters, report OBDII trouble codes and reset the MIL lamp.

___

**Fuel Injection and Ignition Diagnostic Procedures in Earlier Bosch LH-Jetronic 2.2, EZK 102/115/117/118 for B280/B200/B230FT**.

-   Using [test diode #5280](https://www.volvoclub.org.uk/faq/EngineV6.html#DesignforanLEDSensortoDiagnosetheV6), connect the LED to the test terminal (yellow/red lead, usually by left front wheel well), and the red lead to the positive battery terminal.
-   Turn ignition on, do not start car.  LED should be illuminated
-   Start car.

 **B23FT (EZ-102K):** Rev engine past 3000 RPM (light should turn off) and allow it to idle around 1000 RPM.  Watch for flashes.

 **B200E, B230 E/F/K, B280 E/F (EZ-118K, EZ-117K, EZ-115K):** Slowly rev engine past 700 RPM (B280) or 920 RPM (others).  Light should turn off.  Drive car (high and low load conditions).  Then, quickly rev engine past 2500 RPM (to check the knock sensors, B280).  Make sure to reach full throttle, and to rev past 3150 RPM (B200/B230).  Watch for flashes for at least three minutes. 

**EZ-102K codes:**

-   1 flash: Maximum timing retardation reached (9.8 degrees)
-   2 flashes: Low battery voltage
-   3 flashes: Fault in control unit (knock sensor circuit), replace ICU.
-   4 flashes: Fault in knock sensor or wiring.
-   5 flashes: Faulty load signal from fuel injection ECU

 **EZ-115K codes:**

-   1 flash: Knock occurred
-   2 flashes: Faulty signal from temperature sensor
-   3 flashes: ---
-   4 flashes: Faulty signal from knock sensors, or ICU knock detection circuit faulty
-   5 flashes: Faulty signal from #1 cylinder detector (#1 spark plug lead)

 **EZ-117/118K codes:**

-   1 flash: Maximum timing retardation reached under full throttle acceleration
-   2 flashes: Temperature sensor fault (B230K only)
-   3 flashes: Maximum timing retardation reached at idle or > 3150 RPM
-   4 flashes: Faulty load signal from fuel injection ECU (engine at part load, not idling)
-   5 flashes: Insufficient advance at idle (B200E/B230E/B230K only)
-   6 flashes: Insufficient advance (B230K only)

___
