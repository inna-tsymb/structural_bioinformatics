from pymol import cmd

def focus_glu_7_1tta():
    print("--- Перемикаємо фокус на реального аутлаєра 1TTA: GLU 7 ---")
    
    # 1. Створюємо правильну селекцію для поточного білка
    cmd.select("target_res", "chain A and resi 7")
    
    # 2. Налаштування візуалізації
    cmd.show("sticks", "target_res")
    cmd.color("yellow", "target_res")
    
    # 3. Оновлення сітки (якщо карта 1tta_2fofc завантажена)
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "target_res", carve=2.0)
        cmd.color("marine", "mesh_2fofc")
        print("Сітку навколо GLU 7 побудовано.")
    except:
        print("Карта не знайдена. Введіть: fetch 1tta, type=2fofc")
    
    # 4. Тепер зум спрацює, бо залишок існує
    cmd.zoom("target_res", animate=2)

focus_glu_7_1tta()