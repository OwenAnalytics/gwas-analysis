
def hapmap3_hg18_rg():
    """Get Hail reference genome properties for HapMap Phase III data

    This is based largely on the NCBI statistics for hg18 at https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.12/#/st_Primary-Assembly (with minor
    accomodations in non-autosomes)
    """
    return dict(
        name='hapmap3_hg18',
        # Contigs 23 and 25 are not official names yet they appear in the HapMap III data
        contigs=[
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
            '15', '16', '17', '18', '19', '20', '21', '22', '23', '25'
        ],
        # hg18 spec ==> X = 154913754, Y = 57772954 but use X length for 23 + 25
        # Note: 23 and 25 both have loci that exceed the length of Y chromosome, so it's unclear what they
        # actually represent (both have all loci < max X though).  For the tutorial, it makes no difference
        # though as long as hail doesn't drop them.
        lengths={
            '1': 247249719, '2': 242951149, '3': 199501827, '4': 191273063, '5': 180857866, '6': 170899992, '7': 158821424, '8': 146274826,
            '9': 140273252, '10': 135374737, '11': 134452384, '12': 132349534, '13': 114142980, '14': 106368585, '15': 100338915, '16': 88827254,
            '17': 78774742, '18': 76117153, '19': 63811651, '20': 62435964, '21': 46944323, '22': 49691432, '23': 154913754, '25': 154913754
        },
        x_contigs='23'
    )


def canine_rg():
    return dict(
        name='canine',
        contigs=[
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
            "34", "35", "36", "37", "38", "39", "41"
        ],
        lengths={
            "1": 122670980, "2": 85416217, "3": 91858198, "4": 88267880, "5": 88908300, "6": 77552613,
            "7": 80858461, "8": 74057381, "9": 61043804, "10": 69316974, "11": 74388336, "12": 72480470,
            "13": 63232306, "14": 60959782, "15": 64187680, "16": 59511764, "17": 64281982, "18": 55763074,
            "19": 53735656, "20": 58114749, "21": 50855586, "22": 61382644, "23": 52291577, "24": 47651928,
            "25": 51628093, "26": 38939728, "27": 45753342, "28": 41164216, "29": 41841565, "30": 40196606,
            "31": 39786599, "32": 38745890, "33": 31361794, "34": 42089769, "35": 26506199, "36": 30798114,
            "37": 30897806, "38": 23903967, "39": 123833839, "41": 6608343
        },
        x_contigs='39',
        mt_contigs='41'
    )


def load_all(hl):
    hl.ReferenceGenome(**hapmap3_hg18_rg())
    hl.ReferenceGenome(**canine_rg())