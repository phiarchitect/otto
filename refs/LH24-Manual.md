
# Fuel System LH2.4 - 240  

## Specifications

- Gasoline, unleaded 
- Octane requirements: 
  - RON (Research Octane Number) 91-95
  - AKI (Anti Knock Index) 87
- Control unit (part numbers):
  - With EGR (California):  
    - Volvo PIN: 3501687-2  
    - Bosch PIN: 0 280 000 556
  - Without EGR (remainder of USA, Europe):
    - Volvo PIN: 3517407-7
    - Bosch PIN: 0 280 000 561
- Air mass meter:
  - Volvo PIN: 3517020
  - Bosch PIN: 0280212016
- Resistance between connectors 2 and 3: 25-40 Ω
- Fuel pressure regulator:
  - Volvo PIN: 3517064-6
  - Bosch PIN: 0 280 160 294  
- Throttle switch:
  - Volvo PIN: 3517068-7
  - Bosch PIN: 0280120325
- System pressure (fuel pressure above intake manifold pressure): 300 kPa (42 psi)
- Injectors:
  - Volvo PIN: 3517572-8
  - Bosch PIN: 0280150762
- Injection capacity 214 cm3/min at 300 kPa (42 psi) system pressure. 
  - (Note: use only special equipment to test disassembled injector)
- Fuel pump:
  - Volvo PIN: 1389449-8
  - Bosch PIN: 0580 464 039
- Pump capacity at 300 kPa (42 psi) and +20°C (68°F):
  - 12 V: 130 liters/hour, 1.0 liters/30 sec
  - 11 V: 108 liters/hour, 0.8 liters/30 sec 
  - 10 V: 65 liters/hour, 0.6 liters/30 sec
- Current consumption at 300 kPa (42 psi), +20°C (68°F) and 12 V:
  - Maximum: 6.5 amp
- Cold start valve (certain models):
  - Volvo PIN: 3517130-5
  - Bosch PIN: 0 280 170 264  
- Injection capacity around 165 cm3/min.
- Fuel filter:
  - Volvo PIN: 1389450-6
  - Filters particles down to min. of: 0.002 mm
- Tightening torque: 20-35 Nm (15-25 ft-lb)
- Tank pump:
  - Volvo PIN: 1389721-0 (1317671)
  - Current consumption: 3-4 amp

## Special Tools 

999-5011-5: Pressure gauge - indicating fuel pressure. Used with 5116, 5265, 5266.

999-5116-2: Hose - connecting pressure gauge 5011.  

999-5151-9: Adaptor - CO meter.

999-5843-1: Vacuum pump - checking pressure regulator.

999-6450-4: Volt Amp meter - fault tracing.

999-6525-3: Multimeter - volt, amp, ohm, diode. 

999-9724-0: Ohm-diode meter - fault tracing.

999-9921-0: Volvo Mono-Tester - setting ignition, idling speed.

## Design and Function

### System Overview

The fuel system LH2.4 for Volvo 240 has the following characteristics:

- It is used together with the EZ116K ignition system.

- It requires no adjustment of CO because of the adaptive function.

- It is an adaptive system, being capable of multiple adjustments based on driving experience. 

- It has a "limp home" setting at the idle valve. In case of loss of current, the idle valve remains open to provide emergency air intake.

- It is monitored by a self-diagnostic system that lights up a warning lamp on the instrument panel. 

- It has a memory capability of up to three fault codes (Scandinavia/USA Federal) plus seventeen additional codes (USA/California). Subsequent fault tracing can be carried out by actively utilizing the diagnostic program.

- It measures intake air mass via air mass meter supplied with a hot wire. 

- It utilizes a primary pump in the fuel tank and a fuel pump with fuel filter on the fuel line to the engine.

- It works on a fuel pressure of 300 kPa (42 psi).

- It utilizes a separate cold start valve which supplies extra fuel at, or below 15°C (60°F) or colder.

