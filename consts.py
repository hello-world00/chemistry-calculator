CATIONS = "H,Li,K,Na,NH4,Ba,Ca,Mg,Sr,Al,Cr,Fe,Fe,Ni,Co,Mn,Zn,Ag,Hg,Pb,Sn,Cu".split(',')
CATIONS_CHARGE = [1,1,1,1,1,2,2,2,2,3,3,2,3,2,2,2,2,1,2,2,2,2]

ANIONS = "OH,F,Cl,Br,I,S,SO3,SO4,NO3,NO2,PO4,CO3,CH3COO,SiO3".split(',')
ANIONS_CHARGE = [1,1,1,1,1,2,2,2,1,1,3,2,1,2]

# 0 - water
# S - soluble
# M - sl soluble
# I - insoluble
# - - decomposes in the aquatic environment
# ? - no data

SOLUBILITY_TABLE = [
    list("0SSSSSMIMIIIIIIII--III"),
    list("SSSSSMIIMSIIISSMSSMISS"),
    list("SSSSSSSSSSSSSSSSSISMSS"),
    list("SSSSSSSSSSSSSSSSSIMMSS"),
    list("SSSSSSSSSS?S?SSSSIIIMS"),
    list("SSSSSSM-S--I-IIIIIIIII"),
    list("SSSSSMMMI?-M?II?MIII??"),
    list("SSSSSIMSISSSSSSSSM-ISS"),
    list("SSSSSSSSSSSSSSSSSSSS-S"),
    list("SSSSSSSSS????SM??M????"),
    list("SISS-IIIIIIIIIIIIIIIII"),
    list("SSSSSIIII??I?IIIII?I?I"),
    list("SSSSSSSSS-SS-SSSSSSS-S"),
    list("ISSS?IIII??I???II??I??")
]

TYPES = ["WATER", "SALT", "OXIDE", "ACID", "HYDROXIDE", "ALKALI", "ACID SALT", "HYDROXIDE SALT", "ACIDIC OXIDE", "BASIC OXIDE"]
AMPHOTERIC = "Zn,Be,Pb,Sn,Al,Cr,Fe,V".split(',')
METAL = 'Mn,Ge,Pd,Sb,Li,Tl,Sr,Mg,Cu,Ba,Ru,Hg,Co,Ca,Ra,Nb,Na,Zn,Cr,K,V,Rh,Au,Ag,Fe,Tc,Al,Mo,Cd,Ti,Pb,Rb,Ga,Cs,Zr,Sn,Sc,Ni,Y,Fr'.split(',')
NON_METAL = "H,He,B,C,N,O,F,Ne,Si,P,S,Cl,Ar,As,Se,Br,Kr,Te,I,Xe,At,Rn".split(',')
ELECTROCHEMICAL_SERIES = "Li,K,Ba,Ca,Na,Mg,Al,Mn,Zn,Cr,Fe,Co,Sn,Pb,H2,Cu,Hg,Ag,Au".split(',')