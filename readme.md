# Needed to run FlexE

[Prody package from the Bahar lab](http://www.csb.pitt.edu/ProDy/index.html)

# How to execute
    
    ./run_FlexE.py --ref crystal.pdb --pdb template.pdb 

# Output

`pdb_file_name RMSD FlexE_ref2pdb FlexE_pdb2ref`

+  `RMSD` root mean-squared deviation between ref and pdb

+  `FlexE_ref2pdb` energy in kcal/(mol residue) to deform from ref to pdb using the flexible directions of ref

+  `FlexE_pdb2ref` energy in kcal/(mol residue) to deform from pdb to ref using the flexible directions of pdb
