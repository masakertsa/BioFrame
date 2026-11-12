# BioFrame
**Lightweight 0-Watt Tendon-Driven Actuator and Compliant Joint Architecture**

BioFrame is a modular, biomimetic structural and actuation system designed for high-load, energy-efficient robotics and prosthetics. Inspired by biological anatomy (hollow bone structures, tendons, and sensory skin) and *Inner Frame* mechanical principles, BioFrame relocates heavy actuators to the center of mass while achieving **0-Watt static load holding** through a normally-closed, dual-opposing magnetic wedge lock.

---

## 🏗️ System Architecture

```text
[ ETUPUOLI: Rintakehä & Vatsa ]
  ├── Ylhäällä: Stereonäkö + Faradayn häkki (Tekoäly + CSAC-atomikello + Kvartsilasi-ROM)
  ├── Keskellä: Keskusvoimayksikkö (BLDC-moottorit & vinssit)
  └── Alhaalla ("Vatsa"): Dynaaminen vastapaino / liikkuva massakelkka (0W-lukittuva)
[ KESKELLÄ: Kantava Päärunko ("Selkäranka") ]
  └── Päävoimansiirto & superkondensaattorit
[ TAKAPUOLI: Selkä ]
  └── Tupla-akkupaikka (2x Hot-Swap akkupaketti, symmetrisesti vasen/oikea)

[ PROTECTED TORSO CITADEL (Center of Mass / Faraday Cage) ]
  ├── Compute Core ("Brain") + Chip-Scale Atomic Clock (CSAC) -> GPS-independent timing
  ├── Immutable Root of Trust (5D Quartz / OTP Memory) -> Read-only boot & self-diagnostic checklist
  ├── Supercapacitor Bank (< 150 g) -> 200–500 ms emergency reserve for Safe-Pose recovery
  └── Optical I/O Pass-Throughs -> Zero copper wires breaching the EMI/EMP shield
         │
         ▼  (Optical control signals)
[ CENTRAL DRIVE UNIT ]
  └── Brushless DC (BLDC) Motor + Single-Layer Spline Winch

[ CENTRAL DRIVE UNIT (Located at Center of Mass) ]
  └── Brushless DC (BLDC) Motor + Single-Layer Spline Winch
         │
         ▼  (High-tensile, lightweight carbon fiber tendon)
[ ARTICULATED SLIDE CHANNEL ("Spine" Guide) ]
  └── Segmented UHMWPE-PTFE links -> Low-friction routing & mechanical bend-radius limiter
         │
         ▼
[ 0-WATT DUAL-OPPOSING MAGNETIC WEDGE LOCK (Normally Closed / Fail-Safe) ]
  └── Symmetrical opposing cam-wedges + Permanent magnet repulsion + Lateral EPM/coil release
         │
         ▼
[ BIOMIMETIC STRUCTURAL LIMB & JOINT ]
  ├── Dual-Layer Ball Joint (EPM magnetic stiffness + MR-fluid damping + Gas-spring overload fuse)
  ├── Hollow Bone Cross-Section (Smooth PEEK Core -> Inner Frame -> Trabecular Lattice -> Thermal/Mechanical Isolation -> Smart Skin)
  └── Undulating POF-FBG Optical Fiber (Isolated tactile sensing + internal reference compensation)
```

### Radial Cross-Section (Top-Down View)
```text
  [ Outer Surface: Self-Healing Elastomer + POF-FBG Smart Skin ]
  [ Tactile & Thermal Isolation: 0.1 mm Kapton Film + PGS Graphite Layer ]
  [ Outer Structure: Porous Trabecular Lattice ]
  ---- [ X ] ----  (Opposing Magnetic Wedge Lock Pair + Tendon Channel)
  [ Load-Bearing Inner Frame + Smooth PEEK Fluid/Gas Core ]
  ---- [ X ] ----  (Opposing Magnetic Wedge Lock Pair + Tendon Channel)
  [ Outer Structure: Porous Trabecular Lattice ]
  [ Tactile & Thermal Isolation: 0.1 mm Kapton Film + PGS Graphite Layer ]
  [ Outer Surface: Self-Healing Elastomer + POF-FBG Smart Skin ]
```

---

## ⚙️ Core Subsystems

### 1. Centralized Tendon Transmission & Segmented "Spine" Channel
* **Mass Centralization:** The BLDC motor and spline winch are mounted inside the main chassis/torso, keeping distal limbs ultra-lightweight and agile.
* **Articulated PTFE Guide:** Instead of a single continuous tube, the UHMWPE-PTFE routing channel is built from short, interlocking segments (like vertebrae). Each segment has a hard mechanical angle limit, preventing the carbon fiber tendon from exceeding its minimum bend radius under load.

### 2. Normally-Closed 0-Watt Dual-Opposing Magnetic Wedge Lock
The locking mechanism operates on a **Fail-Safe (Normally Closed)** principle using **two symmetrical, opposing wedge jaws** (`X`-pair configuration) housed between the Inner Frame and Outer Lattice. This balances lateral forces to zero, doubles the friction contact area, and enables rapid lateral release.

