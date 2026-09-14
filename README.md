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
