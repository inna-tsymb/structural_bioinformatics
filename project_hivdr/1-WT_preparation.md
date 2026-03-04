# PREPARATION OF BASELINE WILD-TYPE STRUCTURE MODELS

## Justification of target and model selection

Two key pharmacological targets were selected for modelling mechanisms of HIVDR: protease (PR) and integrase (IN). Both targets were studied in combination with the most effective drugs that have a high genetic barrier to resistance: 

- PR inhibitor Darunavir (DRV)
- IN inhibitor Dolutegravir (DTG)

3D structures were processed in PyMOL.

### HIV-1 Protease + Darunavir (PR+DRV)

A high resolution crystal structure of WT HIV-1 Protease in complex with Darunavir were used.

`PDBID: 4HLA`

`Resolution: 1.95A`

Complex isolation: The protease structure is a symmetric homodimer. PR dimer and DRV molecule (ligand code: GRL) were extracted directly from the source file.

Solvent optimization: The binding mechanism of DRV is unique as it forms hydrogen bonds with enzyme backbone via H2O molecule. So, during PR purification solvent was completely removed, except of one structural water molecule -- HOH 301 -- which acts like bridge between ligand and Ile-50 res of both PR monomers.

Separation: Original DRV molecule was retained as separate ref ligand, and protein+HOH complex was retained as WT receptor for further molecular docking.

### HIV-1 Intasoma + Dolutegravir (IN+DTG)

Newest Cryo-EM structure of HIV-1 intasome core bounded with Dolutegravir were used.

`PDBID: 9C9M`

`Resolution: 2.01A`

Active site isolation: Since the complex intasome is a massive multimeric complex, the catalytic core -- sphere with 15A radius around ligand molecule -- was extracted for docking calculations. This step allowed to keep key elements: viral DNA segment and catalytic triad of protein.

Cofactors optimization: INSTI binding is crucially dependent of metal ions. Alternative conformations of atoms that can create false spatial conflicts were removed from the structure. Two Mg2+ ions were left in the catalytic core, which are directly interacts with DTG.

Solvent removal and separation: All water molecules were completely removed, to ensure access of DTG to the pocket. DTG molecule was saved as ref ligand, and purified pocket -- protein+vDNA+Mg2+ -- was retained as WT receptor.

So, we have in `\pdb_files`:
----
`PR_WT_receptor.pdb`

`IN_WT_receptor.pdb`

`DTG_ligand.pdb`

`DRV_ligand.pdb`

