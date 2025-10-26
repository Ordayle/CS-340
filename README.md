# CS-340

## Overview
This repository contains my final dashboard code (Project Two) and the Python CRUD module (Project One) that powers the dashboard’s database operations. The Word version of my README responses is included as  in the repository root.

## How to Run the Dashboard
1. Ensure MongoDB is running locally and that the `AAC` database and `animals` collection are available.
2. Install Python dependencies:
   ```bash
   pip install pymongo dash dash-leaflet plotly pandas
   ```
3. Update the connection details in the CRUD module or environment variables as needed (host, port, database, collection, username, password if required).
4. Launch the dashboard script (Jupyter or Python). If using Jupyter, run the notebook cells. If using a Python script, run:
   ```bash
   python app.py
   ```
5. Open the app in a browser at the URL shown in the console (often http://127.0.0.1:8050).

---

## Portfolio Reflection

### 1) Writing maintainable, readable, and adaptable programs
I treated maintainability and readability as first-class requirements. I separated concerns by placing database logic in a dedicated **CRUD Python module** and user-facing logic in the **dashboard app**. Clear function names, docstrings, and type hints make code intent obvious, and small, single‑purpose functions keep changes localized. Adaptability came from parameterizing the MongoDB connection, encapsulating queries behind a clean interface, and using data-driven filters in the dashboard so that new rescue criteria or breeds can be added without redesigning the UI. Reusing the CRUD module from Project One to power Project Two’s widgets reduced duplication and improved testability. In future work, the same module could be imported by different applications (CLI tools, background jobs, or additional dashboards) without modification.

### 2) My approach to problem solving as a computer scientist
I followed an iterative, test‑early approach. I first clarified functional requirements (filters, maps, tables, and visualizations) and the non‑functional goals (usability, responsiveness, and correctness). I then designed the data boundaries: the CRUD layer handles validation and querying while the dashboard reacts to user input and renders results. I tested the connection and simple queries before building interactivity, which prevented UI bugs from masking data issues. Compared to earlier coursework, I relied more heavily on modular design and instrumentation—logging, small integration tests, and sample queries—so issues were reproducible and quick to isolate. Going forward, I would standardize configuration via environment variables, add automated tests for common queries, and include seed scripts to bootstrap new environments consistently.

### 3) What computer scientists do and why it matters
Computer scientists translate real‑world goals into reliable, measurable systems. For a client like **Grazioso Salvare**, that means turning rescue criteria into precise queries, surfacing insights with clear visualizations, and ensuring the path from data to decision is trustworthy. The dashboard helps coordinators find adoptable candidates faster, reduce manual search time, and track trends in outcomes. Even small improvements in query accuracy or UI clarity can lead to better placements and more lives saved. This work demonstrates how thoughtful data modeling, clean interfaces, and maintainable code directly support organizational missions.
