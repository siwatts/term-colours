from basetheme import BaseTheme

# TODO: Where is a better place for this? Internal helper method
def to_decimal(hex_string):
    # Assume string of form '#abcdef', as checked in BaseTheme
    decimal_vals = []
    decimal_vals.append(str(int(hex_string[1:3], 16)))
    decimal_vals.append(str(int(hex_string[3:5], 16)))
    decimal_vals.append(str(int(hex_string[5:7], 16)))

    return ','.join(decimal_vals)

class MinttyTheme(BaseTheme):

    def __init__(self, theme):
        # Convert from an already ingested theme
        # TODO: Restructure to handle construction by either reading from
        # file like TermTheme or by taking a BaseTheme like here

        # Meta
        name = theme.name
        # Colours
        background = theme.background
        foreground = theme.foreground
        black = theme.black
        red = theme.red
        green = theme.green
        yellow = theme.yellow
        blue = theme.blue
        magenta = theme.magenta
        cyan = theme.cyan
        white = theme.white
        brightblack = theme.brightblack
        brightred = theme.brightred
        brightgreen = theme.brightgreen
        brightyellow = theme.brightyellow
        brightblue = theme.brightblue
        brightmagenta = theme.brightmagenta
        brightcyan = theme.brightcyan
        brightwhite = theme.brightwhite
        # Other
        cursor = theme.cursor

        # Call base class constructor
        BaseTheme.__init__(self, name, background, foreground, black, red,
                green, yellow, blue, magenta, cyan, white, brightblack,
                brightred, brightgreen, brightyellow, brightblue,
                brightmagenta, brightcyan, brightwhite, cursor)

    def __repr__(self):
        string_build = []
        string_build.append('BackgroundColour={}'.format(to_decimal(self.background)))
        string_build.append('ForegroundColour={}'.format(to_decimal(self.foreground)))
        string_build.append('CursorColour={}'.format(to_decimal(self.cursor)))
        string_build.append('Black={}'.format(to_decimal(self.black)))
        string_build.append('BoldBlack={}'.format(to_decimal(self.brightblack)))
        string_build.append('Red={}'.format(to_decimal(self.red)))
        string_build.append('BoldRed={}'.format(to_decimal(self.brightred)))
        string_build.append('Green={}'.format(to_decimal(self.green)))
        string_build.append('BoldGreen={}'.format(to_decimal(self.brightgreen)))
        string_build.append('Yellow={}'.format(to_decimal(self.yellow)))
        string_build.append('BoldYellow={}'.format(to_decimal(self.brightyellow)))
        string_build.append('Blue={}'.format(to_decimal(self.blue)))
        string_build.append('BoldBlue={}'.format(to_decimal(self.brightblue)))
        string_build.append('Magenta={}'.format(to_decimal(self.magenta)))
        string_build.append('BoldMagenta={}'.format(to_decimal(self.brightmagenta)))
        string_build.append('Cyan={}'.format(to_decimal(self.cyan)))
        string_build.append('BoldCyan={}'.format(to_decimal(self.brightcyan)))
        string_build.append('White={}'.format(to_decimal(self.white)))
        string_build.append('BoldWhite={}'.format(to_decimal(self.brightwhite)))

        return '\n'.join(string_build)