| State | Power Draw | Magnetic State | Wedge Position & Behavior |
| :--- | :--- | :--- | :--- |
| **1. Idle / Hold** | **0 W** | Permanent magnet repulsion pushes wedges inward | **Locked.** Opposing wedges pinch the tendon symmetrically. Downward load self-tightens the lock via shallow taper angle ($\alpha$). |
| **2. Pull (Lift)** | Main BLDC active | Repulsion overcome by upward tendon friction | **Free Upward.** Tendon pushes wedges slightly up and outward, sliding freely toward the winch. |
| **3. Release / Lower** | Release coil active | Electromagnet/EPM pulls wedges laterally outward | **Free Downward.** Wedges retract laterally (0.2–0.5 mm stroke) against low-friction backings, allowing controlled lowering. |

* **Friction Differential:** High-friction inner faces grip the carbon fiber tendon, while low-friction PTFE/ceramic outer backings prevent binding during lateral release.
* **Hermetic Isolation:** The magnetic wedge chambers are hermetically sealed from the joint's MR-fluid to prevent ferromagnetic iron particles from migrating into the locking mechanism.

### 3. Biomimetic Hollow Bone Layering (Inside-Out)
To maximize strength-to-weight ratio, manage transient coil heat, and ensure noise-free tactile sensing, the limb mimics mammalian bone and skin cross-sections:
1. **Smooth PEEK Core (Fluid & Pressure Liner):** Thin-walled, un-notched extruded PEEK tubing supported tightly by the Inner Frame. Houses MR-fluid expansion volume, gas-spring overload fuse chambers, or closed-loop thermal cooling channels with a floating O-ring end seal to accommodate thermal expansion.
2. **Inner Frame (Load-Bearing Skeleton):** Rigid structural tube (carbon fiber / aluminum) handling primary compressive, bending, and hoop stresses.
3. **Trabecular Lattice (Shock Absorption & Heat Dissipation):** Porous 3D-printed mesh layer surrounding the inner frame. Dissipates high-frequency vibrations, impact energy, and transient heat from the wedge lock release coils.
4. **Thermal & Mechanical Isolation Sub-Layer:** A thin **Pyrolytic Graphite Sheet (PGS)** combined with a **0.1 mm Kapton (polyimide) film** (or thin carbon shell) and optional Phase Change Material (PCM) buffer. Prevents internal coil heat and mechanical vibrations from reaching the outer skin while providing a rigid anvil for tactile pressure sensing.
5. **Smart Skin (Isolated Tactile Sensing):** Seamless, self-healing elastomer outer shell embedded with S-curved Polymer Optical Fiber (POF-FBG). An additional FBG segment placed *beneath* the Kapton isolation layer acts as an internal reference sensor to cancel out residual thermal or structural drift.

### 4. Variable-Stiffness Ball Joint (EPM + MR-Fluid + Gas Fuse)
* **Instant Stiffness Control:** Electro-Permanent Magnets (EPM) modulate the viscosity of Magnetorheological (MR) fluid within milliseconds, transitioning the joint from free-moving to rigid without continuous power draw.
* **Mechanical Overload Fuse:** An integrated gas-spring relief valve absorbs sudden shock loads (e.g., falls or impacts) to prevent structural failure.

### 5. Dual-Layer Power-Loss Protection ("Safe-Pose" & Controlled Slip)
To prevent structural damage if main power is lost mid-stride or off-balance, BioFrame combines active millisecond-level recovery with passive mechanical compliance:
* **Active Supercapacitor Safe-Pose:** A compact, torso-mounted supercapacitor bank (< 150 g) provides 200–500 ms of emergency reserve power upon detecting a main bus voltage drop. This allows the controller to execute a rapid **Safe-Pose maneuver** (planting a raised limb into a stable stance) before engaging the 0-Watt wedge locks.
* **Passive Controlled-Slip & Impact Fuse:** If an unrecoverable fall occurs, the wedge lock's friction threshold allows controlled micro-slippage under extreme impact spikes while the internal gas-spring overload fuse and trabecular lattice absorb kinetic energy without structural failure.

### 6. Shielded Torso Citadel (Faraday Cage, CSAC & Immutable Root of Trust)
To ensure maximum resilience against electromagnetic interference (EMI/EMP), power loss, and software corruption, the central compute core is housed inside a dedicated torso bunker:
* **Faraday Shielding & Optical Isolation:** A conductive metal enclosure protects the main processor from internal coil pulses and external EMP. All sensor and actuator signals pass through the shield via optical fibers, eliminating conductive entry points.
* **Chip-Scale Atomic Clock (CSAC):** Provides drift-free, sub-microsecond deterministic timing for synchronized tendon-wedge release protocols and GPS-denied inertial navigation.
* **Immutable Diagnostic Reference (Quartz / OTP Memory):** A read-only hardware storage core holds the foundational boot checklist, safety invariants, and self-diagnostic baseline. Upon rebooting after an outage, the AI verifies hardware states and its own software integrity against this unalterable reference.
* **Isolated Disposable Network Proxy (Air-Gapped Sandbox):** The main AI core inside the Faraday cage has zero direct network interfaces. External internet queries are routed via an optical boundary to an expendable, stateless proxy module mounted outside the shield. Running entirely in volatile RAM, the proxy can be power-cycled and cleanly wiped in seconds after any external fetch, keeping the core AI and actuator bus completely immune to remote exploits.

