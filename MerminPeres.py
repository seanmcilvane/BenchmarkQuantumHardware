from qiskit import *
from qiskit import QuantumCircuit

def MerminPeresCircuit(X, Y):
    
    qc = QuantumCircuit(4, 4)

    qc.h(0)
    qc.h(1)
    qc.cx(0, 2)
    qc.cx(1, 3)

    # Select measurement operator based on and 
    if X == 0:
        qc.z(1)
        
        qc.z(0)
        
        qc.z(0)
        qc.z(1)
      
            
    if X == 1:
        qc.x(0)
        
        qc.x(1)
            
        qc.x(0)
        qc.x(1)
        
    if X == 2:
        qc.z(0)
        qc.x(0)
        qc.z(0)
        qc.z(1)
        
        qc.x(0)
        qc.z(0)
        qc.x(0)
        qc.x(1)
        
        qc.y(0)
        qc.y(1)
    
    if Y == 0:
        qc.z(3)
        
        qc.x(2)
        
        qc.z(2)
        qc.x(2)
        qc.z(2)
        qc.z(3)
        
    if Y == 1:
        qc.z(2)
        
        qc.x(3)
        
        qc.x(2)
        qc.z(2)
        qc.x(2)
        qc.x(3)
        
    if Y == 2:
        qc.z(2)
        qc.z(3)
        
        qc.x(2)
        qc.x(3)
        
        qc.y(2)
        qc.y(3)
        
    # Measure in bell basis
    qc.cx(0, 2)
    qc.cx(1, 3)
        
    qc.h(0)
    qc.h(1)
        
    qc.measure_all()
    
    return qc