import matplotlib.pyplot as plt
import numpy as np

# Prompt user to enter the file names for the left headphone
left_file_names = []
for i in range(2):
    file_name = input("Enter the name of data file for the left headphone {}: ".format(i + 1))
    left_file_names.append(file_name)

# Prompt user to enter the file names for the right headphone
right_file_names = []
for i in range(2):
    file_name = input("Enter the name of data file for the right headphone {}: ".format(i + 1))
    right_file_names.append(file_name)

# Prompt user to enter the offset magnitude
offset = float(input("Enter the offset magnitude: "))

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
    plt.plot(left_frequencies[i], left_magnitudes[i], '{}-'.format(colors[i]), label='Left - {}'.format(left_file_names[i]))
    plt.plot(right_frequencies[i], right_magnitudes[i], '{}-'.format(colors[i+2]), label='Right - {}'.format(right_file_names[i]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Audio Graph Tool')
plt.legend()
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.xlim(20, 20000)  # Set x-axis limits
plt.ylim(-50 + offset, 50 + offset)  # Set y-axis limits with offset
plt.grid(True)
plt.show()
