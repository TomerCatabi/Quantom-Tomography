# Quantom-Tomography
This repository consists of a TAU lab C expiriment code created by students in order to process the data that was collected in the lab.
In this particalular brunch you can find the codes relvant for the part 2 i.e. simulation of part 1.

-----
## quantom_comunication_simulation.py

This python script creates a random array of bits and than simulates part one of the expiriment using those bits (note that the bit number is currently hard coded into the code and should be changed manually for different bit numbers).

Description - The script performs the following steps:
  1. Generates a random bit sequance as specified
  2. Calculates the measured bits in Alice's and Bob's stations according to given tolrance angle
  3. Calculates the measurment state vector psi and subsequently the density matrix
  4. Saves the density matrix into a CSV file

Usage - 
  1. Alter the number of bits and the tolrance angle to the desired values
  2. Run python script and find your matrices CSV files in the same directory of the python script 

Dependencies -
  * numpy
  * random
  * pandas
