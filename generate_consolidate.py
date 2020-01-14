# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import qiskit as qk
from qiskit import converters
from qiskit.transpiler import passes


qr = qk.QuantumRegister(3)
qc = qk.QuantumCircuit(qr)
qc.h(qr)
qc.u3(0.1, 0.2, 0.3, qr[0])
qc.cx(qr[1], qr[0])
qc.u3(3.14, 3.14, 3.14, qr[0])
qc.h(qr[0])
qc.h(qr[1])
qc.cx(qr[0], qr[1])
qc.h(qr[0])
qc.h(qr[1])
qc.cx(qr[0], qr[1])
qc.h(qr[0])
qc.h(qr[1])
qc.cx(qr[0], qr[1])
qc.swap(qr[0], qr[2])
qc.ch(qr[0], qr[2])
qc.t(qr[1])
qc.h(qr)

dag = converters.circuit_to_dag(qc)

dag = passes.Unroller(['u1', 'u2', 'u3', 'cx', 'id']).run(dag)

block_pass = passes.Collect2qBlocks()
block_pass.run(dag)
consolidate_pass = passes.ConsolidateBlocks()
consolidate_pass.property_set[
    'block_list'] = block_pass.property_set['block_list']
out_dag = consolidate_pass.run(dag)
out_circ = converters.dag_to_circuit(out_dag)
print(out_circ.draw(output='latex_source'))

unrolled_output_dag = passes.Unroller(
    ['u1', 'u2', 'u3', 'cx', 'id']).run(out_dag)
unrolled_output_dag = passes.Optimize1qGates().run(unrolled_output_dag)
out_unrolled_circ = converters.dag_to_circuit(unrolled_output_dag)
out_unrolled_circ.draw(output='mpl', filename='unrolled_unitary.png')
