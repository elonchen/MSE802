from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt


# Reflection 9
qc = QuantumCircuit(1)

qc.h(0)
qc.z(0)

print(qc)

state = Statevector.from_instruction(qc)

plot_bloch_multivector(state)

plt.show()