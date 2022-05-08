
module QtmStatesGates
using 
export σx, σy, σz, I, H, sOne, sZero, sPlus, sMinus, sIPlus, sIMinus

begin const
     σx = qGate([0 1; 1 0])
     σy = qGate([0 -im; im 0])
     σz = qGate([1 0; 0 -1])
     H = qGate(1/sqrt(2*unit) * [1 1; 1 -1])
     I = qGate([1 0; 0 1])
     sOne = qState([0, 1], "1")
     sZero = qState([1, 0], "0")
     sPlus = qState(1/sqrt(2*unit)*(sZero+sOne).vector, "+")
     sMinus = qState(1/sqrt(2*unit)*(sZero-sOne).vector, "-")
     sIPlus = qState(1/sqrt(2*unit)*(sZero+im*sOne).vector, "+𝑖")
     sIMinus = qState(1/sqrt(2*unit)*(sZero-im*sOne).vector, "-𝑖")
end
end
