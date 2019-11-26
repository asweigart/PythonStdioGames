# This code reads in all the .py files to create the PROGRAMS list in __init__.py.
# It copies the PROGRAMS dictionary to the clipboard to paste into this file.
# It also generates the _originalFiles.zip file.
import os, pprint, zlib, pyperclip, zipfile


PROGRAMS = []

SUPPORT_FILES = {'mazerunner2d.py': ['maze11x11s1.txt', 'maze51x17s42.txt'],
                 'alphabetizewordquiz.py': ['commonenglishwords.txt'],
                 'hamsburger.py': ['nounlist.txt'],
                 'rushhour.py': ['rushhourpuzzles.txt'],
                 'sokoban.py': ['sokobanlevels.txt'],
                 'stickyhands.py': ['stickyhandslevels.txt'],
                 'periodictable.py': ['elements.csv'],
                 'mazerunnerhtml.py': ['maze11x11s1', 'maze_html_images']}

origFilesZip = zipfile.ZipFile('_originalFiles.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)

for filename in os.listdir('.'):
    if not filename.endswith('.py') or filename.startswith('_'):
        continue

    with open(filename, encoding='utf-8') as fo:
        lines = fo.readlines()
        content = ''.join(lines)

        # Get the title from the first line's comment:
        name, credit = lines[0][2:].split(',')

        # Get the description from the subsequent lines' comments:
        descLines = []
        for i in range(1, len(lines)):
            if lines[i].startswith('#'):
                descLines.append(lines[i][2:].strip())
            else:
                break
        desc = ' '.join(descLines)

        hash = zlib.adler32(content.encode('utf-8'))

        entry = {'filename': filename, 'name':name, 'desc': desc, 'hash': hash}
        PROGRAMS.append(entry)

    origFilesZip.write(filename)
    if filename in SUPPORT_FILES:
        for supportFilename in SUPPORT_FILES[filename]:
            origFilesZip.write(supportFilename)
origFilesZip.close()

pprint.pprint(PROGRAMS, indent=4, width=120)
pyperclip.copy('PROGRAMS = ' + pprint.pformat(PROGRAMS, indent=4, width=120))