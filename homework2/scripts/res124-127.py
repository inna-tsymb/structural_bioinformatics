from pymol import cmd

def focus_on_cterminus_1tta():
    print("--- Фокус на C-термінальні помилки 1TTA: 124-127 ---")
    
    # 1. Налаштування (без перезавантаження)
    cmd.bg_color("white")
    cmd.set("cartoon_transparency", 0.4)
    
    # 2. Виділення кінців обох ланцюгів
    cmd.select("cterm", "resi 124-127")
    cmd.show("sticks", "cterm")
    
    # Підсвітимо Rama Outliers
    cmd.color("brightorange", "cterm and resi 125") # PRO 125
    cmd.color("yellow", "cterm and resi 126")       # LYS 126
    
    # 3. Електронна густина
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "cterm", carve=2.0)
        cmd.color("marine", "mesh_2fofc")
    except:
        print("Карта не знайдена. Введіть: fetch 1tta, type=2fofc")
        
    cmd.zoom("cterm", animate=2)
    print("PRO 125 (Помаранчевий) та LYS 126 (Жовтий).")
    print("Спробуйте вирівняти їх так, щоб вони не штовхали один одного.")

focus_on_cterminus_1tta()