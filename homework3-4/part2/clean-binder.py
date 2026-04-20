import os

def final_deep_clean(input_pdb, output_pdb):
    # Словник для заміни нестандартних імен Amber/OpenMM
    res_mapping = {
        'HIE': 'HIS', 'HID': 'HIS', 'HIP': 'HIS',
        'CYX': 'CYS', 'CYM': 'CYS',
        'LYN': 'LYS', 'ARN': 'ARG', 'ASH': 'ASP', 'GLH': 'GLU'
    }
    
    with open(input_pdb, 'r') as f_in, open(output_pdb, 'w') as f_out:
        for line in f_in:
            if line.startswith(("ATOM", "HETATM")):
                # 1. Видаляємо водні
                atom_name = line[12:16].strip()
                if atom_name.startswith('H') or (atom_name[0].isdigit() and atom_name[1] == 'H'):
                    continue
                
                # 2. Заміна імен залишків (HIE -> HIS тощо)
                res_name = line[17:20].strip()
                if res_name in res_mapping:
                    line = line[:17] + res_mapping[res_name] + line[20:]
                
                # 3. Виправлення термінальних атомів
                if atom_name == 'OT1': line = line[:12] + " O  " + line[16:]
                if atom_name == 'OT2': line = line[:12] + " OXT" + line[16:]
                
                # 4. Додавання колонки елемента в кінці (якщо її немає)
                # Елемент - це перша буква імені атома (C, N, O, S)
                element = atom_name[0]
                if element in ['1', '2', '3']: element = atom_name[1] # Для 1CA -> C
                
                # Формуємо рядок PDB заново з колонкою елемента в 77-78 позиції
                clean_line = line[:76].ljust(76) + element.rjust(2) + line[78:]
                f_out.write(clean_line)
            elif line.startswith("TER") or line.startswith("END"):
                f_out.write(line)

# Запустіть це у вашій папці
final_deep_clean('minimised.pdb', 'final_for_damietta.pdb')