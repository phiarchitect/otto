# EMISSION WITH TROUBLE CODES


## Resetting Emission Fault Codes and Memory 

### 1990–94 Vehicles

1. Turn the ignition switch to the ON position.

2. Read fault codes.

3. Press diagnostic socket button 1 time and hold for approximately 5 seconds.
   Release button. After 3 seconds the diode light should light up. While the
   light is still lit, press the button again and hold for approximately 5
   seconds. After releasing the button, the diode light should go off.

4. To ensure that the memory is erased, press the button 1 time, for 1 second
   but not more than 3 seconds. The diode light should flash code 1-1-1.

5. Start and run engine. If engine will not start, correct the problem before
   proceeding and start over with Step 1.

6. Check to see if new fault codes have been stored in the memory by pressing
   the diagnostic socket button 1 time, for 1 second but not more than 3
   seconds.

7. If fault code 1-1-1 flashes, it indicates that there are no additional fault
   codes stored in its memory.

### 1995–98 Vehicles

Control module reset procedures are a very important part of OBD-II system
diagnostics. This step should be done at the end of any fault code repair and at
the end of any driveability repair.

Clearing codes can be performed by any of the methods below:

Clear the control module memory with the Generic Scan Tool (GST)

Clear the control module memory with the vehicle manufacturer's specific tester

Turn the ignition off and remove the negative battery cable for at least 1
minute.

Removing the negative battery cable may cause other systems in the vehicle to
loose their memory. Prior to removing the cable, ensure you have the proper
reset codes for radios and alarms.

NOTE: The MIL will may also be de-activated for some codes if the vehicle
completes three consecutive trips without a fault detected with vehicle
conditions similar to those present during the fault.


## Trouble Code Emission Diagnostics

### Location of Data Link Connector (DLC) for Emission Troubleshooting

The Data Link Connector (DLC) is located in the engine compartment near the
driver's side strut tower on Coupe, 240, 700, and 900 series vehicles without
OBD-II. On 850 models the DLC is located in the engine compartment in front of
the module box, behind the passenger side headlamp. On OBD-II equipped vehicles,
the DLC is located in the interior in center console under a cover.

Fig. 1: DLC location for the Coupe, 240, 700, and 900 series

Fig. 2: Lift the cover up to access the OBD-II DLC

Fig. 3: The OBD-II connector located in the center console with the cover
removed


## Understanding the Electronic Engine Control System

Volvo vehicles employ the Electronic Engine Control (EEC) system, to manage
fuel, ignition and emissions.

The Engine Control Module (ECM) is given responsibility for the operation of the
emission control devices, cooling fans, ignition and advance and in some cases,
automatic transmission functions. Because the EEC oversees both the ignition
timing and the fuel injector operation, a precise air/fuel ratio will be
maintained under all operating conditions. The ECM is a microprocessor or small
computer which receives electrical inputs from several sensors, switches and
relays on and around the engine.

Based on combinations of these inputs, the ECM controls outputs to various
devices concerned with engine operation and emissions. The engine control
assembly relies on the signals to form a correct picture of current vehicle
operation. If any of the input signals is incorrect, the ECM reacts to what ever
picture is painted for it. For example, if the coolant temperature sensor is
inaccurate and reads too low, the ECM may see a picture of the engine never
warming up. Consequently, the engine settings will be maintained as if the
engine were cold. Because so many inputs can affect one output, correct
diagnostic procedures are essential on these systems.

One part of the ECM is devoted to monitoring both input and output functions
within the system. This ability forms the core of the self-diagnostic system. If
a problem is detected within a circuit, the controller will recognize the fault,
assign it an identification code, and store the code in a memory section.
Depending on the year and model, the fault code(s) may be represented by two or
three digit numbers. The stored code(s) may be retrieved during diagnosis.

While the EEC system is capable of recognizing many internal faults, certain
faults will not be recognized. Because the computer system sees only electrical
signals, it cannot sense or react to mechanical or vacuum faults affecting
engine operation. Some of these faults may affect another component which will
set a code. For example, the ECM monitors the output signal to the fuel
injectors, but cannot detect a partially clogged injector. As long as the output
driver responds correctly, the computer will read the system as functioning
correctly. However, the improper flow of fuel may result in a lean mixture. This
would, in turn, be detected by the oxygen sensor and noticed as a constantly
lean signal by the ECM. Once the signal falls outside the pre-programmed limits,
the engine control assembly would notice the fault and set an identification
code.

