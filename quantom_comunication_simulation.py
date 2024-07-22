import numpy as np
import random
import pandas as pd


###########################################################
# Defining functions that will help us run the simulation #
###########################################################

# The following function creats our random bits generator (1 - True, 0 - False)

def generate_bits(num_of_bits):
    bits = np.zeros(num_of_bits)
    for i in range(len(bits)):
        bits[i] = random.getrandbits(1)
    return(bits)


# The following function simulates alices station measurments 
# while tol_angle varible is the laser polarization angle should there be one

def alices_unit(sent_bits, tol_angle):
    
    read_bits = np.zeros(len(sent_bits))
    sample_list = [0,1]
    
    cos = np.cos(tol_angle)
    sin = np.sin(tol_angle)


    for i , bit in enumerate(sent_bits):
        if bit == 0:
            read_bits[i] = random.choices(sample_list, weights = (cos, sin), k = 1)[0]
        elif bit == 1:
            read_bits[i] = random.choices(sample_list, weights = (sin, cos), k = 1)[0]
    
    return(read_bits)

# The following function simulates alices station measurments 
# while tol_angle varible is the laser polarization angle should there be one
# and base refers to measurments base (HHVV or HVVH)

def bobs_unit(sent_bits, tol_angle, base):

    if base == 'HHVV':
        read_bits = alices_unit(sent_bits, tol_angle)
        return(read_bits)
    elif base == 'HVVH':
        read_bits = alices_unit(sent_bits, np.pi/2 - tol_angle)
        return(read_bits)
    else:
        print('Base not recognized')
    

# The following function simulates measurments with bit_num number of bits
# laser polarization angle of tol_angle in base base

def measurements_sim(bit_num, tol_angle, base):
    
    bits = generate_bits(bit_num)
    Alices_data = alices_unit(bits, tol_angle)
    Bobs_data = bobs_unit(bits, tol_angle, base)
    return(Alices_data, Bobs_data)

# The following function calculates our measured state vector given alices and bobs data

def calculate_psi(a_data, b_data):
    
    num_of_bits = len(a_data)
    VV_count = 0
    HH_count = 0
    VH_count = 0
    HV_count = 0

    for i, bit in enumerate(a_data):
        if bit == b_data[i]:
            if bit == 1:
                VV_count += 1
            elif bit == 0:
                HH_count += 1
        else:
            if bit == 1:
                VH_count += 1
            elif bit == 0:
                HV_count += 1

    P_VV, P_HH, P_VH, P_HV = VV_count/num_of_bits, HH_count/num_of_bits, VH_count/num_of_bits, HV_count/num_of_bits
    c_VV, c_HH, c_VH, c_HV = np.sqrt(P_VV), np.sqrt(P_HH), np.sqrt(P_VH), np.sqrt(P_HV)
    
    psi = np.array([c_VV, c_VH, c_HV, c_HH])
    return(psi)


# The following function calculates the density matrix given a state vector
# and write it into a csv file using bit_num and base varibles to create name to the file

def density_mat_calculater_to_csv(bit_num, psi, base):
    
    rho = np.outer(psi, psi)
    df_rho = pd.DataFrame(rho)
    df_rho.to_csv(str(bit_num) + 'bit_num_simulation_' + base +'_rho_matrix.csv', index=False, header=False)

#########################################################################################
# Simulating the expiriment held in lab C assuming no human errors in laser polrization #
# i.e. tolrance angle given is zero                                                     #
#########################################################################################

bits_num = [10, 25, 50]
bases = ['HHVV', 'HVVH']

for bits in bits_num:
    for base in bases:
        Alices_data, Bobs_data = measurements_sim(bits, 0, base)
        psi = calculate_psi(Alices_data, Bobs_data)
        density_mat_calculater_to_csv(bits, psi, base)

