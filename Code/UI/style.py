# Define colors, fonts, and other style-related constants here.

# Colors
BACKGROUND_COLOR = '#242424' #dark grey
SIDE_FRAME_COLOR = '#5F1E89' #purple. can do red ( #772819 ), it matches style too
#BUTTON_BG_COLOR = 'light blue'
TEXT_COLOR = '#8DC12D'
TEXT_HIGHLIGHT_COLOR = '#AD3828'  # Red text color for word "Zmeya"
#BUTTON_HIGHLIGHT_COLOR = 'light blue'

# Fonts
FONT_LARGE = ('DIN Condensed', 16, "bold") #DIN Condensed matching the font style I used fro buttons
FONT_MEDIUM = ('DIN Condensed', 12, "bold")

# Button styles

"""
BUTTON_STYLES = {
    'bg': 'light blue',
    'fg': 'black',  # Sets the button text color
    'width': 15,
    'relief': 'solid',
    'bd': 1,
    'highlightbackground': 'light blue',
    'highlightthickness': 10,
    'font': 'Helvetica 12 bold'
}
"""

# Label styles
LABEL_STYLES = {
    'bg': BACKGROUND_COLOR,
    'fg': TEXT_COLOR,
    'font': FONT_LARGE
}

# Padding styles
PAD_Y = (10, 10)
PAD_X = (10, 10)