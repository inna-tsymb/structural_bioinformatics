from pymol import cmd

def show_1tta_problems():
    print("--- Пошук помилок у структурі 1TTA (Транстиретин) ---")
    
    cmd.reinitialize()
    # Завантажуємо структуру та карти для 1TTA
    cmd.fetch("1tta", async_=0)
    cmd.fetch("1tta", type="fofc", async_=0)
    cmd.fetch("1tta", type="2fofc", async_=0)

    cmd.hide("everything")
    cmd.bg_color("white")
    
    # Відображення білка (тетрамер - 4 ланцюги)
    cmd.show("cartoon")
    cmd.util.cbc() # Розфарбовуємо кожен ланцюг (A, B, C, D) у свій колір
    cmd.set("cartoon_transparency", 0.4) 

    # Карти помилок
    cmd.isomesh("map_clash", "1tta_fofc", -3.0, "polymer", carve=2.0)
    cmd.color("red", "map_clash")
    
    cmd.isomesh("map_void", "1tta_fofc", 3.0, "polymer", carve=2.0)
    cmd.color("green", "map_void")
    
    # Показуємо всі бічні ланцюги тонкими лініями
    cmd.show("sticks", "polymer")
    cmd.set("stick_radius", 0.12)
    cmd.color("gray90", "elem C")

    print("Готово! Шукайте червоні плями (clashes) на стиках ланцюгів.")
    cmd.zoom("polymer")

show_1tta_problems()