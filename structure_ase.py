from ase.build import bulk
from ase.io import write

ti = bulk("Ti", crystalstructure = "hcp", a = 2.95, c = 4.68)

ti = ti.repeat((10, 10, 10))

print(ti.cell)
write("Ti.data", ti, format = "lammps-data", atom_style = "atomic")

print(open("Ti.data").read()[:2000])