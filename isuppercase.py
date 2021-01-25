quote ="""
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capitals = ""
for char in quote:
    if char.isupper():
        capitals += char

print(capitals)