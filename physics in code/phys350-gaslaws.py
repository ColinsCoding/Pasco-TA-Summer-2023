# Air is roughly 78% nitrogen, 21% oxygen, and 1% Argon
# O2 molar mass = 32 g/mol
# N2 molar mass = 28 g/mol
# Ar molar mass = 40 g/mol

# 1 mole of gas = 22.4 L at STP
# 1 atm = 101325 Pa 
# 1 atm = 760 mmHg 
# 1 atm = 14.7 psi
# 1 atm = 1.01325 bar

# calculate the weighted average 
# of the molar masses of the gases

# 9 in the lab 
N2_per = 0.78
O2_per = 0.21
Ar_per = 0.01

N2_mol = 28 # g/mol
O2_mol = 32 # g/mol
Ar_mol = 40 # g/mol

# calculate the weighted average
weighted_avg = (N2_per * N2_mol) + (O2_per * O2_mol) + (Ar_per * Ar_mol)

# set the number of sig figs
weighted_avg = round(weighted_avg, 3)

print("The weighted average of the molar masses of the gases is: ", weighted_avg, "g/mol")

# 10 Convert the mass of the gas into number of moles
# divide weighted average by avagarado's number
moles = weighted_avg / 6.02214076e23 

# set the number of digits before the exponent
# moles = round(moles, 3) its not doing what i want it to do
# # moles = round(moles, 6)

print("The number of moles is: ", moles, "mol")

