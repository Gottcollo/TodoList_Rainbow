themes = [
    {
        "name": "Standard",
        "bg": "white",
        "fg": "black",
        "button_bg": "lightgrey",
        "button_fg": "black",
        "entry_bg": "white",
        "entry_fg": "black"
    },
    {
        "name": "Dunkel",
        "bg": "#2E2E2E",
        "fg": "white",
        "button_bg": "#555555",
        "button_fg": "white",
        "entry_bg": "#3C3C3C",
        "entry_fg": "white"
    },
    # weitere Themes 
]

current_theme = {"index": 0}

def get_current_theme():
    return themes[current_theme["index"]]

def next_theme():
    current_theme["index"] = (current_theme["index"] + 1) % len(themes)
    return get_current_theme()

def prev_theme():
    current_theme["index"] = (current_theme["index"] - 1) % len(themes)
    return get_current_theme()


# Neue Hilfsfunktion für Kontrast

def get_contrast_color(bg_color):
    """
    bg_color als Hex-String, gibt 'black' oder 'white' zurück
    abhängig von Helligkeit des Hintergrunds
    """
    bg_color = bg_color.lstrip('#')
    r = int(bg_color[0:2], 16)
    g = int(bg_color[2:4], 16)
    b = int(bg_color[4:6], 16)
    brightness = (r*299 + g*587 + b*114) / 1000
    return "black" if brightness > 128 else "white"
