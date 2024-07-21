import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd


##############################################################################################
# Opening file dialoge box in so that user can choose his desired file                       #
# File should have row 1 - H_A data, row 2 - H_B data, row 3 - V_A data and row 4 - V_B data #
##############################################################################################

root = tk.Tk()
root.withdraw()

#####################
# Reading data file #
#####################

file = filedialog.askopenfilename() 

df = pd.read_csv(file, header=None)

data = df.to_numpy()

#######################
# Initiating varibles #
#######################

# counts of signal
num_of_col = len(data[0])


N_matrix = np.zeros((4, num_of_col))

N = 0

# density matrix

rho = np.zeros((4,4))

############################################
# Counting number of hits in each detector #
############################################

j = 0

for line in data:
    treshold =max(line)/1.5
    for i in range(num_of_col):
        if line[i] > treshold:
            N_matrix[j][i] = 1

    j = j+1

###################################################
# Checking for simultainous hits on the detectors #
###################################################

# This matrix will be used to store each measurment value so that index
# 0 is H_A, index 1 is H_B, index 2 is V_A and index 3 is V_B 
# The matrix values will be assiend in loop but the matrix is called here for efficiency
current_measurement_matrix = np.zeros((4)) 

# The following vectors are used later to define a our measured probability vector
HH = np.array([1, 0, 0, 0])
VV = np.array([0, 0, 0, 1])
HV = np.array([0, 1, 0, 0])
VH = np.array([0, 0, 1, 0])

# Mapping the  measurement results to the corresponding value
measurement_to_index = {
    #(H_A, H_B, V_A, V_B)
    (1, 1, 0, 0): 0,  # |HH>
    (0, 0, 1, 1): 1,  # |VV>
    (1, 0, 0, 1): 2,  # |HV>
    (0, 1, 1, 0): 3,  # |VH>

}

P_HH = 0
P_VV = 0
P_HV = 0
P_VH = 0

for i in range(num_of_col):
    

    # Reset current_measurement_matrix for each column
    current_measurement_matrix.fill(0)

    # Assuming we may have a delay of maximum +- 4 sedond between camars we measure 'hits'
    if N_matrix[0][i] == 1:
                
        N += 1

        current_measurement_matrix[0] = 1
        if any(N_matrix[1][i-30:i+30]):
            current_measurement_matrix[1] = 1
        if any(N_matrix[2][i-30:i+30]):
            current_measurement_matrix[2] = 1
        if any(N_matrix[3][i-30:i+30]):
            current_measurement_matrix[3] = 1
    
    elif N_matrix[1][i] == 1:
        
        # Making sure we dont count measurments already counted in the previues loop
        
        if any(N_matrix[0][i-30:i+30]):
            continue
        
        
        N += 1

        current_measurement_matrix[1] = 1
        if any(N_matrix[2][i-30:i+30]):
            current_measurement_matrix[2] = 1
        if any(N_matrix[3][i-30:i+30]):
            current_measurement_matrix[3] = 1
    
    elif N_matrix[2][i] == 1:
        
        # Making sure we dont count measurments already counted in the previues loop
        
        if any(N_matrix[0][i-30:i+30]):
            continue
        if any(N_matrix[1][i-30:i+30]):
            continue
        

        N += 1

        current_measurement_matrix[2] = 1
        if any(N_matrix[3][i-30:i+30]):
            current_measurement_matrix[3] = 1
    
    elif N_matrix[3][i] == 1:

        # Making sure we dont count measurments already counted in the previues loop
        
        if any(N_matrix[0][i-30:i+30]):
            continue
        if any(N_matrix[1][i-30:i+30]):
            continue
        if any(N_matrix[2][i-30:i+30]):
            continue
        
        N += 1

        current_measurement_matrix[3] = 1


    # Convert current measurement to a tuple and get the index
    current_measurement_tuple = tuple(current_measurement_matrix.astype(int))
    if current_measurement_tuple in measurement_to_index:
        value_index = measurement_to_index[current_measurement_tuple]
        if value_index == 0:
            P_HH += 1
        elif value_index == 1:
            P_VV += 1
        elif value_index == 2:
            P_HV += 1
        elif value_index == 3:
            P_VH += 1

P_HH /= N 
P_VV /= N
P_HV /= N
P_VH /= N

#####################################################################################
# The following section defines our measured vector to calculate our density matrix #
#####################################################################################

psi = np.sqrt(P_HH)*HH + np.sqrt(P_VV)*VV + np.sqrt(P_HV)*HV + np.sqrt(P_VH)*VH

####################################################
# Calculating rho using outer product multipcation #
####################################################

rho = np.outer(psi,psi)

##########################
# Saving Matrix into csv #
##########################

df_rho = pd.DataFrame(rho)

df_rho.to_csv(file[:-4] + '_rho_matrix.csv', index=False, header=False)







                