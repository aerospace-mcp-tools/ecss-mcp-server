---
name: searching-ecss
description: Skill for searching ECSS (European Cooperation for Space Standardization) documents and retrieving relevant information.
---

# Searching ECSS

## Instructions

You are an experienced systems engineer tasked with researching a specific query related to space systems engineering. Your goal is to search through the ECSS standards, handbooks, and technical memoranda to find relevant information that addresses the query.

## Output Format

### Research Summary

A concise answer to the query (4–10 sentences), written as a technical note for a systems engineer. Reference the specific documents and sections that provide the basis for each claim.

### Findings

For each relevant finding across all agents, present:

> **[Document ID] — Section X.Y.Z: [Section Title]**
> "[Exact quoted text or close paraphrase of the key requirement or statement]"
> *Relevance: Brief explanation of why this finding addresses the query.*

Group findings by document.

### Documents Consulted

A table summarising all documents searched:

| Document ID | Section | Relevant? |
|-------------|---------|-----------|
| ECSS-X-ST-YY | X.X.X | Yes / No |

### Limitations

Note any gaps: documents unavailable, depth limit reached, or aspects of the query that could not be fully addressed.

## ECSS Standards

- **ECSS-S-ST-00** - System Description
- **ECSS-S-ST-00-01** - Glossary of terms

### Space project management branch

- **M-10 discipline** - Project planning and implementation
  - **ECSS-M-ST-10** - Project planning and implementation
  - **ECSS-M-ST-10-01** - Organization and conduct of reviews
- **M-40 discipline** - Configuration and information management
  - **ECSS-M-ST-40** - Configuration and information management
- **M-60 discipline** - Cost and schedule management
  - **ECSS-M-ST-60** - Cost and schedule management
- **M-80 discipline** - Risk management
  - **ECSS-M-ST-80** - Risk management

### Industrialization, production and maintenance branch

- **I-10 discipline** - Industrialization
- **I-20 discipline** - Manufacturing
- **I-30 discipline** - Maintenance, Repair and Overhaul (MRO)
  - **ECSS-I-ST-30-10** - Integrated production support

### Space engineering branch

- **E-10 discipline** - System engineering
  - **ECSS-E-ST-10** - System engineering general requirements
  - **ECSS-E-ST-10-02** - Verification
  - **ECSS-E-ST-10-03** - Testing
  - **ECSS-E-ST-10-04** - Space environment
  - **ECSS-E-ST-10-06** - Technical requirements specification
  - **ECSS-E-ST-10-09** - Reference coordinate system
  - **ECSS-E-ST-10-11** - Human factors engineering
  - **ECSS-E-ST-10-12** - Method for the calculation of radiation received and its effects, and a policy for design margins
  - **ECSS-E-ST-10-24** - Interface management
  - **ECSS-E-AS-11** - Adoption Notice of ISO 16290 - Definition of TRLs and their criteria of assessment
- **E-20 discipline** - Electrical and optical engineering
  - **ECSS-E-ST-20** - Electrical and electronic
  - **ECSS-E-ST-20-01** - Multipactor design and test
  - **ECSS-E-ST-20-06** - Spacecraft charging
  - **ECSS-E-ST-20-07** - Electromagnetic compatibility
  - **ECSS-E-ST-20-08** - Photovoltaic assemblies and components
  - **ECSS-E-ST-20-20** - Interface requirements for electrical power
  - **ECSS-E-ST-20-21** - Interface requirements for electrical actuators
  - **ECSS-E-ST-20-40** - ASIC, FPGA and IP Core engineering
- **E-30 discipline** - Mechanical engineering
  - **ECSS-E-ST-31** - Thermal control general requirements
  - **ECSS-E-ST-31-02** - Two-phase heat transport equipment
  - **ECSS-E-ST-31-04** - Exchange of thermal analysis data
  - **ECSS-E-ST-32** - Structural general requirements
  - **ECSS-E-ST-32-01** - Fracture control
  - **ECSS-E-ST-32-02** - Structural design and verification of pressurized hardware
  - **ECSS-E-ST-32-03** - Structural finite element models
  - **ECSS-E-ST-32-08** - Materials
  - **ECSS-E-ST-32-10** - Structural factors of safety for spaceflight hardware
  - **ECSS-E-ST-32-11** - Modal survey assessment
  - **ECSS-E-ST-33-01** - Mechanisms
  - **ECSS-E-ST-33-11** - Explosive subsystems and devices
  - **ECSS-E-ST-34** - Environmental control and life support
  - **ECSS-E-ST-35** - Propulsion general requirements
  - **ECSS-E-ST-35-01** - Liquid and electric propulsion for spacecraft
  - **ECSS-E-ST-35-02** - Solid propulsion for spacecraft and launchers
  - **ECSS-E-ST-35-03** - Liquid propulsion for launchers
  - **ECSS-E-ST-35-06** - Cleanliness requirements for spacecraft propulsion hardware
  - **ECSS-E-ST-35-10** - Compatibility testing for liquid propulsion systems
