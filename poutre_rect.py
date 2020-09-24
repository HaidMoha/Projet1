# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie

I = ((b*10**-3)*(h*10**-3)**3)/12

#Calcul de la deformation maximal

delta_max = (F*(L*10**-3)**3)/(3*(E*10**9)*I)

print('La deformation maximale de la poutre est', round(delta_max*10**3, 2), 'mm')