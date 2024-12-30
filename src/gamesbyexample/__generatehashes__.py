# This code reads in all the .py files to create the PROGRAMS list in __init__.py.
# It copies the PROGRAMS dictionary to the clipboard to paste into this file.
# It also generates the _originalFiles.zip file.
import os
import pprint
import zipfile
import zlib

PROGRAMS = []

SUPPORT_FILES = {
    'mazerunner2d.py': ['maze11x11s1.txt', 'maze51x17s42.txt'],
    'alphabetizewordquiz.py': ['commonenglishwords.txt'],
    'hamsburger.py': ['nounlist.txt'],
    'rushhour.py': ['rushhourpuzzles.txt'],
    'sokoban.py': ['sokobanlevels.txt'],
    'parkingvalet.py': ['parkingvaletpuzzles.txt'],
    #'stickyhands.py': ['stickyhandslevels.txt'],
    'periodictable.py': ['periodictable.csv'],
    #'mazerunnerhtml.py': ['maze11x11s1', 'maze_html_images', 'maze_html_images/A.jpg', 'maze_html_images/AB.jpg', 'maze_html_images/ABC.jpg', 'maze_html_images/ABCD.jpg', 'maze_html_images/ABCDE.jpg', 'maze_html_images/ABCDEF.jpg', 'maze_html_images/ABCDEF_exitback.jpg', 'maze_html_images/ABCDEF_exitleft.jpg', 'maze_html_images/ABCDEF_exitright.jpg', 'maze_html_images/ABCDE_exitback.jpg', 'maze_html_images/ABCDE_exitleft.jpg', 'maze_html_images/ABCDE_exitright.jpg', 'maze_html_images/ABCDF.jpg', 'maze_html_images/ABCDF_exitback.jpg', 'maze_html_images/ABCDF_exitleft.jpg', 'maze_html_images/ABCDF_exitright.jpg', 'maze_html_images/ABCD_exitback.jpg', 'maze_html_images/ABCD_exitleft.jpg', 'maze_html_images/ABCD_exitright.jpg', 'maze_html_images/ABCE.jpg', 'maze_html_images/ABCEF.jpg', 'maze_html_images/ABCEF_exitback.jpg', 'maze_html_images/ABCEF_exitleft.jpg', 'maze_html_images/ABCEF_exitright.jpg', 'maze_html_images/ABCE_exitback.jpg', 'maze_html_images/ABCE_exitleft.jpg', 'maze_html_images/ABCE_exitright.jpg', 'maze_html_images/ABCF.jpg', 'maze_html_images/ABCF_exitback.jpg', 'maze_html_images/ABCF_exitleft.jpg', 'maze_html_images/ABCF_exitright.jpg', 'maze_html_images/ABC_exitback.jpg', 'maze_html_images/ABC_exitleft.jpg', 'maze_html_images/ABC_exitright.jpg', 'maze_html_images/ABD.jpg', 'maze_html_images/ABDE.jpg', 'maze_html_images/ABDEF.jpg', 'maze_html_images/ABDEF_exitback.jpg', 'maze_html_images/ABDEF_exitleft.jpg', 'maze_html_images/ABDEF_exitright.jpg', 'maze_html_images/ABDE_exitback.jpg', 'maze_html_images/ABDE_exitleft.jpg', 'maze_html_images/ABDE_exitright.jpg', 'maze_html_images/ABDF.jpg', 'maze_html_images/ABDF_exitback.jpg', 'maze_html_images/ABDF_exitleft.jpg', 'maze_html_images/ABDF_exitright.jpg', 'maze_html_images/ABD_exitback.jpg', 'maze_html_images/ABD_exitleft.jpg', 'maze_html_images/ABD_exitright.jpg', 'maze_html_images/ABE.jpg', 'maze_html_images/ABEF.jpg', 'maze_html_images/ABEF_exitback.jpg', 'maze_html_images/ABEF_exitleft.jpg', 'maze_html_images/ABEF_exitright.jpg', 'maze_html_images/ABE_exitback.jpg', 'maze_html_images/ABE_exitleft.jpg', 'maze_html_images/ABE_exitright.jpg', 'maze_html_images/ABF.jpg', 'maze_html_images/ABF_exitback.jpg', 'maze_html_images/ABF_exitleft.jpg', 'maze_html_images/ABF_exitright.jpg', 'maze_html_images/AB_exitback.jpg', 'maze_html_images/AB_exitleft.jpg', 'maze_html_images/AB_exitright.jpg', 'maze_html_images/AC.jpg', 'maze_html_images/ACD.jpg', 'maze_html_images/ACDE.jpg', 'maze_html_images/ACDEF.jpg', 'maze_html_images/ACDEF_exitback.jpg', 'maze_html_images/ACDEF_exitleft.jpg', 'maze_html_images/ACDEF_exitright.jpg', 'maze_html_images/ACDE_exitback.jpg', 'maze_html_images/ACDE_exitleft.jpg', 'maze_html_images/ACDE_exitright.jpg', 'maze_html_images/ACDF.jpg', 'maze_html_images/ACDF_exitback.jpg', 'maze_html_images/ACDF_exitleft.jpg', 'maze_html_images/ACDF_exitright.jpg', 'maze_html_images/ACD_exitback.jpg', 'maze_html_images/ACD_exitleft.jpg', 'maze_html_images/ACD_exitright.jpg', 'maze_html_images/ACE.jpg', 'maze_html_images/ACEF.jpg', 'maze_html_images/ACEF_exitback.jpg', 'maze_html_images/ACEF_exitleft.jpg', 'maze_html_images/ACEF_exitright.jpg', 'maze_html_images/ACE_exitback.jpg', 'maze_html_images/ACE_exitleft.jpg', 'maze_html_images/ACE_exitright.jpg', 'maze_html_images/ACF.jpg', 'maze_html_images/ACF_exitback.jpg', 'maze_html_images/ACF_exitleft.jpg', 'maze_html_images/ACF_exitright.jpg', 'maze_html_images/AC_exitback.jpg', 'maze_html_images/AC_exitleft.jpg', 'maze_html_images/AC_exitright.jpg', 'maze_html_images/AD.jpg', 'maze_html_images/ADE.jpg', 'maze_html_images/ADEF.jpg', 'maze_html_images/ADEF_exitback.jpg', 'maze_html_images/ADEF_exitleft.jpg', 'maze_html_images/ADEF_exitright.jpg', 'maze_html_images/ADE_exitback.jpg', 'maze_html_images/ADE_exitleft.jpg', 'maze_html_images/ADE_exitright.jpg', 'maze_html_images/ADF.jpg', 'maze_html_images/ADF_exitback.jpg', 'maze_html_images/ADF_exitleft.jpg', 'maze_html_images/ADF_exitright.jpg', 'maze_html_images/AD_exitback.jpg', 'maze_html_images/AD_exitleft.jpg', 'maze_html_images/AD_exitright.jpg', 'maze_html_images/AE.jpg', 'maze_html_images/AEF.jpg', 'maze_html_images/AEF_exitback.jpg', 'maze_html_images/AEF_exitleft.jpg', 'maze_html_images/AEF_exitright.jpg', 'maze_html_images/AE_exitback.jpg', 'maze_html_images/AE_exitleft.jpg', 'maze_html_images/AE_exitright.jpg', 'maze_html_images/AF.jpg', 'maze_html_images/AF_exitback.jpg', 'maze_html_images/AF_exitleft.jpg', 'maze_html_images/AF_exitright.jpg', 'maze_html_images/A_exitback.jpg', 'maze_html_images/A_exitleft.jpg', 'maze_html_images/A_exitright.jpg', 'maze_html_images/B.jpg', 'maze_html_images/BC.jpg', 'maze_html_images/BCD.jpg', 'maze_html_images/BCDE.jpg', 'maze_html_images/BCDEF.jpg', 'maze_html_images/BCDEF_exitback.jpg', 'maze_html_images/BCDEF_exitleft.jpg', 'maze_html_images/BCDEF_exitright.jpg', 'maze_html_images/BCDE_exitback.jpg', 'maze_html_images/BCDE_exitleft.jpg', 'maze_html_images/BCDE_exitright.jpg', 'maze_html_images/BCDF.jpg', 'maze_html_images/BCDF_exitback.jpg', 'maze_html_images/BCDF_exitleft.jpg', 'maze_html_images/BCDF_exitright.jpg', 'maze_html_images/BCD_exitback.jpg', 'maze_html_images/BCD_exitleft.jpg', 'maze_html_images/BCD_exitright.jpg', 'maze_html_images/BCE.jpg', 'maze_html_images/BCEF.jpg', 'maze_html_images/BCEF_exitback.jpg', 'maze_html_images/BCEF_exitleft.jpg', 'maze_html_images/BCEF_exitright.jpg', 'maze_html_images/BCE_exitback.jpg', 'maze_html_images/BCE_exitleft.jpg', 'maze_html_images/BCE_exitright.jpg', 'maze_html_images/BCF.jpg', 'maze_html_images/BCF_exitback.jpg', 'maze_html_images/BCF_exitleft.jpg', 'maze_html_images/BCF_exitright.jpg', 'maze_html_images/BC_exitback.jpg', 'maze_html_images/BC_exitleft.jpg', 'maze_html_images/BC_exitright.jpg', 'maze_html_images/BD.jpg', 'maze_html_images/BDE.jpg', 'maze_html_images/BDEF.jpg', 'maze_html_images/BDEF_exitback.jpg', 'maze_html_images/BDEF_exitleft.jpg', 'maze_html_images/BDEF_exitright.jpg', 'maze_html_images/BDE_exitback.jpg', 'maze_html_images/BDE_exitleft.jpg', 'maze_html_images/BDE_exitright.jpg', 'maze_html_images/BDF.jpg', 'maze_html_images/BDF_exitback.jpg', 'maze_html_images/BDF_exitleft.jpg', 'maze_html_images/BDF_exitright.jpg', 'maze_html_images/BD_exitback.jpg', 'maze_html_images/BD_exitleft.jpg', 'maze_html_images/BD_exitright.jpg', 'maze_html_images/BE.jpg', 'maze_html_images/BEF.jpg', 'maze_html_images/BEF_exitback.jpg', 'maze_html_images/BEF_exitleft.jpg', 'maze_html_images/BEF_exitright.jpg', 'maze_html_images/BE_exitback.jpg', 'maze_html_images/BE_exitleft.jpg', 'maze_html_images/BE_exitright.jpg', 'maze_html_images/BF.jpg', 'maze_html_images/BF_exitback.jpg', 'maze_html_images/BF_exitleft.jpg', 'maze_html_images/BF_exitright.jpg', 'maze_html_images/B_exitback.jpg', 'maze_html_images/B_exitleft.jpg', 'maze_html_images/B_exitright.jpg', 'maze_html_images/C.jpg', 'maze_html_images/CD.jpg', 'maze_html_images/CDE.jpg', 'maze_html_images/CDEF.jpg', 'maze_html_images/CDEF_exitback.jpg', 'maze_html_images/CDEF_exitleft.jpg', 'maze_html_images/CDEF_exitright.jpg', 'maze_html_images/CDE_exitback.jpg', 'maze_html_images/CDE_exitleft.jpg', 'maze_html_images/CDE_exitright.jpg', 'maze_html_images/CDF.jpg', 'maze_html_images/CDF_exitback.jpg', 'maze_html_images/CDF_exitleft.jpg', 'maze_html_images/CDF_exitright.jpg', 'maze_html_images/CD_exitback.jpg', 'maze_html_images/CD_exitleft.jpg', 'maze_html_images/CD_exitright.jpg', 'maze_html_images/CE.jpg', 'maze_html_images/CEF.jpg', 'maze_html_images/CEF_exitback.jpg', 'maze_html_images/CEF_exitleft.jpg', 'maze_html_images/CEF_exitright.jpg', 'maze_html_images/CE_exitback.jpg', 'maze_html_images/CE_exitleft.jpg', 'maze_html_images/CE_exitright.jpg', 'maze_html_images/CF.jpg', 'maze_html_images/CF_exitback.jpg', 'maze_html_images/CF_exitleft.jpg', 'maze_html_images/CF_exitright.jpg', 'maze_html_images/C_exitback.jpg', 'maze_html_images/C_exitleft.jpg', 'maze_html_images/C_exitright.jpg', 'maze_html_images/D.jpg', 'maze_html_images/DE.jpg', 'maze_html_images/DEF.jpg', 'maze_html_images/DEF_exitback.jpg', 'maze_html_images/DEF_exitleft.jpg', 'maze_html_images/DEF_exitright.jpg', 'maze_html_images/DE_exitback.jpg', 'maze_html_images/DE_exitleft.jpg', 'maze_html_images/DE_exitright.jpg', 'maze_html_images/DF.jpg', 'maze_html_images/DF_exitback.jpg', 'maze_html_images/DF_exitleft.jpg', 'maze_html_images/DF_exitright.jpg', 'maze_html_images/D_exitback.jpg', 'maze_html_images/D_exitleft.jpg', 'maze_html_images/D_exitright.jpg', 'maze_html_images/E.jpg', 'maze_html_images/EF.jpg', 'maze_html_images/EF_exitback.jpg', 'maze_html_images/EF_exitleft.jpg', 'maze_html_images/EF_exitright.jpg', 'maze_html_images/E_exitback.jpg', 'maze_html_images/E_exitleft.jpg', 'maze_html_images/E_exitright.jpg', 'maze_html_images/F.jpg', 'maze_html_images/forward.png', 'maze_html_images/F_exitback.jpg', 'maze_html_images/F_exitleft.jpg', 'maze_html_images/F_exitright.jpg', 'maze_html_images/OPEN.jpg', 'maze_html_images/OPEN_exitback.jpg', 'maze_html_images/OPEN_exitleft.jpg', 'maze_html_images/OPEN_exitright.jpg', 'maze_html_images/turn_left.png', 'maze_html_images/turn_right.png'],
    'sudoku.py': ['sudokupuzzles.txt'],
    # Pygame games
    'pygame_games/flippy.py': [
        'pygame_games',
        'pygame_games/freesansbold.ttf',
        'pygame_games/flippyboard.png',
        'pygame_games/flippybackground.png',
    ],
    'pygame_games/fourinarow.py': [
        'pygame_games/4row_red.png',
        'pygame_games/4row_black.png',
        'pygame_games/4row_humanwinner.png',
        'pygame_games/4row_computerwinner.png',
        'pygame_games/4row_tie.png',
        'pygame_games/4row_arrow.png',
    ],
    'pygame_games/gemgem.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/badswap.wav',
        'pygame_games/match0.wav',
        'pygame_games/match1.wav',
        'pygame_games/match2.wav',
        'pygame_games/match3.wav',
        'pygame_games/match4.wav',
        'pygame_games/match5.wav',
        'pygame_games/gem1.png',
        'pygame_games/gem2.png',
        'pygame_games/gem3.png',
        'pygame_games/gem4.png',
        'pygame_games/gem5.png',
        'pygame_games/gem6.png',
        'pygame_games/gem7.png',
    ],
    'pygame_games/inkspill.py': [
        'pygame_games/inkspilllogo.png',
        'pygame_games/inkspillspot.png',
        'pygame_games/inkspillsettings.png',
        'pygame_games/inkspillsettingsbutton.png',
        'pygame_games/inkspillresetbutton.png',
    ],
    'pygame_games/pentomino.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/tetrisb.mid',
        'pygame_games/tetrisc.mid',
    ],
    'pygame_games/simulate.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/beep1.ogg',
        'pygame_games/beep2.ogg',
        'pygame_games/beep3.ogg',
        'pygame_games/beep4.ogg',
    ],
    'pygame_games/slidepuzzle.py': ['pygame_games/freesansbold.ttf'],
    'pygame_games/squirrel.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/gameicon.png',
        'pygame_games/squirrel.png',
        'pygame_games/grass1.png',
        'pygame_games/grass2.png',
        'pygame_games/grass3.png',
        'pygame_games/grass4.png',
    ],
    'pygame_games/starpusher.py': [
        'pygame_games/RedSelector.png',
        'pygame_games/Selector.png',
        'pygame_games/Star.png',
        'pygame_games/Wall_Block_Tall.png',
        'pygame_games/Wood_Block_Tall.png',
        'pygame_games/Plain_Block.png',
        'pygame_games/Grass_Block.png',
        'pygame_games/star_title.png',
        'pygame_games/star_solved.png',
        'pygame_games/princess.png',
        'pygame_games/boy.png',
        'pygame_games/catgirl.png',
        'pygame_games/horngirl.png',
        'pygame_games/pinkgirl.png',
        'pygame_games/Rock.png',
        'pygame_games/Tree_Short.png',
        'pygame_games/Tree_Tall.png',
        'pygame_games/Tree_Ugly.png',
        'pygame_games/starPusherLevels.txt',
    ],
    'pygame_games/tetromino.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/tetrisb.mid',
        'pygame_games/tetrisc.mid',
    ],
    'pygame_games/tetrominoforidiots.py': [
        'pygame_games/freesansbold.ttf',
        'pygame_games/tetrisb.mid',
        'pygame_games/tetrisc.mid',
    ],
    'pygame_games/wormy.py': ['pygame_games/freesansbold.ttf'],
}

