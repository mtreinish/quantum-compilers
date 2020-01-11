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
