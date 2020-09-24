# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

I_rect = ((b*10**-3)*(h*10**-3)**3)/12
delta_max_rect = (F*(L*10**-3)**3)/(3*(E*10**9)*I_rect)

# poutre carree
a = 15  # en mm

I_car = ((a*10**-3)**4)/12
delta_max_car = (F*(L*10**-3)**3)/(3*(E*10**9)*I_car)

# poutre ronde
d = 5  # en mm

I_rond = (3.14159*(d*10**-3)**4)/64
delta_max_rond = (F*(L*10**-3)**3)/(3*(E*10**9)*I_rond)

# poutre creuse
D = 15  # en mm
d = 5  # en mm

I_cre = (3.14159*(((D*10**-3)**4)-(d*10**-3)**4))/64
delta_max_cre = (F*(L*10**-3)**3)/(3*(E*10**9)*I_cre)


# Calcul de la section optimale
# Pour mieux me retrouver dans mes calculs j'ai converti mes valeurs en m au lieu de mm et Pa au lieu de GPa


if delta_max_car < delta_max_rect:
    if delta_max_car < delta_max_rond:
        if delta_max_car < delta_max_cre:
            print ("Le type de section minimisant la deformation maximale est carree, avec une deformation de", round(delta_max_car*10**3,2)  ,"mm")

if delta_max_rond < delta_max_car:
    if delta_max_rond < delta_max_rect:
        if delta_max_rond < delta_max_cre:
            print ("Le type de section minimisant la deformation maximale est ronde, avec une deformation de", round(delta_max_rond*10**3,2)  ,"mm")

if delta_max_cre < delta_max_car:
    if delta_max_cre < delta_max_rond:
        if delta_max_cre < delta_max_rect:
            print ("Le type de section minimisant la deformation maximale est creuse, avec une deformation de", round(delta_max_cre*10**3,2) ,"mm")

if delta_max_rect < delta_max_car:
    if delta_max_rect < delta_max_rond:
        if delta_max_rect < delta_max_cre:
            print ("Le type de section minimisant la deformation maximale est rectangulaire, avec une deformation de", round(delta_max_rect*10**3,2)  ,"mm")


