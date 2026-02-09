# ☄️ Ballistic Dynamics & Energy Conservation Simulator

An advanced physics engine and visualization tool developed for **Mathematics and Informatics** students. 

## 🎯 Project Overview
This simulator calculates the flight of a particle in a uniform gravitational field, providing live feedback on the interchange between kinetic and potential energy.

### Key Features:
* **Anti-Flicker Rendering**: Optimized Streamlit placeholders for stable 60fps-like updates.
* **Energy Analysis**: Dynamic tracking of $E_k$ and $E_p$ proving the Law of Conservation of Energy.
* **LaTeX Integration**: Full mathematical derivation included in the UI.



## 🧬 Physics Basis
1. **Displacement**: $y(x) = x \tan(\alpha) - \frac{g}{2v_0^2 \cos^2(\alpha)} x^2$
2. **Conservation**: $E_{total} = \frac{1}{2}mv^2 + mgh = \text{Constant}$



## 🛠️ Setup
1. `pip install -r requirements.txt`
2. `streamlit run app.py`
