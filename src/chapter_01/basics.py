import cirq

def create_bell_pair_circuit():
    """
    Creates a simple Bell Pair circuit (Phi+) state.
    |Phi+> = (|00> + |11>) / sqrt(2)
    """
    # Create two qubits
    q0, q1 = cirq.LineQubit.range(2)

    # Create a circuit
    circuit = cirq.Circuit()

    # Apply Hadamard gate to the first qubit
    circuit.append(cirq.H(q0))

    # Apply CNOT gate with q0 as control and q1 as target
    circuit.append(cirq.CNOT(q0, q1))

    # Measure both qubits
    circuit.append(cirq.measure(q0, q1, key='result'))

    return circuit

def run_circuit(circuit, repetitions=10):
    """
    Simulates the circuit.
    """
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=repetitions)
    return result