Additionally, the EEC system employs adaptive fuel logic. This process is used
to compensate for normal wear and variability within the fuel system. Once the
engine enters steady-state operation, the engine control assembly watches the
oxygen sensor signal for a bias or tendency to run slightly rich or lean. If
such a bias is detected, the adaptive logic corrects the fuel delivery to bring
the air/fuel mixture towards a centered or 14.7:1 ratio. This compensating shift
is stored in a non-volatile memory which is retained by battery power even with
the ignition switched OFF. The correction factor is then available the next time
the vehicle is operated.

NOTE: If the battery cable(s) is disconnected for longer than 5 minutes, the
adaptive fuel factor will be lost. After repair it will be necessary to drive
the vehicle at least 10 miles to allow the processor to relearn the correct
factors. The driving period should include steady-throttle open road driving if
possible. During the drive, the vehicle may exhibit driveability symptoms not
noticed before. These symptoms should clear as the ECM computes the correction
factor.


## Reading Diagnostic Codes

1990–94 Vehicles

1. Open diagnostic socket cover and install selector cable into socket No. 2 for
   fuel injection codes or socket No. 6 (except Motronic systems) for ignition
   codes.

2. Turn the ignition switch to the ON position.

3. Enter control system 1 by pressing the button once. Hold the button for at
   least 1 second, but not more than 3.

4. Watch the diode light and count the number of flashes in the 3 flash series
   indicating a fault code. The flash series are separated by 3 second
   intervals. Note fault codes. 1f there are no fault codes in the diagnostic
   unit, the diode will flash 1-1-1 and the fuel system is operating correctly.

5. If diode light does not flash when button is pressed, or no code is flashed
   there is a problem with the soft-diagnostic system, proceed as follows:

6. 

    A. Check ground connections on the intake manifold, and the ground
    connection for the Lambda-sond at the right front mudguard.

    B. Check the fuses for the pump relay and the primary pump. On 240 models,
    fuses are located inside the engine compartment on the left side wheel well
    housing.  On 760/780 models, fuses are located in the center console, just
    below the radio. On 740/940 models, fuses are located behind the ashtray.
    Access can be gained by removing the ashtray, and pressing upward on the tab
    marked "electrical fuses press". On 850 models, the fuses are located on the
    left side of the engine compartment behind the strut mount plate. The fuses
    on 960 models are located on the far left side of the dashboard. The
    driver's door must be open to gain access to the fuses.

    C. Remove glove compartment, and check control unit ground connections.

    D. Turn the ignition switch to the OFF position. Remove control unit
    connector and connector protective sleeve.

    E. Check diagnostic socket by connecting a voltmeter between ground and No.
    4 connection on the control unit connector. Reading should be 12 volts. If
    no voltage is present, check lead between control unit connector and fuse
    No. 1 in the fuse/relay box.

    F. Turn the ignition to the ON position, and install selector cable into the
    No. 2 socket on the diagnostic socket. Connect a voltmeter between ground
    and No. 12 connection on the control unit connector. Reading should be 12
    volts. Press the button on diagnostic socket and note reading. Reading on
    the voltmeter should be 0 volts. If no voltage at the control unit is
    present, take reading at the diagnostic socket connector. If reading remains
    at 12 volts when button is pressed, check diagnostic socket.

    G. Connect a voltmeter between ground and the red/black lead on the
    diagnostic socket connector. Reading should be 12 volts.

    H. Connect a suitable ohmmeter between ground and the brown/black lead in
    the diagnostic socket connector. Reading should be 0 ohms.

    I. Turn the ignition to the OFF position. Connect ohmmeter between
    diagnostic socket selector cable and the pin under selector button. The
    ohmmeter should read infinity. Press the button and note the reading. The
    reading should be 0 ohms.

    J. Connect a suitable diode/multimeter tester, or equivalent, between the
    diagnostic socket diode light and the selector cable. Connect red test pin
    from the tester to pin under diode light and black test pin from tester to
    selector cable. A reading on the tester indicates correct diode light
    function. With no reading on tester, replace diagnostic socket.

    K. Check the system relay/primary relay by connecting a voltmeter between
    ground and the No. 9 connection on the control unit connector, then connect
    a jumper wire between ground and No. 21 connection on the control unit
    connector. The relay should activate and the reading should be 12 volts.

Press the diagnostic socket button. Note any additional fault codes.  NOTE: The
diagnostic system memory is full when it contains 3 fault codes. Until those
codes are corrected and the memory erased, the system cannot give information on
any other problems.

7. Press the diagnostic socket button for the third time to see if a third fault
   code is stored in the memory. If the diode light flashes the same code 1-1-1,
   there are no other codes in the memory.

Fig. 4: Push button once for mode 1

Fig. 5: Push button twice for mode 2

Fig. 6: Push button three times for mode 3

