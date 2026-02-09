# ☄️ Ballistic Dynamics & Energy Conservation Simulator

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Physics Engine](https://img.shields.io/badge/Engine-Kinematic_Euler-red)
![Mathematical Model](https://img.shields.io/badge/Model-Parabolic_Trajectories-green)

## 📌 Project Architecture
This repository hosts a sophisticated **Computational Physics** environment designed to simulate and analyze the motion of a mass point in a uniform gravitational field. Unlike basic animations, this tool employs **vectorized numerical integration** via NumPy to handle complex motion datasets.

## 🧬 Scientific & Mathematical Framework
The simulation strictly adheres to the principles of **Classical Mechanics**, employing a multi-layered mathematical approach to validate the projectile's behavior:

### I. Kinematic State Evolution
The system propagates the state vector $\mathbf{S}$ through time $t$ using discretized kinematic equations. This represents the temporal evolution of the particle within the 2D Cartesian plane:

$$
\mathbf{S}(t) = \begin{bmatrix} x(t) \\ y(t) \\ v_x(t) \\ v_y(t) \end{bmatrix} = \begin{bmatrix} v_0 \cos(\alpha)t \\ v_0 \sin(\alpha)t - \frac{1}{2}gt^2 \\ v_0 \cos(\alpha) \\ v_0 \sin(\alpha) - gt \end{bmatrix}
$$



### II. Geometric Path (The Trajectory Parabola)
By eliminating the time parameter $t$ from the system, the simulation validates the spatial path via the time-independent Cartesian equation, proving the parabolic nature of the motion:

$$
y(x) = x \tan(\alpha) - \left[ \frac{g}{2v_0^2 \cos^2(\alpha)} \right] x^2
$$

### III. Energetic Consistency (Work-Energy Theorem)
To ensure physical integrity, the engine monitors the Hamiltonian of the system, verifying the **Law of Conservation of Mechanical Energy** at every discrete time step:

$$
E_{total} = \underbrace{\frac{1}{2}m(v_x^2 + v_y^2)}_{E_k} + \underbrace{mgh}_{E_p} \implies \frac{dE}{dt} = 0
$$


---

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

---

## 🔍 Experimental Validation
The simulator provides a comparative analysis between theoretical values and numerical results:
* **Apex Verification**: The simulation cross-references the maximum height $H_{max}$ recorded in the data log with the analytical result $v_y = 0$.
* **Boundary Conditions**: The flight terminates exactly at $y(t) = 0$, validating the quadratic solver's precision.

## 🚧 Project Limitations
* **Fluid Dynamics**: Does not account for the Magnus effect or atmospheric drag.
* **Gravitational Field**: Assumes a constant $g = 9.81 \, m/s^2$ (flat-earth approximation).
---
