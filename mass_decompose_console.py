import sys
import pyopenms as oms

mass = float(sys.argv[1])
tol = float(sys.argv[2])

md_alg = oms.MassDecompositionAlgorithm()
param = md_alg.getParameters()
param.setValue("tolerance", tol)
param.setValue("residue_set", b"Natural20")
md_alg.setParameters(param)
decomps = []
md_alg.getDecompositions(decomps, mass)
for d in decomps:
  print(d.toExpandedString())