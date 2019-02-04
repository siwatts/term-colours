from basetheme import BaseTheme
from termtheme import TermTheme
from minttytheme import MinttyTheme, to_decimal

theme = TermTheme('../themes/dracula.term')
print(theme.red)

minttytheme = MinttyTheme(theme)
print(minttytheme.red)

to_string = str(minttytheme)
print(to_string)

