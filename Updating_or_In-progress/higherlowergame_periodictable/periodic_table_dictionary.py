#element symbol
#element name
#***atomic number = number of protons = number of electrons
#atomic number, number of protons, and number of electrons are all equivalent in neutral-atoms in periodic table, in nature not always the case
#in periodic table, atomic number is usually reference to number of protons, not number of electrons
#***atomic weight = number of protons + number of neutrons (+ number of electrons: very low almost nonexist mass)
#***neutrons = atomic weight - number of protons (atomic number)
#group by properties, same number of valence electrons in outer shell (group 1 has 1 valence electron, group 2 has 2 valence electrons, etc.)
#groups are: alkali metal, alkaline earth metals, lanthanides, transition metals, post-transition metals, metalloids, other non-metals, halogens, noble gases
#***USD cost per 100 grams
#atomic radius
#ionization energy
#electron affinity
#electronegativity


def neutrons(element_atomic_num):
    atomic_weight_for_calc=math.floor(float(find_all_nums(periodic_table[element_atomic_num]['atomic_weight'])[0]))
    neutrons=atomic_weight_for_calc-periodic_table[element_atomic_num]['atomic_number']
    return neutrons





periodic_table = [
    0,
    
    {
        'element_symbol': 'H',
        'name': 'Hydrogen',
        'atomic_number': 1,
        'group': 'Other nonmetals',
        'atomic_weight': '1.00784 g/mol',
        'price': '12 USD per 100 gram' 
    },
    
    {
        'element_symbol': 'He',
        'name': 'Helium',
        'atomic_number': 2,
        'group': 'Noble gases',
        'atomic_weight': '4.002602 g/mol',
        'price': '2.4 USD per 100 gram' 
    },

    {
        'element_symbol': 'Li',
        'name': 'Lithium',
        'atomic_number': 3,
        'group': 'Alkali metals',
        'atomic_weight': '6.941 g/mol',
        'price': '8.65 USD per 100 gram'  
    },

    {
        'element_symbol': 'Be',
        'name': 'Berylium',
        'atomic_number': 4,
        'group': 'Alkaline earth metals',
        'atomic_weight': '9.0121831 g/mol',
        'price': '85.7 USD per 100 gram'  
    },    

    {
        'element_symbol': 'B',
        'name': 'Boron',
        'atomic_number': 5,
        'group': 'Metalloids',
        'atomic_weight': '10.811 g/mol',
        'price': '0.37 USD per 100 gram'  
    },

    {
        'element_symbol': 'C',
        'name': 'Carbon',
        'atomic_number': 6,
        'group': 'Alkali metals',
        'atomic_weight': '12.0107 g/mol',
        'price': '2.4 USD per 100 gram'  
    },

    {
        'element_symbol': 'N',
        'name': 'Nitrogen',
        'atomic_number': 7,
        'group': 'Other nonmetals',
        'atomic_weight': '14.0067 g/mol',
        'price': '0.4 USD per 100 gram'  
    },

    {
        'element_symbol': 'O',
        'name': 'Oxygen',
        'atomic_number': 8,
        'group': 'Other nonmetals',
        'atomic_weight': '15.9994 g/mol',
        'price': '0.3 USD per 100 gram'  
    },    

    {
        'element_symbol': 'F',
        'name': 'Fluorine',
        'atomic_number': 9,
        'group': 'Halogens',
        'atomic_weight': '18.9984 g/mol',
        'price': '0.216 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ne',
        'name': 'Neon',
        'atomic_number': 10,
        'group': 'Noble gases',
        'atomic_weight': '20.1797 g/mol',
        'price': '24 USD per 100 gram'  
    },

    {
        'element_symbol': 'Na',
        'name': 'Sodium',
        'atomic_number': 11,
        'group': 'Alkali metals',
        'atomic_weight': '22.9897 g/mol',
        'price': '0.343 USD per 100 gram'  
    },

    {
        'element_symbol': 'Mg',
        'name': 'Magnesium',
        'atomic_number': 12,
        'group': 'Alkaline earth metals',
        'atomic_weight': '24.3050 g/mol',
        'price': '0.232 USD per 100 gram'  
    },

    {
        'element_symbol': 'Al',
        'name': 'Aluminum',
        'atomic_number': 13,
        'group': 'Post-transition metals',
        'atomic_weight': '26.9815 g/mol',
        'price': '0.179 USD per 100 gram'  
    },

    {
        'element_symbol': 'Si',
        'name': 'Silicon',
        'atomic_number': 14,
        'group': 'Metalloids',
        'atomic_weight': '28.0855 g/mol',
        'price': '5.4 USD per 100 gram'  
    },

    {
        'element_symbol': 'P',
        'name': 'Phosphorus',
        'atomic_number': 15,
        'group': 'Other nonmetals',
        'atomic_weight': '30.9737 g/mol',
        'price': '30 USD per 100 gram'  
    },

    {
        'element_symbol': 'S',
        'name': 'Sulfur',
        'atomic_number': 16,
        'group': 'Other nonmetals',
        'atomic_weight': '32.065 g/mol',
        'price': '50 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cl',
        'name': 'Chlorine',
        'atomic_number': 17,
        'group': 'Halogens',
        'atomic_weight': '35.453 g/mol',
        'price': '0.15 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ar',
        'name': 'Argon',
        'atomic_number': 18,
        'group': 'Noble gases',
        'atomic_weight': '39.948 g/mol',
        'price': '0.5 USD per 100 gram'  
    },

    {
        'element_symbol': 'K',
        'name': 'Potassium',
        'atomic_number': 19,
        'group': 'Alkali metals',
        'atomic_weight': '39.0983 g/mol',
        'price': '1.36 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ca',
        'name': 'Calcium',
        'atomic_number': 20,
        'group': 'Alkaline earth metals',
        'atomic_weight': '40.078 g/mol',
        'price': '0.235 USD per 100 gram'  
    },

    {
        'element_symbol': 'Sc',
        'name': 'Scandium',
        'atomic_number': 21,
        'group': 'Transition metals',
        'atomic_weight': '44.9559 g/mol',
        'price': '346 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ti',
        'name': 'Titanium',
        'atomic_number': 22,
        'group': 'Transition metals',
        'atomic_weight': '47.867 g/mol',
        'price': '661 USD per 100 gram'  
    },

    {
        'element_symbol': 'V',
        'name': 'Vanadium',
        'atomic_number': 23,
        'group': 'Transition metals',
        'atomic_weight': '50.9415 g/mol',
        'price': '235 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cr',
        'name': 'Chromium',
        'atomic_number': 24,
        'group': 'Transition metals',
        'atomic_weight': '51.9961 g/mol',
        'price': '6.72 USD per 100 gram'  
    },

    {
        'element_symbol': 'Mn',
        'name': 'Manganese',
        'atomic_number': 25,
        'group': 'Transition metals',
        'atomic_weight': '54.9380 g/mol',
        'price': '1.36 USD per 100 gram'  
    },

    {
        'element_symbol': 'Fe',
        'name': 'Iron',
        'atomic_number': 26,
        'group': 'Transition metals',
        'atomic_weight': '55.845 g/mol',
        'price': '0.528 USD per 100 gram'  
    },

    {
        'element_symbol': 'Co',
        'name': 'Cobalt',
        'atomic_number': 27,
        'group': 'Transition metals',
        'atomic_weight': '58.9331 g/mol',
        'price': '29.1 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ni',
        'name': 'Nickel',
        'atomic_number': 28,
        'group': 'Transition metals',
        'atomic_weight': '58.6934 g/mol',
        'price': '12.4 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cu',
        'name': 'Copper',
        'atomic_number': 29,
        'group': 'Transition metals',
        'atomic_weight': '63.546 g/mol',
        'price': '9.76 USD per 100 gram'  
    },

    {
        'element_symbol': 'Zn',
        'name': 'Zinc',
        'atomic_number': 30,
        'group': 'Transition metals',
        'atomic_weight': '65.38 g/mol',
        'price': '5.30 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ga',
        'name': 'Gallium',
        'atomic_number': 31,
        'group': 'Post-transition metals',
        'atomic_weight': '69.723 g/mol',
        'price': '220 USD per 100 gram'  
    },    

    {
        'element_symbol': 'Ge',
        'name': 'Germanium',
        'atomic_number': 32,
        'group': 'Metalloids',
        'atomic_weight': '72.64 g/mol',
        'price': '539 USD per 100 gram'  
    },

    {
        'element_symbol': 'As',
        'name': 'Arsenic',
        'atomic_number': 33,
        'group': 'Metalloids',
        'atomic_weight': '74.9216 g/mol',
        'price': '7.58 USD per 100 gram'  
    },

    {
        'element_symbol': 'Se',
        'name': 'Selenium',
        'atomic_number': 34,
        'group': 'Other nonmetals',
        'atomic_weight': '78.96 g/mol',
        'price': '61 USD per 100 gram'  
    },

    {
        'element_symbol': 'Br',
        'name': 'Bromine',
        'atomic_number': 35,
        'group': 'Halogens',
        'atomic_weight': '79.904 g/mol',
        'price': '5 USD per 100 gram'  
    },

    {
        'element_symbol': 'Kr',
        'name': 'Krypton',
        'atomic_number': 36,
        'group': 'Noble gases',
        'atomic_weight': '83.798 g/mol',
        'price': '33 USD per 100 gram'  
    },

    {
        'element_symbol': 'Rb',
        'name': 'Rubidium',
        'atomic_number': 37,
        'group': 'Alkali metals',
        'atomic_weight': '85.467 g/mol',
        'price': '2370 USD per 100 gram'  
    },    

    {
        'element_symbol': 'Sr',
        'name': 'Strontium',
        'atomic_number': 38,
        'group': 'Alkaline earth metals',
        'atomic_weight': '87.62 g/mol',
        'price': '17.6 USD per 100 gram'  
    },

    {
        'element_symbol': 'Y',
        'name': 'Yttrium',
        'atomic_number': 39,
        'group': 'Transition metals',
        'atomic_weight': '88.905 g/mol',
        'price': '13.9 USD per 100 gram'  
    },

    {
        'element_symbol': 'Zr',
        'name': 'Zirconium',
        'atomic_number': 40,
        'group': 'Transition metals',
        'atomic_weight': '91.224 g/mol',
        'price': '24.1 USD per 100 gram'  
    },

    {
        'element_symbol': 'Nb',
        'name': 'Niobium',
        'atomic_number': 41,
        'group': 'Transition metals',
        'atomic_weight': '92.906 g/mol',
        'price': '73.4 USD per 100 gram'  
    },

    {
        'element_symbol': 'Mo',
        'name': 'Molybdenum',
        'atomic_number': 42,
        'group': 'Transition metals',
        'atomic_weight': '95.94 g/mol',
        'price': '41 USD per 100 gram'  
    },

    {
        'element_symbol': 'Tc',
        'name': 'Technetium',
        'atomic_number': 43,
        'group': 'Transition metals, also radio active',
        'atomic_weight': '98.906 g/mol',
        'price': '10000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ru',
        'name': 'Ruthenium',
        'atomic_number': 44,
        'group': 'Transition metals',
        'atomic_weight': '101.07 g/mol',
        'price': '868 USD per 100 gram'  
    },

    {
        'element_symbol': 'Rh',
        'name': 'Rhodium',
        'atomic_number': 45,
        'group': 'Transition metals',
        'atomic_weight': '102.905 g/mol',
        'price': '42765 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pd',
        'name': 'Palladium',
        'atomic_number': 46,
        'group': 'Transition metals',
        'atomic_weight': '106.42 g/mol',
        'price': '7385 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ag',
        'name': 'Silver',
        'atomic_number': 47,
        'group': 'Transition metals',
        'atomic_weight': '107.868 g/mol',
        'price': '85.5 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cd',
        'name': 'Cadmium',
        'atomic_number': 48,
        'group': 'Transition metals',
        'atomic_weight': '112.411 g/mol',
        'price': '23.8 USD per 100 gram'  
    },

    {
        'element_symbol': 'In',
        'name': 'Indium',
        'atomic_number': 49,
        'group': 'Post-transition metals',
        'atomic_weight': '114.818 g/mol',
        'price': '122 USD per 100 gram'  
    },

    {
        'element_symbol': 'Sn',
        'name': 'Tin',
        'atomic_number': 50,
        'group': 'Post-transition metals',
        'atomic_weight': '118.710 g/mol',
        'price': '13.6 USD per 100 gram'  
    },

    {
        'element_symbol': 'Sb',
        'name': 'Antimony',
        'atomic_number': 51,
        'group': 'Metalloids',
        'atomic_weight': '121.760 g/mol',
        'price': '3.87 USD per 100 gram'  
    },

    {
        'element_symbol': 'Te',
        'name': 'Tellurium',
        'atomic_number': 52,
        'group': 'Metalloids',
        'atomic_weight': '127.60 g/mol',
        'price': '39.6 USD per 100 gram'  
    },

    {
        'element_symbol': 'I',
        'name': 'Iodine',
        'atomic_number': 53,
        'group': 'Halogens',
        'atomic_weight': '126.904 g/mol',
        'price': '17.3 USD per 100 gram'  
    },

    {
        'element_symbol': 'Xe',
        'name': 'Xenon',
        'atomic_number': 54,
        'group': 'Noble gases',
        'atomic_weight': '131.293 g/mol',
        'price': '180 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cs',
        'name': 'Caesium',
        'atomic_number': 55,
        'group': 'Alkali metals',
        'atomic_weight': '132.905 g/mol',
        'price': '1100 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ba',
        'name': 'Barium',
        'atomic_number': 56,
        'group': 'Alkaline earth metals',
        'atomic_weight': '137.327 g/mol',
        'price': '55 USD per 100 gram'  
    },

    {
        'element_symbol': 'La',
        'name': 'Lanthanum',
        'atomic_number': 57,
        'group': 'Lanthanoids',
        'atomic_weight': '138.905 g/mol',
        'price': '30 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ce',
        'name': 'Cerium',
        'atomic_number': 58,
        'group': 'Lanthanoids',
        'atomic_weight': '140.116 g/mol',
        'price': '32 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pr',
        'name': 'Praseodymium',
        'atomic_number': 59,
        'group': 'Lanthanoids',
        'atomic_weight': '140.904 g/mol',
        'price': '69.5 USD per 100 gram'  
    },

    {
        'element_symbol': 'Nd',
        'name': 'Neodymium',
        'atomic_number': 60,
        'group': 'Lanthanoids',
        'atomic_weight': '144.242 g/mol',
        'price': '410 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pm',
        'name': 'Promethium',
        'atomic_number': 61,
        'group': 'Lanthanoids, also radioactive',
        'atomic_weight': '144.912 g/mol',
        'price': '4600 USD per 100 gram'  
    },

    {
        'element_symbol': 'Sm',
        'name': 'Samarium',
        'atomic_number': 62,
        'group': 'Lanthanoids',
        'atomic_weight': '150.36 g/mol',
        'price': '360 USD per 100 gram'  
    },

    {
        'element_symbol': 'Eu',
        'name': 'Europium',
        'atomic_number': 63,
        'group': 'Lanthanoids',
        'atomic_weight': '151.964 g/mol',
        'price': '16.5 USD per 100 gram'  
    },

    {
        'element_symbol': 'Gd',
        'name': 'Gadolinium',
        'atomic_number': 64,
        'group': 'Lanthanoids',
        'atomic_weight': '157.25 g/mol',
        'price': '0.26 USD per 100 gram'  
    },

    {
        'element_symbol': 'Tb',
        'name': 'Terbium',
        'atomic_number': 65,
        'group': 'Lanthanoids',
        'atomic_weight': '158.925 g/mol',
        'price': '1166 USD per 100 gram'  
    },

    {
        'element_symbol': 'Dy',
        'name': 'Dysprosium',
        'atomic_number': 66,
        'group': 'Lanthanoids',
        'atomic_weight': '162.500 g/mol',
        'price': '140 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ho',
        'name': 'Holmium',
        'atomic_number': 67,
        'group': 'Lanthanoids',
        'atomic_weight': '164.93 g/mol',
        'price': '100 USD per 100 gram'  
    },

    {
        'element_symbol': 'Er',
        'name': 'Erbium',
        'atomic_number': 68,
        'group': 'Lanthanoids',
        'atomic_weight': '167.259 g/mol',
        'price': '65 USD per 100 gram'  
    },

    {
        'element_symbol': 'Tm',
        'name': 'Thulium',
        'atomic_number': 69,
        'group': 'Lanthanoids',
        'atomic_weight': '168.934 g/mol',
        'price': '1000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Yb',
        'name': 'Ytterbium',
        'atomic_number': 70,
        'group': 'Lanthanoids',
        'atomic_weight': '173.04 g/mol',
        'price': '200 USD per 100 gram'  
    },

    {
        'element_symbol': 'Lu',
        'name': 'Lutetium',
        'atomic_number': 71,
        'group': 'Lanthanoids',
        'atomic_weight': '174.967 g/mol',
        'price': '970 USD per 100 gram'  
    },

    {
        'element_symbol': 'Hf',
        'name': 'Hafnium',
        'atomic_number': 72,
        'group': 'Transition metals',
        'atomic_weight': '178.49 g/mol',
        'price': '100 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ta',
        'name': 'Tantalum',
        'atomic_number': 73,
        'group': 'Transition metals',
        'atomic_weight': '180.947 g/mol',
        'price': '520 USD per 100 gram'  
    },

    {
        'element_symbol': 'W',
        'name': 'Tungsten',
        'atomic_number': 74,
        'group': 'Transition metals',
        'atomic_weight': '183.84 g/mol',
        'price': '67 USD per 100 gram'  
    },

    {
        'element_symbol': 'Re',
        'name': 'Rhenium',
        'atomic_number': 75,
        'group': 'Transition metals',
        'atomic_weight': '186.207 g/mol',
        'price': '415 USD per 100 gram'  
    },

    {
        'element_symbol': 'Os',
        'name': 'Osmium',
        'atomic_number': 76,
        'group': 'Transition metals',
        'atomic_weight': '190.23 g/mol',
        'price': '1286 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ir',
        'name': 'Iridium',
        'atomic_number': 77,
        'group': 'Transition metals',
        'atomic_weight': '192.217 g/mol',
        'price': '5286 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pt',
        'name': 'Platinum',
        'atomic_number': 78,
        'group': 'Transition metals',
        'atomic_weight': '195.084 g/mol',
        'price': '2903 USD per 100 gram'  
    },

    {
        'element_symbol': 'Au',
        'name': 'Gold',
        'atomic_number': 79,
        'group': 'Transition metals',
        'atomic_weight': '196.966 g/mol',
        'price': '6279 USD per 100 gram'  
    },

    {
        'element_symbol': 'Hg',
        'name': 'Mercury',
        'atomic_number': 80,
        'group': 'Transition metals',
        'atomic_weight': '200.59 g/mol',
        'price': '40.9 USD per 100 gram'  
    },

    {
        'element_symbol': 'Tl',
        'name': 'Thallium',
        'atomic_number': 81,
        'group': 'Post-transition metals',
        'atomic_weight': '204.383 g/mol',
        'price': '48 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pb',
        'name': 'Lead',
        'atomic_number': 82,
        'group': 'Post-transition metals',
        'atomic_weight': '207.2 g/mol',
        'price': '2.45 USD per 100 gram'  
    },

    {
        'element_symbol': 'Bi',
        'name': 'Bismuth',
        'atomic_number': 83,
        'group': 'Post-transition metals, also radio active',
        'atomic_weight': '208.9804 g/mol',
        'price': '39 USD per 100 gram'  
    },

    {
        'element_symbol': 'Po',
        'name': 'Polonium',
        'atomic_number': 84,
        'group': 'Metalloids, also radioactive',
        'atomic_weight': '208.9824 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'At',
        'name': 'Astatine',
        'atomic_number': 85,
        'group': 'Halogens, also radioactive',
        'atomic_weight': '209.9871 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Rn',
        'name': 'Radon',
        'atomic_number': 86,
        'group': 'Noble gases, also radioactive',
        'atomic_weight': '222.0176 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Fr',
        'name': 'Francium',
        'atomic_number': 87,
        'group': 'Alkali metals, also radioactive',
        'atomic_weight': '223.0197 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ra',
        'name': 'Radium',
        'atomic_number': 88,
        'group': 'Alkaline earth metals, also radioactive',
        'atomic_weight': '226.0254 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Ac',
        'name': 'Actinium',
        'atomic_number': 89,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '227.0278 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Th',
        'name': 'Thorium',
        'atomic_number': 90,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '232.0380 g/mol',
        'price': '400 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pa',
        'name': 'Protactinium',
        'atomic_number': 91,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '231.0358 g/mol',
        'price': '28000 USD per 100 gram'  
    },

    {
        'element_symbol': 'U',
        'name': 'Uranium',
        'atomic_number': 92,
        'group': 'Actinoids',
        'atomic_weight': '238.0289 g/mol',
        'price': '191 USD per 100 gram'  
    },

    {
        'element_symbol': 'Np',
        'name': 'Neptunium',
        'atomic_number': 93,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '237.0482 g/mol',
        'price': '66000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Pu',
        'name': 'Plutonium',
        'atomic_number': 94,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '244.0642 g/mol',
        'price': '649000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Am',
        'name': 'Americium',
        'atomic_number': 95,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '243.0614 g/mol',
        'price': '150000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cm',
        'name': 'Curium',
        'atomic_number': 96,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '247.0703 g/mol',
        'price': '200000 USD per 100 gram'  
    },

    {
        'element_symbol': 'Bk',
        'name': 'Berkelium',
        'atomic_number': 97,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '247.0703 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cf',
        'name': 'Californium',
        'atomic_number': 98,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '251.0796 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Es',
        'name': 'Einsteinium',
        'atomic_number': 99,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '252.0829 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Fm',
        'name': 'Fermium',
        'atomic_number': 100,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '257.0951 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Md',
        'name': 'Mendelevium',
        'atomic_number': 101,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '258.0951 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'No',
        'name': 'Nobelium',
        'atomic_number': 102,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '259.1009 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Lr',
        'name': 'Lawrencium',
        'atomic_number': 103,
        'group': 'Actinoids, also radioactive',
        'atomic_weight': '266.1193 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Rf',
        'name': 'Rutherfordium',
        'atomic_number': 104,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '261.1087 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Db',
        'name': 'Dubnium',
        'atomic_number': 105,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '262.1138 g/mol',
        'price': '0 USD per 100 gram'  
    },     

    {
        'element_symbol': 'Sg',
        'name': 'Seaborgium',
        'atomic_number': 106,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '263.1182 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Bh',
        'name': 'Bohrium',
        'atomic_number': 107,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '262.1229 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Hs',
        'name': 'Hassium',
        'atomic_number': 108,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '269 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Mt',
        'name': 'Meitnerium',
        'atomic_number': 109,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '278 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ds',
        'name': 'Darmstadtium',
        'atomic_number': 110,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '281.1620 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Rg',
        'name': 'Roentgenium',
        'atomic_number': 111,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '281.1684 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Cn',
        'name': 'Copernicium',
        'atomic_number': 112,
        'group': 'Transition metals, also radioactive',
        'atomic_weight': '285.1744 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Nh',
        'name': 'Nihonium',
        'atomic_number': 112,
        'group': 'Post-transition metal, also radioactive',
        'atomic_weight': '286.1810 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Fl',
        'name': 'Flerovium',
        'atomic_number': 114,
        'group': 'Post-transition metals, also radioactive',
        'atomic_weight': '287.1904 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Mc',
        'name': 'Moscovium',
        'atomic_number': 115,
        'group': 'Post-transition metals, also radioactive',
        'atomic_weight': '288.1943 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Lv',
        'name': 'Livermorium',
        'atomic_number': 116,
        'group': 'Post-trasition metals, also radioactive',
        'atomic_weight': '291.2045 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Ts',
        'name': 'Tennessine',
        'atomic_number': 117,
        'group': 'Halogens, also radioactive',
        'atomic_weight': '294.2104 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Og',
        'name': 'Oganesson',
        'atomic_number': 118,
        'group': 'Noble gases, also radioactive',
        'atomic_weight': '294.2139 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Uue',
        'name': 'Ununennium',
        'atomic_number': 119,
        'group': 'Alkali metals, a theoretical element',
        'atomic_weight': '316 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Ubn',
        'name': 'Unbinilium',
        'atomic_number': 120,
        'group': 'Alkaline earth metals, a theoretical element',
        'atomic_weight': '320 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Ubu',
        'name': 'Unbiunium',
        'atomic_number': 121,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '320 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Ubb',
        'name': 'Unbibium',
        'atomic_number': 122,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '321 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ubt',
        'name': 'Unbitrium',
        'atomic_number': 123,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '325 g/mol',
        'price': '0 USD per 100 gram'   
    },

    {
        'element_symbol': 'Ubq',
        'name': 'Unbiquadium',
        'atomic_number': 124,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '330 g/mol',
        'price': '0 USD per 100 gram'  
    },

    {
        'element_symbol': 'Ubp',
        'name': 'Unbipentium',
        'atomic_number': 125,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '332 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Ubh',
        'name': 'Unbihexium',
        'atomic_number': 126,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '334 g/mol',
        'price': '0 USD per 100 gram' 
    },

    {
        'element_symbol': 'Ubs',
        'name': 'Unbiseptium',
        'atomic_number': 127,
        'group': 'Superactinoid, a theoretical element',
        'atomic_weight': '335 g/mol',
        'price': '0 USD per 100 gram'  
    }
    ]
    

#print(periodic_table)



