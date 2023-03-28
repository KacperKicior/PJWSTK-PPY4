import math

length = float(input("Podaj długość podłogi: "))
width = float(input("Podaj szerokość podłogi: "))

room_surface = length * width

room_surface = room_surface + (room_surface * 0.1)

panel_length = float(input("Podaj długość panela: "))
panel_width = float(input("Podaj szerokość panela: "))
panel_count = float(input("Podaj ilość paneli w opakowaniu: "))

panel_surface = panel_length * panel_width
panels_needed = room_surface / panel_surface
packs_count = panels_needed / panel_count

packs_count = math.ceil(packs_count)
print("Potrzeba: ", packs_count)
