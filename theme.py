# theme.py

# Liste der Themes
themes = [
    {"name": "Standard", "bg": "white", "fg": "black", "button_bg": "lightgrey", "button_fg": "black", "entry_bg": "white", "entry_fg": "black"},
    {"name": "Dunkel", "bg": "#2E2E2E", "fg": "white", "button_bg": "#555555", "button_fg": "white", "entry_bg": "#3C3C3C", "entry_fg": "white"},
    {"name": "Pastell", "bg": "#FFF0F5", "fg": "#333333", "button_bg": "#FFD1DC", "button_fg": "#333333", "entry_bg": "#FFE4E1", "entry_fg": "#333333"},
    {"name": "Blau", "bg": "#E6F0FA", "fg": "#002F6C", "button_bg": "#A9CCE3", "button_fg": "#002F6C", "entry_bg": "#D6EAF8", "entry_fg": "#002F6C"},
    {"name": "Grün", "bg": "#E8F5E9", "fg": "#1B5E20", "button_bg": "#A5D6A7", "button_fg": "#1B5E20", "entry_bg": "#C8E6C9", "entry_fg": "#1B5E20"},
]

# Speichert aktuellen Theme-Index
current_theme = {"index": 0}

def get_current_theme():
    """Gibt das aktuelle Theme zurück"""
    return themes[current_theme["index"]]

def next_theme():
    """Wechselt zum nächsten Theme und gibt es zurück"""
    current_theme["index"] = (current_theme["index"] + 1) % len(themes)
    return get_current_theme()
