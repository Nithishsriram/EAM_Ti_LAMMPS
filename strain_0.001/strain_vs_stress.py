import numpy as np
import matplotlib.pyplot as plt

# Columns: strain_z, sxx, syy, szz (GPa)
data = np.loadtxt("z_compressed.data", comments="#")
eps = -data[:, 0] * 100      # compressive strain (%)
sig = -data[:, 3]            # compressive stress (GPa)

# Moving-average smoothing
w = 10
sig_s = np.convolve(sig, np.ones(w) / w, mode="valid")
eps_s = eps[w // 2 : w // 2 + len(sig_s)]   # keep x aligned with the smoothed y

plt.figure(figsize=(5.5, 4.5))
plt.plot(eps_s, sig_s, lw=2, color="C0")
plt.xlabel("Strain (%)")
plt.ylabel("Stress (GPa)")
plt.title("Ti: z-axis compression")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("stress_strain_z.png", dpi=300)
plt.show()