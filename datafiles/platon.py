"""
:: Moiety_Formula = C24 H27 Au Cl N P, C H2 Cl2, Cl
"""
#  ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  daniel.kratzert@ac.uni-freiburg.de> wrote this file.  As long as you retain
#  this notice you can do whatever you want with this stuff. If we meet some day,
#  and you think this stuff is worth it, you can buy me a beer in return.
#  Dr. Daniel Kratzert
#  ----------------------------------------------------------------------------

import os
import stat
import subprocess
from pathlib import Path
from time import sleep

from tools.pupdate import get_platon


class Platon():
    def __init__(self, file: Path, force=False):
        self.cif_fileobj = file
        curdir = Path(os.curdir).absolute()
        self.chkfile = Path(self.cif_fileobj.stem + '.chk')
        os.chdir(self.cif_fileobj.absolute().parent)
        self.chk_filename = ''
        if not self.chkfile.exists() or force:
            try:
                self.run_platon(self.chkfile)
            except Exception as e:
                print('Platon failed to run:')
                print(e)
                return
        else:
            self.chk_filename = self.chkfile.absolute()
        self.chk_file_text = self.chkfile.read_text(encoding='ascii', errors='ignore')
        self.formula_moiety = ''
        self.parse_file()
        try:
            self.vrf_txt = Path(self.cif_fileobj.stem + '.vrf').read_text(encoding='ascii')
        except FileNotFoundError:
            self.vrf_txt = ''
        sleep(2)
        # delete orphaned files:
        for ext in ['.ckf', '.fcf', '.def', '.lis', '.sar', '.ckf', '.sum', '.hkp', '.pjn', '.bin', '_pl.res',
                    '_pl.spf']:
            try:
                file = Path(self.cif_fileobj.stem + ext)
                if file.stat().st_size < 100:
                    file.unlink()
                if file.suffix in ['.sar', '_pl.res', '_pl.spf', '.ckf']:
                    file.unlink()
            except FileNotFoundError:
                print('##')
                pass
        os.chdir(curdir.absolute())

    def parse_file(self):
        """
        """
        for num, line in enumerate(self.chk_file_text.splitlines(keepends=False)):
            if line.startswith('# MoietyFormula'):
                self.formula_moiety = ' '.join(line.split(' ')[2:])

    def run_platon(self, chkfile: Path):
        """
        >>> fname = Path(r'/Users/daniel/GitHub/FinalCif/test-data/DK_zucker2_0m.cif')
        >>> Platon(fname)
        Platon:
        C12 H22 O11
        """
        plat = None
        os.chdir(self.cif_fileobj.absolute().parent)
        timeticks = 0
        try:
            # This is only available on windows:
            si = subprocess.STARTUPINFO()
            si.dwFlags = 1
            si.wShowWindow = 0
        except AttributeError:
            si = None
        try:
            print('trying local platon')
            plat = subprocess.Popen([r'platon.exe', '-u', self.cif_fileobj.name], startupinfo=si)
        except Exception as e:
            print('Could not run local platon:', e)
            return 
            # a fresh platon exe from the web:
            # this runs only wif salflibc.dll. I have to find a solution to download it.
            # Here is the link to salflib: http://www.chem.gla.ac.uk/~louis/software/dll/salflibc.dll
            #pexe = get_platon()
            #is_exec = stat.S_IXUSR & os.stat(Path(pexe).absolute())[stat.ST_MODE]
            #if pexe and is_exec:
            #    try:
            #        plat = subprocess.Popen([pexe, '-u', self.cif_fileobj.name], startupinfo=si,
            #                                stdout=subprocess.DEVNULL)
            #    except Exception as e:
            #        print('Downloaded platon not found:', e)
            #        return
            #else:
            #    return
                # waiting for chk file to appear:
        #plat.wait(50)
        while not chkfile.is_file():
            timeticks = timeticks + 1
            sleep(0.01)
            if timeticks > 8:
                print('Platon statup took too long. Killing Platon...')
                try:
                    print('Platon took too much time, terminating platon. (1)')
                    plat.terminate()
                    raise FileNotFoundError
                except Exception as e:
                    print(e)
                    raise Exception
        size1 = chkfile.stat().st_size
        size2 = 99999999
        timeticks = 0
        # waiting until size does not increase anymore:
        while size1 <= size2:
            timeticks = timeticks + 1
            size2 = chkfile.stat().st_size
            # print(size1, size2)
            sleep(0.1)
            size1 = chkfile.stat().st_size
            if timeticks > 250:
                try:
                    print('Platon took too much time, terminating platon. (2)')
                    plat.terminate()
                    break
                except Exception:
                    pass
                    break
        try:
            plat.terminate()
        except Exception as e:
            print('foo')
            print(e)

    def __repr__(self):
        return 'Platon:\n{}'.format(self.formula_moiety)


if __name__ == '__main__':
    os.chdir("/Users/daniel/GitHub")
    fname = Path(r'/Users/daniel/GitHub/FinalCif/test-data/DK_zucker2_0m.cif')
    s = Platon(fname)
    print(s)
    print(s.chkfile)
    # print(s.chk_file_text)
    # chkfile = Path(fname.stem + '.chk')
    # chkfile.unlink()
