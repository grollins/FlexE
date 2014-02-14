#! /usr/bin/env python
from argparse import ArgumentParser
from prody import confProDy
from flexe import FlexE

def main():
    #no log messages:
    confProDy(verbosity='none')

    # parse command line arguments
    parser = ArgumentParser(description='Calculate MDENM energies from a pdb \
                                    will calculate energy using modes from pdb\
                                    and then from reference--> crystal should\
                                    be the reference')
    parser.add_argument('--pdb', help='Molecule we want to examine. It will also be used as topology')
    parser.add_argument('--reference',
                        help='Rerence pdb to which we will rmsd everything')
    args = parser.parse_args() 

    flexy = FlexE(ref_pdb_file=args.reference)
    results = flexy.compare_with_ref(pdb_file=args.pdb)
    rmsd, energy_ref_to_pdb, energy_pdb_to_ref = results
    print "%s %.2f %.2f %.2f " % (args.pdb, rmsd, energy_ref_to_pdb, energy_pdb_to_ref)

if __name__ == '__main__':
    main()

