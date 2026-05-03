from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Put qubit 0 into superposition
qc.h(0)

# Apply a 90° phase shift (S gate)
qc.s(0)

# Print the circuit
print(qc)

# Get the quantum state
state = Statevector.from_instruction(qc)

# Print the statevector
print(state)

# Visualize using Q-sphere
plot_state_qsphere(state)