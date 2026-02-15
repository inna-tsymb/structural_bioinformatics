from pymol import cmd

def focus_clash_hotspot_1tta():
    print("--- Фокус на критичні помилки 1TTA: GLU 7 та THR 3 ---")
    
    # 1. Створюємо селекцію для цілей (тільки ланцюг А)
    cmd.select("targets", "chain A and (resi 3 or resi 7)")
    
    # 2. Налаштування візуалізації
    cmd.show("sticks", "targets")
    cmd.color("yellow", "chain A and resi 7") # GLU 7 - Жовтий (Outlier)
    cmd.color("red", "chain A and resi 3")    # THR 3 - Червоний (Clash 1.07)
    
    # 3. Оновлення сітки густини
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "targets", carve=2.0)
        cmd.color("marine", "mesh_2fofc")
        print("Сітку побудовано.")
    except:
        print("Карта не знайдена. Введіть: fetch 1tta, type=2fofc")
    
    # 4. Зум на обидва залишки
    cmd.zoom("targets", animate=2)

focus_clash_hotspot_1tta()