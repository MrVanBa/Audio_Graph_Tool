import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter import Tk, filedialog

# Initialize the Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

# Prompt user to select the file names for the left headphone
left_file_names = []
for i in range(2):
    while True:
        file_path = filedialog.askopenfilename(title="Select data file for the left headphone {}".format(i + 1))
        if os.path.isfile(file_path):
            left_file_names.append(file_path)
            break
        else:
            print("Invalid file or file doesn't exist. Please try again.")

# Prompt user to select the file names for the right headphone
right_file_names = []
for i in range(2):
    while True:
        file_path = filedialog.askopenfilename(title="Select data file for the right headphone {}".format(i + 1))
        if os.path.isfile(file_path):
            right_file_names.append(file_path)
            break
        else:
            print("Invalid file or file doesn't exist. Please try again.")

# Prompt user to enter the offset magnitude
while True:
    offset_str = input("Enter the offset magnitude: ")
    if offset_str.strip() != "":
        try:
            offset = float(offset_str)
            break
        except ValueError:
            print("Invalid offset magnitude. Please enter a valid number.")
    else:
        print("Offset magnitude cannot be empty. Please try again.")

# Initialize lists for frequency and magnitude data
left_frequencies = []
left_magnitudes = []
right_frequencies = []
right_magnitudes = []

# Read data from the text files for the left headphone
for file_name in left_file_names:
    frequency = []
    magnitude = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split()
            freq = float(line[0])
            mag = float(line[1])
            if 20 <= freq <= 20000:
                magnitude.append(mag + offset)
                frequency.append(freq)
    left_frequencies.append(frequency)
    left_magnitudes.append(magnitude)

# Read data from the text files for the right headphone
for file_name in right_file_names:
    frequency = []
    magnitude = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().split()
            freq = float(line[0])
            mag = float(line[1])
            if 20 <= freq <= 20000:
                magnitude.append(mag + offset)
                frequency.append(freq)
    right_frequencies.append(frequency)
    right_magnitudes.append(magnitude)

# Plotting the graph
colors = ['b', 'r', 'g', 'm']  # Color for each line
for i in range(2):
    # Get the file name from the full path
    left_file_name = os.path.basename(left_file_names[i])
    right_file_name = os.path.basename(right_file_names[i])
    
    plt.plot(left_frequencies[i], left_magnitudes[i], '{}-'.format(colors[i]), label='Left - {}'.format(left_file_name))
    plt.plot(right_frequencies[i], right_magnitudes[i], '{}-'.format(colors[i+2]), label='Right - {}'.format(right_file_name))

# Calculate the marker frequencies
marker_frequencies = [20]
x = 0
while 20 * 5 ** x <= 22000:
    marker_frequencies.append(20 * 5 ** x)
    x += 1
marker_frequencies.append(20000)  # Add 22000 Hz to the marker frequencies

# Add marker lines at frequency borders and marker frequencies
for frequency in marker_frequencies:
    plt.axvline(x=frequency, color='k', linestyle='--', alpha=0.5)
    plt.text(frequency, plt.ylim()[1] + 5, '{} Hz'.format(frequency), ha='center')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Audio Wave Graph Tool')
plt.legend()
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.xlim(20, 20000)  # Set x-axis limits
plt.ylim(-50 + offset, 50 + offset)  # Set y-axis limits with offset
plt.grid(True)
plt.show()