IGNORE_FILES = [
    'tutorialguess1.py',
    'tutorialguess2.py',
    'tutorialguess3.py',
    'tutorialguess4.py',
    'tutorialguess5.py',
    'tutorialguess6.py',
    'tutorialguess7.py',
    'zombiebitefight.py',
]

origFilesZip = zipfile.ZipFile('_originalFiles.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)


# allFiles = os.listdir('.') + ['pygame_games/' + f for f in os.listdir('pygame_games')]
allFiles = [
    'affinecipher.py',
    'alphabetizequiz.py',
    'alphabetizewordquiz.py',
    'analogclock.py',
    'bagels.py',
    'barca.py',
    'birthdayparadox.py',
    'bitmapmessage.py',
    'blackjack.py',
    'bouncingdots.py',
    'bouncingdvd.py',
    'bouncinglines.py',
    'caesarcipher.py',
    'caesarhacker.py',
    'calendarmaker.py',
    'carrotinabox.py',
    'chancecheckers.py',
    'checkers.py',
    'chohan.py',
    'chomp.py',
    'clickbait.py',
    'coinflipsimulator.py',
    'collatz.py',
    'collatzstats.py',
    'conwaysgameoflife.py',
    'conwaysgameoflife2.py',
    'countdown.py',
    'countingquiz.py',
    'deepcave.py',
    'diagonalmaze.py',
    'diamonds.py',
    'dicemath.py',
    'diceroller.py',
    'digitalclock.py',
    'digitalstream.py',
    'dna.py',
    'ducklings.py',
    'eenymeeny.py',
    'etchingdrawer.py',
    'factorfinder.py',
    'fastdraw.py',
    'fibonacci.py',
    'fireflies.py',
    'fishtank.py',
    'fizzbuzz.py',
    'fizzbuzzgame.py',
    'flooder.py',
    'floorpainters.py',
    'forestfiresim.py',
    'fourinarow.py',
    'fractalnonuniformtree.py',
    'fractaltree.py',
    'ghostleglottery.py',
    'gomoku.py',
    'guess.py',
    'guillotine.py',
    'gullible.py',
    'hacking.py',
    'hammurabi.py',
    'hamsburger.py',
    'hangman.py',
    'hangmanunfair.py',
    'hardcodedtictactoe.py',
    'hexapawn.py',
    'hexgrid.py',
    'hilbertcurve.py',
    'hourglass.py',
    'hungryrobots.py',
    'jaccuse.py',
    'kaprekarnumbers.py',
    'kochsnowflake.py',
    'langtonsant.py',
    'lawnmower.py',
    'leetspeak.py',
    'lostkitty.py',
    'luckystars.py',
    'luhn.py',
    'magicfortuneball.py',
    'magichexagon.py',
    'mancala.py',
    'matchingparens.py',
    'mazemakerrec.py',
    'mazerunner2d.py',
    'mazerunner3d.py',
    'middleletterscrambler.py',
    'milliondicestats.py',
    'monalisa.py',
    'mondrian.py',
    'montyhall.py',
    'morsecode.py',
    'multiplicationtable.py',
    'multiplicativepersistence.py',
    'ninetyninebottles.py',
    'ninetyninebottles2.py',
    'numeralsystems.py',
    'parkingvalet.py',
    'pegsolitaire.py',
    'periodictable.py',
    'piglatin.py',
    'polygons.py',
    'powerballlottery.py',
    'primenumbers.py',
    'progressbar.py',
    'pythons.py',
    'railfencecipher.py',
    'rainbow.py',
    'rainbow2.py',
    'randomwalk.py',
    'reversegam.py',
    'rockpaperscissors.py',
    'rockpaperscissorsalwayswin.py',
    'rot13cipher.py',
    'rotatingcube.py',
    'royalgameofur.py',
    'sandsimulator.py',
    'sevseg.py',
    'shellgame.py',
    'shimmer.py',
    'shiningcarpet.py',
    'sierpinskisgame.py',
    'sierpinskisquare.py',
    'sierpinskitriangle.py',
    'simplesubcipher.py',
    'sinemessage.py',
    'slidingtilepuzzle.py',
    'slitheringsnakes.py',
    'snailrace.py',
    'sokoban.py',
    'sonar.py',
    'soroban.py',
    'soundmimic.py',
    'spongecase.py',
    'squiggles.py',
    'sudoku.py',
    'texttospeechtalker.py',
    'threecardmonte.py',
    'tictactoe.py',
    'tictactoeoop.py',
    'towerofhanoi.py',
    'trickquestions.py',
    'turtledemowrapper.py',
    'twentyfortyeight.py',
    'ulamspiral.py',
    'ultimatetictactoe.py',
    'vacuumbot.py',
    'vigenerecipher.py',
    'waterbucket.py',
    'zigzag.py',
]
allFiles.extend(['pygame_games/' + f for f in os.listdir('pygame_games')])

pyflakesChecklist = []

for filename in allFiles:
    if not filename.endswith('.py') or filename.startswith('_') or filename in IGNORE_FILES:
        continue

    if 'pygame_games' not in filename:
        # The pygame games have a lot of pyflakes false positives, so we'll skip them.
        pyflakesChecklist.append(filename)

    print('Processing', filename)

    with open(filename, encoding='utf-8') as fo:
        lines = fo.readlines()
        content = ''.join(lines)
        # Get the title from the first line's comment:
        try:
            name, credit = lines[0][3:].split(',')
        except:
            print('WARNING: Badly formed credit docstring in', filename)
            name = lines[0]
            # raise

        # Get the description from the subsequent lines' comments:
        descLines = []
        for i in range(1, len(lines)):
            if '"""' not in lines[i]:
                descLines.append(lines[i])
            else:
                descLines.append(lines[i].replace('"""', ''))
                break
        desc = ''.join(descLines)

        # Remove "This and other games are available at https://nostarch.com/XX"
        desc = desc.replace('This and other games are available at https://nostarch.com/XX\n', '')

        hash = zlib.adler32(content.encode('utf-8'))

        entry = {'filename': filename, 'name': name, 'desc': desc, 'hash': hash}
        PROGRAMS.append(entry)

    origFilesZip.write(filename)
    if filename in SUPPORT_FILES:
        for supportFilename in SUPPORT_FILES[filename]:
            if not os.path.exists(supportFilename):
                raise Exception(supportFilename + ' does not exist. Halting.')
            origFilesZip.write(supportFilename)
origFilesZip.close()

with open('__programdata__.py', 'w', encoding='utf-8') as programDataFile:
    programDataFile.write('PROGRAMS = ' + pprint.pformat(PROGRAMS, indent=4, width=120))
    programDataFile.write('\n\n\n')
    programDataFile.write('SUPPORT_FILES = ' + pprint.pformat(SUPPORT_FILES, indent=4, width=120))

print('Generating __pyflakescheck__.bat')
with open('__pyflakescheck__.bat', 'w') as pyflakeBatFile:
    for filename in pyflakesChecklist:
        pyflakeBatFile.write('@echo Checking ' + filename + '...\n')
        pyflakeBatFile.write('@pyflakes ' + filename + '\n')

print('Done.')
