python
from pymol import cmd

def find_weirdo_trace():
    cmd.reinitialize()
    cmd.fetch("2i61")
    cmd.show_as("lines", "all")
    
    # We will store (chain, resi) and the pseudo-dihedral value
    results = []
    
    # Get all chains
    chains = cmd.get_chains("2i61")
    
    for c in chains:
        # Get list of residue numbers for this chain
        residues = []
        cmd.iterate(f"chain {c} and name CA", "residues.append(int(resi))", space={'residues': residues})
        residues.sort()
        
        # We need 4 consecutive C-alphas to calculate a pseudo-dihedral
        for i in range(len(residues) - 3):
            r1, r2, r3, r4 = residues[i:i+4]
            try:
                angle = cmd.get_dihedral(
                    f"chain {c} and resi {r1} and name CA",
                    f"chain {c} and resi {r2} and name CA",
                    f"chain {c} and resi {r3} and name CA",
                    f"chain {c} and resi {r4} and name CA"
                )
                results.append((c, r2, angle))
            except:
                continue

    # Find the "Weirdo" (The residue with the most extreme angle)
    # Average pseudo-dihedral is usually around 50-60 degrees
    if results:
        results.sort(key=lambda x: x[2])
        min_weird = results[0]
        max_weird = results[-1]
        
        # Let's pick the one furthest from the median as the "weirdo"
        weirdo = max_weird if abs(max_weird[2]) > abs(min_weird[2]) else min_weird
        
        print(f"\n--- Pseudo-Dihedral Report (CA-CA-CA-CA) ---")
        print(f"The 'Weirdo' is Residue {weirdo[1]} in Chain {weirdo[0]} with angle {weirdo[2]:.2f}")
        
        # Highlight it
        sel = f"chain {weirdo[0]} and resi {weirdo[1]}"
        cmd.select("weirdo", sel)
        cmd.show("spheres", "weirdo")
        cmd.color("magenta", "weirdo")
        cmd.zoom("weirdo", 20)
    else:
        print("Could not calculate any angles. Check if CA atoms exist.")

find_weirdo_trace()
python end