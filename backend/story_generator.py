def generate_story(
    prompt,
    character,
    setting,
    tone,
    art_style
):

    panels = [
        {
            "panel": 1,
            "scene": f"{character} starts an exciting journey in {setting}.",
            "dialogue": f"{character}: Today is going to be an amazing day!",
            "style": art_style
        },
        {
            "panel": 2,
            "scene": f"{character} discovers something mysterious related to {prompt}.",
            "dialogue": f"{character}: What is happening here?",
            "style": art_style
        },
        {
            "panel": 3,
            "scene": f"The adventure becomes more exciting in {setting}.",
            "dialogue": f"{character}: I need to find the answer!",
            "style": art_style
        },
        {
            "panel": 4,
            "scene": f"{character} faces a difficult challenge.",
            "dialogue": f"{character}: I will never give up!",
            "style": art_style
        },
        {
            "panel": 5,
            "scene": f"{character} solves the problem and completes the adventure.",
            "dialogue": f"{character}: What an incredible adventure!",
            "style": art_style
        }
    ]

    return {
        "title": f"The Adventure of {character}",
        "tone": tone,
        "panels": panels
    }
