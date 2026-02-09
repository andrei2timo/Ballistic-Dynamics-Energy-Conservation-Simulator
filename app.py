import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

st.set_page_config(page_title="Analiză Balistică Ultra-Smooth", layout="wide")

st.title("🚀 Simulator Fizic: Traiectorie Fluidă și Energie")

# --- SECȚIUNE ECUAȚII (Fixă, nu flicărește) ---
with st.expander("📚 Fundament Teoretic (Ecuațiile Mișcării)", expanded=False):
    st.latex(r"x(t) = v_0 \cdot \cos(\alpha) \cdot t")
    st.latex(r"y(t) = v_0 \cdot \sin(\alpha) \cdot t - \frac{g \cdot t^2}{2}")
    st.latex(r"E_c = \frac{m \cdot v^2}{2}, \quad E_p = m \cdot g \cdot h")
    st.latex(r"H_{max} = \frac{v_0^2 \cdot \sin^2(\alpha)}{2g}")

st.markdown("---")

# --- SIDEBAR ---
st.sidebar.header("⚙️ Setări Experiment")
v0 = st.sidebar.slider("Viteza inițială (v₀) [m/s]", 1.0, 150.0, 50.0, step=1.0)
alfa = st.sidebar.slider("Unghi de lansare (α) [grade]", 0.0, 90.0, 45.0, step=0.5)
masa = st.sidebar.number_input("Masa obiectului (m) [kg]", value=1.0, min_value=0.1)
viteza_sim = st.sidebar.slider("Finețea animației", 0.1, 1.0, 0.7)
g = 9.81

# Inițializăm containerele în afara buclei pentru stabilitate
col_st, col_dr = st.columns([1.5, 1])
with col_st:
    placeholder_traiectorie = st.empty()
with col_dr:
    placeholder_energie = st.empty()

placeholder_metrics = st.empty()

if st.sidebar.button("🚀 Lansează Proiectilul"):
    rad = np.radians(alfa)
    t_zbor = (2 * v0 * np.sin(rad)) / g
    distanta_max = (v0**2 * np.sin(2*rad)) / g
    inaltime_max = (v0**2 * (np.sin(rad)**2)) / (2*g)

    nr_puncte = 200 # Redus ușor pentru viteza de randare a browserului
    t_puncte = np.linspace(0, t_zbor, num=nr_puncte)
    
    istoric_date = []
    pas_afisare = max(1, int(10 * (1.1 - viteza_sim)))

    for i in range(0, len(t_puncte), pas_afisare):
        t_segment = t_puncte[:i+1]
        t_crt = t_puncte[i]
        
        # Calcule
        x_seg = v0 * np.cos(rad) * t_segment
        y_seg = np.maximum(0, v0 * np.sin(rad) * t_segment - 0.5 * g * t_segment**2)
        
        curr_x, curr_y = x_seg[-1], y_seg[-1]
        vx, vy = v0 * np.cos(rad), v0 * np.sin(rad) - g * t_crt
        v_inst = np.sqrt(vx**2 + vy**2)
        
        Ec, Ep = 0.5 * masa * v_inst**2, masa * g * curr_y
        Etot = Ec + Ep

        istoric_date.append({
            "Timp (s)": t_crt, "X (m)": curr_x, "Y (m)": curr_y,
            "Ec (J)": Ec, "Ep (J)": Ep
        })

        # --- FIGURA 1: TRAIECTORIE ---
        fig_traj = go.Figure()
        fig_traj.add_trace(go.Scatter(
            x=x_seg, y=y_seg, mode='lines', 
            line=dict(color='cyan', width=3, dash='dot')
        ))
        fig_traj.add_trace(go.Scatter(
            x=[curr_x], y=[curr_y], mode='markers',
            marker=dict(color='red', size=14, line=dict(width=2, color='white'))
        ))
        fig_traj.update_layout(
            xaxis=dict(range=[0, distanta_max * 1.05], title="Distanță (m)", fixedrange=True),
            yaxis=dict(range=[0, inaltime_max * 1.15], title="Înălțime (m)", fixedrange=True),
            template="plotly_dark", height=400, showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10)
        )

        # --- FIGURA 2: ENERGIE ---
        fig_en = go.Figure()
        df_tmp = pd.DataFrame(istoric_date)
        fig_en.add_trace(go.Scatter(x=df_tmp["Timp (s)"], y=df_tmp["Ec (J)"], name="Ec", line=dict(color='orange', width=3)))
        fig_en.add_trace(go.Scatter(x=df_tmp["Timp (s)"], y=df_tmp["Ep (J)"], name="Ep", line=dict(color='green', width=3)))
        
        fig_en.update_layout(
            xaxis=dict(range=[0, t_zbor], title="Timp (s)", fixedrange=True),
            yaxis=dict(range=[0, Etot * 1.1], title="Energie (J)", fixedrange=True),
            template="plotly_dark", height=400, showlegend=True,
            legend=dict(orientation="h", y=-0.2), margin=dict(l=10, r=10, t=10, b=10)
        )

        # Actualizare fără flickering (re-folosind placeholder-ul stabilit)
        placeholder_traiectorie.plotly_chart(fig_traj, use_container_width=True, config={'displayModeBar': False}, key=f"traj_{i}")
        placeholder_energie.plotly_chart(fig_en, use_container_width=True, config={'displayModeBar': False}, key=f"en_{i}")

        with placeholder_metrics.container():
            m1, m2, m3 = st.columns(3)
            m1.metric("H Max Atins", f"{inaltime_max:.2f} m")
            m2.metric("Viteză Instantanee", f"{v_inst:.2f} m/s")
            m3.metric("Energia Totală", f"{Etot:.1f} J")

        # Mică pauză adaptată
        time.sleep(0.01)

    # Tabel final de date
    st.markdown("---")
    st.subheader("📊 Analiză Tabelară")
    st.dataframe(pd.DataFrame(istoric_date), use_container_width=True)
else:
    st.info("Apasă butonul de lansare pentru a începe simularea.")