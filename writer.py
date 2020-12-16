class Writer:

    def write_list_mebes_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoMEBES', 'a') as f:
            f.write(pptype_values)

    def write_next_mebes_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoMEBES', 'w') as f:
            f.write(pptype_values)

    def write_list_cluster_mebes_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoCLUSTERMEBES', 'a') as f:
            f.write(pptype_values)

    def write_next_cluster_mebes_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoCLUSTERMEBES', 'w') as f:
            f.write(pptype_values)

    def write_list_jeol_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoJEOL', 'a') as f:
            f.write(pptype_values)

    def write_next_jeol_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoJEOL', 'w') as f:
            f.write(pptype_values)

    def write_list_cluster_jeol_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoCLUSTERJEOL', 'a') as f:
            f.write(pptype_values)

    def write_next_cluster_jeol_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoCLUSTERJEOL', 'w') as f:
            f.write(pptype_values)

    def write_list_nuflare_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoNUFLARE', 'a') as f:
            f.write(pptype_values)

    def write_next_nuflare_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoNUFLARE', 'w') as f:
            f.write(pptype_values)

    def write_list_cluster_nuflare_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/listVrfyRunInfoCLUSTERNUFLARE', 'a') as f:
            f.write(pptype_values)

    def write_next_cluster_nuflare_file(self, pptype_values):
        with open('/apps/VRFY/dsg2nc/config/nextVrfyRunInfoCLUSTERNUFLARE', 'w') as f:
            f.write(pptype_values)

