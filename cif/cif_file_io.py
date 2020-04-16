#  ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  daniel.kratzert@ac.uni-freiburg.de> wrote this file.  As long as you retain
#  this notice you can do whatever you want with this stuff. If we meet some day,
#  and you think this stuff is worth it, you can buy me a beer in return.
#  Dr. Daniel Kratzert
#  ----------------------------------------------------------------------------
import re
import textwrap
from pathlib import Path
# noinspection PyUnresolvedReferences
from typing import Dict, List, Tuple, Union

import gemmi

from cif.cif_order import order, special_keys
from datafiles.utils import DSRFind
from tools.misc import essential_keys, non_centrosymm_keys


def quote(string: str, wrapping=80) -> str:
    """
    Quotes a cif string and wrapps it. The shorter strings are directly handled by cif.quote().
    """
    if len(string) < 80:
        return gemmi.cif.quote(string)
    lines = '\n'
    for line in string.split('\n'):
        if len(line) > wrapping:
            line = textwrap.fill(line, width=wrapping)
            lines += line + '\n'
        else:
            lines += line + '\n'
    quoted = gemmi.cif.quote(lines.rstrip('\n'))
    return quoted


charcters = {'°'      : r'\%',
             '±'      : r'+-',
             '×'      : r'\\times',
             '≠'      : r'\\neq',
             '→'      : '\\rightarrow',
             '←'      : '\\leftarrow',
             '∞'      : '\\infty',
             '≈'      : '\\sim',
             '≃'      : '\\simeq',
             'ß'      : r'\&s',
             'ü'      : r'u\"',
             'ö'      : r'o\"',
             'ä'      : r'a\"',
             'é'      : r"\'e",
             'è'      : r'\`e',
             'ó'      : r"\'o",
             'ò'      : r'\`o',
             'ȯ'      : r'\.o',
             'ø'      : r'\/o',
             'á'      : r'\'a',
             'à'      : r'\`a',
             'â'      : r'\^a',
             'å'      : r'\%a',
             'ê'      : r'\^e',
             'î'      : r'\^i',
             'ô'      : r'\^o',
             'û'      : r'\^u',
             'ç'      : r'\,c',
             'ñ'      : r'\~n',
             'ł'      : r'\/l',
             'đ'      : r'\/d',
             u'\u2079': r'^9^',
             u'\u2078': r'^8^',
             u'\u2077': r'^7^',
             u'\u2076': r'^6^',
             u'\u2075': r'^5^',
             u'\u2074': r'^4^',
             u'\u00B3': r'^3^',
             u'\u00B2': r'^2^',
             u'\u2081': r'~1~',
             u'\u2082': r'~2~',
             u'\u2083': r'~3~',
             u'\u2084': r'~4~',
             u'\u2085': r'~5~',
             u'\u2086': r'~6~',
             u'\u2087': r'~7~',
             u'\u2088': r'~8~',
             u'\u2089': r'~9~',
             u'\u0131': r'\?i',
             u"\u03B1": r'\a',  # alpha
             u"\u03B2": r'\b',  # beta
             u"\u03B3": r'\g',  # ...
             u"\u03B4": r'\d',
             u"\u03B5": r'\e',
             u"\u03B6": r'\z',
             u"\u03B7": r'\h',
             u"\u03B8": r'\q',
             u"\u03B9": r'\i',
             u"\u03BA": r'\k',
             u"\u03BB": r'\l',
             u"\u03BC": r'\m',
             u"\u03BD": r'\n',
             u"\u03BE": r'\x',
             u"\u03BF": r'\o',
             u"\u03C0": r'\p',
             u"\u03C1": r'\r',
             u"\u03C3": r'\s',
             u"\u03C4": r'\t',
             u"\u03C5": r'\u',
             u"\u03C6": r'\F',
             u"\u03C9": r'\w',
             u"\u03A9": r'\W',
             u"\u03D5": r'\f',
             # "1̄": r'\=1',  # Does not work in QT?
             }  # , r'\r\n': chr(10)}


def set_pair_delimited(block, key: str, txt: str):
    """
    Converts special characters to their markup counterparts.
    """
    txt = utf8_to_str(txt)
    try:
        # bad hack to get the numbered values correct
        float(txt)
        block.set_pair(key, txt)
    except (TypeError, ValueError):
        # prevent _key '?' in cif:
        if txt == '?':
            block.set_pair(key, txt)
        else:
            block.set_pair(key, quote(txt))


def utf8_to_str(txt):
    """
    Translates an utf-8 text to a CIF ascii string.
    :param txt: utf-8 text
    :return: delimited ascii string
    """
    for char in txt:
        if char in charcters:
            txt = txt.replace(char, charcters[char])
    return txt


