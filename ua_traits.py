import random
import re
from typing import Dict

lines = open("ua_traits.md", "r").readlines()

sections = {}

section_name = None

pattern = f"\[([^\]]+)\]"

for l in lines:
    if l.startswith("$"):
        section_name = l.replace("$", "").strip()
        sections[section_name] = []

    else:
        if l.strip():
            sections[section_name].append(l.strip())

print(sections.keys())


# TODO include non-template text in the output

def render_section(sections: Dict, name: str) -> str:
    output = ""
    section_lines = sections[name]
    selected_line = random.choice(section_lines)
    matches = list(re.finditer(pattern, selected_line))
    if matches:
        for match_group in matches:
            match = selected_line[match_group.start():match_group.end()].replace("[", "").replace("]", "")

            if "-" in match:
                minimum, maximum = match.split("-")
                result = str(random.randint(int(minimum), int(maximum)))
                output += result
            else:
                result = render_section(sections, match)
                output += result

        return output
    else:
        return selected_line


output = render_section(sections, "GmC")
print(output)
