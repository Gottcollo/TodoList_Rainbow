# theme.py
themes = [
    {
        "name": "Standard",
        "bg": "white",
        "fg": "black",
        "button_bg": "lightgrey",
        "button_fg": "black",
        "entry_bg": "white",
        "entry_fg": "black",
        "task_colors": ["black"]  # alle Aufgaben schwarz
    },
    {
        "name": "Dunkel",
        "bg": "#2E2E2E",
        "fg": "white",
        "button_bg": "#555555",
        "button_fg": "white",
        "entry_bg": "#3C3C3C",
        "entry_fg": "white",
        "task_colors": ["#FFD700", "#ADFF2F", "#00FFFF", "#FF69B4", "#FFA500"]
    },
    {
        "name": "Pastell",
        "bg": "#FFF0F5",
        "fg": "#333333",
        "button_bg": "#FFD1DC",
        "button_fg": "#333333",
        "entry_bg": "#FFE4E1",
        "entry_fg": "#333333",
        "task_colors": ["#FFB6C1", "#E6E6FA", "#F0E68C", "#98FB98", "#AFEEEE"]
    },
    {
        "name": "Blau",
        "bg": "#E6F0FA",
        "fg": "#002F6C",
        "button_bg": "#A9CCE3",
        "button_fg": "#002F6C",
        "entry_bg": "#D6EAF8",
        "entry_fg": "#002F6C",
        "task_colors": ["#003366", "#336699", "#6699CC", "#99CCFF", "#CCE5FF"]
    },
    {
        "name": "Grün",
        "bg": "#E8F5E9",
        "fg": "#1B5E20",
        "button_bg": "#A5D6A7",
        "button_fg": "#1B5E20",
        "entry_bg": "#C8E6C9",
        "entry_fg": "#1B5E20",
        "task_colors": ["#1B5E20", "#2E7D32", "#4CAF50", "#66BB6A", "#81C784"]
    },
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
