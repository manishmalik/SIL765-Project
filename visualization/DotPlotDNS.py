import os

import matplotlib.pyplot as plt

dir_prefix = "C:/Users/manis/Documents/GitHub/SIL765-Project/dataset/experiment_results/"

# Read all CSV files in the directory
csv_files = ['dns_visited_experiment.csv', 'dns_not_visited_experiment.csv']

# Create a color map for each file
colors = ['red', 'green']  # specify colors for each file
color_map = {file: colors[i] for i, file in enumerate(csv_files)}

fig, ax = plt.subplots()

# Read the rank file
rank_data = {}
with open(r'C:\Users\manis\Documents\GitHub\SIL765-Project\dataset\alexa-top-1-million' + r'\top-1m.csv', 'r') as f:
    for line in f:
        values = line.strip().split(',')
        rank_data[values[1]] = int(values[0])

for i, file in enumerate(csv_files):
    # Read the CSV file
    data = []
    with open(os.path.join(dir_prefix, file), 'r') as f:
        for line in f:
            values = line.strip().split('\t')
            if len(values) >= 2:
                try:
                    # Parse relative load time and rank values
                    rel_load_time = float(values[1])
                    rank = rank_data[values[0]]
                    data.append((rel_load_time, rank))
                except ValueError:
                    # Ignore any lines that don't have valid data
                    continue

    # Plot the data with a different color
    ax.scatter(*zip(*data), c=color_map[file], label=file)

# Set the x-axis to be the load time and the y-axis to be the rank
ax.set_xlabel('Load Time (seconds)')
ax.set_ylabel('Rank')
ax.legend()

plt.savefig('dns.png')
plt.show()