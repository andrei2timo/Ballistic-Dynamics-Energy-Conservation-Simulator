# ☄️ Computational Ballistics & Thermodynamics Laboratory

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Physics Engine](https://img.shields.io/badge/Engine-Kinematic_Euler-red)
![Mathematical Model](https://img.shields.io/badge/Model-Parabolic_Trajectories-green)

## 📌 Project Architecture
This repository hosts a sophisticated **Computational Physics** environment designed to simulate and analyze the motion of a mass point in a uniform gravitational field. Unlike basic animations, this tool employs **vectorized numerical integration** via NumPy to handle complex motion datasets.



## 🧬 Scientific & Mathematical Framework
The simulation strictly adheres to the principles of **Classical Mechanics**. The application transition between different coordinate systems to validate the motion:

* **Kinematic State Vectors**: The system tracks the state vector $S = [x, y, v_x, v_y]$ at every time step $\Delta t$.
* **The Trajectory Parabola**: Explicit implementation of the time-independent Cartesian equation:
  $$y(x) = x \tan(\alpha) - \frac{g}{2v_0^2 \cos^2(\alpha)} x^2$$
* **Work-Energy Theorem**: Verification of the Mechanical Energy Conservation Law:
  $$\Delta E = E_{k(f)} + E_{p(f)} - (E_{k(i)} + E_{p(i)}) = 0$$



## 🛠️ Computational Features
* **Adaptive Sampling**: Utilizing a dynamic `linspace` algorithm to generate up to 500 data points, ensuring a continuous curve without aliasing artifacts.
* **Deterministic Synchronization**: Zero-flicker rendering using unique session-state keys and Streamlit `empty` containers.
* **Data Persistence**: Automated serialization of physics data into structured DataFrames, allowing for CSV telemetry export.

## 🚀 Technical Installation
1. Clone the repository:
   ```
   git clone [https://github.com/your-repo/ballistic-lab.git](https://github.com/your-repo/ballistic-lab.git)
   ```
2. Initialize the environment:
   ```
   pip install -r requirements.txt
   ```
3. Execute the simulation:
   ```
   streamlit run app.py
   ```
   
