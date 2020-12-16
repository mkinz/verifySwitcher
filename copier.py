from shutil import copyfile
import sys

class Copier:

    def copy_prod_machine_files_to_verify(self):
        try:
            copyfile('/apps/fractureResources/machineFiles/sfc9mhbp02.prod', '/apps/fractureResources/machineFiles/sfc9mhbp02.vrfy')
            copyfile('/apps/fractureResources/machineFiles/sfc9mhtvp01.prod', '/apps/fractureResources/machineFiles/sfc9mhtvp01.vrfy')
            copyfile('/apps/fractureResources/machineFiles/sfc9mhtvp02.prod', '/apps/fractureResources/machineFiles/sfc9mhtvp02.vrfy')
            copyfile('/apps/fractureResources/machineFiles/sfc9mhlsfmp01.prod', '/apps/fractureResources/machineFiles/sfc9mhlsfmp01.vrfy')
        except PermissionError:
            print(f'a machine file cannot be written, do you have write permissions?')
            sys.exit(0)
        except FileNotFoundError:
            print(f'machine files not found; are you sure that you are in the correct directory?')
            sys.exit(0)

    def copier_test(self):
        copyfile('switcher_app.py', 'total_test_bs_file.py')


