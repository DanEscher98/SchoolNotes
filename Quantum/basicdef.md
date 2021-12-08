# Quantum Computing: Basic Definitions

1. Superposition: A probability
2. Entanglement: Distributed probability
3. Interference: Constructive or Destructive

## Applications

1. Quantum Simulation
2. Optimization Problems
3. Cybersecurity

## Models of Quantum Computing

- Gate Model: There is a collection of qubits which are entangled with
    each other and a bunch of gates which can perform operations on
    small numbers of these qubits. These gates, change the states of
    the qubits without measuring them.
- Measurement Based: Set a collection of qubits with an initial
    entangled state and then measuring qubits one by one during the
    computation.
- Adiabatic QC: Takes advantage of the fact that every system in
    physics always moves towards the minimum energy state. It poses
    the problems that want to be solved in such a way so that the
    minimum energy state of the quantum system is the answer to the
    problem. Mathematically, is equivalent to gate model.
- Quantum annealing: Also uses energy minimisation but it's not
    universal.
- Topological QC: This is the most theoretical. It builds its qubits
    from an entity in physics called a *Majorana zero-mode
    quasi-particle* which is a type of *non-abelian anyon*.
    Quasi-particles are created from the collected behaviour of many
    particles together, having particle-like properties despite not
    being actually real or fundamental ones. (e.g. an electron
    "hole"). In this model, the quasi-particles are predicted to be a
    lot more stable than other qubits because they are made from parts
    which are physically separated from each other, avoiding *noise*
    by being protected by an energy gap. Any perturbations of noise
    which have a lower energy than the energy gap is not felt by the
    quasi-particle.

## Obstacles

- Decoherence: It's wanted that the qubits be entangled with each
    other and anything else. It is ever possible to make a working
    quantum computer with a large number of qubits, or will
    decoherence and noise ruin everything?
- Quantum Error Correction: This is an error correction scheme to make
    fault-tolerant quantum computers by using many entangled qubits
    together to represent one noise free qubit. Estimation: 100 to
    1000 qubits for 1 logical qubit.
- Scalability

## Physical implementations

- Superconducting QC: Currenty the most popular method. Their qubits
    are made from superconducting wires with a break in the
    supercounductor called a *Josephson junction*. The level system is
    encoded in pairs of the electric charge moving across the
    junction, specifically the frequency at which charges oscillate
    back and forth across the junctions. Other designs use the
    magnetic flux in a loop of wire or the phase across a wire as a
    two level system known as flux qubits or *phase qubits*.
- Quantum DOT QC: Also known as *Silicon spin QC*. Here the qubits are
    made from electrons or even groups of electrons and the two level
    system is encoded into the spin or charge of the electrons. On the
    chip, there's a small area where the electron is restricted called
    a *quantum dot*. Operations on the qubits are performed through
    voltages, microwaves or magnetic fields on the chip. The materials
    used as the semiconductor are: silicon, gallium arsenide, silicon
    carbide or even diamond.
- Linear Optical QC: They use photons of light as the qubits and they
    operate on these qubits using optical elements like mirrors,
    waveplates or interferometers. The two level system could have
    different designs, either a superposition of different paths a
    single photon takes through the chip or a superposition of
    different numbers of photons present in a path. They could be
    mannipulated applying a voltage to a path.
- Trapped ion QC: They use charged atoms as qubits. The atoms are
    ionised (have a missing electron) meaning they can be levitated
    and moved about with electromagnetic fields. Here the two level
    state is encoded in two specific energy levels of the atom which
    can be manipulated or measured with microwaves or laser beams.
- Colour centre QC: Also *Nitrogen vacancy QC*, are similar to Trapped
    ion QC in that the qubits are made from atoms. But insted of being
    trapped in an electromagnetic field, they are embedded in a gap of
    the material like nitrogen embedded in diamond or silicon carbide.
    Typically the two level system is the nuclear spins of the
    embedded atoms and they are entangled together with electrons.
- Neutral atoms in Optical Lattices: The qubits are atoms, and the
    design uses cold atom physics capturing neutral atoms like caesium
    into an optical lattice which is a crisscrossed arrangement of
    laser beams, which form energy wells shaped kind of like an egg
    box. These atoms are cooled down with lasers to a few millionths
    of a kelvin. There are number ways to encode the two level system:
    either the hyperfine energy level of the atom, the excited states
    or even Rydberg atoms. The atoms can be controlled and entangled
    with each other with lasers.
- Other approaches:
    - Electron on Helium Qubit
    - Cavity Quantum Electrodynamics
    - Magnetic molecules
    - Nuclear Magnetic Resonance QC

