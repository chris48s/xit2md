from stage_left import parse_text
from stage_left.types import State


def _get_description(description):
    lines = description.split("\n")
    return "\n".join([lines[0]] + [f"      {line}" for line in lines[1:]])


def xit2md_text(text):
    out = []
    parsed = parse_text(text)
    for group in parsed:
        if group.title:
            out.append("# " + group.title)
        else:
            out.append("[//]: # (unnamed group)")
        for item in group.items:
            if item.state in [State.OPEN, State.ONGOING]:
                out.append("- [ ] " + _get_description(item.description))
            if item.state == State.CHECKED:
                out.append("- [x] " + _get_description(item.description))
            if item.state == State.OBSOLETE:
                out.append("- [x] ~" + _get_description(item.description) + "~")
        out.append("")
    return "\n".join(out)
