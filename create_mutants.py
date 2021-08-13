"""
Date  : 13.8.2021
Author: Shinji Iida
* Worked with PyMoL Version 2.4.0

Usage:
    pymol -c create_mutants.py -- [Reference PDB file] [mutation_list.inp]

In: 
- A reference structure PDB
- mutation_list.inp

Out: 
- mutant PDBs, which is written in mutation_list.inp

"""
import sys

ref = sys.argv[1] # Template PDB
mt_list = sys.argv[2] # Template PDB

with open(mt_list, "r") as fin: 
    mt_list = []
    for line in fin:
        if line.strip()[0] == "#": continue
        sele       = line.split("->")[0].strip()
        mt_resname = line.split("->")[1].strip()
        print(f"Selection : {sele}")
        print(f"Mutant    : {mt_resname}")
        mt_list.append([sele, mt_resname])

for sele, mt_resname in mt_list:
    cmd.load(ref)
    cmd.wizard("mutagenesis")
    cmd.do("refresh_wizard")
    
    # To get an overview over the wizard API:
    #for i in dir(cmd.get_wizard()): print(i)

    cmd.get_wizard().set_mode(mt_resname)
    cmd.get_wizard().do_select(sele)

    # Select the rotamer
    cmd.frame(1) 
    #         ^ The most frequent rotamer in a library is selected.
    # The libary is backbone-dependent one. 
    
    # Apply the mutation
    cmd.get_wizard().apply()
    
    resi = sele.split()[-1]
    resn = sele.split()[4]
    cmd.save(f"{resn}{resi}{mt_resname}.pdb")
    cmd.reinitialize()
