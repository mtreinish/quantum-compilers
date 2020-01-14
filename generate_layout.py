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
