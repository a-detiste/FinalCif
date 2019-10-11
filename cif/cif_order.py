special_keys = ['_iucr_refine_instructions_details',
                '_iucr_refine_reflections_details',
                '_shelx_res_file', '_shelx_res_checksum',
                '_shelx_hkl_file', '_shelx_hkl_checksum',
                '_shelx_fab_file', '_shelx_fab_checksum',
                '_refln_index_h',
                '_refln_index_k',
                '_refln_index_l',
                '_refln_F_meas',
                '_refln_F_squared_meas',
                '_refln_F_sigma',
                '_refln_F_squared_sigma',
                '_refln_F_calc',
                '_refln_F_squared_calc',
                ]

order = [
    '_journal_data_validation_number',
    '_journal_date_recd_electronic',
    '_journal_date_to_coeditor',
    '_journal_date_from_coeditor',
    '_journal_date_accepted',
    '_journal_date_printers_first',
    '_journal_date_printers_final',
    '_journal_date_proofs_out',
    '_journal_date_proofs_in',
    '_journal_coeditor_name',
    '_journal_coeditor_code',
    '_journal_coeditor_notes',
    '',
    '_journal_techeditor_code',
    '_journal_techeditor_notes',
    '',
    '_journal_coden_ASTM',
    '_journal_name_full',
    '_journal_year',
    '_journal_volume',
    '_journal_issue',
    '_journal_page_first',
    '_journal_page_last',
    '_journal_paper_category',
    '_journal_suppl_publ_number',
    '_journal_suppl_publ_pages',

    '_publ_author_name',
    '_publ_author_footnote',
    '_publ_author_address',
    '_publ_section_title',
    '_publ_section_title_footnote',
    '_publ_section_synopsis',
    '_publ_section_abstract',
    '_publ_body_element',
    '_publ_body_title',
    '_publ_body_contents',
    '_publ_section_comment',
    '_publ_section_acknowledgements',
    '_publ_section_references',
    '_publ_section_figure_captions',
    '_publ_section_exptl_prep',
    '_publ_section_exptl_refinement',
    '_journal_coden_ASTM',
    '_journal_issue',
    '_journal_name_full',
    '_journal_page_first',
    '_journal_page_last',
    '_journal_paper_doi',
    '_journal_volume',
    '_journal_year',
    '_publ_contact_author_name',
    '_publ_contact_author_address',
    '_publ_contact_author_email',
    '_publ_contact_author_fax',
    '_publ_contact_author_phone',
    '_publ_contact_letter',
    '_publ_requested_journal',
    '_publ_requested_category',

    '_audit_contact_author_address',
    '_audit_contact_author_email',
    '_audit_contact_author_name',
    '_audit_contact_author_phone',
    '_publ_contact_author_id_orcid',
    '_audit_creation_method',

    '_shelx_SHELXL_version_number',
    '_chemical_name_systematic',
    '_chemical_name_common',
    '_chemical_formula_sum',
    '_chemical_formula_moiety',
    '_chemical_formula_structural',
    '_chemical_formula_analytical',
    '_chemical_formula_iupac',
    '_chemical_formula_weight',
    '_chemical_melting_point',

    '_chemical_absolute_configuration',
    '_chemical_properties_biological',
    '_chemical_properties_physical',

    '_symmetry_cell_setting',  # superseeded by _space_group_crystal_system
    '_space_group_crystal_system',
    '_symmetry_Int_Tables_number',  # superseeded by '_space_group_IT_number'
    '_space_group_IT_number',
    '_symmetry_space_group_name_H-M',  # superseeded by _space_group_name_H-M_alt
    '_space_group_name_H-M_alt',
    '_space_group_name_Hall',
    '_symmetry_space_group_name_Hall',  # superseeded by _space_group_name_Hall
    '_shelx_space_group_comment',
    '_symmetry_equiv_pos_site_id',  # superseeded by '_space_group_symop_id'
    '_symmetry_equiv_pos_as_xyz',  # superseeded by '_space_group_symop_operation_xyz'
    '_space_group_symop_id',
    '_space_group_symop_operation_xyz',
    '_cell_length_a',
    '_cell_length_b',
    '_cell_length_c',
    '_cell_angle_alpha',
    '_cell_angle_beta',
    '_cell_angle_gamma',
    '_cell_volume',
    '_cell_formula_units_Z',
    '_cell_measurement_temperature',
    '_cell_measurement_reflns_used',
    '_cell_measurement_theta_min',
    '_cell_measurement_theta_max',
    '_exptl_crystal_description',
    '_exptl_crystal_colour',
    '_exptl_crystal_recrystallization_method',
    '_exptl_crystal_density_meas',
    '_exptl_crystal_density_method',
    '_exptl_crystal_density_diffrn',
    '_exptl_crystal_F_000',
    '_exptl_crystal_size_max',
    '_exptl_crystal_size_mid',
    '_exptl_crystal_size_min',
    '_exptl_crystal_size_rad',
    '_exptl_absorpt_coefficient_mu',
    '_exptl_absorpt_correction_type',
    '_exptl_absorpt_correction_T_min',
    '_exptl_absorpt_correction_T_max',
    '_exptl_absorpt_process_details',
    '_exptl_absorpt_special_details',
    '_shelx_estimated_absorpt_T_min',
    '_shelx_estimated_absorpt_T_max',
    '_exptl_transmission_factor_min',
    # http://oldwww.iucr.org/iucr-top/cif/cifdic_html/1/cif_core.dic/Iexptl_transmission_factor_min.html
    '_exptl_transmission_factor_max',
    '_exptl_special_details',
    '_diffrn_ambient_temperature',
    '_diffrn_ambient_environment',
    '_diffrn_radiation_type',
    '_diffrn_radiation_wavelength',
    '_diffrn_radiation_source',  # superseeded by _diffrn_source
    '_diffrn_radiation_monochromator',
    '_olex2_diffrn_ambient_temperature_device',
    '_diffrn_radiation_probe',
    '_diffrn_source',
    '_diffrn_source_type',
    '_diffrn_source_current',
    '_diffrn_source_voltage',
    '_diffrn_detector',
    '_diffrn_detector_type',
    '_diffrn_detector_area_resol_mean',
    '_diffrn_measurement_device',  # superseeded by _diffrn_measurement_device_type
    '_diffrn_measurement_device_type',
    '_diffrn_measurement_method',
    '_diffrn_measurement_specimen_support',
    '_diffrn_measurement_specimen_adhesive',
    '_diffrn_reflns_number',
    '_diffrn_reflns_av_unetI/netI',  # superseeded by '_diffrn_reflns_av_unetI/netI'
    '_diffrn_reflns_av_R_equivalents',
    '_diffrn_reflns_av_sigmaI/netI',
    '_diffrn_reflns_theta_min',
    '_diffrn_reflns_theta_max',
    '_diffrn_reflns_theta_full',
    '_diffrn_reflns_limit_h_min',
    '_diffrn_reflns_limit_h_max',
    '_diffrn_reflns_limit_k_min',
    '_diffrn_reflns_limit_k_max',
    '_diffrn_reflns_limit_l_min',
    '_diffrn_reflns_limit_l_max',
    '_diffrn_reflns_reduction_process',
    '_diffrn_standards_number',
    '_diffrn_standards_interval_count',
    '_diffrn_standards_interval_time',
    '_diffrn_standards_decay_%',
    '_diffrn_standard_refln_index_h',
    '_diffrn_standard_refln_index_k',
    '_diffrn_standard_refln_index_l',
    '_diffrn_measured_fraction_theta_max',
    '_diffrn_measured_fraction_theta_full',
    '_diffrn_reflns_Laue_measured_fraction_max',
    '_diffrn_reflns_Laue_measured_fraction_full',
    '_diffrn_reflns_point_group_measured_fraction_max',
    '_diffrn_reflns_point_group_measured_fraction_full',

    '_reflns_number_total',
    '_reflns_number_gt',
    '_reflns_threshold_expression',
    '_reflns_Friedel_coverage',
    '_reflns_Friedel_fraction_max',
    '_reflns_Friedel_fraction_full',
    '_reflns_special_details',

    '_computing_data_collection',
    '_computing_cell_refinement',
    '_computing_data_reduction',
    '_computing_structure_solution',
    '_computing_structure_refinement',
    '_computing_molecular_graphics',
    '_computing_publication_material',

    '_refine_special_details',
    '_refine_ls_structure_factor_coef',
    '_refine_ls_matrix_type',
    '_refine_ls_weighting_scheme',
    '_refine_ls_weighting_details',
    '_atom_sites_solution_primary',
    '_atom_sites_solution_secondary',
    '_atom_sites_solution_hydrogens',
    '_refine_ls_hydrogen_treatment',
    '_refine_ls_number_reflns',
    '_refine_ls_number_parameters',
    '_refine_ls_number_restraints',
    '_refine_ls_number_constraints',
    '_refine_ls_R_factor_all',
    '_refine_ls_R_factor_gt',
    '_refine_ls_wR_factor_all',
    '_refine_ls_wR_factor_ref',
    '_refine_ls_wR_factor_gt',
    '_refine_ls_goodness_of_fit_all',
    '_refine_ls_goodness_of_fit_ref',
    '_refine_ls_restrained_S_all',
    '_refine_ls_restrained_S_obs',
    '_refine_ls_shift/su_max',
    '_refine_ls_shift/su_mean',
    '_refine_diff_density_max',
    '_refine_diff_density_min',
    '_refine_diff_density_rms',
    '_refine_ls_extinction_method',
    '_refine_ls_extinction_coef',
    '_refine_ls_extinction_expression',
    '_refine_ls_abs_structure_Flack',
    '_refine_ls_abs_structure_details',
    '_refine_ls_abs_structure_Rogers',

    '_atom_type_symbol',
    '_atom_type_description',
    '_atom_type_scat_dispersion_real',
    '_atom_type_scat_dispersion_imag',
    '_atom_type_scat_source',

    '_geom_special_details',
    

]
