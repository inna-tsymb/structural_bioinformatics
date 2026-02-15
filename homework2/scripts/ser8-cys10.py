from pymol import cmd

def focus_critical_nodes_1tta():
    print("--- Фокус на SER 8 та CYS 10 (Rama Outliers + Clashes) ---")
    
    # 1. Виділяємо проблемну петлю 7-11
    cmd.select("hotspot_node", "chain A and resi 7-11")
    
    # 2. Налаштування візуалізації
    cmd.show("sticks", "hotspot_node")
    cmd.color("magenta", "chain A and resi 8") # SER 8 - Фіолетовий (Rama 0%)
    cmd.color("orange", "chain A and resi 10")  # CYS 10 - Помаранчевий (Rama + Rotamer)
    
    # 3. Підсвітимо партнерів по зіткненню
    cmd.select("clash_partners", "chain A and (resi 61 or resi 9 or resi 57)")
    cmd.show("sticks", "clash_partners")
    cmd.color("gray60", "clash_partners")
    
    # 4. Сітка густини (якщо є)
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "hotspot_node", carve=2.0)
        cmd.color("marine", "mesh_2fofc")
    except:
        pass
        
    cmd.zoom("hotspot_node", animate=2)
    print("SER 8 (Фіолетовий): Спробуйте виправити кути остова.")
    print("CYS 10 (Помаранчевий): Тут потрібно виправити і ротамер, і остов.")

focus_critical_nodes_1tta()