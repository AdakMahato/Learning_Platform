"""
Syllabus Coverage Matrix for AI & Machine Learning Lab
Authoritative mapping between mandatory academic syllabus outcomes,
learning paths, interactive laboratories, industry case studies, and assessments.
"""

SYLLABUS_MODULES = {
    "M1": {
        "title": "Module 1: Introduction to AI for Engineers",
        "category": "Foundations",
        "topics": [
            {
                "id": "M1.1",
                "name": "Artificial Intelligence Definition",
                "description": "Definition of AI as rational agent behavior, perception-action cycle, and distinguishing intelligence from rigid automation.",
                "path_ref": "Path 1 (AI Foundations)",
                "case_ref": "Case 00 & Case 01",
                "practice_type": "Interactive Stepper & Conceptual Reflection",
                "assessment": "Foundations Mastery Quiz (Case 00 Module 1 & Path 1)",
                "status": "COMPLETED"
            },
            {
                "id": "M1.2",
                "name": "Machine Learning Definition",
                "description": "Inductive learning from historical data vs deductive algorithmic programming; function approximation.",
                "path_ref": "Path 1 (AI Foundations) & Path 4 (Supervised Studio)",
                "case_ref": "Case 00 Module 1 & Case 16",
                "practice_type": "Data vs Rules Experiment Sandbox",
                "assessment": "ML Definition & Paradigm Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M1.3",
                "name": "Deep Learning Definition",
                "description": "Hierarchical representation learning through multi-layer computational graphs and non-linear transformations.",
                "path_ref": "Path 6 (Neural Networks & Deep Learning)",
                "case_ref": "Path 6 Module 1 & Case 24",
                "practice_type": "Interactive Neural Network Forward-Pass Visualizer",
                "assessment": "Deep Learning Representation Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M1.4",
                "name": "Reinforcement Learning Definition",
                "description": "Agent-environment Markov Decision Process (MDP), reward signals, exploration vs exploitation, value functions.",
                "path_ref": "Path 1 & Path 7",
                "case_ref": "Case 00 Module 4 & Case 20",
                "practice_type": "Grid-World Q-Learning Sandbox",
                "assessment": "Reinforcement Learning Formulation Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M1.5",
                "name": "AI in Engineering Decision-Making",
                "description": "Cost-sensitive matrix decisions, safety bounds, trade-offs between precision and recall in automated systems.",
                "path_ref": "Path 1 & Path 4",
                "case_ref": "Case 15 (The Decision Maker)",
                "practice_type": "Utility Function & Decision Boundary Sandbox",
                "assessment": "Decision Theory Application Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M1.6",
                "name": "Predictive Maintenance",
                "description": "Transition from reactive and scheduled maintenance to condition-based anomaly detection and Remaining Useful Life (RUL) estimation.",
                "path_ref": "Path 3 & Lab A",
                "case_ref": "Honeywell Case Study & Lab A",
                "practice_type": "Motor Temperature & Vibration Degradation Sandbox",
                "assessment": "Predictive Maintenance Workflow Challenge",
                "status": "COMPLETED"
            },
            {
                "id": "M1.7",
                "name": "Process Control",
                "description": "Closed-loop feedback control, setpoint tracking, disturbance rejection using intelligent adaptive algorithms.",
                "path_ref": "Path 1 & Siemens Case Study",
                "case_ref": "Siemens Case Study & Case 01",
                "practice_type": "PLC Edge-Inference Simulation",
                "assessment": "Process Control & Automation Evaluation",
                "status": "COMPLETED"
            }
        ]
    },
    "M2": {
        "title": "Module 2: Data and Preprocessing",
        "category": "Data Engineering",
        "topics": [
            {
                "id": "M2.1",
                "name": "Sensor Data Processing",
                "description": "High-frequency telemetry, analog-to-digital sampling, handling noise, filtering, and calibration offsets.",
                "path_ref": "Path 3 (Data Preparation & Feature Engineering)",
                "case_ref": "Lab A (Motor Temperature Lab)",
                "practice_type": "Interactive Signal Filter & Resampling Sandbox",
                "assessment": "Sensor Telemetry Cleaning Exercise",
                "status": "COMPLETED"
            },
            {
                "id": "M2.2",
                "name": "Image Data Processing",
                "description": "Pixel representation, channels (RGB/Grayscale), spatial resolution, kernel convolution, normalization (0-255 to [0,1]).",
                "path_ref": "Path 3 & Path 6",
                "case_ref": "Lab C (Faulty Circuit Lab)",
                "practice_type": "Interactive Image Kernel & Feature Map Explorer",
                "assessment": "Image Preprocessing & Augmentation Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M2.3",
                "name": "Text Data Processing",
                "description": "Maintenance incident logs, tokenization, stop-word removal, TF-IDF vectorization for diagnostic error parsing.",
                "path_ref": "Path 3 Module 3",
                "case_ref": "Case 18 (The Naive Assumption)",
                "practice_type": "Interactive Diagnostic Log Parser",
                "assessment": "Text Representation & Bag-of-Words Exercise",
                "status": "COMPLETED"
            },
            {
                "id": "M2.4",
                "name": "Time-Series Data Preparation",
                "description": "Datetime indexing, chronological ordering, lag feature construction, sliding windows, preventing future leakage.",
                "path_ref": "Path 7 (Time-Series Intelligence)",
                "case_ref": "Case 12 & Path 7",
                "practice_type": "Interactive Lag Feature Builder & Leakage Validator",
                "assessment": "Time-Series Leakage Prevention Check",
                "status": "COMPLETED"
            },
            {
                "id": "M2.5",
                "name": "Data Cleaning & Missing Value Imputation",
                "description": "Mechanisms of missingness (MCAR, MAR, MNAR), mean/median imputation, forward-fill for time-series, removal hazards.",
                "path_ref": "Path 3 Module 1",
                "case_ref": "Lab A & Path 3",
                "practice_type": "Interactive Data Cleaning Workbench",
                "assessment": "Imputation Strategy Selection Challenge",
                "status": "COMPLETED"
            },
            {
                "id": "M2.6",
                "name": "Normalization & Standardization",
                "description": "Min-Max Scaling vs Z-score Standardization, distance distortion in unscaled KNN/K-Means/Gradient Descent.",
                "path_ref": "Path 3 Module 2",
                "case_ref": "Lab B (Materials Clustering) & Case 17",
                "practice_type": "Before-and-After Scaling Visualizer",
                "assessment": "Feature Scaling Mathematical Mastery Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M2.7",
                "name": "Feature Selection & Correlation Analysis",
                "description": "Pearson & Spearman correlation matrices, multicollinearity detection, variance thresholding, Mutual Information.",
                "path_ref": "Path 3 Module 4",
                "case_ref": "Lab A & Capstone Studio",
                "practice_type": "Interactive Heatmap & Feature Pruning Workbench",
                "assessment": "Feature Importance & Selection Check",
                "status": "COMPLETED"
            }
        ]
    },
    "M3": {
        "title": "Module 3: Supervised Learning",
        "category": "Core Machine Learning",
        "topics": [
            {
                "id": "M3.1",
                "name": "Linear Regression & Regularization",
                "description": "Ordinary Least Squares (OLS), cost function (MSE), gradient descent derivation, Ridge (L2) and Lasso (L1).",
                "path_ref": "Path 4 (Supervised Learning Studio)",
                "case_ref": "Lab A (Motor Temperature Prediction)",
                "practice_type": "Interactive Line-Fitting Playground with Loss Curves",
                "assessment": "Regression Metrics (MAE, MSE, RMSE, R2) Challenge",
                "status": "COMPLETED"
            },
            {
                "id": "M3.2",
                "name": "Logistic Regression & Classification Boundaries",
                "description": "Sigmoid link function, log-odds formulation, binary cross-entropy loss, decision threshold tuning.",
                "path_ref": "Path 4 Module 2",
                "case_ref": "Case 16 & Path 4",
                "practice_type": "Interactive Decision Boundary Explorer",
                "assessment": "Classification Metrics & Confusion Matrix Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M3.3",
                "name": "Decision Trees (ID3 / CART)",
                "description": "Information Gain, Shannon Entropy, Gini Impurity, recursive binary splitting, pruning to prevent overfitting.",
                "path_ref": "Path 4 Module 3",
                "case_ref": "Case 19 (The Tree That Makes Decisions)",
                "practice_type": "Interactive Tree Splitter & Depth Controller",
                "assessment": "Entropy & Information Gain Calculation Exercise",
                "status": "COMPLETED"
            },
            {
                "id": "M3.4",
                "name": "Random Forest & Ensemble Methods",
                "description": "Bootstrap aggregating (Bagging), feature subspace sampling, variance reduction, out-of-bag error.",
                "path_ref": "Path 4 Module 4",
                "case_ref": "Path 4 & Lab A Comparison",
                "practice_type": "Ensemble Forest Voting Sandbox",
                "assessment": "Random Forest vs Single Tree Bias-Variance Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M3.5",
                "name": "Equipment Failure Prediction",
                "description": "Binary and multiclass failure classification from sensor telemetry, addressing severe class imbalance with precision/recall.",
                "path_ref": "Path 4 Module 5",
                "case_ref": "Honeywell Case Study & Path 4",
                "practice_type": "Failure Prediction Model Evaluator",
                "assessment": "Imbalanced Metric Selection Exercise",
                "status": "COMPLETED"
            },
            {
                "id": "M3.6",
                "name": "Component Lifespan Prediction (RUL)",
                "description": "Continuous regression to predict Remaining Useful Life (RUL) in operating cycles or hours, residual analysis.",
                "path_ref": "Path 4 Module 6",
                "case_ref": "GE Case Study & Lab A",
                "practice_type": "RUL Degradation Curve Simulator",
                "assessment": "RUL Model Residual Inspection Challenge",
                "status": "COMPLETED"
            }
        ]
    },
    "M4": {
        "title": "Module 4: Unsupervised Learning",
        "category": "Pattern Recognition",
        "topics": [
            {
                "id": "M4.1",
                "name": "K-Means Clustering",
                "description": "Voronoi partitioning, centroid initialization (K-Means++), iterative Lloyd's algorithm, inertia and Elbow method.",
                "path_ref": "Path 5 (Unsupervised Learning & Anomaly)",
                "case_ref": "Lab B (Material Property Clustering)",
                "practice_type": "Interactive Centroid Step-by-Step Convergence Simulator",
                "assessment": "Optimal K Selection & Inertia Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M4.2",
                "name": "DBSCAN Density-Based Clustering",
                "description": "Core points, border points, density-reachable states, noise identification, resilience to non-spherical clusters.",
                "path_ref": "Path 5 Module 2",
                "case_ref": "Path 5 & Lab B Comparison",
                "practice_type": "Interactive Epsilon & MinSamples Density Sandbox",
                "assessment": "DBSCAN Parameter Selection & Noise Identification",
                "status": "COMPLETED"
            },
            {
                "id": "M4.3",
                "name": "Principal Component Analysis (PCA)",
                "description": "Covariance matrix eigendecomposition, orthogonal variance maximization, Scree plots, dimensionality reduction.",
                "path_ref": "Path 5 Module 3",
                "case_ref": "Lab B 2D/3D Projection & Path 5",
                "practice_type": "Interactive 3D-to-2D Projection & Variance Slider",
                "assessment": "Explained Variance Ratio Calculation Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M4.4",
                "name": "t-SNE Non-Linear Manifold Learning",
                "description": "Kullback-Leibler divergence minimization, perplexity tuning, local neighborhood preservation vs global distances.",
                "path_ref": "Path 5 Module 4",
                "case_ref": "Path 5 Advanced Visualization",
                "practice_type": "Interactive Perplexity Explorer",
                "assessment": "t-SNE Interpretation & Global Distance Pitfalls Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M4.5",
                "name": "Process Classification",
                "description": "Grouping manufacturing operational regimes (startup, steady-state, transient, shutdown) without supervisory labels.",
                "path_ref": "Path 5 Module 5",
                "case_ref": "Siemens Case Study & Lab B",
                "practice_type": "Operating Regime Clustering Workbench",
                "assessment": "Unsupervised Regime Identification Check",
                "status": "COMPLETED"
            },
            {
                "id": "M4.6",
                "name": "Anomaly Detection",
                "description": "Isolation Forests, One-Class SVM, distance-to-centroid thresholds for out-of-distribution mechanical faults.",
                "path_ref": "Path 5 Module 6",
                "case_ref": "GE Case Study & Path 5",
                "practice_type": "Interactive Anomaly Threshold Slider & Telemetry Monitor",
                "assessment": "Anomaly Detection Threshold Tradeoff Quiz",
                "status": "COMPLETED"
            }
        ]
    },
    "M5": {
        "title": "Module 5: Neural Networks and Deep Learning",
        "category": "Deep Learning",
        "topics": [
            {
                "id": "M5.1",
                "name": "Neuron Fundamentals & Perceptrons",
                "description": "Artificial neuron model: weighted summation $\\sum w_i x_i + b$, activation functions (Sigmoid, Tanh, ReLU, LeakyReLU).",
                "path_ref": "Path 6 (Neural Networks & Deep Learning)",
                "case_ref": "Path 6 Module 1",
                "practice_type": "Single Neuron Weight & Activation Playground",
                "assessment": "Activation Function Nonlinearity Challenge",
                "status": "COMPLETED"
            },
            {
                "id": "M5.2",
                "name": "Multilayer Perceptron (MLP) & Backpropagation",
                "description": "Dense forward propagation, chain rule gradient derivation, loss functions, learning rate schedules, weight updates.",
                "path_ref": "Path 6 Module 2",
                "case_ref": "Lab C (Faulty Circuit Detection)",
                "practice_type": "Interactive MLP Training Curve & Loss Surface",
                "assessment": "Backpropagation Gradient Flow Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M5.3",
                "name": "Convolutional Neural Networks (CNN)",
                "description": "Spatial feature hierarchies, 2D convolution filters, padding, stride, MaxPooling, fully connected classification head.",
                "path_ref": "Path 6 Module 3",
                "case_ref": "Path 6 & Lab C",
                "practice_type": "Interactive 2D Convolution Kernel Filter Visualizer",
                "assessment": "Feature Map Output Dimension Calculation",
                "status": "COMPLETED"
            },
            {
                "id": "M5.4",
                "name": "Engineering Image Recognition",
                "description": "Automated visual inspection of components on manufacturing assembly lines, transfer learning baselines.",
                "path_ref": "Path 6 Module 4",
                "case_ref": "Siemens Case Study & Lab C",
                "practice_type": "Visual Inspection Model Benchmark",
                "assessment": "Industrial Image Classification Metric Evaluation",
                "status": "COMPLETED"
            },
            {
                "id": "M5.5",
                "name": "Structural Crack Detection",
                "description": "Applying deep CNN architectures to surface inspection in civil structures, turbine blades, and pipelines.",
                "path_ref": "Path 6 Module 5",
                "case_ref": "GE Case Study & Path 6",
                "practice_type": "Crack vs Non-Crack Image Classification Demo",
                "assessment": "Structural Health Monitoring False-Negative Risk Quiz",
                "status": "COMPLETED"
            }
        ]
    },
    "M6": {
        "title": "Module 6: Time-Series Analysis",
        "category": "Sequential Analytics",
        "topics": [
            {
                "id": "M6.1",
                "name": "Time-Series Components & Stationarity",
                "description": "Trend, seasonality, cyclic patterns, residual noise; Augmented Dickey-Fuller (ADF) test, differencing for stationarity.",
                "path_ref": "Path 7 (Time-Series Intelligence)",
                "case_ref": "Case 12 & Path 7",
                "practice_type": "Interactive Seasonal Decomposition Sandbox",
                "assessment": "Stationarity & Differencing Challenge",
                "status": "COMPLETED"
            },
            {
                "id": "M6.2",
                "name": "ARIMA Modeling (AutoRegressive Integrated Moving Average)",
                "description": "Autocorrelation (ACF) and Partial Autocorrelation (PACF) plots, parameter selection $(p, d, q)$, baseline forecasting.",
                "path_ref": "Path 7 Module 2",
                "case_ref": "Path 7 Interactive Forecasting Lab",
                "practice_type": "Interactive ARIMA Forecast Horizon Explorer",
                "assessment": "ARIMA Parameter Identification & Evaluation Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M6.3",
                "name": "Introductory LSTM Networks",
                "description": "Vanishing gradient problem in RNNs, LSTM gating mechanisms (Forget, Input, Output gates), hidden state memory cell.",
                "path_ref": "Path 7 Module 3",
                "case_ref": "Path 7 Sequential Modeling",
                "practice_type": "LSTM Gate Activation Walkthrough",
                "assessment": "Recurrent Gate Architecture Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M6.4",
                "name": "Electricity Load Prediction",
                "description": "Multivariate industrial power demand forecasting with calendar features, temperature regressors, and lag metrics.",
                "path_ref": "Path 7 Module 4",
                "case_ref": "Path 7 Power Forecast Lab",
                "practice_type": "Grid Load Forecast vs Actual Comparison Workbench",
                "assessment": "Load Forecast MAPE & RMSE Analysis",
                "status": "COMPLETED"
            },
            {
                "id": "M6.5",
                "name": "Vibration Analysis",
                "description": "Fast Fourier Transform (FFT) spectral decomposition, bearing pass fault frequencies, vibration time-series monitoring.",
                "path_ref": "Path 7 Module 5",
                "case_ref": "GE & Honeywell Case Studies",
                "practice_type": "Interactive Vibration Spectrum & Harmonic Peak Detector",
                "assessment": "Vibration Signature Diagnostic Quiz",
                "status": "COMPLETED"
            }
        ]
    },
    "M7": {
        "title": "Module 7: Engineering Toolchain",
        "category": "Practical Engineering Tools",
        "topics": [
            {
                "id": "M7.1",
                "name": "Python for Scientific Computing",
                "description": "NumPy vectorized array operations, broadcasting, memory efficiency, pandas DataFrames, boolean masking, grouping.",
                "path_ref": "Path 2 (Python & Engineering Data Workshop)",
                "case_ref": "Path 2 & Case 01-05 Code Labs",
                "practice_type": "Interactive Python Subprocess Code Runner",
                "assessment": "Vectorized Operation Performance Lab",
                "status": "COMPLETED"
            },
            {
                "id": "M7.2",
                "name": "Jupyter Notebook & Literate Programming",
                "description": "Cell execution lifecycle, kernel state persistence, markdown documentation, inline visualization workflows.",
                "path_ref": "Path 8 (Engineering AI Toolchain)",
                "case_ref": "Path 8 Module 1",
                "practice_type": "Interactive Notebook Simulation & Kernel State Trace",
                "assessment": "Jupyter Workflow & Execution Order Check",
                "status": "COMPLETED"
            },
            {
                "id": "M7.3",
                "name": "scikit-learn Architecture",
                "description": "Consistent API design: Estimators, Transformers, Predictors, Pipelines, GridSearchCV cross-validation.",
                "path_ref": "Path 8 Module 2",
                "case_ref": "Labs A, B, C & Capstone Studio",
                "practice_type": "Pipeline Construction Code Lab",
                "assessment": "Scikit-Learn API & Data Leakage Prevention Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M7.4",
                "name": "TensorFlow / Keras Deployment Patterns",
                "description": "Sequential vs Functional API, compilation (optimizer, loss), callback monitoring (EarlyStopping), CPU/GPU fallback.",
                "path_ref": "Path 8 Module 3",
                "case_ref": "Lab C & Path 8",
                "practice_type": "Keras Model Architecture Builder",
                "assessment": "Deep Learning Training Pipeline Quiz",
                "status": "COMPLETED"
            },
            {
                "id": "M7.5",
                "name": "Git & Experiment Version Control",
                "description": "Repository management, branching, commit discipline, model artifact tracking, requirements.txt, reproducible READMEs.",
                "path_ref": "Path 8 Module 4",
                "case_ref": "Capstone Studio Requirements",
                "practice_type": "Git Branching & Release Workflow Simulator",
                "assessment": "Experiment Reproducibility & Git Hygiene Quiz",
                "status": "COMPLETED"
            }
        ]
    },
    "M8": {
        "title": "Module 8: Engineering AI Capstone Mini-Project",
        "category": "Applied Capstone",
        "topics": [
            {
                "id": "M8.1",
                "name": "Engineering Problem Definition",
                "description": "Formulating physical constraints, operational objectives, performance criteria, and baseline requirements.",
                "path_ref": "Path 9 (Capstone Studio)",
                "case_ref": "Capstone Step 1",
                "practice_type": "Guided Problem Scoping Wizard",
                "assessment": "Problem Statement Formulation Review",
                "status": "COMPLETED"
            },
            {
                "id": "M8.2",
                "name": "Engineering Dataset Selection & Profiling",
                "description": "Uploading or selecting real/synthetic engineering datasets, column schema verification, distribution inspection.",
                "path_ref": "Path 9 (Capstone Studio)",
                "case_ref": "Capstone Step 2-3",
                "practice_type": "Interactive CSV Profiler & Data Visualizer",
                "assessment": "Data Quality & Leakage Audit",
                "status": "COMPLETED"
            },
            {
                "id": "M8.3",
                "name": "Preprocessing & Pipeline Assembly",
                "description": "End-to-end transformation: imputation, scaling, one-hot encoding, feature selection, train/test splitting.",
                "path_ref": "Path 9 (Capstone Studio)",
                "case_ref": "Capstone Step 4-5",
                "practice_type": "Interactive Pipeline Builder",
                "assessment": "Data Preprocessing Verification Check",
                "status": "COMPLETED"
            },
            {
                "id": "M8.4",
                "name": "Model Training & Hyperparameter Tuning",
                "description": "Training multiple candidate architectures, evaluating bias/variance, cross-validation.",
                "path_ref": "Path 9 (Capstone Studio)",
                "case_ref": "Capstone Step 6-7",
                "practice_type": "Real-time Model Training Engine",
                "assessment": "Model Comparison Table & Leaderboard",
                "status": "COMPLETED"
            },
            {
                "id": "M8.5",
                "name": "Engineering Error Analysis & Report Export",
                "description": "Residual plots, worst-case prediction audits, physical plausibility check, automated technical report generation.",
                "path_ref": "Path 9 (Capstone Studio)",
                "case_ref": "Capstone Step 8-12",
                "practice_type": "Interactive Report Generator & Export",
                "assessment": "Final Engineering Technical Deliverable",
                "status": "COMPLETED"
            }
        ]
    }
}

