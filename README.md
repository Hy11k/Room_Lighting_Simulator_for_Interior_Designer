Room Lighting Simulator for Interior Designers
About the Project

This project started from a very practical problem.

As an interior designer and 3D visualizer, I often faced the same situation:
after rendering a scene, the client says — “It feels too dark.”

Instead of adjusting lights randomly inside 3Ds Max or Unreal Engine, I wanted a way to calculate lighting properly before building the full render setup.

So I built this simulator.

Room Lighting Simulator is a Python-based tool that calculates how much light a room actually needs based on real lighting standards. It helps designers make technical decisions before moving to the creative stage.

What It Does

The program calculates:

Total required lumens for the room

Number of light fixtures needed

Balanced grid placement of lights

2D top-view visualization of the layout

This allows you to start your 3D scene with realistic and mathematically correct lighting values instead of guessing.

How It Works

The simulator uses a simple but professional lighting formula:

Required Lumens = Area × Lux Standard / Reflection Factor

Where:

Area = Length × Width

Lux depends on room type (bedroom, living room, office)

Reflection factor represents wall reflectivity (0–1)

By adjusting these parameters, you can simulate different lighting conditions and room materials.

Project Structure

The program is written in Python using Object-Oriented Programming principles.

Main components:

Room class

Stores room dimensions

Calculates area

Applies lux standards

Calculates total required lumens

Light class

Defines light temperature (3000K / 4000K / 6000K)

Stores lumen output per fixture

Calculates quantity needed

Generates grid placement coordinates

Features

Input validation

Automatic lumen calculation

Automatic light quantity calculation

Balanced grid layout generation

2D visualization using matplotlib

Optional PNG export

Why I Built This

Lighting is one of the most important parts of interior visualization.

It affects:

Mood

Realism

Client perception

Render time

Instead of spending hours adjusting light intensity inside a render engine, I wanted a fast way to define technically correct lighting from the beginning.

This tool connects engineering logic with creative workflow.

Technologies Used

Python 3

matplotlib

Mathematical modeling

Object-Oriented Programming

Future Plans

GUI version (Tkinter or PyQt)

Web version (Flask or Streamlit)

Integration with 3D software workflows

Support for photometric IES profiles