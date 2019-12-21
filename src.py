import json
import os

def exit():
    print('Exiting\n')
    quit()

pdfs = [x for x in os.listdir() if '.pdf' in x]

if not pdfs:
    print('\nThere are no pdfs in the current working directory')
    exit()

print('\nFiles available for merging:')
print(json.dumps(pdfs, indent = 2))

initial_message = '\nEnter the file names you want to merge (q to quit):'
print(initial_message)

files = []

while True:
    name = input()

    if name.lower() == 'q': exit()
    if name == '': break

    if '.pdf' not in name:
        name += '.pdf'

    if str(name) not in pdfs:
        print(f"*** {name} is not a pdf in the cwd, so I'm ignoring it ***")

        print(initial_message)
        for name in files:
            print(name)

    else:
        files.append(name)

if not files:
    exit()

output = input('Enter the output file name (q to quit):\n')

if output.lower() == 'q':
    exit()

if '.pdf' not in output:
    output += '.pdf'

command = f'gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile={output}'

for name in files:
    command += f' "{name}"'

os.system(command)

print(f'\n{output} created')
