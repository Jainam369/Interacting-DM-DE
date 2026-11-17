import numpy as np
from cobaya.theories.classy import classy


class CoupledAxionClassy(classy):
    """
    Thin wrapper around Cobaya's classy theory, composing the
    scf_parameters string and Omega_scf_shoot_fa target from the
    sampled Omega_c, beta_axion, log_mphi_H0, delta_i parameters,
    before handing everything to the underlying classy instance.
    """


    def calculate(self, state, want_derived=True, **params_values_dict):
        # Pull out our custom sampled parameters
        delta_i = params_values_dict.pop("delta_i")
        Omega_c = params_values_dict.pop('Omega_c')
        beta_axion = params_values_dict.pop('beta_axion')
        log_mphi_H0 = params_values_dict.pop('log_mphi_H0')
        H0 = params_values_dict.get('H0')
        omega_b = params_values_dict.get('omega_b')

        # Derived/composed quantities
        theta_i = np.pi - delta_i
        m_axion = 10 ** log_mphi_H0
        omega_idm = Omega_c * (H0 / 100.0) ** 2

        # Rough target for Omega_scf closure (radiation contribution kept
        # as the same small constant used throughout validation tonight)
        Omega_scf_target = 1.0 - (omega_b / (H0 / 100.0) ** 2) - Omega_c - 9.2e-5

        params_values_dict['omega_idm'] = omega_idm
        params_values_dict['m_axion'] = m_axion
        params_values_dict['Omega_scf_shoot_fa'] = Omega_scf_target
        params_values_dict['scf_parameters'] = f'{theta_i}, 0'
        params_values_dict['beta_axion'] = beta_axion




        result = super().calculate(state, want_derived=want_derived, **params_values_dict)

        return result

