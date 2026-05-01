import qiskit as qk
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_bloch_vector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Example 1: One qubit in superposition
qc1 = QuantumCircuit(1, 1)

# Apply Hadamard gate
# qc1.h(0)
# qc1.x(0)
qc1.z(0)

# Measure the qubit
qc1.measure(0, 0)

print("Circuit:")
# display(qc1.draw(output='mpl'))
print(qc1.draw(output='text')) 

simulator = AerSimulator()
job = simulator.run(qc1, shots=1024)
result = job.result()
counts = result.get_counts(qc1)

print("Measurement counts:", counts)
plot_histogram(counts)



# Example 2: Two qubits in superposition
qc2 = qk.QuantumCircuit(2, 2)

qc2.h(0)
qc2.h(1)

qc2.measure(0, 0)
qc2.measure(1, 1)

print("Circuit:")
# display(qc2.draw(output='mpl'))
print(qc2.draw(output='text')) 

simulator = AerSimulator()
job = simulator.run(qc2, shots=1024)
result = job.result()
counts = result.get_counts(qc2)

print("Measurement counts:", counts)
plot_histogram(counts)



# Example 3: Entangled qubits
a = QuantumRegister(1, name='a')
b = QuantumRegister(1, name='b')
a_c = ClassicalRegister(1, name='ac')
b_c = ClassicalRegister(1, name='bc')

qc3 = QuantumCircuit(a, b, a_c, b_c)

qc3.h(a[0])          # put qubit a into superposition
qc3.cx(a[0], b[0])   # entangle qubit a and qubit b
qc3.measure(a[0], a_c[0])
qc3.measure(b[0], b_c[0])

print("Circuit:")
# display(qc3.draw(output='mpl'))
print(qc3.draw(output='text'))

simulator = AerSimulator()
job = simulator.run(qc3, shots=4096)
result = job.result()
counts = result.get_counts(qc3)

print("Measurement counts:", counts)
plot_histogram(counts)





qc_b0 = QuantumCircuit(1)
state_b0 = Statevector.from_instruction(qc_b0)

print("Statevector for |0>:", state_b0)
plot_bloch_multivector(state_b0)





qc_b1 = QuantumCircuit(1)
qc_b1.x(0)
state_b1 = Statevector.from_instruction(qc_b1)

print("Statevector for |1>:", state_b1)
plot_bloch_multivector(state_b1)


# Bloch Sphere for H|0>
qc_bh = QuantumCircuit(1)
qc_bh.h(0)
state_bh = Statevector.from_instruction(qc_bh)

print("Statevector for H|0>:", state_bh)
plot_bloch_multivector(state_bh)







fig = plot_bloch_vector([0, 0, 1], title="State |0>")
# fig.savefig('bloch_sphere.png') 
# print("图像已保存为 bloch_sphere.png")
# plt.show()