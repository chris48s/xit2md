from xit2md import xit2md_text

input_ = """[ ] Open
[x] Checked
[@] Ongoing
[~] Obsolete

Named Group
[ ] This #item #has=tags
[ ] This is a longer
    description text
    split over
    multiple lines
[ ] Do this soon -> 2022-01-31
[ ] !! This is important
[ ] ! All #the=things -> 2022-12
[~] ! Obsolete, important,
    multi-line

[ ] Item 1
[ ] Item 2
"""

expected = """[//]: # (unnamed group)
- [ ] Open
- [x] Checked
- [ ] Ongoing
- [x] ~Obsolete~

# Named Group
- [ ] This #item #has=tags
- [ ] This is a longer
      description text
      split over
      multiple lines
- [ ] Do this soon -> 2022-01-31
- [ ] **!! This is important**
- [ ] **! All #the=things -> 2022-12**
- [x] ~**! Obsolete, important,
      multi-line**~

[//]: # (unnamed group)
- [ ] Item 1
- [ ] Item 2
"""


def test_all():
    assert xit2md_text(input_) == expected


def test_heading_level():
    assert "\nNamed Group\n" in xit2md_text(input_, heading_level=0)
    assert "\n### Named Group\n" in xit2md_text(input_, heading_level=3)
    assert "\n###### Named Group\n" in xit2md_text(input_, heading_level=42)