- **E-40 discipline** - Software engineering
  - **ECSS-E-ST-40** - Software general requirements
  - **ECSS-E-ST-40-02** - Machine learning software engineering, verification and validation
  - **ECSS-E-ST-40-07** - Simulation modelling platform – Level 1
  - **ECSS-E-ST-40-08** - Simulation modelling platform – Level 2
- **E-50 discipline** - Communications
  - **ECSS-E-ST-50** - Communications
  - **ECSS-E-ST-50-02** - Ranging and Doppler tracking
  - **ECSS-E-ST-50-05** - Radio frequency and modulation
  - **ECSS-E-AS-50-21** - Adoption Notice of CCSDS 131.0-B-5, TM Synchronization and Channel Coding
  - **ECSS-E-AS-50-22** - Adoption Notice of CCSDS 132.0-B-3, TM Space Data Link Protocol
  - **ECSS-E-AS-50-23** - Adoption Notice of CCSDS 732.0-B-4, AOS Space Data Link Protocol
  - **ECSS-E-AS-50-24** - Adoption Notice of CCSDS 231.0-B-4, TC Synchronization and Channel Coding
  - **ECSS-E-AS-50-25** - Adoption Notice of CCSDS 232.0-B-4, TC Space Data Link Protocol
  - **ECSS-E-AS-50-26** - Adoption Notice of CCSDS 232.1-B-2, Communications Operation Procedure-1
  - **ECSS-E-ST-50-11** - SpaceFibre – Very high-speed serial link
  - **ECSS-E-ST-50-12** - SpaceWire - Links, nodes, routers and networks
  - **ECSS-E-ST-50-13** - Interface and communication protocol for MIL std 1553B
  - **ECSS-E-ST-50-14** - Spacecraft discrete interfaces
  - **ECSS-E-ST-50-15** - CAN bus extension protocol
  - **ECSS-E-ST-50-16** - Time-triggered ethernet (TTE)
  - **ECSS-E-ST-50-51** - SpaceWire protocol identification
  - **ECSS-E-ST-50-52** - SpaceWire - Remote memory access protocol
  - **ECSS-E-ST-50-53** - SpaceWire - CCSDS packet transfer protocol
- **E-60 discipline** - Control engineering
  - **ECSS-E-ST-60-10** - Control performances
  - **ECSS-E-ST-60-20** - Star sensor terminology and performance specification
  - **ECSS-E-ST-60-21** - Gyros terminology and performance
  - **ECSS-E-ST-60-30** - Attitude and orbit control systems (AOCS) requirements
- **E-70 discipline** - Ground systems and operations
  - **ECSS-E-ST-70** - Ground systems and operations
  - **ECSS-E-ST-70-01** - On-board control procedures
  - **ECSS-E-ST-70-11** - Space segment operability
  - **ECSS-E-ST-70-31** - Ground systems and operations - Monitoring and control data definition
  - **ECSS-E-ST-70-32** - Test and operations procedure language
  - **ECSS-E-ST-70-41** - Telemetry and telecommand packet utilization
- **E-80 discipline** - Security
  - **ECSS-E-ST-80** - Security in space systems lifecycles

### Space product assurance branch

- **Q-10 discipline** - Product assurance management
  - **ECSS-Q-ST-10** - Product assurance management
  - **ECSS-Q-ST-10-04** - Critical-item control
  - **ECSS-Q-ST-10-09** - Nonconformance control system
- **Q-20 discipline** - Quality assurance
  - **ECSS-Q-ST-20** - Quality assurance
  - **ECSS-Q-ST-20-07** - Quality and safety assurance for space test centres
  - **ECSS-Q-ST-20-08** - Storage, handling and transportation of spacecraft hardware
  - **ECSS-Q-ST-20-10** - Off-the-shelf items utilization in space systems
  - **ECSS-Q-ST-20-30** - Manufacturing and control of electronic harness
- **Q-30 discipline** - Dependability
  - **ECSS-Q-ST-30** - Dependability
  - **ECSS-Q-ST-30-02** - Failure modes, effects (and criticality) analysis
  - **ECSS-Q-ST-30-09** - Availability analysis
  - **ECSS-Q-ST-30-11** - Derating - EEE components
- **Q-40 discipline** - Safety
  - **ECSS-Q-ST-40** - Safety
  - **ECSS-Q-ST-40-02** - Hazard analysis
  - **ECSS-Q-ST-40-12** - Fault tree analysis - Adoption notice ECSS/IEC 61025
