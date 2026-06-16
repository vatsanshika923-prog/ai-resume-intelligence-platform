def load_skills(file_path: str) -> dict:
    """
    Load skills taxonomy from file.

    Args:
        file_path (str): Path to skills file.

    Returns:
        dict: Categorized skills.
    """

    skills = {}

    current_category = None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("[") and line.endswith("]"):
                current_category = line[1:-1]
                skills[current_category] = []

            else:
                skills[current_category].append(line)

    return skills