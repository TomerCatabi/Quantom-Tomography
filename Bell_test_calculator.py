import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#
#
#

def file_name(a,b):
    
    directory = 'C:/Users/TomerCatabi/Desktop/physics/year 4/second semster/lab C/quantom topography/part 2/'

    a_part = ''
    b_part = ''

    if a > 0:
        a_part = '+' + str(a)
    else:
        a_part = str(a)
    if b > 0:
        b_part = '+' + str(b)
    else:
        b_part = str(b)

    f_name = directory + a_part + b_part + '.csv'
    return(f_name)

def read_counts(data):

    N_tot = 0

    num_of_col = len(data[0])
    N_matrix = np.zeros((2, num_of_col))
    x_axis = np.arange(num_of_col)

    plot_data = []
    trushold_data = []

    for j, line in enumerate(data):

        plot_data.append([x_axis, line])


        treshold = 0
        
        if j == 0:
            treshold = 100000
        elif j == 1:
            treshold = 67400


        trushold_data.append([treshold, 0, num_of_col])

        for i in range(num_of_col):
            if line[i] > treshold:
                N_matrix[j][i] = 1

    # Reading simultainous (spelling ?) hits 
    # and accounting for multiple frames bits / possible delays

    for i, bit in enumerate(N_matrix[0]):
        if bit == 1 and N_matrix[1][i] ==1:
           
            if N_matrix[0][i-1] == 1 and N_matrix[1][i] ==1:
                continue
            
            N_tot += 1
    
    plot_array = [plot_data,trushold_data]

    return (N_tot, plot_array)


def calculate_N_ab(a, b):
    
    a_b_df =  pd.read_csv(file_name(a, b), header=None)
    a_b_data = a_b_df.to_numpy()
    N_ab = read_counts(a_b_data)
    return(N_ab)


E_array = []

angles_a = [-45, 0]
angles_b = [-22.5, 22.5]

tot_plot_array = []
titles = []

for a in (angles_a):
    a_vertical = a + 90

    for b in angles_b:
        b_vertical = b + 90

        N_ab = calculate_N_ab(a, b)[0]
        N_aV_bV = calculate_N_ab(a_vertical, b_vertical)[0]
        N_a_bV = calculate_N_ab(a, b_vertical)[0]
        N_aV_b = calculate_N_ab(a_vertical, b)[0]
        
        # The following lines are used for plotting later 

        tot_plot_array.append([calculate_N_ab(a, b)[1], calculate_N_ab(a_vertical, b_vertical)[1],
                              calculate_N_ab(a, b_vertical)[1], calculate_N_ab(a_vertical, b)[1]])
        
        
        title_1 = r'$\alpha = $' + str(a) + '    ' + r'$\beta = $' + str(b)
        title_2 = r'$\alpha = $' + str(a_vertical) + '    ' + r'$\beta = $' + str(b_vertical)
        title_3 = r'$\alpha = $' + str(a) + '    ' + r'$\beta = $' + str(b)
        title_4 = r'$\alpha = $' + str(a_vertical) + '    ' + r'$\beta = $' + str(b_vertical)

        titles.append([title_1, title_2, title_3, title_4])
        
        ########################
        # End of plotting data #
        ########################

        N_tot = N_ab + N_aV_bV + N_a_bV + N_aV_b

        E = (N_ab + N_aV_bV - N_a_bV - N_aV_b)/N_tot

        E_array.append(E)

line_num = len(tot_plot_array[0])
colmn_num = len(tot_plot_array)



S = E_array[0] - E_array[1] + E_array[2] + E_array[3]

print(S)

#########################
# Starting to plot data #
#########################

# This part was originally made for testing therefore it is a little bit of a mess...

k = 1

fig , ax = plt.subplots(ncols= colmn_num, nrows= line_num, sharex= True, sharey= True)



for i in range(line_num):


    for j in range(colmn_num):
        plt.subplot(line_num, colmn_num, (i)*colmn_num + j + 1)
        plt.plot(tot_plot_array[i][j][0][0][0],tot_plot_array[i][j][0][0][1])
        plt.plot(tot_plot_array[i][j][0][1][0],tot_plot_array[i][j][0][1][1])
        plt.hlines(tot_plot_array[i][j][1][0][0], xmin=tot_plot_array[i][j][1][0][1], xmax = tot_plot_array[i][j][1][0][2], color = 'r')
        plt.hlines(tot_plot_array[i][j][1][1][0], xmin=tot_plot_array[i][j][1][1][1], xmax = tot_plot_array[i][j][1][1][2], color = 'g')

        plt.title(titles[i][j])

    
    
    k += colmn_num

fig.supylabel('Intensity [unitless]')

fig.supxlabel('Frame [unitless]')

plt.show()