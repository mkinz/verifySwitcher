import argparse
import sys

class Runner:
    
    def __init__(self, getter, writer, deleter, copier ):
        self.getter = getter
        self.writer = writer
        self.deleter = deleter
        self.copier = copier
    
    def run_it(self):
        # parse input for cats or mgc
        parser = self.getter.get_input((sys.argv[1:]), argparse.ArgumentParser())

        # run deleter to remove files before writing new ones
        self.deleter.remove_stuff("/apps/VRFY/dsg2nc/config/list*")

        # write files
        if parser.flag == 'cats':

            for key, values in self.getter.cats_pptypes.items():
                if key == 'cats_mebes':
                    for item in values:
                        self.writer.write_list_mebes_file(f'{item}\n')
                        self.writer.write_next_mebes_file(f'{item}\n')
                elif key == 'cats_cluster_mebes':
                    for item in values:
                        self.writer.write_list_cluster_mebes_file(f'{item}\n')
                        self.writer.write_next_cluster_mebes_file(f'{item}\n')
                elif key == 'cats_jeol':
                    for item in values:
                        self.writer.write_list_jeol_file(f'{item}\n')
                        self.writer.write_next_jeol_file(f'{item}\n')
                elif key == 'cats_cluster_jeol':
                    for item in values:
                        self.writer.write_list_cluster_jeol_file(f'{item}\n')
                        self.writer.write_next_cluster_jeol_file(f'{item}\n')
                elif key == 'cats_nuflare':
                    for item in values:
                        self.writer.write_list_nuflare_file(f'{item}\n')
                        self.writer.write_next_nuflare_file(f'{item}\n')
                elif key == 'cats_cluster_nuflare':
                    for item in values:
                        self.writer.write_list_cluster_nuflare_file(f'{item}\n')
                        self.writer.write_next_cluster_nuflare_file(f'{item}\n')

        elif parser.flag == 'mgc':

            for key, values in self.getter.mgc_pptypes.items():
                if key == 'mgc_mebes':
                    for item in values:
                        self.writer.write_list_mebes_file(f'{item}\n')
                        self.writer.write_next_mebes_file(f'{item}\n')
                elif key == 'mgc_cluster_mebes':
                    for item in values:
                        self.writer.write_list_cluster_mebes_file(f'{item}\n')
                        self.writer.write_next_cluster_mebes_file(f'{item}\n')
                elif key == 'mgc_jeol':
                    for item in values:
                        self.writer.write_list_jeol_file(f'{item}\n')
                        self.writer.write_next_jeol_file(f'{item}\n')
                elif key == 'mgc_cluster_jeol':
                    for item in values:
                        self.writer.write_list_cluster_jeol_file(f'{item}\n')
                        self.writer.write_next_cluster_jeol_file(f'{item}\n')
                elif key == 'mgc_nuflare':
                    for item in values:
                        self.writer.write_list_nuflare_file(f'{item}\n')
                        self.writer.write_next_nuflare_file(f'{item}\n')
                elif key == 'mgc_cluster_nuflare':
                    for item in values:
                        self.writer.write_list_cluster_nuflare_file(f'{item}\n')
                        self.writer.write_next_cluster_nuflare_file(f'{item}\n')
        else:
            print("Please enter 'cats' or 'mgc' and try again.")
            sys.exit(0)

        # lastly, sync machine file from prod to vrfy,
        self.copier.copy_prod_machine_files_to_verify()
        # self.copier.copier_test()

        # success message
        print(f'successfully switched files to: {parser.flag}')