def cifstr_to_utf8(txt: str) -> str:
    """
    Translates delimited cif characters back to unicode characters.
    >>> cifstr_to_utf8("Crystals were grown from thf at -20 \%C.")
    'Crystals were grown from thf at -20 °C.'
    """
    inv_map = {v: k for k, v in charcters.items()}
    for char in inv_map.keys():
        txt = txt.replace(char, inv_map[char])
    return txt


class CifContainer():
    """
    This class holds the content of a cif file, independent of the file parser used.
    """

    def __init__(self, file: Path):
        self.fileobj = file
        # I do this in small steps instead of gemmi.cif.read_file() in order to
        # leave out the check_for_missing_values. This was gemmi reads cif files
        # with missing values.
        self.doc = self.read_file(str(self.fileobj.absolute()))
        self.block = self.doc.sole_block()
        # will not ok with non-ascii characters in the res file:
        self.chars_ok = True
        try:
            self.resdata = self.block.find_value('_shelx_res_file')
        except UnicodeDecodeError:
            # This is a fallback in case _shelx_res_file has non-ascii characters.
            print('File has non-ascii characters. Switching to compatible mode.')
            self.doc = self.read_string(self.fileobj.read_text(encoding='cp1250', errors='ignore'))
            self.block = self.doc.sole_block()
            self.resdata = self.block.find_value('_shelx_res_file')
            self.chars_ok = False
        self.doc.check_for_duplicates()
        self.hkl_extra_info = self.abs_hkl_details()
        d = DSRFind(self.resdata)
        self.order = order
        self.dsr_used = d.dsr_used
        self.atomic_struct = gemmi.make_small_structure_from_block(self.block)
        # A dictionary to convert Atom names like 'C1_2' or 'Ga3' into Element names like 'C' or 'Ga'
        self._name2elements = dict(
            zip(self.block.find_loop('_atom_site_label'), self.block.find_loop('_atom_site_type_symbol')))

    def read_file(self, path: str) -> gemmi.cif.Document:
        """
        Reads a cif file and returns a gemmi document object.
        :param path: path to the file
        :return: gemmi document
        """
        doc = gemmi.cif.Document()
        doc.source = path
        doc.parse_file(path)
        return doc

    def read_string(self, cif_string: str) -> gemmi.cif.Document:
        """
        Reads a cif file from a string and returns a gemmi cif docment.
        :param cif_string: cif as string
        :return: gemmi document
        """
        doc = gemmi.cif.Document()
        doc.parse_string(cif_string)
        return doc

    def __getitem__(self, item: str) -> str:
        result = self.block.find_value(item)
        if result:
            if result == '?' or result == "'?'":
                return ''
            # TODO: can I do this?:
            # return retranslate_delimiter(result)
            return gemmi.cif.as_string(result)
        else:
            return ''

    def __delitem__(self, key):
        self.block.find_pair_item(key).erase()

    def save(self, filename: str = None) -> None:
        """
        Saves the current cif file in the specific order of the order list.
        :param filename:  Name to save cif file to.
        """
        if not filename:
            filename = str(self.fileobj.absolute())
        for key in reversed(self.order):
            try:
                self.block.move_item(self.block.get_index(key), 0)
            except RuntimeError:
                pass
                # print('Not in list:', key)
        # make sure hkl file and res file are at the end if the cif file:
        for key in special_keys:
            try:
                self.block.move_item(self.block.get_index(key), -1)
            except RuntimeError:
                continue
        self.doc.write_file(filename, gemmi.cif.Style.Indent35)
        # Path(filename).write_text(self.doc.as_string(gemmi.cif.Style.Indent35))

    def abs_hkl_details(self) -> Dict[str, str]:
        """
        This method tries to determine the information witten at the end of a cif hkl file by sadabs.
        """
        hkl = None
        all = {'_exptl_absorpt_process_details' : '',
               '_exptl_absorpt_correction_type' : '',
               '_exptl_absorpt_correction_T_max': '',
               '_exptl_absorpt_correction_T_min': '',
               '_computing_structure_solution'  : '',
               }
        try:
            hkl = self.block.find_value('_shelx_hkl_file')[:-1]
        except Exception:
            pass
        if not hkl:
            return all
        hkl = hkl[hkl.find('  0   0   0    0'):].split('\n')[1:]
        hkl = 'data_hkldat\n' + '\n'.join(hkl)
        # in-html cif has ')' instead of ';':
        hkl = [re.sub(r'^\)', ';', x) for x in hkl.split('\n')]
        # the keys have a blank char in front:
        hkl = [re.sub(r'^ _', '_', x) for x in hkl]
        hkl = '\n'.join(hkl)
        try:
            hkldoc = gemmi.cif.read_string(hkl)
            hklblock = hkldoc.sole_block()
        except Exception as e:
            print('Unable to get information from hkl foot.')
            print(e)
            return all
        for key in all:
            val = hklblock.find_value(key)
            if val:
                all[key] = gemmi.cif.as_string(val).strip()
        return all

    @property
    def Z_value(self):
        return self.atomic_struct.cell.volume / self.atomic_struct.cell.volume_per_image()

    @property
    def solution_program_details(self) -> str:
        return self.hkl_extra_info['_computing_structure_solution']

    @property
    def absorpt_process_details(self) -> str:
        return self.hkl_extra_info['_exptl_absorpt_process_details']

    @property
    def absorpt_correction_type(self) -> str:
        return self.hkl_extra_info['_exptl_absorpt_correction_type']

    @property
    def absorpt_correction_T_max(self) -> str:
        return self.hkl_extra_info['_exptl_absorpt_correction_T_max']

    @property
    def absorpt_correction_T_min(self) -> str:
        return self.hkl_extra_info['_exptl_absorpt_correction_T_min']

    def _spgr(self) -> gemmi.SpaceGroup:
        if self.symmops:
            symm_ops = self.symmops
        else:
            symm_ops = self.symmops_from_spgr
        return gemmi.find_spacegroup_by_ops(gemmi.GroupOps([gemmi.Op(o) for o in symm_ops]))

    @property
    def space_group(self) -> str:
        """
        Returns the space group from the symmetry operators.
        spgr.short_name() gives the short name.
        """
        try:
            return self._spgr().xhm()
        except (AttributeError, RuntimeError):
            if self['_space_group_name_H-M_alt']:
                return self['_space_group_name_H-M_alt'].strip("'")
            else:
                return ''

    @property
    def symmops_from_spgr(self) -> List[str]:
        # _symmetry_space_group_name_Hall
        space_group = None
        if self['_space_group_name_H-M_alt']:
            space_group = self['_space_group_name_H-M_alt']
        if self['_symmetry_space_group_name_H-M']:
            space_group = self['_symmetry_space_group_name_H-M']
        if not space_group:
            return []
        ops = [op.triplet() for op in
               gemmi.find_spacegroup_by_name(gemmi.cif.as_string(space_group)).operations()]
        return ops

    @property
    def spgr_number_from_symmops(self) -> int:
        return self._spgr().number

    @property
    def crystal_system(self) -> str:
        return self._spgr().crystal_system_str()

    @property
    def hall_symbol(self) -> str:
        return self._spgr().hall

    @property
    def hkl_checksum_calcd(self) -> int:
        """
        Calculates the shelx checksum for the hkl file content of a cif file.

        #>>> c = CifContainer(Path('test-data/DK_zucker2_0m.cif'))
        #>>> c.hkl_checksum_calcd
        #69576
        #>>> c = CifContainer(Path('test-data/4060310.cif'))
        #>>> c.hkl_checksum_calcd
        #0
        """
        hkl = self.block.find_value('_shelx_hkl_file')
        if hkl:
            return self.calc_checksum(hkl[1:-1])
        else:
            return 0

    @property
    def res_checksum_calcd(self) -> int:
        """
        Calculates the shelx checksum for the res file content of a cif file.

        #>>> c = CifContainer(Path('test-data/DK_zucker2_0m.cif'))
        #>>> c.res_checksum_calcd
        #52593
        #>>> c = CifContainer(Path('test-data/4060310.cif'))
        #>>> c.res_checksum_calcd
        #0
        """
        res = self.block.find_value('_shelx_res_file')
        if res:
            return self.calc_checksum(res[1:-1])
        return 0

    @staticmethod
    def calc_checksum(input_str: str) -> int:
        """
        Calculates the shelx checksum of a cif file.
        """
        sum = 0
        try:
            input_str = input_str.encode('cp1250', 'ignore')
        except Exception:
            input_str = input_str.encode('ascii', 'ignore')
        for char in input_str:
            # print(char)
            if char > 32:  # ascii 32 is space character
                sum += char
        sum %= 714025
        sum = sum * 1366 + 150889
        sum %= 714025
        sum %= 100000
        return sum

    @property
    def symmops(self) -> List[str]:
        """
        Reads the symmops from the cif file.

        >>> cif = CifContainer(Path('test-data/DK_ML7-66-final.cif'))
        >>> cif.symmops
        ['x, y, z', '-x, -y, -z']
        """
        xyz1 = self.block.find(("_symmetry_equiv_pos_as_xyz",))  # deprecated
        xyz2 = self.block.find(("_space_group_symop_operation_xyz",))  # New definition
        if xyz1:
            return [i.str(0) for i in xyz1]
        elif xyz2:
            return [i.str(0) for i in xyz2]
        else:
            return []

    @property
    def is_centrosymm(self) -> bool:
        """
        >>> from cif.cif_file_io import CifContainer
        >>> from pathlib import Path
        >>> c = CifContainer(Path('test-data/DK_zucker2_0m-finalcif.cif'))
        >>> c.is_centrosymm
        False
        >>> c = CifContainer(Path('test-data/DK_ML7-66-final.cif'))
        >>> c.is_centrosymm
        True
        """
        ops = gemmi.GroupOps([gemmi.Op(o) for o in self.symmops])
        return ops.is_centric()

    def atoms_loop(self) -> Tuple[str, str, str, str, str, str, str, str]:
        labels = self.block.find_loop('_atom_site_label')
        types = self.block.find_loop('_atom_site_type_symbol')
        x = self.block.find_loop('_atom_site_fract_x')
        y = self.block.find_loop('_atom_site_fract_y')
        z = self.block.find_loop('_atom_site_fract_z')
        part = self.block.find_loop('_atom_site_disorder_group')
        occ = self.block.find_loop('_atom_site_occupancy')
        u_eq = self.block.find_loop('_atom_site_U_iso_or_equiv')
        for label, type, x, y, z, part, occ, ueq in zip(labels, types, x, y, z, part, occ, u_eq):
            #         0    1   2  3  4   5   6     7
            yield label, type, x, y, z, part, occ, ueq

    @property
    def atoms_fract(self) -> List:
        for at in self.atomic_struct.sites:
            yield [at.label, at.type_symbol, at.fract.x, at.fract.y, at.fract.z, at.disorder_group, at.occ, at.u_iso]

    @property
    def atoms_orth(self):
        cell = self.atomic_struct.cell
        for at in self.atomic_struct.sites:
            x, y, z = at.orth(cell)
            yield [at.label, at.type_symbol, x, y, z, at.disorder_group, at.occ, at.u_iso]

    @property
    def hydrogen_atoms_present(self) -> bool:
        for at in self.atomic_struct.sites:
            if at.type_symbol in ('H', 'D'):
                return True
        else:
            return False

    @property
    def disorder_present(self) -> bool:
        for at in self.atomic_struct.sites:
            if at.disorder_group:
                return True
        else:
            return False

    @property
    def cell(self) -> tuple:
        c = self.atomic_struct.cell
        return c.a, c.b, c.c, c.alpha, c.beta, c.gamma, c.volume

    def ishydrogen(self, label: str) -> bool:
        """Decide wether an atom name is of type hydrogen."""
        hydrogen = ('H', 'D')
        if self.iselement(label) in hydrogen:
            return True
        else:
            return False

    def bonds(self, without_H: bool = False):
        """
        Yields a list of bonds in the cif file.
        """
        label1 = self.block.find_loop('_geom_bond_atom_site_label_1')
        label2 = self.block.find_loop('_geom_bond_atom_site_label_2')
        dist = self.block.find_loop('_geom_bond_distance')
        symm = self.block.find_loop('_geom_bond_site_symmetry_2')
        for label1, label2, dist, symm in zip(label1, label2, dist, symm):
            if without_H and (self.ishydrogen(label1) or self.ishydrogen(label2)):
                continue
            else:
                yield (label1, label2, dist, symm)

    def angles(self, without_H: bool = False):
        label1 = self.block.find_loop('_geom_angle_atom_site_label_1')
        label2 = self.block.find_loop('_geom_angle_atom_site_label_2')
        label3 = self.block.find_loop('_geom_angle_atom_site_label_3')
        angle = self.block.find_loop('_geom_angle')
        symm1 = self.block.find_loop('_geom_angle_site_symmetry_1')
        symm2 = self.block.find_loop('_geom_angle_site_symmetry_3')
        for label1, label2, label3, angle, symm1, symm2 in zip(label1, label2, label3, angle, symm1, symm2):
            if without_H and (self.ishydrogen(label1) or self.ishydrogen(label2) or self.ishydrogen(label3)):
                continue
            else:
                yield (label1, label2, label3, angle, symm1, symm2)

    def iselement(self, name: str) -> str:
        return self._name2elements[name]

    def nbonds(self, without_h: bool = False) -> int:
        """
        Number of bonds in the cif object, with and without hydrogen atoms.
        """
        return len(list(self.bonds(without_h)))

    def nangles(self, without_h: bool = False) -> int:
        """
        Number of bond angles in the cif object, with and without hydrogen atoms.
        """
        return len(list(self.angles(without_h)))

    def ntorsion_angles(self, without_h: bool = False) -> int:
        """
        Number of torsion angles in the cif object, with and without hydrogen atoms.
        """
        return len(list(self.torsion_angles(without_h)))

    def torsion_angles(self, without_h: bool = False):
        label1 = self.block.find_loop('_geom_torsion_atom_site_label_1')
        label2 = self.block.find_loop('_geom_torsion_atom_site_label_2')
        label3 = self.block.find_loop('_geom_torsion_atom_site_label_3')
        label4 = self.block.find_loop('_geom_torsion_atom_site_label_4')
        torsang = self.block.find_loop('_geom_torsion')
        symm1 = self.block.find_loop('_geom_torsion_site_symmetry_1')
        symm2 = self.block.find_loop('_geom_torsion_site_symmetry_2')
        symm3 = self.block.find_loop('_geom_torsion_site_symmetry_3')
        symm4 = self.block.find_loop('_geom_torsion_site_symmetry_4')
        # publ = self.block.find_loop('_geom_torsion_publ_flag')
        for label1, label2, label3, label4, torsang, symm1, symm2, symm3, symm4 in \
                zip(label1, label2, label3, label4, torsang, symm1, symm2, symm3, symm4):
            if without_h and (self.ishydrogen(label1) or self.ishydrogen(label2)
                              or self.ishydrogen(label3) or self.ishydrogen(label3)):
                continue
            yield label1, label2, label3, label4, torsang, symm1, symm2, symm3, symm4

    def hydrogen_bonds(self):
        label_d = self.block.find_loop('_geom_hbond_atom_site_label_D')
        label_h = self.block.find_loop('_geom_hbond_atom_site_label_H')
        label_a = self.block.find_loop('_geom_hbond_atom_site_label_A')
        dist_dh = self.block.find_loop('_geom_hbond_distance_DH')
        dist_ha = self.block.find_loop('_geom_hbond_distance_HA')
        dist_da = self.block.find_loop('_geom_hbond_distance_DA')
        angle_dha = self.block.find_loop('_geom_hbond_angle_DHA')
        symm = self.block.find_loop('_geom_hbond_site_symmetry_A')
        # publ = self.block.find_loop('_geom_hbond_publ_flag')
        for label_d, label_h, label_a, dist_dh, dist_ha, dist_da, angle_dha, symm in zip(label_d, label_h, label_a,
                                                                                         dist_dh, dist_ha, dist_da,
                                                                                         angle_dha, symm):
            yield label_d, label_h, label_a, dist_dh, dist_ha, dist_da, angle_dha, symm

    def key_value_pairs(self):
        """
        Returns the key/value pairs of a cif file sorted by priority.

        >>> c = CifContainer(Path('test-data/P21c-final.cif'))
        >>> c.key_value_pairs()[:2]
        [['_audit_contact_author_address', '?'], ['_audit_contact_author_email', '?']]
        """
        high_prio_no_values, high_prio_with_values = self.get_keys()
        return high_prio_no_values + [['These below are already in:', '---------------------']] + high_prio_with_values

    def is_centrokey(self, key):
        """
        Is True if the kurrent key is only valid 
        for non-centrosymmetric structures
        """
        return self.is_centrosymm and key in non_centrosymm_keys

    def get_keys(self):
        """
        Returns the keys to be displayed in the main table as two separate lists.
        """
        questions = []
        # contains the answered keys:
        with_values = []
        # holds keys that are not in the cif file but in essential_keys:
        missing_keys = []
        for item in self.block:
            if item.pair is not None:
                key, value = item.pair
                if len(value) > 1000:
                    # do not include res and hkl file:
                    continue
                if key.startswith('_shelx'):
                    continue
                if self.is_centrokey(key):
                    continue
                if not value or value == '?' or value == "'?'":
                    questions.append([key, value])
                else:
                    with_values.append([key, value])
        all_keys = [x[0] for x in with_values] + [x[0] for x in questions]
        # check if there are keys not in the cif but in essential_keys:
        for key in essential_keys:
            if key not in all_keys:
                if self.is_centrokey(key):
                    continue
                questions.append([key, '?'])
                missing_keys.append(key)
        for k in missing_keys:
            if self.is_centrokey(k):
                continue
            self.block.set_pair(k, '?')
        return sorted(questions), sorted(with_values)

    def add_to_cif(self, key: str, value: str = '?'):
        """
        Add an additional key value pair to the cif block.
        """
        self.block.set_pair(key, value)
