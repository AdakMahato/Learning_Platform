"""
Learning Paths Architecture for AI & Machine Learning Lab
Comprehensive 9-Path Engineering Curriculum:
Path 1: AI Foundations for Engineers
Path 2: Python and the Engineering Data Workshop
Path 3: Data Preparation and Feature Engineering
Path 4: Supervised Learning Studio
Path 5: Unsupervised Learning and Anomaly Detection
Path 6: Neural Networks and Deep Learning
Path 7: Time-Series Intelligence
Path 8: Engineering AI Toolchain
Path 9: Engineering AI Capstone Mini-Project
"""

import streamlit as st
import engineering_labs

LEARNING_PATHS_CATALOG = [
    {
        "id": "path_1",
        "number": 1,
        "title": "AI Foundations for Engineers",
        "icon": "🧠",
        "level": "Introductory",
        "duration": "3 Hours",
        "summary": "From deterministic automation to inductive learning. Master agent perception, search vs ML, and engineering decision trade-offs.",
        "topics": [
            "What Artificial Intelligence Means in Engineering Systems",
            "Deterministic Rule-Based Code vs Machine Learning",
            "Supervised, Unsupervised, and Reinforcement Learning Paraphrased",
            "Features, Targets, Loss Functions, and Parameters",
            "Limitations, Telemetry Quality, and Human Oversight"
        ],
        "lab_connection": "Foundations Exploration & Case 00-01",
        "status_key": "path_1_completed"
    },
    {
        "id": "path_2",
        "number": 2,
        "title": "Python & Engineering Data Workshop",
        "icon": "🐍",
        "level": "Foundational",
        "duration": "4 Hours",
        "summary": "NumPy vectorized computing, pandas DataFrames for sensor logs, and writing high-performance data processing pipelines.",
        "topics": [
            "Vectorized Arrays with NumPy (Avoiding Slow Python Loops)",
            "Handling Multi-Channel Telemetry with pandas DataFrames",
            "Filtering, Masking, and Aggregating Sensor Datasets",
            "Plotly and Matplotlib for Engineering Data Visualization",
            "Building Reusable Data Ingestion Functions"
        ],
        "lab_connection": "Interactive Code Runner & Subprocess Sandbox",
        "status_key": "path_2_completed"
    },
    {
        "id": "path_3",
        "number": 3,
        "title": "Data Preparation & Feature Engineering",
        "icon": "🧹",
        "level": "Intermediate",
        "duration": "5 Hours",
        "summary": "Sensor, image, text, and time-series data cleaning. Outlier rejection, scaling, encoding, and preventing catastrophic data leakage.",
        "topics": [
            "Sensor Imputation: Median, Forward-Fill, and Drop Risks",
            "Feature Scaling: StandardScaler vs MinMaxScaler (Why Euclidean distances fail unscaled)",
            "Categorical Encoding for Industrial Component Families",
            "Feature Selection, Heatmap Correlation & Multicollinearity",
            "Strict Train/Test Pipeline Isolation to Prevent Future Leakage"
        ],
        "lab_connection": "Laboratory 1 Preprocessing & Lab B Scaling Explorer",
        "status_key": "path_3_completed"
    },
    {
        "id": "path_4",
        "number": 4,
        "title": "Supervised Learning Studio",
        "icon": "📈",
        "level": "Intermediate",
        "duration": "6 Hours",
        "summary": "Linear & Logistic Regression, Decision Trees, Random Forests. Equipment failure classification and motor temperature prediction.",
        "topics": [
            "Regression vs Classification Formulations in Engineering",
            "Loss Functions: MSE, Cross-Entropy, and Gradient Descent",
            "Decision Trees (Information Gain, Shannon Entropy, Gini Impurity)",
            "Random Forest Ensembles: Bagging and Variance Reduction",
            "Overfitting vs Underfitting: The Bias-Variance Trade-off"
        ],
        "lab_connection": "Laboratory 1 (Electric Motor Temperature Regression)",
        "status_key": "path_4_completed"
    },
    {
        "id": "path_5",
        "number": 5,
        "title": "Unsupervised Learning & Anomaly Detection",
        "icon": "🌀",
        "level": "Intermediate",
        "duration": "5 Hours",
        "summary": "K-Means, DBSCAN, PCA, and t-SNE. Unsupervised grouping of material properties and finding out-of-distribution mechanical faults.",
        "topics": [
            "K-Means Clustering: Centroid Initialization, Inertia & Lloyd's Loop",
            "DBSCAN: Density-Based Clustering and Outlier/Noise Detection",
            "Principal Component Analysis (PCA): Eigenvectors & Dimensionality Reduction",
            "t-SNE Manifold Visualization: Local vs Global Geometry Cautions",
            "Industrial Anomaly Detection with Distance Metrics"
        ],
        "lab_connection": "Laboratory 2 (Material Property Clustering & DBSCAN Playground)",
        "status_key": "path_5_completed"
    },
    {
        "id": "path_6",
        "number": 6,
        "title": "Neural Networks & Deep Learning",
        "icon": "⚡",
        "level": "Advanced",
        "duration": "7 Hours",
        "summary": "Perceptrons, Multilayer Perceptrons, Backpropagation, and Convolutional Neural Networks (CNN) for automated quality inspection.",
        "topics": [
            "The Artificial Neuron: Weighted Sums and Non-linear Activations",
            "Why Deep Networks Need ReLU and Backpropagation (Chain Rule)",
            "Multilayer Perceptron (MLP) for Multi-Sensor Defect Classification",
            "Convolutional Neural Networks: 2D Spatial Filters, Strides, and Pooling",
            "Structural Crack Detection & Circuit Inspection Telemetry"
        ],
        "lab_connection": "Laboratory 3 (Faulty Circuit Detection) & CNN Filter Visualizer",
        "status_key": "path_6_completed"
    },
    {
        "id": "path_7",
        "number": 7,
        "title": "Time-Series Intelligence",
        "icon": "⏱️",
        "level": "Advanced",
        "duration": "5 Hours",
        "summary": "Sequential telemetry modeling: trend, seasonality, stationarity, autoregressive lag features, ARIMA, and introductory LSTM concepts.",
        "topics": [
            "Characteristics of Sensor Streams: Sampling Rates, Jitter, and Stationarity",
            "Constructing Autoregressive Lag Features Without Chronological Leakage",
            "Baseline Persistence vs Moving Average vs ARIMA Formulations",
            "Introductory Recurrent Neural Networks & LSTM Gating Mechanics",
            "Vibration FFT Spectral Decomposition & Bearing Fault Frequencies"
        ],
        "lab_connection": "Time-Series Forecasting Laboratory & Vibration Playground",
        "status_key": "path_7_completed"
    },
    {
        "id": "path_8",
        "number": 8,
        "title": "Engineering AI Toolchain",
        "icon": "🧰",
        "level": "Practical Tools",
        "duration": "3 Hours",
        "summary": "Mastering the standard production toolchain: Jupyter Notebook, scikit-learn Pipelines, Git experiment tracking, and reproducible READMEs.",
        "topics": [
            "Jupyter Notebook Kernel Execution Lifecycle and Best Practices",
            "scikit-learn Estimator, Transformer, and Pipeline Architecture",
            "Model Serialization: Saving and Loading Artifacts Safely",
            "Git Version Control for Machine Learning Experiments and Code",
            "Dependency Isolation with Virtual Environments and Requirements Files"
        ],
        "lab_connection": "Integrated Subprocess Python Runner & Pipeline Workbench",
        "status_key": "path_8_completed"
    },
    {
        "id": "path_9",
        "number": 9,
        "title": "Engineering AI Capstone Mini-Project",
        "icon": "🚀",
        "level": "Applied Capstone",
        "duration": "8 Hours",
        "summary": "A 12-step guided engineering project: formulate the physical problem, clean telemetry, train baselines, evaluate failure risks, and export reports.",
        "topics": [
            "1. Engineering Problem Scoping & Constraint Definition",
            "2. Dataset Ingestion (Turbofan Telemetry or Custom CSV Upload)",
            "3. Profiling, Cleaning, and Null Value Imputation",
            "4. Scaled Feature Engineering and Leakage-Free Train/Test Split",
            "5. Model Benchmarking, Hyperparameter Selection & Cross-Validation",
            "6. Rigorous Error Analysis, Safety Thresholds & Automated Technical Export"
        ],
        "lab_connection": "Capstone Studio Guided 12-Step Workspace",
        "status_key": "path_9_completed"
    }
]

