import pymol
from pymol import cmd

def hydrophobic_representation():
    cmd.color("white", "all")  # Default color for all atoms
    cmd.color("yellow", "resn Cys+Met")  # Cysteine and Methionine
    cmd.color("firebrick", "resn Ile+Leu+Val+Phe+Ala+Trp")  # Hydrophobic residues
    cmd.color("purpleblue", "resn Lys+Arg+His+Asp+Glu+Asn+Gln")  # Positively charged residues
cmd.extend("hydrophobic_representation", hydrophobic_representation)  # Register the function with PyMOL
    