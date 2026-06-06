'''
------------------------------------------------------------------
Projeto ResMat Python - Cálculo de momento de inércia (Seção em T)
------------------------------------------------------------------
'''

print("É necessário a aquisição de algumas informações para o cálculo\n")

b1 = float(input("Largura da mesa (b1) [mm]:"))
h1 = float(input("Altura da mesa (h1) [mm]:"))

b2 = float(input("Largura da alma (b2) [mm]:"))
h2 = float(input("Altura da alma (h2) [mm]:"))

A1 = b1 * h1
A2 = b2 * h2

Area_total = A1 + A2

y1 = h2 + (h1/2.0)
y2 = h2 / 2.0

yc = ((A1*y1) + (A2 *y2))

d1 = y1 - yc
d2 = y2 - yc

I1 = (b1 * (h1**3) / 12.0) + (A1 * (d1**2))
I2 = (b2 * (h2**3) / 12.0) + (A2 * (d2**2))
Ix_total = I1 + I2

print("\nPropriedades da seção")
print(f"Área total: {Area_total:.2f} mm²")
print(f"Posição da linha neutra: {yv:.2f} mm")
print(f"Momento de Inércia: {Ix_total:.2}mm⁴")




