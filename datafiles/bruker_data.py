#  ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  daniel.kratzert@ac.uni-freiburg.de> wrote this file.  As long as you retain
#  this notice you can do whatever you want with this stuff. If we meet some day,
#  and you think this stuff is worth it, you can buy me a beer in return.
#  Dr. Daniel Kratzert
#  ----------------------------------------------------------------------------
from contextlib import suppress

from gemmi import cif as gcif

from cif.cif_file_io import CifContainer
from datafiles.bruker_frame import BrukerFrameHeader
from datafiles.data import WorkDataMixin
from datafiles.p4p_reader import P4PFile
from datafiles.sadabs import Sadabs
from datafiles.saint import SaintListFile
from datafiles.shelx import SolutionProgram


class MissingCifData():
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value


class BrukerData(WorkDataMixin, object):

    def __init__(self, app: 'AppWindow', cif: CifContainer):
        super(BrukerData, self).__init__()
        self.cif = cif
        self.app = app
        self.basename = cif.fileobj.stem.split('_0m')[0]
        self.saint_data = SaintListFile(name_patt='*_0*m._ls')
        # This is only in this list file, not in the global:
        saint_first_ls = SaintListFile(name_patt='*_01._ls')
        sol = SolutionProgram(cif)
        solution_program = None
        if 'shelx' in self.cif.block.find_value('_audit_creation_method').lower():
            shelx = 'Sheldrick, G.M. (2015). Acta Cryst. A71, 3-8.\nSheldrick, G.M. (2015). Acta Cryst. C71, 3-8.\n'
        else:
            shelx = ''
        if cif.resdata:
            if cif.dsr_used:
                dsr = 'The program DSR was used for model building:\n' \
                      'D. Kratzert, I. Krossing, J. Appl. Cryst. 2018, 51, 928-934. doi: 10.1107/S1600576718004508'
                shelx += dsr
        abstype = '?'
        t_min = '?'
        t_max = '?'
        # Going back from last dataset:
        for n in range(1, len(self.sadabs.datasets) + 1):
            try:
                abstype = 'numerical' if self.sadabs.dataset(-n).numerical else 'multi-scan'
                t_min = min(self.sadabs.dataset(-n).transmission)
                t_max = max(self.sadabs.dataset(-n).transmission)
                if all([abstype, t_min, t_max]):
                    break
            except (KeyError, AttributeError, TypeError):
                pass
                # print('No .abs file found.')
                # no abs file found
        # the lower temp is more likely:
        try:
            temp1 = self.frame_header.temperature
        except (AttributeError, KeyError, FileNotFoundError):
            temp1 = 293
        try:
            kilovolt = self.frame_header.kilovolts
        except (AttributeError, KeyError, FileNotFoundError):
            kilovolt = ''
        try:
            milliamps = self.frame_header.milliamps
        except (AttributeError, KeyError, FileNotFoundError):
            milliamps = ''
        try:
            frame_name = self.frame_header.filename.name
        except FileNotFoundError:
            frame_name = ''
        if self.cif.solution_program_details:
            solution_program = (self.cif.solution_program_details, self.cif.fileobj.name)
        if self.cif['_computing_structure_solution']:
            solution_program = (gcif.as_string(self.cif['_computing_structure_solution']), self.cif.fileobj.name)
        if not solution_program:
            solution_program = (sol.program.version, sol.program.filename)
        if self.cif.absorpt_process_details:
            absdetails = (self.cif.absorpt_process_details, self.cif.fileobj.name)
        else:
            absdetails = (self.sadabs.version, self.sadabs.filename.name)
        if self.cif.absorpt_correction_type:
            abscorrtype = (self.cif.absorpt_correction_type, self.cif.fileobj.name)
        else:
            abscorrtype = (abstype, self.sadabs.filename.name)
        if self.cif.absorpt_correction_T_max:
            abs_tmax = (self.cif.absorpt_correction_T_max, self.cif.fileobj.name)
        else:
            abs_tmax = (str(t_max), self.sadabs.filename.name)
        if self.cif.absorpt_correction_T_min:
            abs_tmin = (self.cif.absorpt_correction_T_min, self.cif.fileobj.name)
        else:
            abs_tmin = (str(t_min), self.sadabs.filename.name)

        if self.sadabs.Rint:
            rint = (self.sadabs.Rint, self.sadabs.filename.name)
        else:
            rint = ('', '')
        temp2 = self.p4p.temperature
        temperature = round(min([temp1, temp2]), 1)
        if temperature < 0.01:
            temperature = '?'
        if (self.cif['_diffrn_ambient_temperature'].split('(')[0] or
            self.cif['_cell_measurement_temperature']).split('(')[0] == '0':
            self.app.show_general_warning('<b>Warning</b>: You probably entered &minus;273.15 °C instead '
                                          'of &minus;173.15 °C into the SHELX file.<br>'
                                          'Zero temperature is likely to be wrong.')
        try:
            if abs(int(self.cif['_diffrn_ambient_temperature'].split('(')[0]) - int(temperature)) >= 2:
                self.app.show_general_warning('<b>Warning</b>: The temperature from the measurement and '
                                              'from SHELX differ. Please double-check for correctness.<br><br>'
                                              'SHELX says: {} K<br>'
                                              'P$P file says: {} K<br>'
                                              'Frame header says: {} K<br><br>'
                                              'You may add a '
                                              '<a href="http://shelx.uni-goettingen.de/shelxl_html.php#TEMP">TEMP</a> '
                                              'instruction to your SHELX file (in °C).'
                                              .format(self.cif['_diffrn_ambient_temperature'].split('(')[0],
                                                      round(temp2, 1),
                                                      round(temp1, 1)))
        except ValueError:
            # most probably one value is '?'
            pass
        # TODO: refrator space group things into a general method:
        spgr = '?'
        if not self.cif['_space_group_name_H-M_alt']:
            try:
                spgr = self.cif.space_group()
            except AttributeError:
                pass
        hallsym = '?'
        if not self.cif['_space_group_name_Hall']:
            with suppress(AttributeError):
                hallsym = self.cif.hall_symbol()
        spgrnum = '?'
        if not self.cif['_space_group_IT_number']:
            with suppress(AttributeError):
                spgrnum = self.cif.spgr_number_from_symmops()
        csystem = '?'
        if not self.cif['_space_group_crystal_system']:
            with suppress(AttributeError):
                csystem = self.cif.crystal_system()
        if self.saint_data.is_twin and self.saint_data.components_firstsample == 2 \
                and not self.cif['_twin_individual_twin_matrix_11']:
            with suppress(Exception):
                law = self.saint_data.twinlaw[list(self.saint_data.twinlaw.keys())[0]]
                self.sources['_twin_individual_twin_matrix_11'] = (str(law[0][1]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_12'] = (str(law[0][2]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_13'] = (str(law[0][0]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_21'] = (str(law[1][1]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_22'] = (str(law[1][2]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_23'] = (str(law[1][0]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_31'] = (str(law[2][1]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_32'] = (str(law[2][2]), self.saint_data.filename)
                self.sources['_twin_individual_twin_matrix_33'] = (str(law[2][0]), self.saint_data.filename)
                self.sources['_twin_individual_id']= (str(self.saint_data.components_firstsample), self.saint_data.filename)
                self.sources['_twin_special_details']= ('The data was integrated as a 2-component twin.', self.saint_data.filename)
        """
        #TODO: symmops are missing, need loops for that
        if not self.symmops:
            for x in reversed(self.symmops_from_spgr()):
                self.add_to_cif(cif_as_list, key=x, value='')
            self.add_to_cif(cif_as_list, key='_space_group_symop_operation_xyz', value='')
            self.add_to_cif(cif_as_list, key='_loop', value='')"""
        # All sources that are not filled with data will be yellow in the main table
        #                          data                         tooltip
        self.sources['_cell_measurement_reflns_used'] = (self.saint_data.cell_reflections, self.saint_data.filename.name)
        self.sources['_cell_measurement_theta_min'] = (
            self.saint_data.cell_res_min_theta or '', self.saint_data.filename.name)
        self.sources['_cell_measurement_theta_max'] = (
            self.saint_data.cell_res_max_theta or '', saint_first_ls.filename.name)
        self.sources['_computing_data_collection'] = (saint_first_ls.aquire_software, self.saint_data.filename.name)
        self.sources['_computing_cell_refinement'] = (self.saint_data.version, self.saint_data.filename.name)
        self.sources['_computing_data_reduction'] = (self.saint_data.version, self.saint_data.filename.name)
        self.sources['_exptl_absorpt_correction_type'] = abscorrtype
        self.sources['_exptl_absorpt_correction_T_min'] = abs_tmin
        self.sources['_exptl_absorpt_correction_T_max'] = abs_tmax
        self.sources['_diffrn_reflns_av_R_equivalents'] = rint
        self.sources['_cell_measurement_temperature'] = (temperature, self.p4p.filename.name)
        self.sources['_diffrn_ambient_temperature'] = (temperature, self.p4p.filename.name)
        self.sources['_exptl_absorpt_process_details'] = absdetails
        self.sources['_exptl_crystal_colour'] = (self.p4p.crystal_color, self.p4p.filename.name)
        self.sources['_exptl_crystal_description'] = (self.p4p.morphology, self.p4p.filename.name)
        self.sources['_exptl_crystal_size_min'] = (self.p4p.crystal_size[0] or '', self.p4p.filename.name)
        self.sources['_exptl_crystal_size_mid'] = (self.p4p.crystal_size[1] or '', self.p4p.filename.name)
        self.sources['_exptl_crystal_size_max'] = (self.p4p.crystal_size[2] or '', self.p4p.filename.name)
        self.sources['_computing_structure_solution'] = solution_program
        self.sources['_atom_sites_solution_primary'] = (sol.method, '')
        self.sources['_diffrn_source_voltage'] = (kilovolt or '', frame_name)
        self.sources['_diffrn_source_current'] = (milliamps or '', frame_name)
        self.sources['_chemical_formula_moiety'] = ('', '')
        self.sources['_publ_section_references'] = (shelx, '')
        self.sources['_refine_special_details'] = ('', '')
        self.sources['_exptl_crystal_recrystallization_method'] = ('', '')
        self.sources['_chemical_absolute_configuration'] = ('', '')
        self.sources['_space_group_name_H-M_alt'] = (spgr, 'calculated by gemmi')
        self.sources['_space_group_name_Hall'] = (hallsym, 'calculated by gemmi')
        self.sources['_space_group_IT_number'] = (spgrnum, 'calculated by gemmi')
        self.sources['_space_group_crystal_system'] = (csystem, 'calculated by gemmi')

    @property
    def sadabs(self):
        sad = Sadabs(basename='*.abs')
        # self.sad_fileLE, button = self.app.add_new_datafile(0, 'SADABS', 'add specific .abs file here, if needed...')
        # self.sad_fileLE.setText(str(sad.filename.absolute()))
        # button.clicked.connect(self.app.get_cif_file_block)
        # I have to run self.app.get_cif_file_block but data sources for abs file should be updated
        return sad

    @property
    def frame_header(self):
        return BrukerFrameHeader(self.basename, self.cif)

    @property
    def p4p(self):
        return P4PFile(self.basename, self.cif)
