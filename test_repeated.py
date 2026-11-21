from classy import Class

params = {
    'h': 0.675, 'omega_b': 0.02237, 'n_s': 0.9649, 'A_s': 2.0989031673191437e-09,
    'tau_reio': 0.0544, 'omega_idm': 0.13878337500000001,
    'm_axion': 0.45081670454146017, 'scf_parameters': '2.302592653589793, 0',
    'Omega_scf_shoot_fa': 0.6462106063100137, 'beta_axion': 0.077,
    'scf_potential': 'axion', 'n_axion': 1.0, 'attractor_ic_scf': 'no',
    'do_shooting_scf': 'no', 'scf_evolve_as_fluid': 'no', 'scf_evolve_like_axionCAMB': 'no',
    'scf_has_perturbations': 'yes', 'use_big_theta_scf': 'no', 'use_delta_scf_over_1plusw': 'no',
    'include_scf_in_delta_m': 'no', 'loop_over_background_for_closure_relation': 'yes',
    'precision_loop_over_background': 0.01, 'DMDE_interaction': 0, 'evolver': 0,
    'gauge': 'synchronous', 'background_verbose': 1, 'input_verbose': 1,
    'non_linear': 'none', 'Omega_cdm': 0,
    'output': 'lCl pCl tCl', 'l_max_scalars': 2500.0, 'lensing': 'yes',
}

for i in range(3):
    print(f"=== Call {i+1} ===")
    cosmo = Class()
    cosmo.set(params)
    cosmo.compute()
    print(f"Call {i+1} succeeded!")
    cosmo.struct_cleanup()
    cosmo.empty()
    del cosmo
print("All calls succeeded")
