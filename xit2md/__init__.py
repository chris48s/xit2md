from stage_left import parse_text
from stage_left.types import State


def _get_description(description):
    lines = description.split("\n")
    return "\n".join([lines[0]] + [f"      {line}" for line in lines[1:]])


def _get_heading(title, heading_weight):
    if heading_weight == 0:
        return title
    return f"{'#'*heading_weight} " + title


def xit2md_text(text, heading_weight=1):
    out = []
    parsed = parse_text(text)
    for group in parsed:
        if group.title:
            if heading_weight > 6:
                out.append(_get_heading(group.title, 6))
            else:
                out.append(_get_heading(group.title, heading_weight))
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
