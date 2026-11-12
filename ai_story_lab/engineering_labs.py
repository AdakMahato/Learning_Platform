"""
Interactive Engineering Laboratories for AI & Machine Learning Lab
Contains the implementations and UI renderers for:
- Lab A: Electric Motor Temperature Prediction (Regression)
- Lab B: Engineering Materials Clustering (K-Means & PCA)
- Lab C: Integrated Circuit Defect Detection (Neural Network)
- Interactive Playgrounds: DBSCAN Explorer, CNN Filter Visualizer, Time-Series Forecasting
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.neural_network import MLPClassifier

# -------------------------------------------------------------
# 1. LAB A: ELECTRIC MOTOR TEMPERATURE PREDICTION
# -------------------------------------------------------------
@st.cache_data
def load_motor_temperature_dataset(n_samples=600, random_state=42):
    """
    Generates a physically grounded educational dataset simulating
    permanent magnet synchronous motor (PMSM) telemetry.
    Physical relationships:
    Stator Temp increases with: current^2 (Joule heating), speed (iron losses),
    torque, and ambient temperature; cooled by coolant flow.
    """
    np.random.seed(random_state)
    speed = np.random.uniform(800, 4500, n_samples)  # RPM
    torque = np.random.uniform(5, 120, n_samples)    # Nm
    ambient_temp = np.random.uniform(18, 42, n_samples) # °C
    coolant_temp = np.random.uniform(15, 65, n_samples) # °C
    voltage = np.random.uniform(200, 480, n_samples)   # V
    
    # Motor current proportional to torque with efficiency variations
    current = (torque * speed * 2 * np.pi / 60) / (np.sqrt(3) * voltage * 0.88) + np.random.normal(0, 3, n_samples)
    current = np.clip(current, 2, 95)
    
    # Stator temperature physics formulation:
    # Joule heat ~ I^2 * R, Core loss ~ speed * B^2, Ambient offset, Coolant cooling effect
    stator_temp = (
        ambient_temp * 0.45 +
        coolant_temp * 0.55 +
        (current ** 1.8) * 0.038 +
        (speed / 1000.0) ** 1.4 * 4.2 +
        (torque / 10.0) * 2.1 +
        np.random.normal(0, 2.5, n_samples)
    )
    
    df = pd.DataFrame({
        "Motor_Speed_RPM": np.round(speed, 1),
        "Torque_Nm": np.round(torque, 2),
        "Current_A": np.round(current, 2),
        "Voltage_V": np.round(voltage, 1),
        "Ambient_Temp_C": np.round(ambient_temp, 2),
        "Coolant_Temp_C": np.round(coolant_temp, 2),
        "Stator_Winding_Temp_C": np.round(stator_temp, 2)
    })
    return df

def render_motor_temperature_lab():
    st.markdown("""
    <div style="background: rgba(124, 77, 255, 0.08); border-left: 4px solid #7C4DFF; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h2 style="color: #F8F7FF; margin: 0 0 8px 0;">⚡ Laboratory 1: Motor Temperature Prediction</h2>
        <div style="color: #C4B5FD; font-size: 0.95rem;">
            <b>Physical Objective:</b> Model the thermal dynamics of a Permanent Magnet Synchronous Motor (PMSM). 
            Predict stator winding temperature rise to prevent thermal insulation breakdown and motor burnout.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = load_motor_temperature_dataset()
    
    tab_data, tab_model, tab_infer, tab_theory = st.tabs([
        "📊 1. Data Exploration", 
        "🛠️ 2. Model Training & Comparison", 
        "🎛️ 3. Live Physical Inference", 
        "📐 4. Physical Equations & Insights"
    ])
    
    with tab_data:
        st.markdown("### 🔍 Motor Telemetry Dataset")
        st.write("Examine 600 steady-state operational measurements captured from simulated dyno test-cell telemetry:")
        st.dataframe(df.head(10), use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            feature_x = st.selectbox("Select Feature for Correlation with Stator Temp:", 
                                     ["Current_A", "Motor_Speed_RPM", "Torque_Nm", "Coolant_Temp_C", "Ambient_Temp_C"],
                                     key="mot_feat_x")
            fig_scatter = px.scatter(
                df, x=feature_x, y="Stator_Winding_Temp_C", 
                color="Current_A",
                title=f"Stator Winding Temp vs {feature_x}",
                color_continuous_scale="Turbo",
                template="plotly_dark"
            )
            fig_scatter.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        with col2:
            st.markdown("#### 🌡️ Temperature Distribution Statistics")
            st.write(df[["Current_A", "Coolant_Temp_C", "Stator_Winding_Temp_C"]].describe().T)
            st.info("💡 **Engineering Observation:** Notice that as current increases, temperature increases non-linearly. This matches Joule heating ($P = I^2 R$), a key non-linearity for regression.")

    with tab_model:
        st.markdown("### ⚙️ Train & Compare Regression Architectures")
        
        all_features = ["Motor_Speed_RPM", "Torque_Nm", "Current_A", "Voltage_V", "Ambient_Temp_C", "Coolant_Temp_C"]
        selected_features = st.multiselect("Select Input Features:", all_features, default=all_features, key="mot_sel_feats")
        
        if not selected_features:
            st.warning("Please select at least one feature.")
            return

        split_pct = st.slider("Training Set Split Percentage:", 50, 90, 80, 5, key="mot_split")
        model_choice = st.selectbox("Select Candidate Algorithm:", ["Linear Regression (OLS)", "Ridge Regression (L2)", "Decision Tree Regressor", "Random Forest Regressor"], key="mot_algo")
        
        X = df[selected_features]
        y = df["Stator_Winding_Temp_C"]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(100-split_pct)/100.0, random_state=42)
        
        # Model initialization
        if model_choice == "Linear Regression (OLS)":
            model = LinearRegression()
        elif model_choice == "Ridge Regression (L2)":
            model = Ridge(alpha=1.0)
        elif model_choice == "Decision Tree Regressor":
            model = DecisionTreeRegressor(max_depth=5, random_state=42)
        else:
            model = RandomForestRegressor(n_estimators=50, max_depth=6, random_state=42)
            
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("MAE (Mean Absolute Error)", f"{mae:.2f} °C", help="Average magnitude of temperature error in degrees.")
        col_m2.metric("RMSE (Root Mean Squared Error)", f"{rmse:.2f} °C", help="Penalizes large temperature deviations heavily.")
        col_m3.metric("R² Score (Goodness of Fit)", f"{r2:.3f}", help="1.0 indicates perfect variance explanation.")
        
        # Actual vs Predicted plot
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            fig_pred = go.Figure()
            fig_pred.add_trace(go.Scatter(x=y_test, y=y_pred, mode='markers', name='Predictions', marker=dict(color='#A78BFA', opacity=0.7)))
            # Perfect fit line
            min_v, max_v = min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())
            fig_pred.add_trace(go.Scatter(x=[min_v, max_v], y=[min_v, max_v], mode='lines', name='Perfect Ideal Fit', line=dict(color='#34D399', dash='dash')))
            fig_pred.update_layout(title="Actual vs Predicted Stator Temperature", xaxis_title="Actual Temp (°C)", yaxis_title="Predicted Temp (°C)", template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_pred, use_container_width=True)
            
        with col_p2:
            residuals = y_test - y_pred
            fig_res = px.histogram(residuals, nbins=25, title="Residual Distribution (Actual - Predicted)", labels={'value': 'Residual Error (°C)'}, template="plotly_dark", color_discrete_sequence=['#38BDF8'])
            fig_res.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_res, use_container_width=True)
            
        if hasattr(model, "coef_"):
            st.markdown("#### 📐 Learned Linear Model Weights")
            coef_df = pd.DataFrame({"Feature": selected_features, "Coefficient (Weight)": model.coef_}).sort_values(by="Coefficient (Weight)", ascending=False)
            st.dataframe(coef_df, use_container_width=True)

    with tab_infer:
        st.markdown("### 🎛️ Interactive Digital-Twin Simulator")
        st.write("Adjust operational parameters to evaluate the trained model's real-time prediction:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            sim_speed = st.slider("Motor Speed (RPM)", 800, 4500, 2500, 50, key="sim_spd")
            sim_torque = st.slider("Torque (Nm)", 5.0, 120.0, 45.0, 1.0, key="sim_trq")
        with c2:
            sim_current = st.slider("Current (A)", 5.0, 90.0, 35.0, 1.0, key="sim_cur")
            sim_voltage = st.slider("Bus Voltage (V)", 200, 480, 400, 10, key="sim_vlt")
        with c3:
            sim_amb = st.slider("Ambient Temp (°C)", 15.0, 45.0, 25.0, 0.5, key="sim_amb")
            sim_cool = st.slider("Coolant Temp (°C)", 15.0, 70.0, 30.0, 0.5, key="sim_col")
            
        input_data = pd.DataFrame([{
            "Motor_Speed_RPM": sim_speed,
            "Torque_Nm": sim_torque,
            "Current_A": sim_current,
            "Voltage_V": sim_voltage,
            "Ambient_Temp_C": sim_amb,
            "Coolant_Temp_C": sim_cool
        }])[selected_features]
        
        pred_temp = model.predict(input_data)[0]
        
        # Display gauge / metric
        st.markdown("<br>", unsafe_allow_html=True)
        if pred_temp > 105:
            alert_color = "#EF4444"
            status_text = "🚨 DANGER: Thermal Limit Exceeded! High risk of stator insulation degradation."
        elif pred_temp > 85:
            alert_color = "#F59E0B"
            status_text = "⚠️ WARNING: Elevated winding temperature. Derating recommended."
        else:
            alert_color = "#10B981"
            status_text = "✅ NORMAL: Operating well within safe thermal thresholds (Class H insulation)."
            
        st.markdown(f"""
        <div style="background: rgba(0,0,0,0.3); border: 2px solid {alert_color}; border-radius: 12px; padding: 24px; text-align: center;">
            <div style="color: #AAB3CC; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em;">Predicted Stator Winding Temperature</div>
            <div style="font-size: 3.5rem; font-weight: 800; color: {alert_color}; margin: 8px 0;">{pred_temp:.1f} °C</div>
            <div style="font-size: 1rem; color: #F8F7FF;">{status_text}</div>
        </div>
        """, unsafe_allow_html=True)

    with tab_theory:
        st.markdown("""
        ### 📚 Engineering Thermal Physics Principles
        
        In electric traction drives, temperature rise $\\Delta T$ is governed by the heat generation rate $P_{loss}$ balanced by convective/conductive heat dissipation $Q_{cool}$:
        
        $$\\Delta T = \\frac{P_{loss}}{h \\cdot A}$$
        
        Where electromagnetic losses $P_{loss}$ comprise:
        1. **Copper Losses ($I^2 R$):** Directly proportional to current squared. Dominates at high torque / heavy load.
        2. **Iron Core Losses ($P_{iron}$):** Eddy current and hysteresis losses, proportional to frequency (motor speed) squared: $P_{eddy} \\propto B^2 f^2$.
        3. **Friction and Windage Losses:** Mechanical drag proportional to angular velocity.
        
        **Why AI is Necessary:**
        Physical thermal finite element analysis (FEA) or lumped-parameter models require minutes of simulation time. A trained machine learning regression model can predict stator temperature in **under 200 microseconds**, enabling embedded digital-twin monitoring directly inside motor controllers!
        """)

# -------------------------------------------------------------
# 2. LAB B: MATERIAL PROPERTY CLUSTERING (K-MEANS)
# -------------------------------------------------------------
@st.cache_data
def load_materials_dataset():
    """
    Realistic engineering materials dataset containing physical, mechanical,
    and thermal properties across distinct metallurgical families.
    """
    materials = [
        # Structural Steels
        {"Material": "Carbon Steel AISI 1045", "Family": "Steel", "Density": 7.85, "Tensile_MPa": 565, "Hardness_HV": 170, "Thermal_Cond": 49.8, "Modulus_GPa": 205},
        {"Material": "Alloy Steel 4140 (Annealed)", "Family": "Steel", "Density": 7.85, "Tensile_MPa": 655, "Hardness_HV": 197, "Thermal_Cond": 42.6, "Modulus_GPa": 210},
        {"Material": "Stainless Steel 316L", "Family": "Steel", "Density": 8.00, "Tensile_MPa": 485, "Hardness_HV": 160, "Thermal_Cond": 16.3, "Modulus_GPa": 193},
        {"Material": "Tool Steel D2 (Hardened)", "Family": "Steel", "Density": 7.70, "Tensile_MPa": 1750, "Hardness_HV": 650, "Thermal_Cond": 20.0, "Modulus_GPa": 210},
        {"Material": "Spring Steel 5160", "Family": "Steel", "Density": 7.85, "Tensile_MPa": 725, "Hardness_HV": 220, "Thermal_Cond": 46.0, "Modulus_GPa": 207},
        
        # Aluminum Alloys (Lightweight, High Conductivity)
        {"Material": "Aluminum 6061-T6", "Family": "Lightweight Metal", "Density": 2.70, "Tensile_MPa": 310, "Hardness_HV": 107, "Thermal_Cond": 167.0, "Modulus_GPa": 68.9},
        {"Material": "Aluminum 7075-T6", "Family": "Lightweight Metal", "Density": 2.81, "Tensile_MPa": 572, "Hardness_HV": 175, "Thermal_Cond": 130.0, "Modulus_GPa": 71.7},
        {"Material": "Aluminum 2024-T3", "Family": "Lightweight Metal", "Density": 2.78, "Tensile_MPa": 483, "Hardness_HV": 137, "Thermal_Cond": 121.0, "Modulus_GPa": 73.1},
        {"Material": "Cast Al A356-T6", "Family": "Lightweight Metal", "Density": 2.68, "Tensile_MPa": 260, "Hardness_HV": 85, "Thermal_Cond": 151.0, "Modulus_GPa": 72.4},
        
        # Titanium & Superalloys
        {"Material": "Titanium Ti-6Al-4V (Grade 5)", "Family": "Titanium", "Density": 4.43, "Tensile_MPa": 950, "Hardness_HV": 349, "Thermal_Cond": 6.7, "Modulus_GPa": 113.8},
        {"Material": "Titanium Grade 2 (CP)", "Family": "Titanium", "Density": 4.51, "Tensile_MPa": 345, "Hardness_HV": 145, "Thermal_Cond": 16.4, "Modulus_GPa": 105.0},
        {"Material": "Inconel 718 (Nickel Superalloy)", "Family": "Superalloy", "Density": 8.19, "Tensile_MPa": 1240, "Hardness_HV": 390, "Thermal_Cond": 11.4, "Modulus_GPa": 211.0},
        
        # Engineering Ceramics (Ultra Hard, Brittle, Low Thermal Expansion)
        {"Material": "Alumina (Al2O3 99.5%)", "Family": "Ceramic", "Density": 3.90, "Tensile_MPa": 220, "Hardness_HV": 1440, "Thermal_Cond": 30.0, "Modulus_GPa": 370.0},
        {"Material": "Silicon Carbide (SiC)", "Family": "Ceramic", "Density": 3.10, "Tensile_MPa": 350, "Hardness_HV": 2500, "Thermal_Cond": 120.0, "Modulus_GPa": 410.0},
        {"Material": "Zirconia (ZrO2 Y-TZP)", "Family": "Ceramic", "Density": 6.05, "Tensile_MPa": 800, "Hardness_HV": 1200, "Thermal_Cond": 2.0, "Modulus_GPa": 210.0},
        {"Material": "Silicon Nitride (Si3N4)", "Family": "Ceramic", "Density": 3.20, "Tensile_MPa": 700, "Hardness_HV": 1600, "Thermal_Cond": 28.0, "Modulus_GPa": 310.0},
        
        # Engineering Polymers
        {"Material": "PEEK (Polyetheretherketone)", "Family": "Polymer", "Density": 1.32, "Tensile_MPa": 100, "Hardness_HV": 28, "Thermal_Cond": 0.25, "Modulus_GPa": 3.6},
        {"Material": "PTFE (Teflon)", "Family": "Polymer", "Density": 2.20, "Tensile_MPa": 25, "Hardness_HV": 10, "Thermal_Cond": 0.25, "Modulus_GPa": 0.5},
        {"Material": "Nylon 6/6", "Family": "Polymer", "Density": 1.14, "Tensile_MPa": 82, "Hardness_HV": 20, "Thermal_Cond": 0.25, "Modulus_GPa": 2.8},
        {"Material": "Polycarbonate (Lexan)", "Family": "Polymer", "Density": 1.20, "Tensile_MPa": 65, "Hardness_HV": 15, "Thermal_Cond": 0.20, "Modulus_GPa": 2.4}
    ]
    return pd.DataFrame(materials)

def render_materials_clustering_lab():
    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.08); border-left: 4px solid #10B981; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h2 style="color: #F8F7FF; margin: 0 0 8px 0;">🔬 Laboratory 2: Material Property Clustering</h2>
        <div style="color: #A7F3D0; font-size: 0.95rem;">
            <b>Metallurgical Objective:</b> Discover natural groupings of structural materials from unlabelled multi-dimensional physical properties 
            (Density, Tensile Strength, Vickers Hardness, Thermal Conductivity, Elastic Modulus) using K-Means and PCA.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = load_materials_dataset()
    feature_cols = ["Density", "Tensile_MPa", "Hardness_HV", "Thermal_Cond", "Modulus_GPa"]
    
    tab_inspect, tab_cluster, tab_pca, tab_theory = st.tabs([
        "📋 1. Material Properties Table", 
        "🌀 2. Interactive K-Means", 
        "🌌 3. PCA 2D Manifold Projection", 
        "💡 4. Engineering Material Selection"
    ])
    
    with tab_inspect:
        st.markdown("### 🧪 Engineering Materials Benchmark Database")
        st.write("20 standard engineering materials across metals, ceramics, and polymers:")
        st.dataframe(df, use_container_width=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### ⚖️ The Critical Importance of Feature Scaling")
            st.info("""
            Notice the vast magnitude differences:
            - **Density:** 1.14 to 8.19 $g/cm^3$
            - **Hardness:** 10 to 2,500 $HV$
            - **Thermal Conductivity:** 0.20 to 167.0 $W/m\\cdot K$
            
            If we run K-Means **without scaling**, the Euclidean distance $(\\Delta x)^2$ will be completely dominated by Hardness (variations of $\\pm 1000$), completely ignoring density and conductivity!
            """)
        with c2:
            st.markdown("#### 📈 Property Correlation Matrix")
            corr = df[feature_cols].corr()
            fig_corr = px.imshow(corr, text_auto=".2f", color_continuous_scale="Viridis", template="plotly_dark")
            fig_corr.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_corr, use_container_width=True)

    with tab_cluster:
        st.markdown("### 🌀 Interactive K-Means Clustering Studio")
        
        col_c1, col_c2 = st.columns([1, 2])
        with col_c1:
            k_val = st.slider("Select Number of Clusters (K):", 2, 6, 4, key="mat_k")
            use_scaling = st.toggle("Enable StandardScaler (Z-Score Normalization)", value=True, key="mat_scale")
            x_axis = st.selectbox("Plot X-Axis:", feature_cols, index=0, key="mat_plot_x")
            y_axis = st.selectbox("Plot Y-Axis:", feature_cols, index=1, key="mat_plot_y")
            
        X = df[feature_cols].values
        if use_scaling:
            scaler = StandardScaler()
            X_proc = scaler.fit_transform(X)
        else:
            X_proc = X
            
        kmeans = KMeans(n_clusters=k_val, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(X_proc)
        df["Cluster_Label"] = [f"Cluster {c}" for c in df["Cluster"]]
        
        with col_c2:
            fig_cluster = px.scatter(
                df, x=x_axis, y=y_axis, color="Cluster_Label",
                hover_name="Material",
                hover_data=["Family", "Density", "Tensile_MPa", "Hardness_HV", "Thermal_Cond"],
                title=f"K-Means Clustering (K={k_val}, Scaled={use_scaling})",
                template="plotly_dark",
                size_max=12
            )
            fig_cluster.update_traces(marker=dict(size=12, line=dict(width=1, color='white')))
            fig_cluster.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_cluster, use_container_width=True)
            
        st.markdown("#### 📊 Cluster Profiles (Mean Property Values per Cluster)")
        summary_table = df.groupby("Cluster_Label")[feature_cols].mean().round(2)
        st.dataframe(summary_table, use_container_width=True)

    with tab_pca:
        st.markdown("### 🌌 Principal Component Analysis (PCA) Projection")
        st.write("Reduce 5-dimensional material property space down to 2 principal axes:")
        
        X_scaled = StandardScaler().fit_transform(df[feature_cols].values)
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        
        df["PC1"] = X_pca[:, 0]
        df["PC2"] = X_pca[:, 1]
        
        explained_var = pca.explained_variance_ratio_ * 100
        
        fig_pca = px.scatter(
            df, x="PC1", y="PC2", color="Cluster_Label", symbol="Family",
            hover_name="Material",
            title=f"PCA 2D Projection (Explains {explained_var[0]:.1f}% + {explained_var[1]:.1f}% = {sum(explained_var):.1f}% of Total Variance)",
            template="plotly_dark"
        )
        fig_pca.update_traces(marker=dict(size=14))
        fig_pca.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
        st.plotly_chart(fig_pca, use_container_width=True)
        
        st.success(f"✅ **PCA Interpretation:** PC1 captures structural stiffness and hardness vs lightness. Notice how Polymers, Light Metals, Steels, and Ceramics naturally separate into distinct spatial quadrants!")

    with tab_theory:
        st.markdown("""
        ### 📐 Mathematical Formulation: K-Means & Lloyd's Algorithm
        
        The objective of K-Means is to partition $n$ observations into $K$ clusters $S = \\{S_1, S_2, ..., S_K\\}$ to minimize the Within-Cluster Sum of Squares (Inertia):
        
        $$\\arg\\min_S \\sum_{i=1}^K \\sum_{x \\in S_i} \\| x - \\mu_i \\|^2$$
        
        Where $\\mu_i$ is the centroid (mean coordinates) of cluster $S_i$.
        
        **The Iteration Cycle:**
        1. **Assignment Step:** Assign each observation to the cluster whose centroid is closest by Euclidean distance:
           $$S_i^{(t)} = \\{ x_p : \\| x_p - m_i^{(t)} \\|^2 \\le \\| x_p - m_j^{(t)} \\|^2 \\; \\forall j \\}$$
        2. **Update Step:** Calculate the new centroids as the mean of all assigned vectors:
           $$m_i^{(t+1)} = \\frac{1}{|S_i^{(t)}|} \\sum_{x_j \\in S_i^{(t)}} x_j$$
        """)