def render_learning_paths_dashboard():
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <h1 style="color: #F8F7FF; font-size: 2.5rem; margin-bottom: 8px;">🎓 Engineering Learning Paths</h1>
        <p style="color: #AAB3CC; font-size: 1.1rem; max-width: 800px; line-height: 1.6;">
            A progressive, structured curriculum designed specifically for engineering students. 
            Learn through physical intuition, interactive visualizations, and real-world industrial datasets.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3-column grid of learning path cards
    for i in range(0, len(LEARNING_PATHS_CATALOG), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(LEARNING_PATHS_CATALOG):
                path = LEARNING_PATHS_CATALOG[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div style="background: #121B32; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 22px; margin-bottom: 16px; height: 340px; display: flex; flex-direction: column;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span style="font-size: 1.8rem;">{path['icon']}</span>
                            <span style="background: rgba(124, 77, 255, 0.15); color: #C4B5FD; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 12px;">{path['level']} • {path['duration']}</span>
                        </div>
                        <div style="color: #F8F7FF; font-weight: 800; font-size: 1.15rem; margin-bottom: 8px;">Path {path['number']}: {path['title']}</div>
                        <div style="color: #AAB3CC; font-size: 0.85rem; line-height: 1.5; margin-bottom: 14px; flex-grow: 1;">{path['summary']}</div>
                        <div style="color: #64748B; font-size: 0.75rem; margin-bottom: 12px;"><b>Lab:</b> {path['lab_connection']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Enter Path {path['number']} →", key=f"btn_enter_{path['id']}", use_container_width=True):
                        st.session_state["active_learning_path"] = path["id"]
                        st.rerun()

def render_active_learning_path(path_id: str):
    path = next((p for p in LEARNING_PATHS_CATALOG if p["id"] == path_id), None)
    if not path:
        st.error("Learning path not found.")
        return
        
    if st.button("← Back to All Learning Paths", key="back_to_paths"):
        del st.session_state["active_learning_path"]
        st.rerun()
        
    st.markdown(f"""
    <div style="background: rgba(124, 77, 255, 0.08); border-left: 4px solid #7C4DFF; padding: 20px 24px; border-radius: 8px; margin-bottom: 24px;">
        <div style="color: #A78BFA; font-size: 0.8rem; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 6px;">
            LEARNING PATH {path['number']} • {path['level'].upper()}
        </div>
        <h1 style="color: #F8F7FF; margin: 0 0 10px 0;">{path['icon']} {path['title']}</h1>
        <p style="color: #AAB3CC; font-size: 1.05rem; line-height: 1.6; margin: 0;">{path['summary']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Syllabus Core Learning Objectives")
    for t in path["topics"]:
        st.markdown(f"- 📌 **{t}**")
        
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Route to specialized interactive laboratory view if available
    if path["id"] == "path_4":
        st.markdown("### ⚡ Interactive Lab for this Path:")
        engineering_labs.render_motor_temperature_lab()
    elif path["id"] == "path_5":
        st.markdown("### 🔬 Interactive Labs for this Path:")
        t1, t2 = st.tabs(["Material Property Clustering", "DBSCAN Density Explorer"])
        with t1:
            engineering_labs.render_materials_clustering_lab()
        with t2:
            engineering_labs.render_dbscan_playground()
    elif path["id"] == "path_6":
        st.markdown("### ⚡ Interactive Labs for this Path:")
        t1, t2 = st.tabs(["Faulty Circuit Detection Neural Net", "CNN 2D Filter Convolution Visualizer"])
        with t1:
            engineering_labs.render_circuit_detection_lab()
        with t2:
            engineering_labs.render_cnn_filter_visualizer()
    elif path["id"] == "path_7":
        st.markdown("### 📈 Interactive Lab for this Path:")
        engineering_labs.render_timeseries_forecasting_lab()
    elif path["id"] == "path_9":
        import capstone_project
        capstone_project.render_capstone_studio()
    else:
        st.info(f"💡 This path provides foundational theory and code labs. You can explore the connected cases in the Classical & Algorithmic AI Archive or open the Engineering Labs from the navigation bar!")
