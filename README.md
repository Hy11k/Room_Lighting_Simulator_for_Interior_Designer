🏗 Room Lighting Simulator for Interior Designers
📌 Project Overview

Room Lighting Simulator is a Python-based engineering tool designed for interior designers and 3D visualizers who want to pre-calculate lighting requirements before rendering in software like 3Ds Max, Revit, or Unreal Engine.

Instead of manually adjusting lighting in a render scene, this tool calculates:

Required total lumens

Number of light fixtures needed

Optimal grid placement of lights

2D visualization of the lighting layout

It helps designers make data-driven lighting decisions based on real-world lighting standards (Lux values).

🎯 What Problem It Solves

Clients often say:

“The room looks too dark.”

Before modifying the full 3D render setup, this simulator allows designers to:

Calculate scientifically accurate lighting levels

Adjust brightness based on room size

Consider wall reflection coefficients

Select light color temperature (3000K / 4000K / 6000K)

Visualize fixture placement in a structured layout

🧮 Lighting Calculation Formula

The program uses a professional interior lighting estimation formula:

Required Lumens = Area × Lux Standard / Reflection Factor

Where:

Area = Length × Width

Lux Standard depends on room type:

Bedroom → 150–300 lux

Living Room → 200–400 lux

Office → 300–500 lux

Reflection Factor = wall reflectivity coefficient (0–1)

🧠 Technical Implementation

The program is built using:

math module

Object-Oriented Programming (OOP)

Input validation

Automatic grid generation algorithm

Data visualization with matplotlib

Core Classes
🔹 Room

Handles:

Room dimensions

Area calculation

Reflection coefficient

Lux standard application

Total required lumens calculation

🔹 Light

Handles:

Light temperature (3000K / 4000K / 6000K)

Lumen output per fixture

Quantity calculation

Grid placement coordinates

⚙️ Features

✔ User input validation
✔ Automatic lumen calculation
✔ Automatic light quantity calculation
✔ Optimal grid layout generation
✔ 2D room lighting visualization
✔ Optional PNG export

📊 Visualization

The program generates a 2D top-view layout using matplotlib:

Room boundaries

Light positions plotted in grid format

Balanced distribution algorithm

Clear visual reference for designers

🚀 Advanced Features (Mid+ Level)

Optional advanced implementations:

Window-based natural light contribution

Shadow zone estimation

Multiple light power options

Cost calculation per fixture

Energy consumption estimation

🎨 Why This Is Useful for Interior Designers

As a 3D visualizer, lighting directly affects:

Mood

Realism

Client perception

Render time efficiency

This tool bridges engineering calculations with creative visualization.

Instead of guessing light intensity in 3D software, you start with mathematically correct lighting values.

🛠 Technologies Used

Python 3

matplotlib

Object-Oriented Programming

Mathematical modeling

📌 Future Improvements

GUI version (Tkinter / PyQt)

Web version (Flask / Streamlit)

Integration with Blender or 3Ds Max export

Photometric IES profile support