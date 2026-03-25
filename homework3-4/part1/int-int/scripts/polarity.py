from pymol import cmd

def hydrophobic_representation():
    cmd.color("white", "all")
    cmd.color("yellow", "resn Cys+Met")
    cmd.color("firebrick", "resn Ile+Val+Leu+Phe+Ala+Trp")
    cmd.color("purpleblue", "resn Lys+Arg+His+Asp+Glu+Gln+Asn")

cmd.extend("hydrophobic_representation", hydrophobic_representation)