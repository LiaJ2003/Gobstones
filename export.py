# move this to newgame after; this is a prototype!!

# credits to https://www.guru99.com/reading-and-writing-files-in-python.html
# for code template
from marbles import Marble

def exporting(marblelist):
    f = open("commands.txt", "w+")

    for marble in marblelist:
        coords = (marble.x, marble.y)
        f.write(f'''{marble.team}
{coords}
''')
    f.close()

marble1= Marble(800, 550, 15, "red")
marble2 = Marble(400, 349, 15, "red")
marble3 = Marble(720, 847, 15, "blue")
marble4 = Marble(850, 635, 15, "blue")
marble5 = Marble(650, 435, 15, "blue")
marblelist_1 = [marble1, marble2, marble3, marble4, marble5]

exporting(marblelist_1)

def arduinoCommands(marblelist):
    f = open("ardiuno.txt", "w+")

    for marble in marblelist:
        f.write(f'''(Begin, {marble.x}, {marble.y}, End, {marble.x+60}, {marble.y+60})
''')
    f.close()

arduinoCommands(marblelist_1)

