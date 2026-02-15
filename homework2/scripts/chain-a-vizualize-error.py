from pymol import cmd

def focus_on_1tta_target_clean():
    print("--- Налаштування візуалізації 1TTA (Світлий стиль) ---")
    
    # 1. Завантаження (якщо ще не завантажено)
    cmd.reinitialize()
    cmd.fetch("1tta", async_=0)
    cmd.fetch("1tta", type="2fofc", async_=0)
    
    # 2. Налаштування фону та загального вигляду
    cmd.bg_color("white") # Білий фон за вашим запитом
    cmd.hide("everything")
    cmd.show("cartoon")
    
    # 3. Світла структура протеїну
    cmd.color("gray90", "polymer") # Дуже світло-сірий для всього білка
    cmd.set("cartoon_transparency", 0.4) # Напівпрозорість для кращої видимості sticks
    
    # 4. Виділення цілей (Ланцюг A, залишки 1-10)
    # Відображаємо палички (sticks)
    cmd.show("sticks", "chain A and resi 1-10")
    
    # Підсвічуємо критичний THR 3 (Clash 1.07 Å)
    cmd.color("red", "chain A and resi 3")
    
    # Підсвічуємо аутлаєр THR 5 (0.2%)
    cmd.color("magenta", "chain A and resi 5")
    
    # 5. Електронна густина (2Fo-Fc)
    # Створюємо сітку навколо цільової ділянки
    cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "chain A and resi 1-10", carve=2.0)
    cmd.color("marine", "mesh_2fofc") # Приємний синій колір для сітки
    
    # 6. Фінальний ракурс
    cmd.zoom("chain A and resi 1-10")
    
    print("Готово!")
    print("THR 3 (Червоний): Усуньте зіткнення 1.072 Å.")
    print("THR 5 (Фіолетовий): Виправте аутлаєр (0.2%).")

# Запуск
focus_on_1tta_target_clean()