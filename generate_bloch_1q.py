import math

import qiskit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector


qc = qiskit.QuantumCircuit(1)
plot_bloch_multivector(Statevector(qc)).savefig('bloch_fresh.png', dpi=900)
qc.h(0)
plot_bloch_multivector(Statevector(qc)).savefig('bloch_h.png', dpi=900)
qc.t(0)
plot_bloch_multivector(Statevector(qc)).savefig('bloch_t.png', dpi=900)
qc.s(0)
plot_bloch_multivector(Statevector(qc)).savefig('bloch_s.png', dpi=900)
qc.rz(math.pi/4, 0)
plot_bloch_multivector(Statevector(qc)).savefig('result_1q_bloch.png', dpi=900)
print(qc.draw('latex_source'))
