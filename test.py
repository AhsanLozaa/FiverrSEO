import argparse

# Define the options
options = ['option1', 'option2', 'option3', 'option4']

# Create the argument parser
parser = argparse.ArgumentParser(description='Select multiple options from the list.')
parser.add_argument('selected_options', nargs='+', choices=options, help='Select one or more options from the list.')

# Parse the arguments
args = parser.parse_args()

# Print the selected options
print('Selected options:', args.selected_options)
