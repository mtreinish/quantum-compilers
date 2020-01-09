import qiskit as qk

qr = qk.QuantumRegister(4)
cr = qk.ClassicalRegister(4)
qc = qk.QuantumCircuit(qr, cr)
qc.h(qr[0])
qc.cx(qr[0], qr[1])
qc.cx(qr[0], qr[2])
qc.cx(qr[0], qr[3])
qc.barrier(qr)
qc.x(0)
qc.cx(qr[0], qr[1])
qc.cx(qr[0], qr[2])
qc.cx(qr[0], qr[3])
qc.barrier(qr)
qc.measure(qr, cr)
qc.draw(output='mpl').savefig('no_layout.png', dpi=900)

from qiskit.test import mock
from qiskit.providers.ibmq import least_busy
backend = mock.FakeYorktown()
prov = qk.IBMQ.load_account()
small_devices = prov.backends(
    filters=lambda x: x.configuration().n_qubits == 5
    and not x.configuration().simulator)
backend = least_busy(small_devices)
print(backend)
qk.visualization.plot_gate_map(backend).savefig('layout_device.png', dpi=900)
qk.visualization.plot_error_map(backend).savefig('layout_error_map.png', dpi=900)

print('optimization 1')
qk.transpile(qc, backend=backend, optimization_level=1).draw(output='mpl').savefig('layout_1.png', dpi=900)
job_1 = qk.execute(qc, backend, optimization_level=1)

print('optimization 2')
qk.transpile(qc, backend=backend, optimization_level=2).draw(output='mpl').savefig('layout_2.png', dpi=900)
job_2 = qk.execute(qc, backend, optimization_level=2)

print('optimization 3')
qk.transpile(qc, backend=backend, optimization_level=3).draw('mpl').savefig('layout_3.png', dpi=900)
job_3 = qk.execute(qc, backend, optimization_level=3)

layout = {qr[1]: 1, qr[0]: 2, qr[2]: 3, qr[3]: 4}
qk.transpile(qc, backend=backend, initial_layout=layout).draw('mpl').savefig('custom_layout.png', dpi=900)
custom_job = qk.execute(qc, backend, initial_layout=layout)

qk.visualization.plot_histogram(job_1.result().get_counts()).savefig('layout_1_results.png', dpi=900)
qk.visualization.plot_histogram(job_2.result().get_counts()).savefig('layout_2_results.png', dpi=900)
qk.visualization.plot_histogram(job_3.result().get_counts()).savefig('layout_3_results.png', dpi=900)
qk.visualization.plot_histogram(custom_job.result().get_counts()).savefig('custom_layout_results.png', dpi=900)
