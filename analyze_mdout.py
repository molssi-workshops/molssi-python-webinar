import os
import argparse

# python analyze_mdout.py 'data/*.mdout'
# python analyze_mdout.py data/*.mdout


if __name__ == "__main__":
    
    # Use argparse to get file name.
    parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy.")
    parser.add_argument("filepath", help="The filepath to the file to be analyzed.", nargs='*')
    
    args = parser.parse_args()
    
    # Open the file for reading.
    filenames = args.filepath
    
    for filename in filenames:

        f = open(filename, 'r')
        fname = os.path.basename(filename).split('.')[0]

        # Read the data.
        data = f.readlines()

        # Close the file.
        f.close()

        f_write = open(F'{fname}_Etot.txt', 'w+')

        # Loop through lines in the file.
        values = []
        for line in data:
            # Get information from lines.
            split_line = line.split()

            if 'Etot' in line:
                #print(split_line[2])
                #f_write.write(f'{split_line[2]}\n')
                values.append(split_line[2])

        values = values[:-2]

        for value in values:
            f_write.write(F'{value}\n')

        f_write.close()