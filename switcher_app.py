import argparse
import sys

from writer import Writer
from getter import Getter
from copier import Copier
from deleter import Deleter

def main():
    my_getter = Getter()
    my_writer = Writer()
    my_deleter = Deleter()
    my_copier = Copier()

    # parse input for cats or mgc
    parser = my_getter.get_input((sys.argv[1:]),argparse.ArgumentParser())

    # run deleter to remove files before writing new ones
    my_deleter.remove_stuff("/apps/VRFY/dsg2nc/config/list*")

    # write files
    if parser.flag == 'cats':

        for key,values in my_getter.cats_pptypes.items():
            if key == 'cats_mebes':
                for item in values:
                    my_writer.write_list_mebes_file(f'{item}\n')
                    my_writer.write_next_mebes_file(f'{item}\n')
            elif key == 'cats_cluster_mebes':
                for item in values:
                    my_writer.write_list_cluster_mebes_file(f'{item}\n')
                    my_writer.write_next_cluster_mebes_file(f'{item}\n')
            elif key == 'cats_jeol':
                for item in values:
                    my_writer.write_list_jeol_file(f'{item}\n')
                    my_writer.write_next_jeol_file(f'{item}\n')
            elif key == 'cats_cluster_jeol':
                for item in values:
                    my_writer.write_list_cluster_jeol_file(f'{item}\n')
                    my_writer.write_next_cluster_jeol_file(f'{item}\n')
            elif key == 'cats_nuflare':
                for item in values:
                    my_writer.write_list_nuflare_file(f'{item}\n')
                    my_writer.write_next_nuflare_file(f'{item}\n')
            elif key == 'cats_cluster_nuflare':
                for item in values:
                    my_writer.write_list_cluster_nuflare_file(f'{item}\n')
                    my_writer.write_next_cluster_nuflare_file(f'{item}\n')

    elif parser.flag == 'mgc':

        for key,values in my_getter.mgc_pptypes.items():
            if key == 'mgc_mebes':
                for item in values:
                    my_writer.write_list_mebes_file(f'{item}\n')
                    my_writer.write_next_mebes_file(f'{item}\n')
            elif key == 'mgc_cluster_mebes':
                for item in values:
                    my_writer.write_list_cluster_mebes_file(f'{item}\n')
                    my_writer.write_next_cluster_mebes_file(f'{item}\n')
            elif key == 'mgc_jeol':
                for item in values:
                    my_writer.write_list_jeol_file(f'{item}\n')
                    my_writer.write_next_jeol_file(f'{item}\n')
            elif key == 'mgc_cluster_jeol':
                for item in values:
                    my_writer.write_list_cluster_jeol_file(f'{item}\n')
                    my_writer.write_next_cluster_jeol_file(f'{item}\n')
            elif key == 'mgc_nuflare':
                for item in values:
                    my_writer.write_list_nuflare_file(f'{item}\n')
                    my_writer.write_next_nuflare_file(f'{item}\n')
            elif key == 'mgc_cluster_nuflare':
                for item in values:
                    my_writer.write_list_cluster_nuflare_file(f'{item}\n')
                    my_writer.write_next_cluster_nuflare_file(f'{item}\n')
    else:
        print("Please enter 'cats' or 'mgc' and try again.")
        sys.exit(0)

    # lastly, sync machine file from prod to vrfy,
    my_copier.copy_prod_machine_files_to_verify()
    #my_copier.copier_test()

    # success message
    print(f'successfully switched files to: {parser.flag}')


if __name__ == '__main__':
    main()