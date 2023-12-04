# themes.py

# Define each theme as a dictionary of style properties
default_theme = {
    'BACKGROUND_COLOR': '#A7BEAE',
    'SIDE_FRAME_COLOR': '#B85042',
    'BUTTON_BG_COLOR': '#E7E8D1',
    'TEXT_COLOR': '#B85042',
    'BUTTON_HIGHLIGHT_COLOR': '#B85042'
}

colorblind_friendly_theme = {
    'BACKGROUND_COLOR': '#444444',
    'SIDE_FRAME_COLOR': '#333333',
    'BUTTON_BG_COLOR': '#555555',
    'TEXT_COLOR': '#EEEEEE',
    'BUTTON_HIGHLIGHT_COLOR': '#666666'
}

black_white_grey_theme = {
    'BACKGROUND_COLOR': '#FFFFFF',
    'SIDE_FRAME_COLOR': '#EEEEEE',
    'BUTTON_BG_COLOR': '#CCCCCC',
    'TEXT_COLOR': '#000000',
    'BUTTON_HIGHLIGHT_COLOR': '#BBBBBB'
}

high_contrast_theme = {
    'BACKGROUND_COLOR': '#000000',
    'SIDE_FRAME_COLOR': '#FFD700',
    'BUTTON_BG_COLOR': '#00FF00',
    'TEXT_COLOR': '#FFFFFF',
    'BUTTON_HIGHLIGHT_COLOR': '#0000FF'
}

ocean_breeze_theme = {
    'BACKGROUND_COLOR': '#2B7A78',
    'SIDE_FRAME_COLOR': '#17252A',
    'BUTTON_BG_COLOR': '#3AAFA9',
    'TEXT_COLOR': '#DEF2F1',
    'BUTTON_HIGHLIGHT_COLOR': '#FEFFFF'
}

sunset_sorbet_theme = {
    'BACKGROUND_COLOR': '#FF5E5B',
    'SIDE_FRAME_COLOR': '#7A5C58',
    'BUTTON_BG_COLOR': '#FFAA5E',
    'TEXT_COLOR': '#D8D8D8',
    'BUTTON_HIGHLIGHT_COLOR': '#FF8C61'
}

nature_walk_theme = {
    'BACKGROUND_COLOR': '#4B7447',
    'SIDE_FRAME_COLOR': '#2C302E',
    'BUTTON_BG_COLOR': '#A2A2A1',
    'TEXT_COLOR': '#0E1111',
    'BUTTON_HIGHLIGHT_COLOR': '#5E5E5E'
}

cotton_candy_theme = {
    'BACKGROUND_COLOR': '#FFC0CB',  # A soft pink color
    'SIDE_FRAME_COLOR': '#F8B7D4',  # A lighter shade of pink
    'BUTTON_BG_COLOR': '#B5E4F9',   # A light sky blue
    'TEXT_COLOR': '#FFFFFF',        # White for text for contrast
    'BUTTON_HIGHLIGHT_COLOR': '#FFDEE9'  # A pale, almost white pink
}

# Combine all themes into a dictionary
themes = {
    'default': default_theme,
    'Colorblind Friendly': colorblind_friendly_theme,
    'Black & White': black_white_grey_theme,
    'High Contrast': high_contrast_theme,
    'Ocean Breeze': ocean_breeze_theme,
    'Sunset Sorbet': sunset_sorbet_theme,
    'Nature Walk': nature_walk_theme,
    'Cotton Candy': cotton_candy_theme
}
