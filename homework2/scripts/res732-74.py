from pymol import cmd

def focus_on_water_clashes():
    print("--- Фінальна чистка 1TTA: Конфлікти з водою ---")
    
    # 1. Налаштування (світлий стиль)
    cmd.bg_color("white")
    cmd.set("cartoon_transparency", 0.4)
    
    # 2. Виділення амінокислот (GLU 72 та ASP 74)
    cmd.select("residues_clash", "chain B and (resi 72 or resi 74)")
    cmd.show("sticks", "residues_clash")
    cmd.color("yellow", "residues_clash")
    
    # 3. Виділення конкретних молекул води
    # У PDB вони часто мають номер резиденту, як у звіті
    cmd.select("problem_waters", "chain B and (resi 792 or resi 709)")
    cmd.show("spheres", "problem_waters") # Воду краще бачити сферами
    cmd.set("sphere_scale", 0.3, "problem_waters")
    cmd.color("red", "problem_waters")
    
    # 4. Карта густини
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "residues_clash", carve=3.0)
        cmd.color("marine", "mesh_2fofc")
    except:
        pass
        
    cmd.zoom("residues_clash", animate=2)
    print("Жовті: GLU 72 та ASP 74. Червоні сфери: Конфліктні молекули води.")

focus_on_water_clashes()