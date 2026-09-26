"""
================================================================================
 ISTRORIGAN HOUDINI PROCEDURAL PIPELINE - COMMON HELPERS & TEMPLATES
================================================================================
 Provides studio-standard node creation, parameter templating, and VEX helpers.
 Modeled after the production HDA builder architecture.
================================================================================
"""

import sys
import os

try:
    import hou  # type: ignore
    HOUDINI_AVAILABLE = True
except ImportError:
    HOUDINI_AVAILABLE = False

# region CONSTANTS & VEX LOADER
COL_W = 2.4
ROW_H = 1.7


def load_vex(filename):
    """
    Load pure VEX code from the adjacent vex/ directory.
    Provides clean separation between Python node orchestration and VEX math.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    vex_path = os.path.join(base_dir, "vex", filename)
    if not os.path.exists(vex_path):
        vex_path = filename
    with open(vex_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def get_hou():
    if not HOUDINI_AVAILABLE:
        print("[!] Error: 'hou' module is only available inside Houdini or hython.")
        sys.exit(0)
    return hou
# endregion


# region HOUDINI NODE BUILDERS & WRANGLERS
def mk(parent, node_type, name, col, row, comment=""):
    """Create a node at (col, row) on the grid with fallback for versioned types."""
    try:
        n = parent.createNode(node_type, name)
    except Exception:
        n = parent.createNode(node_type.split("::")[0], name)
    n.setPosition(hou.Vector2(col * COL_W, -row * ROW_H))
    if comment:
        n.setComment(comment)
        n.setGenericFlag(hou.nodeFlag.DisplayComment, True)
    return n


def setp(node, name, value):
    """Set parameter value safely."""
    p = node.parm(name)
    if p is not None:
        try:
            p.set(value)
        except Exception:
            pass


def sete(node, name, expr):
    """Set parameter expression safely."""
    p = node.parm(name)
    if p is not None:
        try:
            p.setExpression(expr)
        except Exception:
            pass


def wr(parent, name, cls, code, col, row, *inputs, comment="", cref="../"):
    """
    Create an attribwrangle node with class (0=detail, 1=prim, 2=point, 3=vertex)
    and replace macro %C% with cref (e.g. "../" or custom).
    """
    n = mk(parent, "attribwrangle", name, col, row, comment)
    setp(n, "class", cls)
    setp(n, "snippet", code.replace("%C%", cref))
    for i, s in enumerate(inputs):
        if s is not None:
            n.setInput(i, s)
    return n


def netbox(parent, name, label, color, nodes):
    """Create a colored Network Box grouping nodes and auto-fitting contents."""
    b = parent.createNetworkBox(name)
    b.setComment(label)
    b.setColor(hou.Color(color))
    for n in nodes:
        if n is not None:
            b.addNode(n)
    try:
        b.fitAroundContents()
    except Exception:
        pass
    return b


def stickynote(parent, name, text, col, row, width=4.5, height=2.8, color=(0.14, 0.18, 0.24), text_color=(0.90, 0.95, 1.0)):
    """
    Creates a styled Sticky Note in the Houdini network view for architectural documentation,
    specifications, and technical annotations.
    """
    try:
        note = parent.createStickyNote(name)
        note.setPosition(hou.Vector2(col * COL_W, -row * ROW_H))
        note.setSize(hou.Vector2(width, height))
        note.setText(text)
        note.setColor(hou.Color(color))
        if hasattr(note, "setTextColor"):
            note.setTextColor(hou.Color(text_color))
        return note
    except Exception:
        return None
# endregion


# region PARAMETER TEMPLATE BUILDERS
def F(n, l, d, lo, hi, dw=None, hidden=False, strict=False):
    kw = dict(default_value=(d,), min=lo, max=hi,
              min_is_strict=strict, max_is_strict=strict)
    if dw:
        kw["disable_when"] = dw
    if hidden:
        kw["is_hidden"] = True
    return hou.FloatParmTemplate(n, l, 1, **kw)


def I(n, l, d, lo, hi, dw=None, strict=False):
    kw = dict(default_value=(d,), min=lo, max=hi,
              min_is_strict=strict, max_is_strict=strict)
    if dw:
        kw["disable_when"] = dw
    return hou.IntParmTemplate(n, l, 1, **kw)


def B(n, l, d, dw=None):
    kw = dict(default_value=bool(d))
    if dw:
        kw["disable_when"] = dw
    return hou.ToggleParmTemplate(n, l, **kw)


def COL(n, l, rgb):
    kw = dict(default_value=rgb)
    look = getattr(hou, "parmLook", None)
    if look is not None:
        kw["look"] = look.ColorSquare
    scheme = None
    for a in ("parmNamingScheme", "parmNaming"):
        s = getattr(hou, a, None)
        if s is not None:
            scheme = s.RGBA
            break
    for key in ("naming_scheme", "naming"):
        if scheme is None:
            break
        try:
            return hou.FloatParmTemplate(n, l, 3, **dict(kw, **{key: scheme}))
        except TypeError:
            pass
    t = hou.FloatParmTemplate(n, l, 3, **kw)
    try:
        t.setNamingScheme(scheme)
    except Exception:
        pass
    return t


def SEP(n):
    return hou.SeparatorParmTemplate(n)


def STR(n, l, d=""):
    return hou.StringParmTemplate(n, l, 1, default_value=(d,))


def MENU(n, l, items, labels, d=0):
    return hou.MenuParmTemplate(n, l, tuple(items), menu_labels=tuple(labels), default_value=d)


def SIMPLE(name, label, items):
    f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Simple)
    for it in items:
        f.addParmTemplate(it)
    return f


def MULTI(name, label, items, default_count=0):
    """Multiparm block: instance parm names must contain '#' (1-based index)."""
    f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.MultiparmBlock)
    for it in items:
        f.addParmTemplate(it)
    try:
        f.setDefaultValue(default_count)
    except Exception:
        pass
    return f


def TAB(name, label, items):
    f = hou.FolderParmTemplate(name, label, folder_type=hou.folderType.Tabs)
    for it in items:
        f.addParmTemplate(it)
    return f
# endregion


# region STANDALONE TEST HELPERS
def create_standalone_geo(geo_name="test_part"):
    """Helper for standalone testing: cleans old node and creates geo container."""
    hou = get_hou()
    obj = hou.node("/obj")
    old = obj.node(geo_name)
    if old:
        old.destroy()
    geo = obj.createNode("geo", geo_name)
    geo.setColor(hou.Color((0.15, 0.65, 0.90)))
    return geo
# endregion

