import configparser
from basetheme import BaseTheme

class TermTheme(BaseTheme):

    def __init__(self, filepath):
        # Read in the file using ConfigParser, since this is our bespoke format
        theme = configparser.ConfigParser()
        theme.read(filepath)

        # TODO: Handle other properties with defaults and convert between
        # colour formats etc. 255 -> hex. Missing properties?
        # Meta
        name = theme['Meta']['Name']
        # Colours
        background = theme['Colours']['Background']
        foreground = theme['Colours']['Foreground']
        black = theme['Colours']['Black']
        red = theme['Colours']['Red']
        green = theme['Colours']['Green']
        yellow = theme['Colours']['Yellow']
        blue = theme['Colours']['Blue']
        magenta = theme['Colours']['Magenta']
        cyan = theme['Colours']['Cyan']
        white = theme['Colours']['White']
        brightblack = theme['Colours']['BrightBlack']
        brightred = theme['Colours']['BrightRed']
        brightgreen = theme['Colours']['BrightGreen']
        brightyellow = theme['Colours']['BrightYellow']
        brightblue = theme['Colours']['BrightBlue']
        brightmagenta = theme['Colours']['BrightMagenta']
        brightcyan = theme['Colours']['BrightCyan']
        brightwhite = theme['Colours']['BrightWhite']

        # Call base class constructor
        BaseTheme.__init__(self, name, background, foreground, black, red,
                green, yellow, blue, magenta, cyan, white, brightblack,
                brightred, brightgreen, brightyellow, brightblue,
                brightmagenta, brightcyan, brightwhite)

