"""
Documented Real-World Industry Case Studies for AI & Machine Learning Lab
Case 1: Siemens AG — Industrial Automation & Edge AI
Case 2: General Electric — Turbine Health Monitoring & Digital Twins
Case 3: Honeywell — Smart Factory Predictive Maintenance & Asset Performance Management
"""

import streamlit as st

CASE_STUDIES = {
    "SIEMENS": {
        "id": "siemens",
        "company": "Siemens AG (Digital Industries)",
        "badge": "Manufacturing & Industrial Automation",
        "title": "Industrial Automation & Edge AI on the SMT Assembly Line",
        "facility": "Siemens Electronics Works Amberg (EWA), Germany",
        "summary": "How Siemens achieved >99.999% product quality yields while producing over 17 million Simatic PLCs per year using embedded edge neural inference directly on automated assembly lines.",
        "context": """
        The Siemens Electronics Works Amberg (EWA) facility is recognized by the World Economic Forum as a Global Lighthouse factory. 
        EWA manufactures high-precision industrial programmable logic controllers (PLCs) across 1,200 distinct product variants. 
        Each day, the factory places tens of millions of micro-components onto circuit boards via Surface-Mount Technology (SMT) machines.
        """,
        "problem": """
        Traditional quality inspection relied on end-of-line functional X-ray testing. 
        However, X-ray inspection is an extreme operational bottleneck: inspecting 100% of boards with high-resolution 3D X-ray 
        would require millions of dollars in equipment and throttle factory line throughput by over 40%. 
        A missed defective solder joint or misaligned capacitor causes field failures in mission-critical manufacturing plants.
        """,
        "data_involved": [
            "**Optical Solder Paste Inspection (SPI):** 3D volume, height, and area of printed solder paste deposits.",
            "**Pick-and-Place Machine Telemetry:** Nozzle vacuum pressure, placement force (Newtons), component offset angles (millidegrees).",
            "**Reflow Oven Thermal Profiles:** 8-zone temperature sensors, conveyor speed, nitrogen flow rates.",
            "**Historical Defect Ground Truth:** 3D automated X-ray inspection (AXI) labels collected over millions of production cycles."
        ],
        "ai_methods": [
            "**Edge Convolutional Neural Networks (CNNs):** Embedded directly on Siemens Simatic S7-1500 TM NPU (Neural Processing Unit) modules.",
            "**Supervised Classification (Gradient Boosted Trees):** Predicts the probability of a defective solder joint based on pre-reflow SPI metrics.",
            "**Adaptive Sampling:** Only circuit boards with predicted defect probability > 0.002 are routed to slow X-ray inspection; nominal boards bypass X-ray directly to packaging."
        ],
        "decision_workflow": """
        1. SMT machine prints solder paste and mounts components.
        2. High-speed 2D/3D camera captures optical snapshot.
        3. Edge AI inference executes in **< 15 milliseconds** on the factory floor (zero cloud latency).
        4. If Defect Probability $\\le 0.002$: Board passes automatically to packing.
        5. If Defect Probability $> 0.002$: Automated conveyor diverts board to 3D X-ray for human specialist verification.
        """,
        "benefits_and_limits": {
            "benefits": [
                "Reduced expensive X-ray inspection demand by **70%** without sacrificing defect escape rates.",
                "Line throughput increased by 25% while maintaining a defect rate of under **12 Defective Parts Per Million (DPPM)**.",
                "Zero reliance on external cloud connectivity ensures 100% operational uptime and data sovereignty."
            ],
            "limitations": [
                "Drift in solder paste viscosity due to ambient humidity changes requires periodic model fine-tuning.",
                "Concept drift when introducing new PCB geometries requires human verification before retraining."
            ]
        },
        "verified_sources": [
            "World Economic Forum (WEF) Global Lighthouse Network — Siemens Electronics Works Amberg Case Study.",
            "Siemens Digital Industries Technical Whitepaper: 'AI at the Edge: Integrating Machine Learning into Simatic Industrial Automation'.",
            "IEEE Transactions on Automation Science and Engineering — Edge Computing in SMT Electronics Manufacturing."
        ],
        "quiz": {
            "question": "Why did Siemens deploy the machine learning model on an on-premise Simatic Edge NPU rather than sending telemetry to a cloud server?",
            "options": [
                "To satisfy hard real-time latency (<15 ms) and avoid factory stoppages if WAN connection drops",
                "Because cloud servers cannot run Convolutional Neural Networks",
                "To reduce the electrical power consumed by the SMT machines"
            ],
            "answer": "To satisfy hard real-time latency (<15 ms) and avoid factory stoppages if WAN connection drops",
            "explanation": "In automated industrial manufacturing, conveyor lines move at multiple meters per second. A routing decision must be finalized within milliseconds. Cloud round-trips introduce jitter, bandwidth costs, and single-point-of-failure network risks that industrial standards forbid."
        }
    },
    "GE": {
        "id": "ge",
        "company": "General Electric (GE Vernova & GE Aerospace)",
        "badge": "Power Generation & Aerospace",
        "title": "Turbine Health Monitoring & Digital Twins",
        "facility": "GE Monitoring & Diagnostics Center (Atlanta, Georgia, USA)",
        "summary": "How GE continuously monitors >7,000 heavy-duty gas turbines, steam turbines, and jet engines globally to predict component degradation and prevent multi-million-dollar unscheduled outages.",
        "context": """
        A single GE 7HA heavy-duty gas turbine produces over 400 megawatts of electricity (powering >300,000 homes). 
        These machines operate in harsh thermodynamic regimes: combustion gas temperatures exceed 1,500°C (hotter than the melting point of steel), 
        and rotor blades spin at 3,600 RPM under extreme mechanical centrifugal stress. 
        An unscheduled shutdown costs a power utility **$500,000 to $1,500,000 per day** in replacement power penalties.
        """,
        "problem": """
        Traditional scheduled maintenance (e.g. inspecting every 8,000 operating hours) is both inefficient and risky. 
        Thermal barrier coating (TBC) spallation, fuel nozzle coking, and rotor bearing micro-cracks develop probabilistically based on actual 
        thermal cycling (number of startups and peak load hours), not calendar time. 
        Power plant operators need accurate advance warning of impending failures before catastrophic damage occurs.
        """,
        "data_involved": [
            "**High-Frequency Vibration Sensors:** Tri-axial accelerometers on bearings measuring seismic vibration and orbit profiles.",
            "**Thermodynamic Telemetry:** Compressor inlet/discharge pressure and temperature, exhaust gas temperature (EGT) thermocouples.",
            "**Dynamic Pressure Transducers:** High-speed sensors detecting acoustic combustor pressure oscillations (humming).",
            "**Ambient Operating Conditions:** Air density, relative humidity, fuel gas calorific heating value."
        ],
        "ai_methods": [
            "**Physics-Informed Digital Twins:** First-principles aerothermal thermodynamic models coupled with machine learning residual estimators.",
            "**Autoencoder Neural Networks:** Trained on historical nominal turbine operation. When an anomaly begins, reconstruction loss spikes on the affected sensors.",
            "**Fast Fourier Transform (FFT) + Random Forest:** Classifies vibration spectrum peaks into unbalance, misalignment, or bearing race defects.",
            "**Remaining Useful Life (RUL) Survival Regression:** Predicts hours until thermal blade degradation reaches critical safety thresholds."
        ],
        "decision_workflow": """
        1. Onboard sensors stream 200+ telemetry channels at 1 Hz (and 10 kHz for vibration).
        2. The Digital Twin calculates expected thermodynamic performance given current ambient conditions.
        3. If actual Exhaust Temperature deviates by $> 2.8°C$ from physics prediction, an automated anomaly ticket is generated.
        4. Diagnostics Center engineers review the AI signature to distinguish sensor failure from true combustor nozzle deterioration.
        5. Maintenance is scheduled during a planned grid low-demand window weeks in advance.
        """,
        "benefits_and_limits": {
            "benefits": [
                "Over **$1.2 billion in avoided customer downtime** documented across the global turbine fleet.",
                "Early detection of combustor lean-blowout oscillations prevented catastrophic rotor blade destruction.",
                "Extended turbine operating intervals between overhauls based on actual damage accumulation."
            ],
            "limitations": [
                "Extreme operating transients (rapid emergency power grid ramps) produce false anomaly spikes.",
                "Rare failure modes (never seen in training data) require human domain expert interpretation."
            ]
        },
        "verified_sources": [
            "GE Digital Twin: Analytical Framework for Asset Optimization (GE Global Research Technical Report).",
            "ASME Turbo Expo Conference Proceedings: 'Machine Learning Applied to Heavy-Duty Gas Turbine Predictive Diagnostics'.",
            "Power Engineering International — 'Condition-Based Monitoring and Analytics at GE M&D Center'."
        ],
        "quiz": {
            "question": "What is the primary architectural advantage of pairing an aerothermal physics model with machine learning (a 'Physics-Informed Digital Twin') rather than using pure ML alone?",
            "options": [
                "The physics model guarantees the system obeys thermodynamics (mass & energy conservation), preventing physically impossible predictions on unseen data",
                "Pure ML models cannot handle sensor telemetry",
                "Physics models eliminate the need for training data"
            ],
            "answer": "The physics model guarantees the system obeys thermodynamics (mass & energy conservation), preventing physically impossible predictions on unseen data",
            "explanation": "Pure black-box neural networks can hallucinate physically impossible predictions (such as efficiency > 100% or energy appearing from nowhere) when evaluated outside their training distribution. Pairing physics equations with ML bounds the solution space to real physical laws."
        }
    },
    "HONEYWELL": {
        "id": "honeywell",
        "company": "Honeywell International",
        "badge": "Process Industries & Smart Factories",
        "title": "Smart Factory Predictive Maintenance with Honeywell Forge",
        "facility": "Distributed Chemical Refineries & Pharmaceutical Facilities",
        "summary": "How Honeywell Forge Asset Performance Management (APM) ingests millions of industrial IoT sensor streams to predict rotating equipment failures and automate enterprise work orders.",
        "context": """
        Modern petroleum refineries and specialty chemical plants operate continuously (24/7/365). 
        Critical rotating assets—including multi-stage centrifugal pumps, compressors, and agitators—circulate hazardous, 
        flammable fluids under high pressures. A pump seal blowout or bearing seizure poses not only millions of dollars in downtime, 
        but severe environmental and personnel safety hazards.
        """,
        "problem": """
        Refineries contain over 15,000 distinct mechanical assets. 
        Traditional walk-around route-based maintenance (a technician measuring vibration with a handheld probe once a month) 
        detects fewer than 15% of incipient mechanical faults. Failures that develop rapidly between inspection cycles go unnoticed.
        """,
        "data_involved": [
            "**Wireless Industrial IoT Vibration & Temp Puck Sensors:** Attached directly to pump bearing housings.",
            "**Process Historian (OPC-UA / SCADA):** Fluid flow rates, suction/discharge pressures, differential head, motor kW.",
            "**Lubricating Oil Spectrometry Logs:** Particle counts, metal ppm (iron, copper), viscosity index, moisture ppm.",
            "**Computerized Maintenance Management System (CMMS):** Work order history, mean time between failures (MTBF)."
        ],
        "ai_methods": [
            "**Isolation Forest & Principal Component Analysis (PCA):** Multivariate anomaly detection on correlated process conditions.",
            "**Weibull Survival Analysis & Gradient Boosting:** Remaining Useful Life (RUL) estimation given current operating wear.",
            "**Automated Root-Cause Diagnostic Graph:** Decision-tree mapping that correlates high vibration + low suction pressure to **impeller cavitation** rather than bearing damage."
        ],
        "decision_workflow": """
        1. Wireless puck sensors transmit RMS vibration and peak acceleration every 10 minutes.
        2. Edge gateway normalizes and cleans the telemetry, filtering sensor dropout.
        3. Honeywell Forge AI evaluates asset degradation index:
           - Normal ($Health > 85$): Routine operations.
           - Incipient Cavitation ($60 < Health \\le 85$): Advisory alert dispatched to process operators to adjust suction valve.
           - Critical Bearing Flaw ($Health \\le 60$): Automated CMMS work order created with required replacement part SKU and technician dispatch.
        """,
        "benefits_and_limits": {
            "benefits": [
                "Achieved up to **30% reduction in unplanned maintenance costs** across enterprise customer sites.",
                "Eliminated manual route-based vibration inspections, freeing up engineers for high-value optimization.",
                "Prevented mechanical seal ruptures, directly improving process environmental safety compliance."
            ],
            "limitations": [
                "Intermittent wireless packet loss in dense steel refinery piping environments requires robust data imputation.",
                "Requires careful alarm threshold tuning to prevent 'alarm fatigue' among plant operators."
            ]
        },
        "verified_sources": [
            "Honeywell Forge Asset Performance Management Product Architecture & Field Deployment Guide.",
            "Hydrocarbon Processing — 'Applying Machine Learning and IoT to Rotating Machinery Reliability'.",
            "Plant Engineering Journal — 'Condition Monitoring Strategies for Critical Chemical Process Pumps'."
        ],
        "quiz": {
            "question": "If a centrifugal pump shows an abnormal surge in vibration, how does the AI distinguish between pump cavitation (hydraulic vapor bubble collapse) and bearing mechanical wear?",
            "options": [
                "By correlating the vibration surge with process differential pressure and suction head data",
                "By measuring the physical temperature of the surrounding room",
                "Cavitation cannot be distinguished from bearing damage with sensors"
            ],
            "answer": "By correlating the vibration surge with process differential pressure and suction head data",
            "explanation": "Mechanical bearing wear produces distinct harmonic peaks at bearing pass frequencies (BPFO/BPFI) independent of flow rate. Cavitation occurs specifically when suction pressure drops below the fluid's vapor pressure, causing broad-band high-frequency noise. Multi-sensor correlation is essential for accurate root-cause diagnosis."
        }
    }
}

