class BaseTheme:

    def __init__(self, name, background, foreground, black, red, green, yellow,
            blue, magenta, cyan, white, brightblack, brightred, brightgreen,
            brightyellow, brightblue, brightmagenta, brightcyan, brightwhite):
        # Properties
        self.name = name
        # Convert and assign colours here, for now just assume hex
        self.background = background
        self.foreground = foreground
        self.black = black
        self.red = red
        self.green = green
        self.yellow = yellow
        self.blue = blue
        self.magenta = magenta
        self.cyan = cyan
        self.white = white
        self.brightblack = brightblack
        self.brightred = brightred
        self.brightgreen = brightgreen
        self.brightyellow = brightyellow
        self.brightblue = brightblue
        self.brightmagenta = brightmagenta
        self.brightcyan = brightcyan
        self.brightwhite = brightwhite

