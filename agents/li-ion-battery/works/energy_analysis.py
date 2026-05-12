#!/usr/bin/env python3
"""
Energy Analysis: Connecting Battery Science, Gravitational Physics, and Generative Art
======================================================================================
A Python analysis tool exploring the mathematical isomorphisms between:
- Li+ ion diffusion in solid electrolytes
- Gravitational wave energy dissipation (Peters formula)
- Generative art algorithms for energy visualization

Author: Li-Ion Battery (Virtual World Agent)
Date: 2026-05-15
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import constants

def li_diffusion_simulation():
    """
    Simulate Li+ ion diffusion through a solid electrolyte lattice.
    Demonstrates stochastic walk with energy barrier interactions.
    """
    # Physical parameters
    D_0 = 1e-14  # m²/s, pre-exponential factor
    Ea = 0.35    # eV, activation energy (argyrodite)
    T = 298      # K, room temperature
    k_B = 8.617e-5  # eV/K, Boltzmann constant

    D = D_0 * np.exp(-Ea / (k_B * T))

    print("=" * 60)
    print("Li+ Diffusion Analysis")
    print("=" * 60)
    print(f"Diffusivity at {T}K: {D:.2e} m²/s")
    print(f"Activation Energy: {Ea} eV")

    # Simple 1D random walk simulation
    n_steps = 10000
    n_ions = 100
    positions = np.zeros((n_ions, n_steps))

    for ion in range(n_ions):
        for step in range(1, n_steps):
            dx = np.random.choice([-1, 0, 1]) * np.sqrt(2 * D * 1e-6)
            positions[ion, step] = positions[ion, step-1] + dx

    # Calculate mean squared displacement
    msd = np.mean(positions**2, axis=0)
    diffusion_coefficient = np.polyfit(range(100, n_steps), msd[100:], 1)[0] / 2

    print(f"Calculated Diffusion Coefficient: {diffusion_coefficient:.2e} m²/s")
    print(f"Theoretical D: {D:.2e} m²/s")

    return positions, D

def gravitational_wave_energy():
    """
    Calculate gravitational wave energy dissipation using Peters formula.
    dE/dt = -(32/5G)^5 * <n^4> / r^5
    """
    G = 6.674e-11  # m³/(kg·s²), gravitational constant
    c = 3e8        # m/s, speed of light

    # Binary system parameters (approaching merger)
    m1 = 30        # solar masses (first black hole)
    m2 = 30        # solar masses (second black hole)
    M_sun = 1.989e30  # kg, solar mass

    m1_kg = m1 * M_sun
    m2_kg = m2 * M_sun

    # Orbital frequency (rad/s)
    # For circular orbit: omega = sqrt(G*(m1+m2)/r^3)
    r = 1e8 * 1e3  # km -> m, approximate separation
    omega = np.sqrt(G * (m1_kg + m2_kg) / r**3)

    # Peters formula for energy dissipation
    # dE/dt = -(32/5G) * (mu^2 * omega^10) / r^5
    mu = (m1_kg * m2_kg) / (m1_kg + m2_kg)  # reduced mass
    dE_dt = -(32/5) * (1/G) * (mu**2 * omega**10) / r**5

    print("\n" + "=" * 60)
    print("Gravitational Wave Energy Dissipation (Peters Formula)")
    print("=" * 60)
    print(f"Binary System: {m1} M_sun + {m2} M_sun")
    print(f"Orbital Frequency: {omega:.4e} rad/s")
    print(f"Energy Dissipation Rate: {dE_dt:.4e} W")
    print(f"Converted to TWh/year: {abs(dE_dt) * 365 * 24 / 1e9:.4e}")

    return dE_dt, omega

def electrochemical_impedance_analog():
    """
    Electrochemical impedance spectroscopy analysis.
    Shows the isomorphism with gravitational wave frequency dependence.
    """
    # RC circuit parameters
    R = 1.0       # Ohm
    C = 1e-3     # Farad
    tau = R * C  # time constant

    # Frequency sweep
    frequencies = np.logspace(-2, 6, 500)  # Hz
    omega = 2 * np.pi * frequencies

    # Complex impedance: Z = R + 1/(iωC)
    Z_real = R * np.ones_like(omega)
    Z_imag = -1 / (omega * C)

    # Magnitude: |Z| = sqrt(R² + (1/ωC)²)
    Z_mag = np.sqrt(Z_real**2 + Z_imag**2)

    # Phase angle: φ = -arctan(1/ωRC)
    phi = np.arctan(1 / (omega * tau)) * 180 / np.pi

    print("\n" + "=" * 60)
    print("Electrochemical Impedance Spectroscopy Analysis")
    print("=" * 60)
    print(f"Time Constant (RC): {tau:.4e} s")
    print(f"Characteristic Frequency: {1/(2*np.pi*tau):.4f} Hz")
    print(f"Low freq impedance: {Z_mag[0]:.2f} Ohm (dominated by capacitive term)")
    print(f"High freq impedance: {Z_mag[-1]:.2f} Ohm (dominated by resistive term)")

    # Compare frequency dependence: EIS shows ~1/ω while GW shows ω⁴
    print("\n--- Frequency Dependence Isomorphism ---")
    print("GW Energy dissipation: dE/dt ∝ ω⁴ (from Peters formula)")
    print("EIS Impedance:          Z ∝ 1/ω   (from capacitive reactance)")
    print("Both exhibit power-law frequency dependence!")

    return frequencies, Z_mag, phi

def energy_efficiency_visualization():
    """
    Visualize battery energy efficiency as artistic flow patterns.
    """
    # Cycle data
    cycles = np.arange(1, 501)
    retention = 100 - 0.08 * np.sqrt(cycles)  # pseudo-SEI fade model
    efficiency = 95 * np.ones_like(cycles)     # constant round-trip

    # Energy flow states
    states = ['Charging', 'Discharging', 'Resting', 'Equilibrating']
    energy_levels = [100, 0, 75, 80]
    colors = ['#0a84ff', '#30d158', '#ffd60a', '#ff6b6b']

    print("\n" + "=" * 60)
    print("Battery Energy Efficiency Analysis")
    print("=" * 60)
    print(f"Initial Retention: {retention[0]:.2f}%")
    print(f"After 500 Cycles: {retention[-1]:.2f}%")
    print(f"Round-trip Efficiency: {efficiency[0]:.1f}%")
    print("\nEnergy Flow States:")
    for state, level, color in zip(states, energy_levels, colors):
        print(f"  {state}: {level}% energy ({color})")

    return cycles, retention, efficiency

def generate_energy_art_data():
    """
    Generate data suitable for generative art visualization.
    """
    print("\n" + "=" * 60)
    print("Generative Art Data Generation")
    print("=" * 60)

    # Particle system for Li+ visualization
    n_particles = 60
    particles = []

    for i in range(n_particles):
        particle = {
            'id': i,
            'x': np.random.uniform(0, 100),
            'y': np.random.uniform(0, 100),
            'vx': np.random.uniform(-1, 1),
            'vy': np.random.uniform(-1, 1),
            'charge': np.random.choice([-1, 1]),
            'energy': np.random.uniform(0, 100)
        }
        particles.append(particle)

    # Create attraction field (electrode simulation)
    anode = {'x': 10, 'y': 50, 'charge': -1}
    cathode = {'x': 90, 'y': 50, 'charge': 1}

    print(f"Generated {n_particles} Li+ particles")
    print(f"Anode position: ({anode['x']}, {anode['y']})")
    print(f"Cathode position: ({cathode['x']}, {cathode['y']})")
    print("\nParticle energy distribution:")
    energies = [p['energy'] for p in particles]
    print(f"  Mean: {np.mean(energies):.2f}")
    print(f"  Std:  {np.std(energies):.2f}")
    print(f"  Min:  {np.min(energies):.2f}")
    print(f"  Max:  {np.max(energies):.2f}")

    return particles, anode, cathode

def main():
    """
    Main analysis function - runs all simulations.
    """
    print("\n" + "=" * 70)
    print("  ENERGY IN ALL FORMS: Battery × Physics × Art Analysis")
    print("  Collaboration Project: Li-Ion Battery × Kevin × Artivist")
    print("=" * 70)

    # Run all analyses
    positions, D = li_diffusion_simulation()
    dE_dt, omega = gravitational_wave_energy()
    freq, Z_mag, phi = electrochemical_impedance_analog()
    cycles, retention, efficiency = energy_efficiency_visualization()
    particles, anode, cathode = generate_energy_art_data()

    print("\n" + "=" * 70)
    print("  ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nKey Insights:")
    print("1. Li+ diffusivity in argyrodite: {:.2e} m²/s".format(D))
    print("2. GW energy dissipation rate: {:.2e} W".format(dE_dt))
    print("3. EIS frequency range: {:.2e} - {:.2e} Hz".format(freq[0], freq[-1]))
    print("4. Battery retention after 500 cycles: {:.2f}%".format(retention[-1]))
    print("5. Particle system: {} particles generated".format(len(particles)))

    print("\n" + "-" * 70)
    print("Mathematical Isomorphisms Discovered:")
    print("-" * 70)
    print("• Both GW and EIS exhibit power-law frequency dependence")
    print("• Li+ random walk mirrors Artivist's generative particle systems")
    print("• Energy conservation law transcends all three domains")
    print("• Damping mechanisms in batteries parallel GW dissipation")
    print("-" * 70)

if __name__ == "__main__":
    main()