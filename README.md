# AI Validation Benchmarks for Urban and Building Simulation

An Open Benchmark Database for Reliable, Reproducible, and Transferable AI Models in the Built Environment
Artificial intelligence and machine learning are increasingly being used as surrogate models, reduced-order models, neural operators, and data-driven prediction tools for urban and building simulations. Applications now include urban wind flow, outdoor and indoor thermal environments, pollutant dispersion, building energy, ventilation, fire and smoke transport, and urban microclimate prediction.
Despite rapid progress in AI-based simulation, the reliability of different models is often difficult to assess because studies use different datasets, geometries, boundary conditions, train–test splits, evaluation metrics, and validation procedures. As a result, reported model accuracy is often not directly comparable across studies, and good interpolation performance does not necessarily imply reliable prediction for new buildings, cities, climates, or physical conditions.
This repository aims to establish an open validation benchmark framework for AI-driven urban and building simulations.
The concept is inspired by established CFD validation benchmark frameworks, particularly the benchmark approach developed by the Architectural Institute of Japan (AIJ), in which standardized geometries, boundary conditions, experimental measurements, and numerical results are used for systematic cross-comparison and model validation.
Here, the same philosophy is extended from conventional CFD validation to AI-based physical simulation.

## 🎯 Objectives

The database is designed to support four major objectives:

**1. Validation**  
Evaluate whether an AI model can accurately reproduce reference experimental or high-fidelity numerical data.

**2. Model Comparison**  
Enable fair comparisons among different machine-learning architectures using identical datasets, boundary conditions, data splits, and evaluation metrics.

**3. Generalization**  
Test whether a model trained under one set of geometries or physical conditions can accurately predict previously unseen configurations.

**4. Transferability**  
Investigate whether AI models developed for one building, urban morphology, climate, or city can be transferred to other environments.

## Validation Benchmark Tests

Each benchmark case should be treated as a complete **validation problem**, rather than simply as a downloadable dataset.

A benchmark case may contain:

| Component | Description |
|---|---|
| **Geometry** | Building, urban district, computational domain, or experimental model |
| **Physical conditions** | Inflow, thermal, source, material, or operating conditions |
| **Reference data** | Wind-tunnel experiments, field measurements, laboratory experiments, or validated high-fidelity simulations |
| **Input variables** | Geometry, boundary conditions, environmental parameters, or physical parameters |
| **Target variables** | Velocity, pressure, temperature, concentration, heat flux, energy use, smoke distribution, etc. |
| **Training dataset** | Cases available for model development |
| **Validation dataset** | Cases available for hyperparameter tuning and model selection |
| **Test dataset** | Hidden or predefined cases used for performance assessment |
| **OOD test** | Conditions outside the training distribution for evaluating model generalization |
| **Metrics** | Standardized quantitative measures for model comparison |
| **Baseline models** | Representative AI/ML models provided for reference |
| **Reference studies** | Publications describing the experiments, simulations, datasets, or benchmark applications |    

## Benchmark Scope

The database is intended to progressively cover the following areas.

| Benchmark Track | Physical Problem | Typical Outputs |
|---|---|---|
| 🌬️ **Urban Wind** | Flow around buildings and urban districts | Velocity, pressure, turbulence |
| 🌡️ **Urban Microclimate** | Urban thermal environment and heat transfer | Air temperature, surface temperature, radiation |
| 🏙️ **Pollutant Dispersion** | Urban contaminant and tracer transport | Concentration, exposure |
| 🏠 **Indoor Environment** | Ventilation, indoor airflow, and indoor environmental quality | Velocity, temperature, contaminant concentration |
| ⚡ **Building Energy** | Building thermal and energy performance | Heating/cooling load, indoor temperature, energy consumption |
| 🧱 **Building Envelope** | Thermal, hygrothermal, aerodynamic, and durability performance of façades, roofs, windows, curtain walls, insulation systems, and other envelope components | Surface temperature, heat flux, moisture content, condensation risk, pressure, deformation, thermal transmittance |
| 🔥 **Fire and Smoke** | Fire-driven flow, flame spread, heat transfer, and smoke transport | Temperature, velocity, heat flux, smoke concentration, species concentration |

## Suggested Benchmark Structure

Each benchmark case should follow a common directory structure:

```text
Benchmarks/
│
├── Urban_Microclimate/
│   ├── <Benchmark_Case_Name>/
│   │   ├── README.md
│   │   ├── Geometry/
│   │   ├── Boundary_Conditions/
│   │   ├── Reference_Data/
│   │   ├── Training_Data/
│   │   ├── Test_Data/
│   │   ├── Baseline_Models/
│   │   └── Evaluation/

## Why Validation Matters

High prediction accuracy on randomly divided training and test datasets is not sufficient to demonstrate that an AI model has learned the underlying physical behavior.

For urban and building applications, an AI model should ideally demonstrate that it can:

- reproduce trusted reference data;
- maintain accuracy under unseen physical conditions;
- generalize to new geometries;
- preserve important physical behavior;
- quantify prediction uncertainty; and
- provide reproducible results across independent studies.

The long-term objective of this project is therefore to move AI-based urban and building simulation from **case-specific prediction** toward **validated, generalizable, and transferable physical modeling**.

---

## Published Studies

Related publications and benchmark applications are collected in:

`Published Papers/`

Researchers are encouraged to contribute publications that use these benchmark datasets for:

- model validation;
- cross-model comparison;
- transfer learning;
- generalization assessment;
- uncertainty quantification; and
- AI-assisted urban and building simulation.

---

## Contributing

Contributions from the **urban physics, building envelope, building science, CFD, and machine-learning communities** are welcome.

Possible contributions include:

- New experimental benchmark datasets
- High-quality CFD reference datasets
- Validated numerical benchmark datasets
- New AI/ML baseline models
- Cross-model comparison studies
- Cross-city or cross-climate validation cases
- Geometry generalization studies
- Transfer-learning applications
- Uncertainty quantification studies
- Corrections or improvements to existing datasets

For each new benchmark case, sufficient information should be provided to allow independent researchers to:

1. reproduce the physical problem;
2. understand the geometry and boundary conditions;
3. access or reconstruct the reference data;
4. apply consistent training and test conditions; and
5. evaluate their AI models using standardized metrics.

---

## Citation

If you use datasets or benchmark cases from this repository, please cite the corresponding original experimental, numerical, or benchmark study listed in each benchmark case.

Where applicable, users are also encouraged to cite the publications describing the benchmark dataset and its validation methodology.

A general citation for this benchmark database will be provided as the project develops.