- It provides a richer fuel mixture to counteract knock when the fuel system's anti-knock control system has been unsuccessful at reducing knock by adjusting downward several degrees. 

- In the USA: It has an integrated shift indicator related to vehicle speed and engine rpm. The indicator lamp lights up if the rpm for the next gear are higher than the pre-programmed limits.

- It uses an induction sensor on the flywheel to indicate rpm and crankshaft position via the ignition system control unit.

- It is fitted with the same model Lambda-sond as for previous LH fuel systems. The resistance of the Lambda-sond is affected by the exhaust-gas/oxygen concentration. The Lambda-sond is mounted on the exhaust manifold between the engine and the catalytic converter.

- It is fitted with a three-way catalytic converter. 

- It utilizes an EVAP system to handle fuel vapors in the fuel tank.

- It provides a richer fuel mixture to counteract knock when the fuel system's anti-knock control system has been unsuccessful at reducing knock by adjusting downward several degrees on all cylinders. Knock causes high combustion temperatures. When knock occurs, the control unit increases the amount of fuel in order bring the combustion temperature down and reduce the knock.

- Excess rpm is prevented via a rotation speed limiter which turns off the injectors. They are turned on again when the engine rotation is reduced. 

- During deceleration, fuel injection is discontinued above 1,800 rpm in all gears. It is resumed at 1,400 to 2,000 rpm, depending on engine temperature.

### Control Unit

The control unit has a microprocessor that receives signals from the various sensors regarding operational conditions, evaluates them in relation to pre-programmed values and calculates the correct injector opening durations (in milli-seconds per revolution). 

The control unit governs idling rpm by regulating the amount of air by-passing the throttle valve. It also controls other functions, such as the cold start valve, the fuel pump and the relay. One important function is monitoring fault tracing via the diagnostic socket.

#### Self-Adjusting Functions

The control unit is adaptive in that it adjusts its calculations according to assimilated input. 

In time, wear and coatings will affect the operation of the throttle valve, causing less air to enter the intake system. Instead of working from a pre-programmed value the idle valve receives a signal that is adapted to the experiences which the control unit has learned from previous driving periods.

The Lambda-sond operates in a similar fashion. It senses if the fuel mixture is rich or lean and adjusts the control unit's Lambda regulator accordingly. The self-regulating mechanism keeps the control unit function at midpoint. This does away with the need to adjust the CO content and automatically compensates for the effects of tolerances and wear in the injection system.

Whenever the vehicle is started and driven, the control unit will use the value that has been learned from previous driving periods.

#### The Control Unit Microprocessor:

- Sets the voltage of the system by grounding the system relay.

- Breaks the system relay ground if engine turns over too slowly (engine has stopped). This keeps the battery from being drained and cuts off fuel flow from the fuel pump when the engine isn't in operation.

- Grounds the injectors, which regulates opening, timing and injection duration.

- Controls air valve for constant idle speed (CIS).

- Is connected to the diagnostic unit and provides fault information about the various functions. 

- Provides the ignition system control unit with load information. 

- Protects against too high rpm by shutting off fuel injection until the engine has slowed down.

- USA/Canada: governs CHECK ENGINE warning lamps and shift indicator lamp.

#### The Control Unit Microprocessor Receives:

- Exhaust gas oxygen content information from the Lambda-sond.

- Rpm and crankshaft position information from the ignition system control unit. If this information is not forthcoming, the fuel system control unit will not function.

- Engine temperature information from the coolant temperature sensor. 

- Engine load information from the air mass meter.

- Information from the shutter switch as to whether the throttle shutter is closed or wide open.

- Electrical system voltage from the battery current. 

- The signal from the AC switch informs if it is on, and the signal from the compressor connection indicates that the compressor is operating.

#### Start-Up Program:

The start-up program provides for two injection durations per revolution.

The cold-start valve is activated when the temperature is at -15°C (5°F) or below, and the engine speed is under approximately 900 rpm. Once the rpm exceed the pre-programmed limit, the cold-start valve is turned off.

