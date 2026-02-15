from pymol import cmd

def analyze_1tta_stability():
    print("--- Аналіз B-фактора 1TTA ---")
    
    # Малюємо товсту стрічку, розфарбовану за стабільністю
    cmd.show("cartoon")
    cmd.set("cartoon_tube_radius", 0.2)
    
    # Спектр: Синій (холодний/стабільний) -> Червоний (гарячий/рухливий)
    cmd.spectrum("b", "blue_white_red", "polymer")
    
    print("Сині ділянки - стабільне ядро, Червоні - рухливі петлі.")
    cmd.zoom("polymer")

analyze_1tta_stability()