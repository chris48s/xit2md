from stage_left import parse_text
from stage_left.types import State


def _get_description(item):
    lines = item.description.split("\n")
    description = "\n".join([lines[0]] + [f"      {line}" for line in lines[1:]])
    if item.priority > 0:
        description = f"**{description}**"
    return description


def _get_heading(title, heading_level):
    if heading_level == 0:
        return title
    return f"{'#'*heading_level} " + title


def xit2md_text(text, heading_level=1):
    """Convert a [x]it string to a markdown task list
    https://www.markdownguide.org/extended-syntax/#task-lists

    Args:
        text (str): String containing a todo list in [x]it format
        heading_level (int): A number 0 to 6.
            Group titles will be represented using this heading level
            https://www.markdownguide.org/basic-syntax/#headings
            Default: ``1``

    Returns:
        str
    """
    out = []
    parsed = parse_text(text)
    for group in parsed:
        if group.title:
            if heading_level > 6:
                out.append(_get_heading(group.title, 6))
            else:
                out.append(_get_heading(group.title, heading_level))
        else:
            # https://www.markdownguide.org/hacks/#comments
            out.append("[//]: # (unnamed group)")

        for item in group.items:
            if item.state in [State.OPEN, State.ONGOING]:
                out.append("- [ ] " + _get_description(item))
            if item.state == State.CHECKED:
                out.append("- [x] " + _get_description(item))
            if item.state == State.OBSOLETE:
                out.append("- [x] ~" + _get_description(item) + "~")
        out.append("")
    return "\n".join(out)
