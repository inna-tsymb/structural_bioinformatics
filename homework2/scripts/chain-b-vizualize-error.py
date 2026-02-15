from pymol import cmd

def focus_on_1tta_chain_B():
    print("--- Налаштування візуалізації 1TTA: Фокус на Ланцюг B ---")
    
    # 1. ВИДІЛЕННЯ НОВОЇ ЦІЛІ (Clash 1.096 Å)
    # Створюємо селекцію для PRO 2 та SER 50 у ланцюзі B
    cmd.select("target_clash", "chain B and (resi 2 or resi 50)")
    
    # Показуємо їх як палички (sticks)
    cmd.show("sticks", "target_clash")
    
    # Фарбуємо в контрастні кольори:
    cmd.color("orange", "chain B and resi 2")  # PRO 2 - Помаранчевий
    cmd.color("cyan", "chain B and resi 50")    # SER 50 - Блакитний
    
    # 2. Електронна густина навколо цілі
    # Видаляємо стару сітку, якщо вона була, і створюємо нову
    cmd.delete("mesh_2fofc")
    cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "target_clash", carve=2.0)
    cmd.color("marine", "mesh_2fofc")
    
    # 3. Зум та ракурс
    cmd.zoom("target_clash", animate=2)
    
    print("Готово! Фокус на парі PRO 2 (Помаранчевий) та SER 50 (Блакитний).")
    print("Зіткнення: 1.096 Ангстрем. Спробуйте змінити ротамер SER 50.")

# Запуск
focus_on_1tta_chain_B()