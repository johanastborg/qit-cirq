import cirq
import pytest
from src.chapter_01.basics import create_bell_pair_circuit, run_circuit

def test_create_bell_pair_circuit():
    circuit = create_bell_pair_circuit()
    assert isinstance(circuit, cirq.Circuit)
    # Check if there are 3 operations (H, CNOT, Measure)
    assert len(list(circuit.all_operations())) == 3

def test_run_circuit():
    circuit = create_bell_pair_circuit()
    result = run_circuit(circuit, repetitions=100)

    # Check that we mostly get 00 or 11
    # Note: In a simulator, we might rarely get something else if there's noise,
    # but the default simulator is noiseless.
    counts = result.histogram(key='result')

    # counts is a Counter object, e.g., Counter({0: 50, 3: 50}) where 0 is 00 and 3 is 11 in binary
    # We expect keys 0 and 3 to be present, and sum to 100.
    # Keys might be missing if they never occurred (random chance), but very unlikely with 100 reps.

    # Just check that observed states are valid Bell states for Phi+ (00 -> 0, 11 -> 3)
    for state in counts.keys():
        assert state in [0, 3]
