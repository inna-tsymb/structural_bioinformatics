from pymol import cmd

def find_extra_water_clashes():
    print("--- Пошук додаткових артефактів води у 1TTA ---")
    
    # Виділяємо всі критичні молекули води
    # Номери взяті безпосередньо зі звіту MolProbity
    bad_waters = "chain A and (resi 664 or resi 724) or chain B and (resi 411 or resi 704 or resi 779)"
    cmd.select("bad_water_list", bad_waters)
    
    # Налаштування вигляду
    cmd.show("spheres", "bad_water_list")
    cmd.set("sphere_scale", 0.4, "bad_water_list")
    cmd.color("red", "bad_water_list")
    
    # Підсвітимо амінокислоти-партнери
    cmd.select("partner_residues", "chain A and (resi 63 or resi 99) or chain B and (resi 104 or resi 27 or resi 2)")
    cmd.show("sticks", "partner_residues")
    cmd.color("yellow", "partner_residues")
    
    cmd.zoom("bad_water_list", buffer=5)
    print("Всі червоні сфери - кандидати на видалення.")

find_extra_water_clashes()