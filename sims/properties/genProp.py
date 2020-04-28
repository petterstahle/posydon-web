def genProp(object):
    """This function takes simulation properties arguments in the form of database fields represented by the SimProp model object (which the SimPropGenView view handles), and outputs the simulation properties in the form of a dictionary, which can then be passed as the kwargs to the SimulationProperties function.

    Example of passing kwargs to SimulationProperties:
    prop = SimulationProperties(
        flow=properties[flow],
        step_cosmic=CosmicBSE(*properties[step_cosmic]),
        step_mesa=step_MESA(**properties[step_mesa]),
        step_end=properties[step_end],
        max_time=properties[max_time]
        )
    """

    properties = {
        'flow' : object.flow,
        #step_cosmic args are passed as positional *args in CosmicBSE function
        'step_cosmic' : [object.cosmic_end, object.cosmic_evolve_dict],
        #step_mesa args are passed as **kwargs in step_MESA function
        'step_mesa': {
            'mechanism': object.mesa_mechanism,
            'sigma_kick': object.mesa_sigma_kick,
            'phi': object.mesa_phi,
            'cos_theta': object.mesa_cos_theta,
            'mean_anomaly': object.mesa_mean_anomaly,
            'mass_central_BH': object.mesa_mass_central_BH,
            'neutrino_mass_loss_fraction': object.mesa_neutrino_mass_loss_fraction,
            'neutrino_AM_loss': object.mesa_neutrino_AM_loss,
            'PISN': object.mesa_PISN,
            'log_scale': object.mesa_log_scale,
            'verbose': object.mesa_verbose
        },
        'step_end' : object.step_end,
        'max_time' : object.max_time
    }

    return properties
