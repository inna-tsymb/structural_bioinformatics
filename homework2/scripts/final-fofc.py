from pymol import cmd

def show_clean_crystallography():
    print("--- Фінальний вигляд: Карти 2Fo-Fc та Fo-Fc ---")
    
    # 1. Очистка
    cmd.reinitialize()
    
    # 2. Завантаження (Тільки структура і карти)
    cmd.fetch("1tta", async_=0)
    cmd.fetch("1tta", type="2fofc", async_=0)
    cmd.fetch("1tta", type="fofc", async_=0)
    
    # 3. Налаштування білка (Стиль "Nature/Science")
    cmd.bg_color("white")
    cmd.hide("everything")
    
    # Каркас + Палички
    cmd.show("cartoon")
    cmd.set("cartoon_fancy_helices", 1)
    cmd.show("sticks")
    
    # Класичні кольори (CPK)
    # Carbon=White, Nitrogen=Blue, Oxygen=Red
    cmd.color("white", "elem C")
    cmd.color("blue", "elem N")
    cmd.color("red", "elem O")
    cmd.color("yellow", "elem S")
    
    # Робімо палички тоншими, щоб не перекривали сітку
    cmd.set("stick_radius", 0.15)

    # 4. НАЛАШТУВАННЯ КАРТ (Найважливіше)
    
    # А. Синя карта (2Fo-Fc) - ТІЛО БІЛКА
    # carve=1.6 означає "малювати сітку не далі ніж 1.6 Ангстрем від атома"
    # Це прибирає шум навколо
    cmd.isomesh("map_blue_shape", "1tta_2fofc", 1.0, "polymer", carve=1.6)
    cmd.color("marine", "map_blue_shape") # Marine - приємніший відтінок синього
    
    # Б. Зелена карта (Fo-Fc) - ТРЕБА ДОДАТИ
    cmd.isomesh("map_green_miss", "1tta_fofc", 3.0, "polymer", carve=2.0)
    cmd.color("green", "map_green_miss")
    
    # В. Червона карта (Fo-Fc) - ТРЕБА ПРИБРАТИ
    cmd.isomesh("map_red_clash", "1tta_fofc", -3.0, "polymer", carve=2.0)
    cmd.color("red", "map_red_clash")

    # 5. Косметика для красивого скріншоту
    # Робимо лінії сітки тонкими та елегантними
    cmd.set("mesh_width", 0.5)
    
    # Робимо синю сітку напівпрозорою, щоб крізь неї було видно атоми
    cmd.set("transparency", 0.6, "map_blue_shape")

    print("Готово!")
    print("Синя 'хмара' = Електронна густина (правильна форма).")
    print("Червоні/Зелені плями = Помилки.")

    # Фокус на гарному ракурсі
    cmd.zoom("polymer")

show_clean_crystallography()