REQUIRED_LABORATORIES = {
    "LAB_A": {
        "title": "Laboratory 1: Motor Temperature Prediction (Regression)",
        "objective": "Predict electric motor stator winding temperature rise under varying operating conditions.",
        "input_features": ["Motor Speed (RPM)", "Torque (Nm)", "Coolant Temp (°C)", "Ambient Temp (°C)", "Current (A)", "Voltage (V)"],
        "target": "Stator Winding Temperature (°C)",
        "algorithms": ["Linear Regression (OLS)", "Decision Tree Regressor", "Random Forest Regressor"],
        "evaluation_metrics": ["MAE", "RMSE", "R²", "Residual Distribution"],
        "interactive_features": ["Dynamic Feature Selection", "Train/Test Split Ratio", "Live Temperature Inference Slider"],
        "status": "IMPLEMENTED"
    },
    "LAB_B": {
        "title": "Laboratory 2: Material Property Clustering (K-Means)",
        "objective": "Unsupervised partitioning of engineering materials based on metallurgical and physical properties.",
        "input_features": ["Density (g/cm³)", "Tensile Strength (MPa)", "Vickers Hardness (HV)", "Thermal Conductivity (W/m·K)", "Elastic Modulus (GPa)"],
        "target": "Unsupervised Material Grouping (Structural Metals, Lightweight Alloys, Ceramics, Polymers)",
        "algorithms": ["K-Means Clustering", "PCA (2D Projection)", "DBSCAN Comparison"],
        "evaluation_metrics": ["Inertia (Elbow Method)", "Silhouette Score", "Cluster Centroid Profiles"],
        "interactive_features": ["K Slider (2-8)", "Feature Scaling Toggle", "Step-by-Step Centroid Movement Visualizer"],
        "status": "IMPLEMENTED"
    },
    "LAB_C": {
        "title": "Laboratory 3: Faulty Circuit Detection (Neural Networks)",
        "objective": "Binary defect classification for integrated electronic circuits from electrical diagnostic test vectors.",
        "input_features": ["Test Voltage V1 (V)", "Clock Frequency (MHz)", "Operating Temp (°C)", "Leakage Current (µA)", "Signal Jitter (ps)", "Power Supply Noise (mV)"],
        "target": "Circuit Status (0: Normal / Nominal, 1: Defective / Faulty)",
        "algorithms": ["Multilayer Perceptron (MLP)", "Lightweight Pure-Python Neural Network", "Logistic Baseline"],
        "evaluation_metrics": ["Confusion Matrix", "Precision", "Recall (Safety-Critical)", "F1-Score", "ROC-AUC"],
        "interactive_features": ["Hidden Layer Architecture Slider", "Learning Rate & Epoch Controls", "False Negative Cost Impact Calculator"],
        "status": "IMPLEMENTED"
    }
}

