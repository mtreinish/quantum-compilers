import qiskit as qk

qr = qk.QuantumRegister(5)
qc = qk.QuantumCircuit(qr)

qc.x(qr[4])
qc.h(qr)
for i in range(4):
    qc.cx(qr[i], qr[4])
qc.h(qr)
qc.draw(output='mpl').savefig('no_compile.png', dpi=400)
qc.measure_all()

qk.IBMQ.load_account()
prov = qk.IBMQ.get_provider(hub='ibm-q-internal', group='dev-qiskit')
#small_devices = prov.backends(
#    filters=lambda x: x.configuration().n_qubits == 5
#    and not x.configuration().simulator)
#backend = qk.providers.ibmq.least_busy(small_devices)
backend = prov.get_backend('ibmq_london')

#job_bad = qk.execute(qc, backend, optimization_level=0)
#job_good = qk.execute(qc, backend, optimization_level=3)
qk.transpile(qc, backend=backend, optimization_level=0).draw(output='mpl', fold=28).savefig('bad_compile_circ.png', dpi=400)
qk.transpile(qc, backend=backend, optimization_level=3).draw(output='mpl').savefig('good_compile_circ.png', dpi=400)

#qk.visualization.plot_histogram(job_bad.result().get_counts()).savefig('bad_compile.png', dpi=400)

#qk.visualization.plot_histogram(job_good.result().get_counts()).savefig('good_compile.png', dpi=400)
