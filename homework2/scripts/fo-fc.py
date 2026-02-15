from pymol import cmd

def show_clean_maps():
    print("--- Завантаження чистих карт густини ---")
    
    # 1. Очистка і завантаження
    cmd.reinitialize()
    cmd.fetch("1tta", async_=0)
    cmd.fetch("1tta", type="2fofc", async_=0) # Карта форми
    cmd.fetch("1tta", type="fofc", async_=0)  # Карта різниці
    
    # 2. Налаштування білка (Стиль "Publication Quality")
    cmd.hide("everything")
    cmd.bg_color("white")
    
    # Малюємо простий сірий каркас + палички
    cmd.show("cartoon")
    cmd.show("sticks")
    
    # Розфарбовуємо атоми в стандартні кольори (CPK)
    # C = Світло-сірий, N = Синій, O = Червоний, S = Жовтий
    cmd.color("white", "elem C")
    cmd.color("blue", "elem N")
    cmd.color("red", "elem O")
    cmd.color("yellow", "elem S")
    
    # 3. КАРТА 1: 2Fo-Fc (СИНЯ) - Основна форма
    # carve=1.6 показує сітку тільки в радіусі 1.6 Å від атомів
    cmd.isomesh("map_shape", "1tta_2fofc", 1.0, "polymer", carve=1.6)
    cmd.color("blue", "map_shape")
    
    # 4. КАРТА 2: Fo-Fc (ЗЕЛЕНА) - Позитивна різниця (Missing)
    cmd.isomesh("map_pos", "1tta_fofc", 3.0, "polymer", carve=2.0)
    cmd.color("green", "map_pos")
    
    # 5. КАРТА 3: Fo-Fc (ЧЕРВОНА) - Негативна різниця (Clash)
    cmd.isomesh("map_neg", "1tta_fofc", -3.0, "polymer", carve=2.0)
    cmd.color("red", "map_neg")

    print("Готово!")
    print("Синя = Електронна хмара (форма).")
    print("Зелена/Червона = Помилки/Відхилення.")

    # 6. Зум на цікаве місце (приклад)
    # Можна прибрати цей рядок, якщо хочете бачити весь білок
    cmd.zoom("resi 170", animate=2)

show_clean_maps()