REQUIRED_INDUSTRY_CASES = {
    "SIEMENS": {
        "company": "Siemens AG",
        "title": "Industrial Automation & Edge AI in Manufacturing",
        "domain": "Manufacturing & PLC Control",
        "context": "Siemens Electronics Works Amberg (EWA) produces Simatic PLCs with >99.999% quality yields using AI edge inference.",
        "documented_applications": [
            "Industrial Edge AI for automated surface-mount technology (SMT) optical inspection.",
            "Simatic S7-1500 TM NPU (Neural Processing Unit) executing neural inference directly on the factory floor.",
            "Predictive tool-wear monitoring in precision computer numerical control (CNC) milling."
        ],
        "engineering_decision": "Automating continuous setpoint optimization and defect classification with zero cloud latency.",
        "verified_sources": [
            "Siemens Industrial Edge Architecture Whitepaper (Siemens Digital Industries)",
            "World Economic Forum Global Lighthouse Network - Siemens Amberg Smart Factory Case Study"
        ],
        "status": "VERIFIED_AND_DOCUMENTED"
    },
    "GE": {
        "company": "General Electric (GE Vernova / GE Aerospace)",
        "title": "Turbine Health Monitoring & Digital Twins",
        "domain": "Power Generation & Aviation",
        "context": "Monitoring >7,000 gas, steam, and aviation turbines globally with multi-gigabyte continuous sensor telemetry.",
        "documented_applications": [
            "Digital Twin thermodynamic simulation coupled with ML anomaly detection.",
            "Early detection of combustor acoustic oscillations (combustion dynamics) prior to flameout.",
            "Vibration signature spectral tracking for rotor blade creep and bearing degradation."
        ],
        "engineering_decision": "Scheduling maintenance during planned outages rather than suffering catastrophic in-service trips costing >$1M/day.",
        "verified_sources": [
            "GE Digital Twin: Analytical Framework for Asset Optimization (GE Global Research Technical Report)",
            "ASME Turbo Expo - Machine Learning Applied to Heavy-Duty Gas Turbine Predictive Diagnostics"
        ],
        "status": "VERIFIED_AND_DOCUMENTED"
    },
    "HONEYWELL": {
        "company": "Honeywell International",
        "title": "Smart Factory Predictive Maintenance (Honeywell Forge)",
        "domain": "Process Industries & Industrial Facilities",
        "context": "Honeywell Forge Asset Performance Management deployed across refineries, chemical plants, and discrete facilities.",
        "documented_applications": [
            "Vibration, pressure, and thermal telemetry ingestion for centrifugal compressors and pumps.",
            "Remaining Useful Life (RUL) estimation algorithms triggering automated work orders.",
            "Cross-asset benchmark anomaly detection across distributed enterprise plants."
        ],
        "engineering_decision": "Balancing operational throughput against component thermal stress to maximize plant profitability.",
        "verified_sources": [
            "Honeywell Forge APM Product Architecture & Deployment Overview",
            "Hydrocarbon Processing - Machine Learning in Refinery Asset Integrity Management"
        ],
        "status": "VERIFIED_AND_DOCUMENTED"
    }
}