# -------------------------------------------------------------
# 3. LAB C: FAULTY CIRCUIT DETECTION (NEURAL NETWORK)
# -------------------------------------------------------------
@st.cache_data
def load_circuit_dataset(n_samples=500, random_state=42):
    """
    Simulates integrated circuit (IC) automated test equipment (ATE) test vectors.
    Features:
    - Test_Voltage_V1 (Nominal 3.3V)
    - Clock_Frequency_MHz (Nominal 100MHz)
    - Leakage_Current_uA (Low in good chips, spikes in defective chips)
    - Signal_Jitter_ps (Clock uncertainty)
    - Supply_Noise_mV (Power rail ripple)
    - Operating_Temp_C
    Target: Defective (0: Pass/Nominal, 1: Fail/Defective)
    """
    np.random.seed(random_state)
    
    # 80% good chips, 20% defective chips (realistic semiconductor yield test)
    n_good = int(n_samples * 0.8)
    n_bad = n_samples - n_good
    
    # Good chip distributions
    v1_good = np.random.normal(3.30, 0.05, n_good)
    clk_good = np.random.normal(100.0, 1.2, n_good)
    leak_good = np.random.exponential(1.8, n_good) + 0.5
    jitter_good = np.random.normal(18.0, 3.5, n_good)
    noise_good = np.random.normal(12.0, 2.5, n_good)
    temp_good = np.random.normal(45.0, 8.0, n_good)
    
    # Defective chip distributions (manufacturing flaws, gate oxide breakdown, delay faults)
    v1_bad = np.concatenate([np.random.normal(3.05, 0.1, n_bad//2), np.random.normal(3.55, 0.1, n_bad - n_bad//2)])
    clk_bad = np.random.normal(94.0, 5.0, n_bad)
    leak_bad = np.random.exponential(14.0, n_bad) + 6.0  # Excessive leakage
    jitter_bad = np.random.normal(48.0, 12.0, n_bad)     # Excessive jitter
    noise_bad = np.random.normal(28.0, 7.0, n_bad)
    temp_bad = np.random.normal(68.0, 12.0, n_bad)       # Overheating
    
    v1 = np.concatenate([v1_good, v1_bad])
    clk = np.concatenate([clk_good, clk_bad])
    leak = np.concatenate([leak_good, leak_bad])
    jitter = np.concatenate([jitter_good, jitter_bad])
    noise = np.concatenate([noise_good, noise_bad])
    temp = np.concatenate([temp_good, temp_bad])
    label = np.concatenate([np.zeros(n_good, dtype=int), np.ones(n_bad, dtype=int)])
    
    # Shuffle
    indices = np.random.permutation(n_samples)
    df = pd.DataFrame({
        "Voltage_V": np.round(v1[indices], 3),
        "Clock_Freq_MHz": np.round(clk[indices], 2),
        "Leakage_uA": np.round(leak[indices], 2),
        "Signal_Jitter_ps": np.round(jitter[indices], 1),
        "Supply_Noise_mV": np.round(noise[indices], 1),
        "Die_Temp_C": np.round(temp[indices], 1),
        "Defective": label[indices]
    })
    return df

def render_circuit_detection_lab():
    st.markdown("""
    <div style="background: rgba(239, 68, 68, 0.08); border-left: 4px solid #EF4444; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h2 style="color: #F8F7FF; margin: 0 0 8px 0;">⚡ Laboratory 3: Faulty Circuit Detection with Neural Networks</h2>
        <div style="color: #FECACA; font-size: 0.95rem;">
            <b>Semiconductor Quality Objective:</b> Train an Artificial Neural Network (Multilayer Perceptron) to classify integrated circuits 
            as <i>Nominal (Pass)</i> or <i>Defective (Fail)</i> based on automated electrical test measurements.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    df = load_circuit_dataset()
    features = ["Voltage_V", "Clock_Freq_MHz", "Leakage_uA", "Signal_Jitter_ps", "Supply_Noise_mV", "Die_Temp_C"]
    
    tab_data, tab_nn, tab_costs, tab_theory = st.tabs([
        "📋 1. Test Vector Telemetry", 
        "🧠 2. Neural Network Architecture & Training", 
        "⚠️ 3. Engineering Cost Matrix (False Negatives)", 
        "🔬 4. Backpropagation & Activation"
    ])
    
    with tab_data:
        st.markdown("### 💽 Automated Test Equipment (ATE) Output")
        st.dataframe(df.head(10), use_container_width=True)
        
        c1, c2 = st.columns(2)
        with c1:
            fig_leak = px.box(df, x="Defective", y="Leakage_uA", color="Defective", 
                              title="Leakage Current Distribution (0=Good, 1=Bad)", template="plotly_dark")
            fig_leak.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_leak, use_container_width=True)
        with c2:
            fig_jit = px.scatter(df, x="Signal_Jitter_ps", y="Clock_Freq_MHz", color="Defective", 
                                 title="Signal Jitter vs Clock Frequency", template="plotly_dark")
            fig_jit.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_jit, use_container_width=True)

    with tab_nn:
        st.markdown("### 🧠 MLP Neural Network Hyperparameters")
        
        col_h1, col_h2, col_h3 = st.columns(3)
        with col_h1:
            hidden_units = st.selectbox("Hidden Layer Architecture:", 
                                        [(16,), (32, 16), (64, 32, 16)], 
                                        index=1, 
                                        format_func=lambda x: f"{len(x)} Hidden Layer(s): {x} Neurons",
                                        key="nn_arch")
        with col_h2:
            activation = st.selectbox("Activation Function:", ["relu", "tanh", "logistic"], index=0, key="nn_act")
        with col_h3:
            max_iter = st.slider("Training Epochs / Iterations:", 50, 400, 200, 50, key="nn_iter")
            
        X = df[features].values
        y = df["Defective"].values
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train MLPClassifier
        mlp = MLPClassifier(hidden_layer_sizes=hidden_units, activation=activation, max_iter=max_iter, random_state=42)
        mlp.fit(X_train_scaled, y_train)
        
        y_pred = mlp.predict(X_test_scaled)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Accuracy", f"{acc*100:.1f}%")
        m2.metric("Precision", f"{prec*100:.1f}%")
        m3.metric("Recall (Sensitivity)", f"{rec*100:.1f}%")
        m4.metric("F1 Score", f"{f1:.3f}")
        
        col_cm1, col_cm2 = st.columns(2)
        with col_cm1:
            cm = confusion_matrix(y_test, y_pred)
            cm_df = pd.DataFrame(cm, index=["Actual Nominal (0)", "Actual Defective (1)"], 
                                 columns=["Pred Nominal (0)", "Pred Defective (1)"])
            fig_cm = px.imshow(cm_df, text_auto=True, color_continuous_scale="Reds", 
                               title="Confusion Matrix (Evaluation on Unseen Test Chips)", template="plotly_dark")
            fig_cm.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_cm, use_container_width=True)
            
        with col_cm2:
            st.markdown("#### 📉 Neural Network Loss Convergence Curve")
            fig_loss = px.line(mlp.loss_curve_, title="Loss Curve vs Iteration", template="plotly_dark")
            fig_loss.update_layout(xaxis_title="Epoch", yaxis_title="Cross-Entropy Loss", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_loss, use_container_width=True)

    with tab_costs:
        st.markdown("### ⚠️ Asymmetric Engineering Risk Analysis")
        st.markdown("""
        In consumer apps, a false positive has similar cost to a false negative. 
        **In aerospace, medical, and automotive engineering, the costs are drastically asymmetric!**
        """)
        
        cost_fp = st.number_input("Cost of False Positive (Discarding or re-testing a good chip):", value=5.0, step=1.0)
        cost_fn = st.number_input("Cost of False Negative (Shipping a defective chip into a flight control system):", value=50000.0, step=1000.0)
        
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        total_risk = (fp * cost_fp) + (fn * cost_fn)
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.metric("Total Test Batch Cost Liability", f"${total_risk:,.2f}")
            st.write(f"- False Positives ({fp} chips) cost: **${fp * cost_fp:,.2f}**")
            st.write(f"- False Negatives ({fn} chips) cost: **${fn * cost_fn:,.2f}**")
        with col_r2:
            if fn > 0:
                st.error(f"🚨 **Safety Alert:** The model missed {fn} defective chips. In high-reliability engineering, threshold tuning must prioritize **Recall = 100%** over pure accuracy!")
            else:
                st.success("✅ **Zero Escapes:** The neural network detected 100% of defective circuits in the test sample!")

    with tab_theory:
        st.markdown("""
        ### 📐 Artificial Neuron Mathematics & Backpropagation
        
        An artificial neuron calculates a weighted sum of inputs followed by a non-linear activation:
        
        $$z = \\sum_{j=1}^m w_j x_j + b = \\mathbf{w}^T \\mathbf{x} + b$$
        $$a = \\sigma(z)$$
        
        **Why Non-Linearity Matters:**
        Without non-linear activations (like ReLU: $f(x) = \\max(0, x)$), stacking multiple layers reduces to a single linear matrix multiplication:
        
        $$W_2 (W_1 X + b_1) + b_2 = (W_2 W_1) X + (W_2 b_1 + b_2) = W' X + b'$$
        
        Non-linear activations allow Multilayer Perceptrons to approximate any continuous function, creating curved, complex decision boundaries capable of separating defective from nominal silicon test vectors!
        """)

# -------------------------------------------------------------
# 4. INTERACTIVE PLAYGROUND: DBSCAN DENSITY EXPLORER
# -------------------------------------------------------------
def render_dbscan_playground():
    st.markdown("""
    <div style="background: rgba(56, 189, 248, 0.08); border-left: 4px solid #38BDF8; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h3 style="color: #F8F7FF; margin: 0 0 8px 0;">🌀 DBSCAN Density-Based Spatial Clustering Explorer</h3>
        <div style="color: #BAE6FD; font-size: 0.95rem;">
            DBSCAN clusters points based on local density and does not assume spherical clusters like K-Means. 
            Points in low-density regions are identified as <b>noise / mechanical anomalies</b>!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        eps = st.slider("Epsilon (Neighborhood Radius ε):", 0.1, 1.5, 0.35, 0.05, key="dbscan_eps")
        min_samples = st.slider("MinSamples (Minimum Core Points):", 2, 15, 5, 1, key="dbscan_min")
        pattern = st.selectbox("Synthetic Dataset Topology:", ["Concentric Rings (Bearings)", "Interlocking Moons", "Vibration Clusters + Noise"], key="dbscan_pat")
        
    np.random.seed(42)
    n_pts = 300
    if pattern == "Concentric Rings (Bearings)":
        r1 = np.random.normal(1.0, 0.08, n_pts//2)
        th1 = np.random.uniform(0, 2*np.pi, n_pts//2)
        r2 = np.random.normal(2.2, 0.10, n_pts//2)
        th2 = np.random.uniform(0, 2*np.pi, n_pts//2)
        X = np.vstack([
            np.column_stack([r1 * np.cos(th1), r1 * np.sin(th1)]),
            np.column_stack([r2 * np.cos(th2), r2 * np.sin(th2)])
        ])
    elif pattern == "Interlocking Moons":
        t = np.linspace(0, np.pi, n_pts//2)
        X1 = np.column_stack([np.cos(t), np.sin(t)]) + np.random.normal(0, 0.06, (n_pts//2, 2))
        X2 = np.column_stack([1 - np.cos(t), 1 - np.sin(t) - 0.5]) + np.random.normal(0, 0.06, (n_pts//2, 2))
        X = np.vstack([X1, X2])
    else:
        # Clusters with random outliers
        c1 = np.random.normal([2, 2], 0.35, (n_pts//3, 2))
        c2 = np.random.normal([-1.5, 1.5], 0.35, (n_pts//3, 2))
        noise = np.random.uniform(-3, 3, (n_pts//3, 2))
        X = np.vstack([c1, c2, noise])
        
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
    labels = db.labels_
    
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)
    
    with col2:
        df_db = pd.DataFrame(X, columns=["X1", "X2"])
        df_db["Cluster"] = ["Noise (Anomaly)" if l == -1 else f"Cluster {l}" for l in labels]
        
        fig_db = px.scatter(df_db, x="X1", y="X2", color="Cluster", 
                            title=f"DBSCAN Result: {n_clusters_} Clusters Discovered | {n_noise_} Noise Points",
                            template="plotly_dark",
                            color_discrete_map={"Noise (Anomaly)": "#64748B"})
        fig_db.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
        st.plotly_chart(fig_db, use_container_width=True)

# -------------------------------------------------------------
# 5. INTERACTIVE PLAYGROUND: CNN 2D FILTER CONVOLUTION
# -------------------------------------------------------------
def render_cnn_filter_visualizer():
    st.markdown("""
    <div style="background: rgba(245, 158, 11, 0.08); border-left: 4px solid #F59E0B; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h3 style="color: #F8F7FF; margin: 0 0 8px 0;">👁️ Convolutional Neural Network (CNN) 2D Filter Visualizer</h3>
        <div style="color: #FDE68A; font-size: 0.95rem;">
            Watch how a discrete 2D spatial convolution filter extracts low-level features (edges, horizontal lines, corners) 
            from an input image matrix to generate a <b>Feature Map</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        kernel_type = st.selectbox("Select 3x3 Convolution Kernel:", 
                                   ["Vertical Edge Detector (Sobel-X)", "Horizontal Edge Detector (Sobel-Y)", "Ridge / Laplacian", "Sharpen", "Box Blur"],
                                   key="cnn_kern_sel")
        
        if kernel_type == "Vertical Edge Detector (Sobel-X)":
            K = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        elif kernel_type == "Horizontal Edge Detector (Sobel-Y)":
            K = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        elif kernel_type == "Ridge / Laplacian":
            K = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        elif kernel_type == "Sharpen":
            K = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        else:
            K = np.ones((3, 3)) / 9.0
            
        st.markdown("**Kernel Weights:**")
        st.write(pd.DataFrame(K).round(2))
        
    # Create synthetic 8x8 input image with a diagonal edge
    img = np.zeros((8, 8))
    img[:, 4:] = 1.0  # Vertical step boundary
    img[2:6, 2:6] = 0.8
    
    # Valid convolution output: size (8 - 3 + 1) = 6x6
    output = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            receptive_field = img[i:i+3, j:j+3]
            output[i, j] = np.sum(receptive_field * K)
            
    with col2:
        c_i1, c_i2 = st.columns(2)
        with c_i1:
            fig_in = px.imshow(img, text_auto=".1f", color_continuous_scale="gray", title="Input Image (8x8 Pixels)", template="plotly_dark")
            fig_in.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_in, use_container_width=True)
        with c_i2:
            fig_out = px.imshow(output, text_auto=".1f", color_continuous_scale="Viridis", title="Feature Map Output (6x6 Activation)", template="plotly_dark")
            fig_out.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
            st.plotly_chart(fig_out, use_container_width=True)
            
    st.info(f"💡 **Spatial Arithmetic:** Output Dimension = $\\frac{{W - K + 2P}}{{S}} + 1 = \\frac{{8 - 3 + 0}}{{1}} + 1 = 6$. Convolution is translation-invariant!")

# -------------------------------------------------------------
# 6. INTERACTIVE PLAYGROUND: TIME-SERIES FORECASTING
# -------------------------------------------------------------
def render_timeseries_forecasting_lab():
    st.markdown("""
    <div style="background: rgba(168, 85, 247, 0.08); border-left: 4px solid #A855F7; padding: 18px 24px; border-radius: 8px; margin-bottom: 24px;">
        <h3 style="color: #F8F7FF; margin: 0 0 8px 0;">📈 Time-Series Intelligence & Forecasting Laboratory</h3>
        <div style="color: #E9D5FF; font-size: 0.95rem;">
            Explore sequential telemetry (industrial electricity demand and turbine vibration). 
            Learn why random train/test splitting causes catastrophic future data leakage and evaluate autoregressive lag forecasting!
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate 180 days of hourly electricity demand telemetry
    np.random.seed(42)
    n_hours = 24 * 60  # 60 days
    time_idx = pd.date_range("2026-01-01", periods=n_hours, freq="h")
    
    # Physics trend + 24-hour diurnal cycle + weekly cycle + noise
    trend = np.linspace(50, 85, n_hours)
    daily_cycle = 25 * np.sin(2 * np.pi * time_idx.hour / 24)
    weekly_cycle = 12 * (time_idx.dayofweek < 5).astype(float) # Weekday industrial factory load
    noise = np.random.normal(0, 4, n_hours)
    demand = trend + daily_cycle + weekly_cycle + noise
    
    df_ts = pd.DataFrame({"Timestamp": time_idx, "Demand_MW": np.round(demand, 2)})
    df_ts["Hour"] = df_ts["Timestamp"].dt.hour
    df_ts["DayOfWeek"] = df_ts["Timestamp"].dt.dayofweek
    df_ts["Lag_1h"] = df_ts["Demand_MW"].shift(1)
    df_ts["Lag_24h"] = df_ts["Demand_MW"].shift(24)
    df_ts = df_ts.dropna()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("#### ⏳ Chronological Splitting (No Leakage)")
        train_split = st.slider("Historical Training Days:", 20, 50, 45, 1, key="ts_split")
        cutoff = df_ts["Timestamp"].min() + pd.Timedelta(days=train_split)
        
        model_type = st.selectbox("Forecasting Algorithm:", 
                                  ["Lag-Autoregression (Ridge)", "24h Naive Persistence Baseline", "Moving Average (7-Day Rolling)"],
                                  key="ts_algo")
                                  
    train_df = df_ts[df_ts["Timestamp"] < cutoff]
    test_df = df_ts[df_ts["Timestamp"] >= cutoff]
    
    if model_type == "Lag-Autoregression (Ridge)":
        X_tr = train_df[["Hour", "DayOfWeek", "Lag_1h", "Lag_24h"]]
        y_tr = train_df["Demand_MW"]
        X_te = test_df[["Hour", "DayOfWeek", "Lag_1h", "Lag_24h"]]
        y_te = test_df["Demand_MW"]
        
        reg = Ridge().fit(X_tr, y_tr)
        preds = reg.predict(X_te)
    elif model_type == "24h Naive Persistence Baseline":
        preds = test_df["Lag_24h"].values
        y_te = test_df["Demand_MW"]
    else:
        # Moving average
        rolling_mean = train_df["Demand_MW"].iloc[-24:].mean()
        preds = np.full(len(test_df), rolling_mean)
        y_te = test_df["Demand_MW"]
        
    mae = mean_absolute_error(y_te, preds)
    rmse = np.sqrt(mean_squared_error(y_te, preds))
    
    with col2:
        m1, m2 = st.columns(2)
        m1.metric("Forecast MAE", f"{mae:.2f} MW")
        m2.metric("Forecast RMSE", f"{rmse:.2f} MW")
        
        fig_ts = go.Figure()
        fig_ts.add_trace(go.Scatter(x=train_df["Timestamp"].iloc[-168:], y=train_df["Demand_MW"].iloc[-168:], mode='lines', name='Historical Training (Past 7 Days)', line=dict(color='#64748B')))
        fig_ts.add_trace(go.Scatter(x=test_df["Timestamp"], y=y_te, mode='lines', name='Actual Future Test Data', line=dict(color='#38BDF8')))
        fig_ts.add_trace(go.Scatter(x=test_df["Timestamp"], y=preds, mode='lines', name='Model Forecast Horizon', line=dict(color='#F43F5E', dash='dash')))
        fig_ts.update_layout(title="Time-Series Forecast Horizon vs Actual Telemetry", xaxis_title="Timestamp", yaxis_title="Grid Power Demand (MW)", template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0.2)")
        st.plotly_chart(fig_ts, use_container_width=True)
