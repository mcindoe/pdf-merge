import os

def exit():
    print('Exiting\n')
    quit()

print('\nEnter the file names you want to merge (q to quit):')

files = []

while True:
    name = input()

    if name.lower() == 'q': exit()
    if name == '': break

    if '.pdf' not in name:
        name = name + '.pdf'

    files.append(name)

if not files:
    exit()

output = input('Enter the output file name (q to quit):\n')

if output.lower() == 'q':
    exit()

if '.pdf' not in output:
    output = output + '.pdf'

command = f'gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile={output}'

for name in files:
    command = command + f' {name}'

os.system(command)

print(f'\n{output} created')