def get_coverage_stats():
    total_topics = sum(len(m["topics"]) for m in SYLLABUS_MODULES.values())
    completed_topics = sum(1 for m in SYLLABUS_MODULES.values() for t in m["topics"] if t["status"] == "COMPLETED")
    
    total_labs = len(REQUIRED_LABORATORIES)
    implemented_labs = sum(1 for lab in REQUIRED_LABORATORIES.values() if lab["status"] == "IMPLEMENTED")
    
    total_cases = len(REQUIRED_INDUSTRY_CASES)
    verified_cases = sum(1 for c in REQUIRED_INDUSTRY_CASES.values() if c["status"] == "VERIFIED_AND_DOCUMENTED")
    
    return {
        "total_topics": total_topics,
        "completed_topics": completed_topics,
        "topic_coverage_pct": round(completed_topics / total_topics * 100, 1),
        "total_labs": total_labs,
        "implemented_labs": implemented_labs,
        "lab_coverage_pct": round(implemented_labs / total_labs * 100, 1),
        "total_cases": total_cases,
        "verified_cases": verified_cases,
        "case_coverage_pct": round(verified_cases / total_cases * 100, 1)
    }

if __name__ == "__main__":
    stats = get_coverage_stats()
    print("=== SYLLABUS COVERAGE AUDIT REPORT ===")
    print(f"Academic Topics: {stats['completed_topics']}/{stats['total_topics']} ({stats['topic_coverage_pct']}%)")
    print(f"Engineering Labs: {stats['implemented_labs']}/{stats['total_labs']} ({stats['lab_coverage_pct']}%)")
    print(f"Industry Cases: {stats['verified_cases']}/{stats['total_cases']} ({stats['case_coverage_pct']}%)")