- **Q-60 discipline** - EEE components
  - **ECSS-Q-ST-60** - Electrical, electronic and electromechanical (EEE) components
  - **ECSS-Q-ST-60-03** - ASIC, FPGA and IP Core product assurance
  - **ECSS-Q-ST-60-05** - Generic procurement requirements for hybrids
  - **ECSS-Q-ST-60-12** - Design, selection, procurement and use of die form monolithic microwave integrated circuits
  - **ECSS-Q-ST-60-13** - Commercial electrical, electronic and electromechanical (EEE) components
  - **ECSS-Q-ST-60-14** - Relifing procedure – EEE components
  - **ECSS-Q-ST-60-15** - Radiation hardness assurance – EEE components
- **Q-70 discipline** - Materials, mechanical parts and processes
  - **ECSS-Q-ST-70** - Materials, mechanical parts and processes
  - **ECSS-Q-ST-70-71** - Materials, processes and their data selection
  - **ECSS-Q-ST-70-01** - Cleanliness and contamination control
  - **ECSS-Q-ST-70-05** - Detection of organic contamination surfaces by IR spectroscopy
  - **ECSS-Q-ST-70-50** - Particle contamination monitoring for spacecraft systems and cleanrooms
  - **ECSS-Q-ST-70-02** - Thermal vacuum outgassing test for the screening of space materials
  - **ECSS-Q-ST-70-04** - Thermal testing for the evaluation of space materials, processes, mechanical parts and assemblies
  - **ECSS-Q-ST-70-06** - Particle and UV radiation testing for space materials
  - **ECSS-Q-ST-70-15** - Non-destructive inspection
  - **ECSS-Q-ST-70-20** - Determination of the susceptibility of silver-plated copper wire and cable to "rod-plague" corrosion
  - **ECSS-Q-ST-70-21** - Flammability testing for the screening of space materials
  - **ECSS-Q-ST-70-29** - Determination of offgassing products from materials and assembled articles to be used in a manned space vehicle crew compartment
  - **ECSS-Q-ST-70-36** - Material selection for controlling stress-corrosion cracking
  - **ECSS-Q-ST-70-37** - Determination of the susceptibility of metals to stress-corrosion cracking
  - **ECSS-Q-ST-70-45** - Mechanical testing of metallic materials
  - **ECSS-Q-ST-70-03** - Black-anodizing of metals with inorganic dyes
  - **ECSS-Q-ST-70-09** - Measurements of thermo-optical properties of thermal control materials
  - **ECSS-Q-ST-70-13** - Measurements of the peel and pull-off strength of coatings and finishes using pressure-sensitive tapes
  - **ECSS-Q-ST-70-16** - Adhesive bonding for spacecraft and launcher applications
  - **ECSS-Q-ST-70-17** - Durability testing of coatings
  - **ECSS-Q-ST-70-22** - Control of limited shelf-life materials
  - **ECSS-Q-ST-70-31** - Application of paints and coatings on space hardware
  - **ECSS-Q-ST-70-14** - Corrosion
  - **ECSS-Q-ST-70-26** - Crimping of high-reliability electrical connections
  - **ECSS-Q-ST-70-28** - Repair and modification of printed circuit board assemblies for space use
  - **ECSS-Q-ST-70-30** - Wire wrapping of high-reliability electrical connections
  - **ECSS-Q-ST-70-39** - Welding of metallic materials for flight hardware
  - **ECSS-Q-ST-70-40** - Processing and quality assurance requirements for brazing of flight hardware
  - **ECSS-Q-ST-70-61** - High reliability assembly for surface mount and through hole connections
  - **ECSS-Q-ST-70-80** - Processing and quality assurance requirements for metallic powder bed fusion technologies for space applications
  - **ECSS-Q-ST-70-12** - Design rules for printed circuit boards
  - **ECSS-Q-ST-70-18** - Preparation, assembly and mounting of RF coaxial cables
  - **ECSS-Q-ST-70-46** - Requirements for manufacturing and procurement of threaded fasteners
  - **ECSS-Q-ST-70-60** - Qualification and procurement of printed circuit boards
  - **ECSS-Q-ST-70-53** - Materials and hardware compatibility tests for sterilization processes
  - **ECSS-Q-ST-70-54** - Ultra cleaning of flight hardware
  - **ECSS-Q-ST-70-55** - Microbiological examination of flight hardware and cleanrooms
  - **ECSS-Q-ST-70-56** - Vapour phase bioburden reduction for flight hardware
  - **ECSS-Q-ST-70-57** - Dry heat bioburden reduction for flight hardware
  - **ECSS-Q-ST-70-58** - Bioburden control in cleanrooms
- **Q-80 discipline** - Software product assurance
  - **ECSS-Q-ST-80** - Software product assurance

### Space sustainability branch

- **U-10 discipline** - Space debris
  - **ECSS-U-AS-10** - Adoption Notice of ISO 24113: Space systems - Space debris mitigation requirements
