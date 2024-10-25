import sys
import matplotlib.pyplot as plt

# File names
query_file = "normalized_rescale_sorted.tsv"
reference_file = "reference.hist"

# Read data from query and reference files
query_data = []
reference_data = []

with open(query_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            x, y = map(float, line.split())
            query_data.append((x, y))

with open(reference_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            x, y = map(float, line.split())
            reference_data.append((x, y))

# Plot the data
plt.plot([x for x, _ in query_data], [y for _, y in query_data], label='Rescaled Query', color='purple')
plt.plot([x for x, _ in reference_data], [y for _, y in reference_data], label='Reference', color='cyan')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Rescaled Query vs. Reference')
plt.legend()

# Save the plot as a PNG image
plt.savefig('plot2.png')
plt.show()