The choke provides a richer fuel mixture to the engine up to an engine temperature of 60°C (140°F). 

#### Injection Duration: 

Injection duration increases during acceleration.

During normal driving conditions, injection duration is regulated mostly with reference to signals from the air mass meter.

At full load, a richer air/fuel mixture is used to provide maximum engine power and to lessen the effects of combustion heat on the engine and the catalytic converter.

### Sensors

#### Air Mass Meter

Measures engine intake air mass. Those factors which affect air density, such as temperature, humidity and pressure (altitude) etc. are taken into consideration during measurement. 

The measurement sensor inside the air mass meter consists of a wire which is maintained at 120°C (250°F) (previously 100°C (215°F)) higher than the ambient air entering the engine. As the air mass passing over the wire increases, more current is required to maintain the correct temperature. The amount of current required is used to calculate the air mass taken in. 

When the engine is turned off, any dirt on the wire is burned off electrically by heating the wire to over 1000°C (1800°F). Any dirt remaining on the wire would cause it to send incorrect information to the control unit and result in an incorrect fuel/air mixture.

Earlier models of the air mass meter were provided with an adjustment screw for CO settings. However, because the LH2.4 Lambda-sond is self-adjusting this screw is no longer necessary.

#### Coolant Temperature Sensor

Provides the control unit with information regarding the engine temperature necessary for proper adjustment of injection duration.

#### Throttle Switch  

Tells the fuel system and ignition system control units whether the throttle valve is closed or fully open.

#### Lambda-Sond 

Under normal conditions, the optimum mixture ratio is 14.7kg air to 1kg fuel. The ratio is monitored by post-combustion measurement of the oxygen content in the exhaust gas using the Lambda-sond. This particular model of Lambda-sond is known as a "comparing Lambda-sond". It produces a measurable current by comparing the amount of oxygen in the exhaust gas with the amount in the ambient air.

The Lambda-sond operates only within a certain temperature range - approx. 285-850°C (545-1530°F). It is electrically heated to enable it to reach operating temperature quickly. When the ignition is turned on, current is sent to a PTC resistor (Positive Temperature Coefficient) whose resistance increases with rising temperature. Because of this system, the Lambda-sond quickly reaches correct operating temperature, even at low exhaust gas temperatures.

The exhaust gases reach the outer surface of the Lambda-sond sensor via slits in the protective sleeve. Ambient air reaches the sensor's inner surface via channels. The sensor itself consists of a platinum covered zirconium-oxide pipe. 

The Lambda-sond signal strength is in direct proportion to the amount of oxygen in the exhaust gases. This depends on the air/fuel ratio. A Lambda value of 1 represents the theoretically perfect ratio. A rich mixture results in a higher voltage and a lean mixture gives the opposite result. 

The current sent by the Lambda-sond to the control unit varies between 0.1 and 1.0 volt. The shift between high and low voltage occurs when the Lambda value is at 1. The control unit uses this information to adjust the amount of fuel injected.

The Lambda-sond is mounted in the exhaust gas manifold about 15 cm (6 in.) in front of the catalytic converter.

### Catalytic Converter, Pressure Regulator

#### Catalytic Converter

In order to be able to operate as intended, the catalytic converter is dependent on correct information from the Lambda-sond. The air/fuel mixture must be adjusted so that fuel is completely burned in the engine prior to the exhaust gases reaching the catalytic converter. 

The converter can be damaged through overheating if unburnt fuel is emitted in the exhaust where oxygen is present. This can happen if a large amount of unburnt fuel reaches the catalytic converter prior to starting. It can also happen if there is a loose ignition cable, and a cylinder pumps unburned fuel into the exhaust.

Lead in the fuel will quickly affect the Lambda-sond and cause the exhaust gas cleaning function to stop working. If this happens, the Lambda-sond will stop providing the information needed by the control unit to set the fuel mixture and the catalytic converter will then be destroyed.

