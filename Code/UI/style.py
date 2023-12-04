import themes

# Current theme
current_theme = 'default'

# Define styles
LABEL_STYLES = {}
BUTTON_STYLES = {}
ENTRY_STYLES = {}
FRAME_STYLES = {}
TEXT_STYLES = {}
CHECKBUTTON_STYLES = {}
RADIOBUTTON_STYLES = {}
LISTBOX_STYLES = {}
SCROLLBAR_STYLES = {}
PAD_Y = (10, 10)
PAD_X = (10, 10)
BACKGROUND_COLOR = ''
SIDE_FRAME_COLOR = ''

def update_styles():
    global LABEL_STYLES, BUTTON_STYLES, ENTRY_STYLES, FRAME_STYLES, TEXT_STYLES, CHECKBUTTON_STYLES, RADIOBUTTON_STYLES, LISTBOX_STYLES, SCROLLBAR_STYLES, BACKGROUND_COLOR, SIDE_FRAME_COLOR

    # Ensure the current theme is available in the themes dictionary
    if current_theme not in themes.themes:
        print(f"Theme '{current_theme}' not found. Using default theme.")
        theme = themes.themes['default']
    else:
        theme = themes.themes[current_theme]

    # Update each style category with the corresponding theme properties
     # Update the background colors
    BACKGROUND_COLOR = theme['BACKGROUND_COLOR']
    SIDE_FRAME_COLOR = theme['SIDE_FRAME_COLOR']

    LABEL_STYLES = {
        'bg': theme['BACKGROUND_COLOR'],
        'fg': theme['TEXT_COLOR'],
        'font': 'Helvetica 16 bold'
    }

    BUTTON_STYLES = {
        'bg': theme['BUTTON_BG_COLOR'],
        'fg': theme['TEXT_COLOR'],
        'activebackground': theme['BUTTON_HIGHLIGHT_COLOR'],
        'width': 15,
        'relief': 'flat',
        'bd': 1,
        'highlightbackground': theme['BUTTON_HIGHLIGHT_COLOR'],
        'highlightthickness': 10,
        'font': 'Helvetica 12 bold'
    }

    ENTRY_STYLES = {
        'bg': theme['BACKGROUND_COLOR'],
        'fg': theme['TEXT_COLOR'],
        'insertbackground': theme['TEXT_COLOR'],
        'font': 'Helvetica 12'
    }

    FRAME_STYLES = {
        'bg': theme['SIDE_FRAME_COLOR']
    }

    TEXT_STYLES = {
        'bg': theme['BACKGROUND_COLOR'],
        'fg': theme['TEXT_COLOR'],
        'font': 'Helvetica 12'
    }


# Initialize styles with the default theme
update_styles()