from pymol import cmd

def focus_chain_B_rotamers():
    print("--- Фокус на 4 аутлаєри ланцюга B (80-87) ---")
    
    # 1. Виділення всієї ділянки для контексту
    cmd.select("hotspot_B", "chain B and resi 80-87")
    cmd.show("sticks", "hotspot_B")
    cmd.color("gray90", "hotspot_B")
    
    # 2. Підсвітка конкретних аутлаєрів жовтим
    targets = "chain B and (resi 80 or resi 82 or resi 85 or resi 86)"
    cmd.color("yellow", targets)
    
    # 3. Підсвітка партнера по зіткненню для LEU 82
    cmd.show("sticks", "chain B and resi 21")
    cmd.color("cyan", "chain B and resi 21") # ARG 21 - Блакитний
    
    # 4. Сітка густини навколо всієї групи
    cmd.delete("mesh_2fofc")
    try:
        cmd.isomesh("mesh_2fofc", "1tta_2fofc", 1.0, "hotspot_B", carve=2.0)
        cmd.color("marine", "mesh_2fofc")
    except:
        print("Карта не знайдена. Спробуйте: fetch 1tta, type=2fofc")
        
    cmd.zoom("hotspot_B", animate=2)
    print("Жовті: LYS 80, LEU 82, SER 85, PRO 86. Удачі!")

focus_chain_B_rotamers()