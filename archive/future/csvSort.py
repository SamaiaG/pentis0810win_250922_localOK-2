import csv
import os
from pathlib import Path
os.chdir(Path(__file__).parent)

with open('testscores.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Sort the data by the first column
    sorted_data = sorted(reader, key=lambda row: row[0])

    # Write the sorted data to the output file
    for row in sorted_data:
        writer.writerow(row)