The active area is about 20,000 sq. m (215,000 sq. ft.). (California EGR converter approx. 32,000 sq. m (345,000 sq. ft.)). The precious metal content is about 2 grams (0.07 oz) of platinum/rhodium. 

The catalytic converter cleans the exhaust gases in three ways:

1. By incinerating unburned hydrocarbons (HC) at high temperature, releasing the residue as steam (H2O).

2. By converting carbon oxide (CO) to carbon dioxide (CO2) through oxidation. 

3. By reducing nitrogen oxides (NOx) to gaseous nitrogen (N).

90 to 95% of the dangerous gases are rendered harmless.

#### Fuel Pressure Regulator 

The fuel pressure regulator ensures that the fuel pressure remains constant at the injectors. Using a vacuum tube connected to the engine intake manifold, the fuel pressure is kept at 300kPa (42 psi) above (below) the intake manifold pressure. In this way the pressure over the injectors is kept constant, regardless of throttle position. The amount of fuel injected depends entirely on the injection duration. Excess fuel is returned to the fuel tank via a return pipe.

### Injectors, Cold Start Valve, Fuel Pumps

#### Injectors

The injector is fitted with a solenoid, a magnetic actuator and a fuel needle which opens or shuts a nozzle. The control unit feeds current to the injectors in calculated time units. This ensures that all the injectors spray a fine fuel mist simultaneously. 

While the starter motor is operating, there are two injections per rotation. This is reduced to one for normal driving. Injection occurs in the intake manifold near the intake valves.

Disassembled injectors should only be inspected using specially designed equipment in order to minimize the risk of explosion from the fuel mist. 

#### Cold Start Valve (Certain Models)

At cold start, a lot of fuel condenses on the cold surfaces in the form of droplets. Having a separate cold start valve improves cold starting. It's placed farther away from the engine block than the ordinary injectors and delivers the fuel more as a gas than as drops. The cold start valve is controlled directly by the control unit, rather than by the thermal time switch. It cuts in when the temperature is about -15°C (5°F) and when the engine rotation is below approx. 900 rpm. It cuts out permanently if the rpm exceed the permissible limit.

#### Fuel Pump 

The fuel pump is an electric roller pump, cooled by the fuel which flows through it. It has a non-return valve and an overflow valve which opens if the pressure gets too high. 

Both the primary pump and the fuel pump operate when either the starter motor or the engine is running. However, should the engine stop while the ignition remains on, the control unit will cut off the current to the pumps in order to eliminate the risk of fire in the event of an accident.

### Fuel Filter, Idle Valve

#### Tank Pump (Pre-Pump) 

The electric impeller pump in the fuel tank keeps pressure in the fuel line prior to the (main) fuel pump to prevent vapor lock.

The pump has a coarse, strainer type filter and a non-return valve to maintain a certain amount of pressure in the system even if the main pump is not in operation. 

#### Fuel Filter

The fuel filter is adjacent to the fuel pump and both are mounted on a plate below the vehicle under the back seat.

It consists of a paper filter and a safety screen to catch any pieces of the paper filter which come loose.

#### Idle Valve

In order to set the correct air valve opening and thus achieve constant idle speed, the control unit uses information from the air mass meter regarding the amount of air entering the engine and from the ignition system control unit regarding rpm. This means that the idle valve is not affected by air leaks or a jammed throttle valve.

When the current is off, a spring sets the idle valve opening for an idle speed between 1,000 and 1,100 rpm. 

Once the engine is running, the control unit ensures that the idle valve is more or less open at all rotation speeds in order to prevent the development of unnecessarily high negative pressure in the intake manifold when the throttle shutter closes suddenly during deceleration.

The control unit receives a signal from the AC control when the AC is turned on or off to enable it to adjust the idle valve. Signals are also sent to the control unit from the AC compressor so that the idle valve can be adjusted each time the compressor turns on or off. 

### System Relay, Fuses  

#### System Relay

Governed by the control unit, it provides current to the fuel pump, the injectors, the cold start valve, the air mass meter and to certain control unit functions.

