# term-colours

## Terminal Colourschemes

Converters between various terminal colourscheme formats, and a repository of themes.

Will eventually contain a website for displaying and converting between them.

## Theme file format

A description for the chosen file format of colourscheme will go here. Use a
`.term` file type.

Converts to and from this and the format files of other terminal emulators.

Python configparser style file format / TOML.
- Booleans are case insensitive, accepts yes/no, true/false, on/off, 1/0.
- Section headers and sub section key/value pairs
- Strings don't need escaping

Format details:
- [Meta] section optional.
    - Stuff for printing on a future web viewer.
    - Name can default to the filename (minus an extension if we choose one).
- [Colours] section mandatory.
    - Could move BG and FG to [Other] and rename to [Palette]. Take Black and
      White as default BG/FG vals?
- [Other] section optional
    - Cursor default to FG
    - CursorForeground default to BG
    - Selection default to reversing or BrightBlack, depending on terminal?
    - `reverse` could be an option for Cursor and Selection fields instead of a
      hex colour?

```
[Meta]
Name = Friendly name
Source = Author or website
Description = Short description of theme
Is dark = True

[Colours]
Background = #000000
Foreground = #FFFFFF
Black = #123456
Red = #123456
Green = #123456
Yellow = #123456
Blue = #123456
Magenta = #123456
Cyan = #123456
White = #123456
BrightBlack = #123456
BrightRed = #123456
BrightGreen = #123456
BrightYellow = #123456
BrightBlue = #123456
BrightMagenta = #123456
BrightCyan = #123456
BrightWhite = #123456

[Other]
Cursor = #123456
CursorForeground = #123456
Selection = #123456
```

## Code

- Base (abstract?) class for colour theme
- Constructor of base class instantiates all fields required, this will ensure
  all inheriting classes meet the format
    - How about optional fields / sections?
- Classes inheriting from this will read their respective terminal colour theme
  format, mapping into inherited properties
    - eg. base reader, Xresources reader
- Where are writers?
    - Another constructor that takes any class inheriting from base class, so
      you can instatiate the class for the desired output format using any other
      class?
    - Or separate writer classes

## Requirements

- Miniconda3 environment
    - Packages?

