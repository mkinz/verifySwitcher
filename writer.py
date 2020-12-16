class Writer:

    def write_list_mebes_file(self, pptype_values):
        with open(test_List_MEBES, 'a') as f:
            f.write(pptype_values)

    def write_next_mebes_file(self, pptype_values):
        with open(test_next_MEBES, 'w') as f:
            f.write(pptype_values)

    def write_list_jeol_file(self, pptype_values):
        with open(test_list_JEOL, 'a') as f:
            f.write(pptype_values)

    def write_next_jeol_file(self, pptype_values):
        with open(test_next_JEOL, 'w') as f:
            f.write(pptype_values)

    def write_list_nuflare_file(self, pptype_values):
        with open(test_list_NF, 'a') as f:
            f.write(pptype_values)

    def write_next_nuflare_file(self, pptype_values):
        with open(test_next_NF, 'w') as f:
            f.write(pptype_values)