The system relay and its functions are protected by a 20 amp fuse.

#### Fuses

The system relay is protected by a 25 amp fuse and the tank pump by a 15 amp fuse.

### Ignition System

Connected to the fuel system control unit to provide rpm and crankshaft position information. If this information is not forthcoming, the fuel system control unit will not function.

### EVAP System

This system handles the gases that result from normal fuel tank evaporation, keeping them from escaping and polluting the air.

Via a hose system, the fuel vapor passes from the filler opening through a roll-over valve to a reservoir ("canister", "carbon filter"). The fuel vapor is absorbed here. The reservoir is provided with an EVAP valve which prevents leakage of fuel vapor while the engine is not in operation.

#### Reservoir (Carbon Filter)

The fuel vapors from the fuel tank enter the top of the active carbon filter and are absorbed. Air is pushed out through a channel in the bottom of the filter. Depending on temperature and other conditions, the filter can bind approx. 90 grams of fuel.

#### Roll-Over Valve

If the vehicle leans sideways at more than a 45° angle, this valve closes, helping to prevent fuel spills during accidents.

#### EVAP Valve

This valve is located at the top of the carbon filter and is closed when the engine is turned off. It's also closed during idling in order not to interfere with the automatic idle settings or make the fuel mixture too rich. The valve is closed using vacuum pressure taken from the intake manifold and through being connected to the throttle shutter positive terminal.

Increased engine load opens the EVAP valve, allowing fuel vapor to flow from the carbon filter into the engine intake manifold. Air is drawn in at the same time through the bottom channel. Under normal conditions, the filter is emptied of fuel in 15 to 20 minutes.

### Fuel System Diagnostics

The fuel system has a built-in self-diagnostic system and a functions testing system. It uses the same diagnostic socket as the ignition system and is located behind the left spring strut tower in the engine compartment.

The diagnostic system uses socket 2 for the fuel system and socket 6 for the ignition system.

There are eighteen different fault codes in the diagnostic system. It is capable of storing up to three fuel system faults.

The fuel system control unit carries out continuous checks of the following functions while the engine is running:

- The control unit's own internal functions.

- Lambda-sond and Lambda settings.

- Coolant temperature sensor.

- Air mass meter.

- Battery voltage.

- Throttle shutter.

- Ignition settings and engine rpm (through the ignition system control unit).

- Speedometer.

- Knock indicator.

- Idle speed air valve.

- Injectors.

Faults in any of these functions are registered in the diagnostic system memory.

### Fault Tracing, Repairs, Maintenance

#### Placement of Components

**Lambda-Sond:** Mounted in the exhaust gas manifold about 15 cm (6 in.) in front of the catalytic converter.

**Fuel System Control Unit and System Relay:** Located inside the panel in front of the right door pillar, along with the ignition system control unit.

**Tank Pump (Pre-Pump):** Inside fuel tank (fuel level sensor section).

**Fuel Pump and Fuel Filter:** On a shelf below the vehicle, under the back seat.

#### Fault Tracing

The fuel system has a built-in fault tracing system mounted in the control unit. It has three different control functions:

- Read fault codes stored in the memory
- Continuous testing of components
- Initiate functions cycle to test component operation

Communication uses the diagnostic socket, also used by the ignition system.

**Control Function 1 - Read Fault Codes**

- Up to 3 fault codes can be stored simultaneously.
- Codes are read through flash sequences from the diagnostic socket light diode.
- There are 18 possible fault codes.
- Once faults are corrected, the memory must be erased.

**Control Function 2 - Component Testing**

- Tests functions like throttle switch, idle valve, AC compressor, etc.
- Activates components and gets feedback through flash sequences.

**Control Function 3 - Functions Cycle**

- Tests adjustment functions with ignition off.
- Activates components like injectors and idle valve to check operation.

#### Complete Fuel System Check

**Fuses, Grounding, Connectors:** Confirm fuses are OK, ground connections are tight, and connectors properly installed.