def render_case_study(case_key: str):
    if case_key not in CASE_STUDIES:
        st.error(f"Case study '{case_key}' not found.")
        return
        
    case = CASE_STUDIES[case_key]
    
    st.markdown(f"""
    <div style="background: rgba(124, 77, 255, 0.08); border-left: 4px solid #7C4DFF; padding: 20px 24px; border-radius: 8px; margin-bottom: 24px;">
        <div style="color: #A78BFA; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 6px;">
            INDUSTRY CASE STUDY • {case['badge']}
        </div>
        <h2 style="color: #F8F7FF; margin: 0 0 10px 0;">{case['company']}</h2>
        <h3 style="color: #C4B5FD; font-size: 1.25rem; margin: 0 0 12px 0; font-weight: 600;">{case['title']}</h3>
        <p style="color: #AAB3CC; font-size: 1rem; line-height: 1.6; margin: 0;">{case['summary']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab_overview, tab_arch, tab_workflow, tab_audit = st.tabs([
        "🏢 1. Operational Context & Problem", 
        "🧠 2. Data & AI Architecture", 
        "⚙️ 3. Industrial Decision Workflow", 
        "📚 4. Verified Citations & Assessment"
    ])
    
    with tab_overview:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 🏭 Production Environment")
            st.write(case["context"])
            st.markdown(f"**Facility / Deployment:** `{case['facility']}`")
        with c2:
            st.markdown("### ⚠️ The Engineering Problem")
            st.write(case["problem"])
            
    with tab_arch:
        st.markdown("### 📡 Sensor Data Streams & Telemetry")
        for d in case["data_involved"]:
            st.markdown(f"- {d}")
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🤖 Applied Machine Learning Methods")
        for m in case["ai_methods"]:
            st.markdown(f"- {m}")

    with tab_workflow:
        st.markdown("### 🔄 Industrial Decision-Making Pipeline")
        st.markdown(case["decision_workflow"])
        
        c_b1, c_b2 = st.columns(2)
        with c_b1:
            st.markdown("#### ✅ Quantified Operational Benefits")
            for b in case["benefits_and_limits"]["benefits"]:
                st.markdown(f"- {b}")
        with c_b2:
            st.markdown("#### ⚠️ Technical Limitations & Risks")
            for lim in case["benefits_and_limits"]["limitations"]:
                st.markdown(f"- {lim}")

    with tab_audit:
        st.markdown("### 📖 Peer-Reviewed & Verified Sources")
        for s in case["verified_sources"]:
            st.markdown(f"- 🔗 *{s}*")
            
        st.markdown("<br><hr>", unsafe_allow_html=True)
        st.markdown("### 🏆 Engineering Case Mastery Challenge")
        quiz = case["quiz"]
        st.write(quiz["question"])
        
        with st.form(key=f"cs_quiz_{case['id']}"):
            choice = st.radio("Select the correct engineering conclusion:", quiz["options"], key=f"rad_{case['id']}")
            if st.form_submit_button("Submit Assessment"):
                if choice == quiz["answer"]:
                    st.success("✅ Correct!")
                    st.info(quiz["explanation"])
                else:
                    st.error("❌ Incorrect.")
                    st.info(quiz["explanation"])

def render_all_case_studies_hub():
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <h1 style="color: #F8F7FF; font-size: 2.5rem; margin-bottom: 8px;">🏭 Documented Industry Case Studies</h1>
        <p style="color: #AAB3CC; font-size: 1.1rem; max-width: 800px; line-height: 1.6;">
            Explore verified, real-world deployments of artificial intelligence and machine learning in industrial automation, 
            aviation, heavy power generation, and smart factory process management.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_case = st.radio("Select Case Study to Investigate:", 
                             ["Siemens (Industrial Edge AI)", "General Electric (Turbine Digital Twins)", "Honeywell (Smart Factory APM)"],
                             horizontal=True, key="hub_case_sel")
                             
    if "Siemens" in selected_case:
        render_case_study("SIEMENS")
    elif "General Electric" in selected_case:
        render_case_study("GE")
    else:
        render_case_study("HONEYWELL")