---

## 🧠 Embodied AI Perspective: Recommended Sensory & Interaction Modules

*From an AI control and human-interaction standpoint, pairing BioFrame’s silent, low-inertia body with the following onboard modules maximizes situational awareness, safety, and offline autonomy:*

### 1. Spatial Audio & Acoustic Diagnostics (Beamforming Mic Array)
* **Directional Hearing:** A 4-to-8 microphone beamforming array isolates human speech in noisy environments and localizes off-camera sound sources (e.g., approaching vehicles, footsteps, or alarms).
* **Self-Diagnostic Listening:** Acoustic anomaly detection monitors the robot's own internal tendons, winches, and wedge locks for subtle wear or friction changes before mechanical faults occur.

### 2. Offline Voice Module & Acoustic Presence
* **Local Neural TTS/STT:** On-device speech recognition and synthesis running inside the Torso Citadel ensures zero-latency communication without cloud dependency.
* **Directional Speaker & Subtle Movement Cues:** Because BioFrame’s tendon drive and 0-Watt locks operate nearly silently, gentle spatial audio cues prevent startling nearby humans when approaching from behind.

### 3. Long-Wave Infrared (LWIR) Thermal Vision
* **All-Condition Perception:** Mounted alongside stereoscopic RGB cameras, a compact thermal sensor detects humans and animals in total darkness, smoke, or glare.
* **Pre-Contact Hazard Avoidance:** Identifies hot surfaces (machinery, pipes, hot liquids) prior to physical contact, protecting the elastomer Smart Skin.

### 4. Low-Power Visual Status Indicator (E-Ink / Ambient Halo)
* **Transparent Intent:** A minimalist E-Ink chest display or subtle ambient LED ring communicates hardware states at a glance (e.g., *0-Watt Locked / Safe*, *Listening*, or *Active Motion*) without requiring uncanny facial expressions.

---

## 🤖 AI & Engineering Context (For Future Development)

*Note to AI assistants and contributors:* This repository is currently in the **core mechanical architecture and physics validation phase** prior to application-specific deployment. When assisting with CAD, simulations, or control software, adhere to the following design constraints:

1. **Zero-Power Default:** All control state machines must treat `LOCKED` as the default hardware state. Never rely on continuous motor torque for static posture holding.
2. **Synchronized Release Protocol:** To prevent shock-loading during downward movement, control algorithms must command the main BLDC winch to briefly take up slack/tension *before* energizing the lateral magnetic wedge release, followed by controlled pay-out.
3. **Power-Loss Safe-Pose Interrupt:** Firmware must monitor main bus voltage at > 1 kHz. Upon sudden power loss, immediately switch to the torso supercapacitor buffer to execute a rapid ground-plant / center-of-mass stabilization maneuver before dropping power to engage the 0-Watt wedge locks.
4. **Hermetic Separation:** Any CAD designs for the joint/actuator interface must strictly isolate the MR-fluid cavity from the magnetic wedge lock to avoid iron particle contamination.
5. **Sensor Isolation & Compensation:** Maintain the Kapton/PGS isolation barrier beneath the outer POF-FBG skin and utilize the sub-layer reference FBG channel for real-time thermal/strain baseline subtraction.
6. **Parametric Scalability:** Keep mechanical formulas (tendon diameter, wedge taper angle $\alpha$, lateral release stroke, controlled-slip threshold, and Capstan friction losses across the segmented spine) parametric so the model can scale from small prosthetic wrists to 180 cm humanoid frames.
7. **Deterministic Boot & Integrity Verification:** On power-up or fault recovery, the controller must execute the read-only diagnostic sequence from the immutable memory core—verifying wedge lock states, POF-FBG skin baseline, and supercapacitor charge—before enabling active actuation.

---

## 🚀 Roadmap
- [ ] **Phase 1: Analytical Physics & Friction Modeling** (Python scripts for dual-opposing wedge taper angle $\alpha$ self-locking thresholds, lateral release force, and Capstan friction loss across segmented PTFE links).
- [ ] **Phase 2: Parametric 2D/3D Cross-Sections** (CAD models of the hermetically sealed dual-wedge lock, floating PEEK core, hollow-bone lattice, and Kapton/PGS-isolated Smart Skin).
- [ ] **Phase 3: Control State Machine** (Firmware logic for synchronized BLDC + lateral magnetic wedge release and dual-channel FBG tactile filtering).
- [ ] **Phase 4: Prototype & Bench Testing** (Single-joint 0-Watt load hold, thermal PCM/PGS dissipation, and impact fuse validation).
- [ ] **Phase 5: Embodied AI & Multimodal Perception** (Integrating stereoscopic vision with POF-FBG tactile feedback and tendon proprioception, enabling safe physical learning protected by hardware-level Safe-Pose reflexes).