**Air Leaks, Throttle Shutters:** Check for intake leaks. Clean throttle housing. Set basic idle. Adjust throttle switch and cable.

**Pumps, Pressure Regulator:** Check fuel pressure. Test pump operation. Ensure pressure regulator functions properly.

**Components, Electrical Cables:** Check sensors, solenoids, switches, and cabling. Confirm voltages, resistances, etc.

**Injectors:** Quick check operation using diagnostic system.

#### Fuses, Grounding, Connectors 

- Check all ground connections make good contact, especially intake manifold.

- Confirm fuses for pump relay and primary pump are OK.

- Check connectors installed properly for components like air mass meter, sensors, etc.

- Verify injector connectors have correct colored sleeves.

#### Air Leaks, Throttle Shutters

- Check intake system for leaks in hoses, connections, manifold, etc. 

- Clean throttle housing and replace gasket if needed.

- Set basic idle by fully closing throttle and adjusting screw.

- Check/adjust throttle switch setting by listening for click when opening throttle slightly.

- Ensure throttle cable and linkage allow full throttle travel without restricting idle stop.

#### Pumps, Pressure Regulator, Fuel Lines

- Connect pressure gauge between fuel line and distribution pipe.

- Operate pumps by jumping relay connector terminals. Listen for pump operation.

- Check system pressure is 300 kPa (42 psi). 

- If too high/low, test by removing return hose from regulator. Replace regulator if faulty.

- Verify regulator function by applying vacuum and checking pressure drops.

- Inspect fuel lines, filters, strainers if pressure too low. Test fuel pump separately if needed.

#### Components, Electrical Cables 

- Check ground connections on control unit connector.

- Verify diagnostic socket wiring and function using voltmeter, ohmmeter, diode test.

- Confirm sensor connections and perform resistance tests:

  - Air mass meter: 2.5-4.0 Ω between pins 6 & 7

  - Coolant temperature: depends on temperature 

    - -10°C = 8260-10560 Ω

    - +20°C = 2280-2720 Ω  

    - +80°C = 290-364 Ω

  - Throttle switches: 

    - Idle: 0 Ω when closed, 2-3 kΩ when open

    - Full load: ∞ Ω when closed, 0 Ω when open

- Ensure rpm signal by testing voltage on control unit with starter motor running.

- Check AC related wires using ohmmeter.

- Test injector resistance (4 Ω) and cold start valve (10 Ω). 

- Verify knock sensor, speedometer, lambda-sond wiring.

- Try new control unit if engine won't start and no faults found. 


#### Injectors

Quickly test injector operation using diagnostic system control function 3 to activate the injectors. 

Listen and feel each injector to verify operation. Swap connectors to faulty injectors to check if issue is with connector/wiring or injector itself. 

Check resistance of each injector separately - should be approximately 16 Ω.

#### Fuel Distribution Pipe, Injectors, Pressure Regulator - Remove/Install

- Remove/install fuel distribution pipe, injectors and cold start valve as one unit. Use a brace to loosen/tighten fuel line fittings.

- Check O-rings and lubricate with petroleum jelly before reinstalling. 

- Install pressure regulator against fuel distribution pipe and bolt to bracket.

- Inspect vacuum hose and return hose when reinstalling.

#### Fault Tracing

**Step 1:** Read and note any fault codes stored in diagnostic system memory using control function 1.

**Step 2:** Erase codes once faults are repaired so new codes can register. 

**Step 3:** Run engine and check for new codes. Continue troubleshooting if necessary.

**Step 4:** Use control function 2 to test components like throttle switch, AC compressor, etc.

**Step 5:** Control function 3 activates injectors, idle valve, etc. to quickly check operation.

**Step 6:** Check entire fuel system thoroughly:

- Fuses, grounding, connectors 

- Air leaks, throttle linkage

- Fuel pumps, pressure regulator

- Sensors, wiring  

- Try new control unit if needed

