
from classy import Class

cosmo = Class()
cosmo.set({
    'root': 'output/CA_',
    'write background': 'yes',
    'write parameters': 'yes',
    'k_output_values': 0.001,
    'h': 0.6756,
    'omega_b': 0.02237,
    'n_s': 0.9649,
    'A_s': 2.1e-9,
    'tau_reio': 0.0544,

    'Omega_cdm': 0,
    'omega_idm': 0.1199,

    'scf_potential': 'axion',
    'n_axion': 1.0,
    'Omega_scf_shoot_fa': 0.6847,
    'm_axion': 1.88,
    'scf_parameters': '1.737, 0',
    'scf_evolve_as_fluid': 'no',
    'scf_evolve_like_axionCAMB': 'no',
    'scf_has_perturbations': 'yes',
    'use_big_theta_scf': 'no',
    'use_delta_scf_over_1plusw': 'no',
    'include_scf_in_delta_m': 'no',
    'attractor_ic_scf': 'no',

    'loop_over_background_for_closure_relation': 'yes',
    'precision_loop_over_background': 1e-2,
    'beta_axion': 0.068,
    'DMDE_interaction': 0,

    'evolver': 0,
    'gauge': 'synchronous',

    'input_verbose': 1,
    'background_verbose': 1,
    'output_verbose': 1,
    'perturbations_verbose': 1,
})
print("About to compute...")
cosmo.compute()
print("Computed successfully!")