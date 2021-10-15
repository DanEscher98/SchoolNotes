#conda activate qsharp-env

import qsharp
from Qrng import SampleQuantumRandomNumberGenerator

for _ in range(10):
	print(SampleQuantumRandomNumberGenerator.simulate())