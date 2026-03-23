from pymol import cmd, stored

def interfaceResidues(cmpx, cA='c. A', cB='c. B', cutoff=1.0, selName="interface"):
    """
    interfaceResidues -- finds 'interface' residues between two chains in a complex.
    """
    # Save user's settings, before setting dot_solvent
    oldDS = cmd.get("dot_solvent")
    cmd.set("dot_solvent", 1)
    
    # set some string names for temporary objects/selections
    tempC, selName1 = "tempComplex", selName+"1"
    chA, chB = "chA", "chB"
    
    # operate on a new object & turn off the original
    cmd.create(tempC, cmpx)
    cmd.disable(cmpx)
    
    # remove cruft and inrrelevant chains
    cmd.remove(tempC + " and not (polymer and (%s or %s))" % (cA, cB))
    
    # get the area of the complete complex
    cmd.get_area(tempC, load_b=1)
    # copy the areas from the loaded b to the q, field.
    cmd.alter(tempC, 'q=b')
    
    # extract the two chains and calc. the new area
    cmd.extract(chA, tempC + " and (" + cA + ")")
    cmd.extract(chB, tempC + " and (" + cB + ")")
    cmd.get_area(chA, load_b=1)
    cmd.get_area(chB, load_b=1)
    
    # update the chain-only objects w/the difference
    cmd.alter( "%s or %s" % (chA,chB), "b=b-q" )
    
    # determine which residues are over the cutoff
    stored.r, rVal, seen = [], [], []
    cmd.iterate('%s or %s' % (chA, chB), 'stored.r.append((model,resi,b))')

    cmd.enable(cmpx)
    cmd.select(selName1, 'none')
    for (model,resi,diff) in stored.r:
        key=resi+"-"+model
        if abs(diff)>=float(cutoff):
            if key in seen: continue
            else: seen.append(key)
            rVal.append( (model,resi,diff) )
            cmd.select( selName1, selName1 + " or (%s and i. %s)" % (model,resi))

    # transfer a selection to another object
    cmd.select(selName, cmpx + " in " + selName1)
    
    # clean up after ourselves
    cmd.delete(selName1)
    cmd.delete(chA)
    cmd.delete(chB)
    cmd.delete(tempC)
    
    # show the selection
    cmd.enable(selName)
    
    # reset users settings
    cmd.set("dot_solvent", oldDS)
    
    return rVal

cmd.extend("interfaceResidues", interfaceResidues)