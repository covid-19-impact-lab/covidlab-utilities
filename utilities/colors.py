import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap


def get_colors(palette, number, as_cmap=False):
    """Return a list with hex codes representing a color palette.

    Args:
        palette (str): One of ["categorical", "ordered", "blue", "red", "yellow",
            "green", "orange", "purple"]
        number (int): Number of colors needed. Between 1 and 12.

    Returns:
        list or cmap: List of hex codes or cmap.

    """
    if as_cmap and palette in ["categorical", "ordered"]:
        raise ValueError("cmap can only be returned for monochrome palettes.")
    if palette == "categorical":
        triangle = {i + 1: CAT_LIST[: i + 1] for i in range(12)}
    elif palette == "ordered":
        triangle = ORDERED
    elif palette in ["blue", "red", "green", "yellow", "orange", "purple"]:
        triangle = _mono_list_to_triangle(MONO_COLORS[palette])
    else:
        raise NotImplementedError(f"{palette} is not implemented.")

    res = triangle[number]
    if as_cmap:
        res = LinearSegmentedColormap.from_list(palette, res)
    return res


def plot_colors(palette, number, size=1):
    """Plot a color palette.

    Args:
        palette (str): One of ["categorical", "ordered", "blue", "red", "yellow",
            "green", "orange", "purple"]
        number (int): Between 1 and 12.
        size (float): Scaling factor for the plot size.

    """
    return sns.palplot(get_colors(palette, number), size=size)


def _mono_list_to_triangle(mono_list):
    indices_to_delete = [5, 6, 3, 8, 0, 11, 2, 9, 4, 7, 10]
    arr = np.array(mono_list)
    triangle = {}
    for i in range(12):
        subset = np.delete(arr.copy(), indices_to_delete[:i]).tolist()
        triangle[len(subset)] = subset
    return triangle


# =====================================================================================
# Hex codes for the basic color palettes
# =====================================================================================

CAT_LIST = [
    "#547482",
    "#C87259",
    "#C2D8C2",
    "#F1B05D",
    "#818662",
    "#6C4A4D",
    "#7A8C87",
    "#EE8445",
    "#C8B05C",
    "#3C2030",
    "#C89D64",
    "#2A3B49",
]

ORDERED = {
    1: ["#547482"],
    2: ["#547482", "#c87259"],
    3: ["#547482", "#F1B05D", "#c87259"],
    4: ["#547482", "#7A8C87", "#F1B05D", "#c87259"],
    5: ["#547482", "#7A8C87", "#C2D8C2", "#F1B05D", "#c87259"],
    6: ["#547482", "#7A8C87", "#C2D8C2", "#F1B05D", "#EE8445", "#c87259"],
    7: ["#547482", "#7A8C87", "#C2D8C2", "#C8B05C", "#F1B05D", "#EE8445", "#c87259"],
    8: [
        "#547482",
        "#7A8C87",
        "#C2D8C2",
        "#C8B05C",
        "#C89D64",
        "#F1B05D",
        "#EE8445",
        "#c87259",
    ],
    9: [
        "#547482",
        "#7A8C87",
        "#C2D8C2",
        "#818662",
        "#C8B05C",
        "#C89D64",
        "#F1B05D",
        "#EE8445",
        "#c87259",
    ],
    10: [
        "#547482",
        "#7A8C87",
        "#C2D8C2",
        "#818662",
        "#C8B05C",
        "#C89D64",
        "#F1B05D",
        "#EE8445",
        "#c87259",
        "#6c4a4d",
    ],
    11: [
        "#2A3B49",
        "#547482",
        "#7A8C87",
        "#C2D8C2",
        "#818662",
        "#C8B05C",
        "#C89D64",
        "#F1B05D",
        "#EE8445",
        "#c87259",
        "#6c4a4d",
    ],
    12: [
        "#2A3B49",
        "#547482",
        "#7A8C87",
        "#C2D8C2",
        "#818662",
        "#C8B05C",
        "#C89D64",
        "#F1B05D",
        "#EE8445",
        "#c87259",
        "#6c4a4d",
        "#3C2030",
    ],
}

MONO_COLORS = {
    "blue": [
        "#547482",
        "#5c7f8e",
        "#63899a",
        "#6f92a2",
        "#7b9baa",
        "#87a4b1",
        "#93adb9",
        "#9fb6c1",
        "#abbfc8",
        "#b6c8d0",
        "#c2d1d8",
        "#cedae0",
    ],
    "red": [
        "#a04d35",
        "#b3563b",
        "#c26246",
        "#c87259",
        "#ce826c",
        "#d5937f",
        "#dba392",
        "#e0b1a3",
        "#e5bdb1",
        "#eacac0",
        "#efd6cf",
        "#f4e3de",
    ],
    "yellow": [
        "#d98213",
        "#eb8d15",
        "#ec9627",
        "#efa74b",
        "#f1b05d",
        "#f3b96f",
        "#f4c281",
        "#f6ca93",
        "#f7d3a5",
        "#f9dcb7",
        "#fae5c9",
        "#fceedb",
    ],
    "green": [
        "#606449",
        "#6b6f51",
        "#767b5a",
        "#818662",
        "#8c916a",
        "#959a75",
        "#9ea280",
        "#a6ab8c",
        "#afb397",
        "#b8bba2",
        "#c1c4ae",
        "#c9ccb9",
    ],
    "orange": [
        "#d35b13",
        "#ea6516",
        "#ec752e",
        "#ee8445",
        "#f0935c",
        "#f2a374",
        "#f4b28b",
        "#f6bf9f",
        "#f8cbb1",
        "#f9d7c3",
        "#fbe3d5",
        "#fdefe7",
    ],
    "purple": [
        "#4e3537",
        "#5d4042",
        "#6c4a4d",
        "#7b5458",
        "#8a5f63",
        "#996a6e",
        "#a2777a",
        "#a98286",
        "#b18e91",
        "#b9999c",
        "#c1a5a8",
        "#c9b1b3",
    ],
}
