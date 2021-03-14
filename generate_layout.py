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
qc.h(qr)
qc.barrier(qr)
qc.cz(qr[1], qr[0])
qc.cz(qr[2], qr[0])
qc.cz(qr[3], qr[0])
qc.barrier(qr)
qc.h(qr)
qc.x(qr)
qc.cz(qr[1], qr[0])
qc.cz(qr[2], qr[0])
qc.cz(qr[3], qr[0])
qc.x(qr)
qc.h(qr)
qc.barrier(qr)
qc.measure(qr, cr)
qc.draw(output='mpl').savefig('no_layout.png', dpi=900)

rov = qk.IBMQ.load_account()
ackend = prov.get_backend('ibmq_quito')
rint(backend)
k.visualization.plot_gate_map(backend).savefig('layout_device.png')
k.visualization.plot_error_map(backend).savefig('layout_error_map.png')

print('Trivial Layout')
trivial_qc = qk.transpile(qc, backend=backend, layout_method='trivial')
trivial_qc.draw(output='mpl', fold=-1).savefig('layout_1.png', dpi=900)

print('Dense Layout')
dense_qc = qk.transpile(qc, backend=backend, layout_method='dense')
dense_qc.draw(output='mpl', fold=-1).savefig('layout_2.png', dpi=900)

print('Noise Adaptive Layout')
noise_qc = qk.transpile(qc, backend=backend, layout_method='noise_adaptive')
noise_qc.draw('mpl', fold=-1).savefig('layout_3_noise.png', dpi=900)

layout = {qr[1]: 0, qr[0]: 1, qr[2]: 2, qr[3]: 3}
custom_qc = qk.transpile(qc, backend=backend, initial_layout=layout)
custom_qc.draw('mpl', fold=-1).savefig('custom_layout.png', dpi=900)
job = backend.run([trivial_qc, dense_qc, noise_qc, custom_qc])

qk.visualization.plot_histogram(job.result().get_counts(0)).savefig('layout_1_results.png', dpi=900)
qk.visualization.plot_histogram(job.result().get_counts(1)).savefig('layout_2_results.png', dpi=900)
qk.visualization.plot_histogram(job.result().get_counts(2)).savefig('layout_3_results.png', dpi=900)
qk.visualization.plot_histogram(job.result().get_counts(3)).savefig('custom_layout_results.png', dpi=900)
