import qiskit.qasm2
from qiskit.circuit import QuantumCircuit
 
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
print(qiskit.qasm2.dumps(qc))

qiskit.qasm2.dump(qc, "test2.qasm")



# import and run it in qiskit
circuit = qiskit.qasm2.load("test2.qasm")
print(circuit)