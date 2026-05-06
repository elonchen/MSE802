OPENQASM 2.0;

// Define 4 quantum qubits and 4 classical bits
qreg q[4];
creg c[4];

// --- 1. Initialization ---
h q[0];
h q[1];
h q[2];
h q[3];

// --- 2. Entanglement ---
cx q[0], q[1];
cx q[1], q[2];
cx q[2], q[3];

// --- 3. Measurement ---
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];