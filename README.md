# EAM Ti LAMMPS

Molecular dynamics simulation of bulk HCP titanium using the **Finnis–Sinclair (FS) EAM potential** in LAMMPS.

## Simulation Workflow

- HCP Ti structure generated using **ASE**
- 10 × 10 × 10 supercell containing **2000 atoms**
- Energy minimization to obtain the equilibrium structure
- NVT equilibration at **300 K**
- NPT equilibration at **300 K and 0 bar**
- Uniaxial compression along the **z-direction**
- Compression up to **10% strain** at a strain rate of **0.001 ps⁻¹**
- Stress–strain curve obtained using Python

## Workflow

```text
HCP Ti
  ↓
Energy Minimization
  ↓
NVT (300 K)
  ↓
NPT (300 K, 0 bar)
  ↓
Compression along z
  ↓
10% strain
  ↓
Stress–Strain Curve
