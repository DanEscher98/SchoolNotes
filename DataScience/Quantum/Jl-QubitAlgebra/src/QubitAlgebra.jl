module QubitAlgebra
using SymPy
import Base.:+, Base.:*, Base.:-, Base.:^, Base.==

export qState, qGate
export BlochCoordinates, print

unit = 1 #Sym(1)

struct qState
    vector::Vector
    c::Union{Sym, Float64}
    name::String
    function qState(vector::Vector{<:Number}, name::String="_")
        if size(vector)[1]==2
            arg = abs(vector[1]^2) + abs(vector[2]^2)
            c = 1/sqrt(arg*unit)
            return new(unit*vector, c, name)
        else
            error("Invalid vector")
        end
    end
    function qState(values::Tuple{Number, Number}, name::String="_")
       if (0 <= values[1] <= π) && (0 <= values[2] < 2π)
           θ, φ = Sym("θ φ")
           ans = [cos(θ/2) , ℯ^(φ*im)*sin(θ/2)]
           ans = ans.subs(θ, values[1])
           ans = ans.subs(φ, values[2]==π ? PI : values[2])
           return qState(vec(ans), name)
       else
           error("Angles out of range")
       end
    end
end


struct qGate
    matrix::Array{<:Number, 2}
end

# Basic operations between States and Gates
+(m::qState,n::qState)  = qState(m.vector + n.vector)
-(m::qState,n::qState)  = qState(m.vector - n.vector)
+(m::qGate, n::qGate)   = qGate(m.matrix + n.matrix)
*(m::Number, n::qState) = qState(m*n.vector)
*(m::qState,n::qState)  = (m.c*n.c)*(transpose(m.vector)*n.vector)
*(G::qGate, S::qState)  = qState(G.matrix*S.vector)
*(m::qGate, n::qGate)   = qGate(m.matrix*n.matrix)
*(n::Number,G::qGate)   = qGate(n*G.matrix)
^(G::qGate, n::Int64)   = qGate(G.matrix^n)
==(m::qState, n::qState)= m.vector == n.vector
Base.show(io::IO, m::qState)= print(io, "|$(m.name)⟩ = $(m.vector)")
Base.show(io::IO, m::qGate) = show(stdout, "text/plain", m.matrix)

function BlochCoordinates(m::qState)
    x = m.vector[2].as_real_imag()[1]
    y = m.vector[2].as_real_imag()[2]
    z = m.vector[1]
    return m.c*[x, y, z]
end

end
