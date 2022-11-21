from stage_left import parse_text
from stage_left.types import State


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
                out.append("- [ ] " + item.description)
            if item.state == State.CHECKED:
                out.append("- [x] " + item.description)
            if item.state == State.OBSOLETE:
                out.append("- [x] ~" + item.description + "~")
        out.append("")
    return "\n".join(out)
