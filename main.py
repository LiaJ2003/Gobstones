from cmu_graphics import *

from home import *
from newgame import *
from contgame import *
from helpscreen import *
from settings import *


def onAppStart(app):
    print('In onAppStart')



def onAppStop(app):
    print('In onAppStop')

##################################
# main
##################################

def main():
    runAppWithScreens(initialScreen='home', width=1600, height = 800)

main()