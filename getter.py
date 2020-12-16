class Getter:

    cats_pptypes = {
    "cats_mebes" : ["CDM", "CTM"],
    "cats_cluster_mebes" : ["CLM"],
    "cats_jeol" : ["CDJ", "CTJ"],
    "cats_cluster_jeol" : ["CLJ"],
    "cats_nuflare" : ["CDN"],
    "cats_cluster_nuflare" : ["CLN"],
    }

    mgc_pptypes = {
    "mgc_mebes" : ["MDM"],
    "mgc_cluster_mebes" : ["MLM", "MCM"],
    "mgc_jeol" : ["MDJ"],
    "mgc_cluster_jeol" : ["MLJ", "MCJ"],
    "mgc_nuflare" : ["MDN"],
    "mgc_cluster_nuflare" : ["MLN", "MCN"],
    }

    def get_input(self, args, parser):
        parser.add_argument('flag', type=str, help='Enter the flag for cats or mgc verification')
        return parser.parse_args(args)


