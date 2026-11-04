#!/usr/bin/env python3
"""Writes content/blueprint.json: subjects, topics, per-topic targets and the CSCA paper pattern.

CSCA (China Scholastic Competency Assessment, csca.cn, checked 4 Nov 2026): Mathematics, Physics and Chemistry are
each a separate 60-minute paper of 48 single-answer multiple-choice questions, scored 0-100, no calculator. Topic
weights per paper are our estimate from the 2025 syllabi (CSC publishes no weights). Mocks use 4 options (A-D).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# section key, title, group, [(topic key, id prefix, title, items per mock paper, practice items, scope note)]
SECTIONS = [
    ("math", "Mathematics", "math", [
        ("sets", "ms", "Sets and Inequalities", 6, 30, "Sets: notation, subsets, union, intersection, complement, Venn diagrams; necessary and sufficient conditions, simple quantifiers; properties of inequalities; linear, quadratic, rational (fractional) and absolute-value inequalities; AM-GM for simple maxima/minima."),
        ("functions", "mf", "Functions, Exponents and Logarithms", 8, 40, "Function concept, domain, range, composition, inverse functions; monotonicity, odd/even, periodicity, graph transformations; linear and quadratic functions; power, exponential and logarithmic functions and their laws; solving exponential and log equations; piecewise functions; zeros of functions."),
        ("trig", "mt", "Trigonometry", 6, 30, "Radians, unit-circle definitions, special angle values, signs by quadrant; identities, induction (reduction) formulas, sum and difference, double angle; graphs of sin, cos, tan, y = A sin(ωx + φ), period, amplitude, phase; solving triangles with the sine and cosine rules, triangle area."),
        ("sequences", "mq", "Sequences", 5, 25, "General term, recursive definitions; arithmetic sequences (nth term, sum, mean); geometric sequences (nth term, sum, infinite sum with |r| < 1); mixed and telescoping sums."),
        ("calculus", "md", "Derivatives and Their Applications", 5, 25, "Definition and geometric meaning of the derivative; derivatives of basic functions; sum, product, quotient and simple chain rules; tangent lines; increasing/decreasing intervals, extrema, maximum and minimum on an interval; simple optimisation."),
        ("analytic", "ma", "Analytic Geometry: Lines, Circles and Conics", 7, 35, "Slope, inclination, equations of lines, parallel and perpendicular, distance from a point to a line; circles (standard and general form, line-circle and circle-circle position); ellipse, hyperbola, parabola: standard equations, foci, eccentricity, asymptotes, directrix, simple chord problems."),
        ("vectors", "mv", "Vectors and Complex Numbers", 4, 25, "Plane vectors: addition, scalar multiples, coordinates, dot product, angle, length, parallel and perpendicular conditions; complex numbers: i, algebraic form, arithmetic, conjugate, modulus, the complex plane."),
        ("solid", "mg", "Solid Geometry", 3, 20, "Prisms, pyramids, cylinders, cones, spheres: surface area and volume; lines and planes in space (parallel, perpendicular); 3-D rectangular coordinates, distance between points, midpoints; simple angles in solids."),
        ("probability", "mp", "Probability and Statistics", 4, 25, "Counting basics (multiplication principle, simple permutations and combinations); classical probability, complementary and independent events; mean, median, mode, variance and standard deviation; reading frequency tables; normal distribution basics (symmetry, μ ± σ ideas)."),
    ]),
    ("physics", "Physics", "physics", [
        ("kinematics", "pk", "Kinematics", 6, 25, "Displacement, velocity, acceleration; uniform and uniformly accelerated motion equations; free fall, vertical throw; motion graphs (x-t, v-t); projectile motion; relative motion basics."),
        ("forces", "pn", "Forces and Newton's Laws", 6, 25, "Gravity, normal force, friction (static/kinetic), tension, springs (Hooke's law); force resolution and equilibrium; Newton's three laws; inclines, connected bodies, pulleys, apparent weight in lifts."),
        ("momentum", "pm", "Momentum and Impulse", 3, 20, "Momentum, impulse-momentum theorem, conservation of momentum, elastic and inelastic collisions, recoil, explosions."),
        ("energy", "pw", "Work, Energy and Power", 4, 20, "Work, power, kinetic energy, work-energy theorem, gravitational and elastic potential energy, conservation of mechanical energy, efficiency, energy with friction."),
        ("circular", "pg", "Circular Motion and Gravitation", 4, 20, "Angular velocity, period, centripetal acceleration and force; vertical circles, banked curves; Newton's law of gravitation, g at altitude, satellite orbits, orbital speed and period, Kepler's third law."),
        ("waves", "ps", "Oscillations and Waves", 3, 20, "Simple harmonic motion, spring and simple pendulum periods, energy in SHM; transverse and longitudinal waves, v = fλ, wave graphs, reflection, superposition, standing waves, sound, Doppler effect (qualitative)."),
        ("electrostatics", "pe", "Electrostatics", 4, 20, "Charge, Coulomb's law, electric field strength and field lines, potential and potential difference, work done on charges, capacitors (C = Q/U, parallel plate), motion of charges in uniform fields."),
        ("circuits", "pc", "DC Circuits", 4, 20, "Current, resistance, resistivity, Ohm's law, series and parallel, EMF and internal resistance, electrical power and energy, meters, simple circuit analysis."),
        ("magnetism", "pb", "Magnetic Fields", 3, 20, "Magnetic field and field lines, field of currents (right-hand rule), force on a current-carrying wire (F = BIL), Lorentz force, circular motion of charges in a magnetic field."),
        ("induction", "pi", "Electromagnetic Induction and AC", 3, 20, "Magnetic flux, Faraday's law, Lenz's law, motional EMF (E = BLv), self-induction basics, alternating current, rms values, ideal transformers."),
        ("thermal", "pt", "Thermal Physics", 3, 20, "Molecular kinetic theory, temperature and internal energy, ideal gas law and gas laws, specific heat and latent heat, first law of thermodynamics, second law (qualitative)."),
        ("optics", "po", "Optics", 3, 20, "Reflection, refraction, refractive index, Snell's law, total internal reflection and critical angle, lenses and mirrors (basic), dispersion; interference (double slit), diffraction, polarisation."),
        ("modern", "pq", "Modern Physics", 2, 20, "Photoelectric effect and photon energy, wave-particle duality, Bohr model and energy levels, spectra, nuclear structure, radioactivity (alpha, beta, gamma), half-life, nuclear equations, mass-energy, fission and fusion."),
    ]),
    ("chemistry", "Chemistry", "chemistry", [
        ("concepts", "cb", "Matter, Chemical Language and Equations", 4, 25, "Classification of matter (elements, compounds, mixtures, pure substances), physical vs chemical change, states of matter, formulas and valency, naming, balancing equations, reaction types, colloids."),
        ("mole", "cm", "The Mole and Calculations", 6, 30, "Relative atomic and molecular mass, the mole, Avogadro constant, molar mass, molar volume of gases, ideal gas equation, solution concentration (mol/L, mass fraction), dilution, reaction stoichiometry, limiting reagent, yield."),
        ("inorganic", "ci", "Inorganic Elements and Compounds", 7, 35, "Properties and reactions of Na, Mg, Al, Fe, Cu and their compounds; non-metals Cl, S, N, C, Si and their oxides and acids; common acids, bases and salts; amphoteric behaviour; everyday and environmental chemistry."),
        ("organic", "co", "Organic Chemistry", 6, 30, "Alkanes, alkenes, alkynes, benzene; functional groups (alcohols, aldehydes, carboxylic acids, esters); isomerism; naming simple compounds; substitution, addition, elimination, esterification, polymerisation; basic biomolecules (sugars, proteins, fats)."),
        ("redox", "cr", "Redox Reactions", 4, 20, "Oxidation states, oxidation and reduction, oxidising and reducing agents, electron transfer, balancing redox equations, galvanic cells and electrolysis basics."),
        ("ionic", "cn", "Ionic Reactions and Tests for Ions", 4, 20, "Electrolytes, ionic equations, conditions for ionic reactions, ion coexistence in solution, tests for common cations and anions (Cl⁻, SO₄²⁻, CO₃²⁻, NH₄⁺, Fe³⁺, Fe²⁺)."),
        ("atomic", "ca", "Atomic Structure and the Periodic Table", 4, 25, "Protons, neutrons, electrons, isotopes, electron configuration (first 20 elements and simple transition cases), periodic trends (radius, ionisation energy, electronegativity, metallic character), groups and periods."),
        ("bonding", "cd", "Chemical Bonding and Structure", 3, 20, "Ionic, covalent and metallic bonds, electron-dot structures, polarity, molecular shapes (VSEPR basics), intermolecular forces and hydrogen bonding, crystal types and their properties."),
        ("equilibrium", "ce", "Reaction Rates and Equilibrium", 4, 25, "Factors affecting rate, activation energy and catalysts, reversible reactions, dynamic equilibrium, Le Chatelier's principle, equilibrium constant expressions, energy changes (exothermic/endothermic, ΔH)."),
        ("solutions", "cp", "Acids, Bases and Electrolyte Solutions", 3, 20, "Acid-base theories, strong and weak electrolytes, pH and its calculation for simple cases, neutralisation, hydrolysis of salts, buffers (qualitative), titration basics."),
        ("lab", "cl", "Laboratory Work and Industrial Chemistry", 3, 20, "Lab safety, common apparatus, preparing and collecting gases (O₂, H₂, CO₂, NH₃, Cl₂), separation and purification (filtration, distillation, crystallisation, extraction), identifying substances, industrial processes (Haber process, contact process, metal extraction)."),
    ]),
]

PAPERS = 20
MODES = {
    k: {"title": {"math": "Maths"}.get(k, t), "subtitle": "48 questions · 60 minutes · no calculator", "minutes": 60, "questions": 48,
        "streams": {"mock": {"title": f"{t} Mock", "sections": [(k, {tp[0]: tp[3] for tp in topics})]}}}
    for k, t, _, topics in SECTIONS
}

doc = {
    "sections": [
        {"key": k, "title": t, "group": g, "topics": [
            {"key": tk, "prefix": p, "title": tt, "test": n * PAPERS, "practice": b, "scope": s} for tk, p, tt, n, b, s in topics
        ]} for k, t, g, topics in SECTIONS
    ],
    "modes": {m: {**v, "streams": {s: {"title": d["title"], "sections": [{"section": k, "quota": q} for k, q in d["sections"]]} for s, d in v["streams"].items()}} for m, v in MODES.items()},
    "papers": PAPERS,
}
for k, _, _, topics in SECTIONS:
    assert sum(t[3] for t in topics) == 48, k
prefixes = [t[1] for *_, ts in SECTIONS for t in ts]
assert len(prefixes) == len(set(prefixes)), "duplicate prefix"
(ROOT / "content/blueprint.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print("test", sum(t[3] for *_, ts in SECTIONS for t in ts) * PAPERS, "practice", sum(t[4] for *_, ts in SECTIONS for t in ts))