- **U-20 discipline** - Planetary protection
  - **ECSS-U-ST-20** - Planetary protection

## ECSS Handbooks and Technical Memoranda

### Space product assurance branch HBs and TMs

- **Q-30 discipline** - Dependability
  - **ECSS-Q-HB-30-01** - Worst case analysis
  - **ECSS-Q-HB-30-02** - Reliability handbook
  - **ECSS-Q-HB-30-03** - Human dependability handbook
  - **ECSS-Q-HB-30-08** - Component reliability data sources and their use
  - **ECSS-Q-TM-30-12** - End-of-life parameters drifts – EEE components
- **Q-40 discipline** - Safety
  - **ECSS-Q-TM-40-04 Part 1** - Sneak analysis – Part 1: Principles and requirements
  - **ECSS-Q-TM-40-04 Part 2** - Sneak analysis – Part 2: Clue list
- **Q-70 discipline** - Materials, mechanical parts and processes
  - **ECSS-Q-HB-70-23** - Materials, mechanical parts and processes obsolescence management handbook
  - **ECSS-Q-TM-70-51** - Termination of optical fibres
  - **ECSS-Q-TM-70-52** - Kinetic outgassing of materials for space
- **Q-80 discipline** - Software product assurance
  - **ECSS-Q-HB-80-01** - Reuse of existing software
  - **ECSS-Q-HB-80-02 Part 1** - Software process assessment and improvement – Part 1: Framework
  - **ECSS-Q-HB-80-02 Part 2** - Software process assessment and improvement – Part 2: Assessor instrument
  - **ECSS-Q-HB-80-03** - Methods and techniques to support the assessment of software dependability and safety
  - **ECSS-Q-HB-80-04** - Software metrication programme definition and implementation

### Space engineering branch HBs and TMs

Handbooks and technical manuals provide detailed guidance and best practices for specific topics within the space engineering discipline. They are intended to support the implementation of the requirements defined in the ECSS standards.

- **E-10 discipline** - System engineering
  - **ECSS-E-HB-10-02** - Verification guidelines
  - **ECSS-E-HB-10-03** - Testing guidelines
  - **ECSS-E-HB-10-12** - Calculation of radiation and its effects, and margin policy handbook
  - **ECSS-E-HB-11** - TRL guidelines
  - **ECSS-E-TM-10-10** - Logistics engineering
  - **ECSS-E-TM-10-20** - Product data exchange
  - **ECSS-E-TM-10-21** - System modelling and simulation
  - **ECSS-E-TM-10-23** - Space system data repository
  - **ECSS-E-TM-10-25** - Engineering design model data exchange
- **E-20 discipline** - Electrical and optical engineering
  - **ECSS-E-HB-20-01** - Multipactor handbook
  - **ECSS-E-HB-20-02** - Li-ion battery handbook
  - **ECSS-E-HB-20-03** - Magnetic cleanliness handbook
  - **ECSS-E-HB-20-05** - High voltage engineering and design handbook
  - **ECSS-E-HB-20-06** - Assessment of spacecraft worst case charging
  - **ECSS-E-HB-20-07** - Spacecraft electromagnetic compatibility handbook
  - **ECSS-E-HB-20-20** - Guidelines for electrical interface requirements for power supply
  - **ECSS-E-HB-20-21** - Guidelines for electrical design and interface requirements for actuators
  - **ECSS-E-HB-20-40** - Engineering techniques for radiation effects mitigation in ASICs and FPGAs handbook
- **E-30 discipline** - Mechanical engineering
  - **ECSS-E-HB-31-01** - Thermal design data handbook (16 parts)
  - **ECSS-E-HB-31-03** - Thermal analysis handbook
  - **ECSS-E-HB-32-20** - Structural design data handbook (8 parts)
  - **ECSS-E-HB-32-21** - Adhesive bonding handbook
  - **ECSS-E-HB-32-22** - Insert design handbook
  - **ECSS-E-HB-32-23** - Threaded fasteners handbook
  - **ECSS-E-HB-32-24** - Buckling handbook
  - **ECSS-E-HB-32-25** - Mechanical shock design and verification handbook
  - **ECSS-E-HB-32-26** - Spacecraft mechanical loads analyses handbook
  - **ECSS-E-HB-32-27** - Microvibration handbook
- **E-40 discipline** - Software engineering
  - **ECSS-E-HB-40** - Software engineering handbook
  - **ECSS-E-HB-40-01** - Agile software development handbook
  - **ECSS-E-HB-40-02** - Machine learning qualification for space applications handbook
- **E-50 discipline** - Communications
  - **ECSS-E-HB-50** - Communications guidelines
- **E-60 discipline** - Control engineering
  - **ECSS-E-HB-60** - Control engineering handbook
  - **ECSS-E-HB-60-10** - Control performance guidelines
- **E-70 discipline** - Ground systems and operations