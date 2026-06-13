SECTION_HEADERS = [
    "Summary",
    "Skills",
    "Profiles",
    "Projects",
    "Certifications",
    "Education"
]


def extract_sections(text: str) -> dict:
    sections = {}

    section_positions = {}

    for header in SECTION_HEADERS:
        position = text.find(header)

        if position != -1:
            section_positions[header] = position

    sorted_sections = sorted(
        section_positions.items(),
        key=lambda item: item[1]
    )

    for i in range(len(sorted_sections)):
        current_header = sorted_sections[i][0]
        start_pos = sorted_sections[i][1]

        if i < len(sorted_sections) - 1:
            end_pos = sorted_sections[i + 1][1]
        else:
            end_pos = len(text)

        section_content = text[start_pos:end_pos].strip()

        sections[current_header] = section_content

    return sections