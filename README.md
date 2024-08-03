# Quantom-Tomography

## General
This repository consists of a TAU lab C expiriment code created by students in order to process the data that was collected in the lab
In this particalular brunch you can find the codes relvant for the part 1 i.e. density matrix calculations.

-----
## plotter_gary.m
This matlab script reads video file of the expiriment and extruct the the intensities read by the camera choosen so that the user can extruct it to a csv file.

Description - The scripts performs the following steps
  1. Reads vidoe file
  2. Itrates over each frame and calcualte the intensity value for the choosen camera
  3. Save the data into a matlab varible the user can extruct into a csv file

Usage -
  1. Ensure file is in the same directory as the script.
  2. Run matlab script
  3. Exturct data from matlab interface into a CSV file manually

** Please note that the python file reads data from a CVS file for wich each line corrsipnds to data from a different camera and each coulmn corisponds to a different frame. All toghter each CVS file should have 4 lines, and number of doulmns equal to the number of frames for the video you are currently analyzing. Therefore in order to use the rest of the code provided one should extruct the data with the relvant format in mind.

-----
## density_matrix_part_1.py

This python script reads a CSV file with the measured data from the expiriment, calcualtes the density matrix according to the given data and generates a CSV file with the density martrix calculated.

Description - The scripts performs the following steps
  1. Prompts user to choose the relvant file
  2. Itrates over the file and identify simultaneous reads
  3. Use data to calculate psi vector
  4. Use psi vector to calculate the density matrix
  5. Save calculated density matrix into a CSV file

Usage -
  1. Run script
  2. Choose relvant file from file explorer window
  3. CSV file will appear in the same directory as the pyhton script

Dependencies -
 * Tkinter
 * pandas
 * numpy
