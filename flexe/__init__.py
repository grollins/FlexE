from prody import confProDy, parsePDB, calcTransformation, calcRMSD
from .hamiltonian import EDENMHamiltonian


class FlexE(object):
    """this comment is false"""
    def __init__(self, ref_pdb_file):
        ref = parsePDB(ref_pdb_file)
        self.number_of_residues = ref.numResidues()
        self.ref_struct = ref.select('calpha')

    def compare_with_ref(self, pdb_file):
        pdb_struct = parsePDB(pdb_file).select('calpha')
        
        # Make sure we are in same reference set
        t = calcTransformation(pdb_struct, self.ref_struct)
        t.apply(pdb_struct)

        # Compute rmsd to reference structure
        rmsd = calcRMSD(pdb_struct, target=self.ref_struct)
        
        # Compute elastic deformation energies
        ref_coords = self.ref_struct.getCoords()
        pdb_coords = pdb_struct.getCoords()
        h = EDENMHamiltonian(ref_coords)
        energy_ref_to_pdb = h.evaluate_energy(pdb_coords)
        h = EDENMHamiltonian(pdb_coords)
        energy_pdb_to_ref = h.evaluate_energy(ref_coords)
        
        # Scale energies by number of residues
        energy_ref_to_pdb /= self.number_of_residues
        energy_pdb_to_ref /= self.number_of_residues
        
        return rmsd, energy_ref_to_pdb, energy_pdb_to_ref
