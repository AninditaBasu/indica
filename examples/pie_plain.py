import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from itertools import cycle, islice

# =========================
# STYLE
# =========================
TITLE_FONT = "DejaVu Serif"
BODY_FONT = "DejaVu Sans"
TITLE_COLOUR = "#3E4A89"
BG_COLOUR = "#F7F2E8"
FRAME_COLOUR = "#6B4423"
colour_palette = [
    "#5B6C8F", "#C28F5C", "#8A9A5B", "#6B8E8E", "#C06C84",
    "#A67B5B", "#7D8F69", "#D4A373", "#7B5E7B", "#8D99AE",
    "#BC8F8F", "#9C6644", "#B5A642", "#52796F", "#C97C5D",
    "#7F5539", "#A3B18A", "#9A8C98", "#DDB892", "#6A994E"
]

# =========================
# DATA
# =========================
data = {
    "meters": {
        "Abhisarini": 2,
        "Anushtup": 281,
        "Ashti": 6,
        "Atidhriti": 1,
        "Atyashti": 28,
        "Brihati": 91,
        "Dhriti": 4,
        "Gayatri": 469,
        "Jagati": 540,
        "Kakumanyamkushira": 1,
        "Kakup": 9,
        "Kriti": 1,
        "Nyangkusarini": 2,
        "Pankti": 108,
        "Pipilika Madhya": 1,
        "Pragath": 81,
        "Pratishtha": 1,
        "Purastajjyoti": 1,
        "Shakchari": 16,
        "Trishtup": 1230,
        "Uparishtajjyoti": 2,
        "Ushnik": 76,
        "Vardhamana": 2,
        "Virangarupa": 8,
        "Virat": 64
    }
}

labels = list(data["meters"].keys())
sizes = list(data["meters"].values())

# =========================
# GROUP SMALL VALUES
# =========================
threshold = 30
filtered_labels = []
filtered_sizes = []
other_sum = 0

for label, size in zip(labels, sizes):
    if size < threshold:
        other_sum += size
    else:
        filtered_labels.append(label)
        filtered_sizes.append(size)

if other_sum > 0:
    filtered_labels.append("Others")
    filtered_sizes.append(other_sum)

# Colours
pie_colours = list(islice(cycle(colour_palette), len(filtered_sizes)))

if filtered_labels[-1] == "Others":
    pie_colours[-1] = "#CFCFCF"

# =========================
# FIGURE
# =========================
fig = plt.figure(figsize=(12, 12), facecolor=BG_COLOUR)

# Dedicated pie axis
ax = fig.add_axes([0.08, 0.13, 0.84, 0.72])

# Title
fig.suptitle(
    "Meters in the Rig Veda",
    fontsize=18,
    fontweight="bold",
    color=TITLE_COLOUR,
    fontname=TITLE_FONT,
    x=0.5,
    y=0.93
)

# Footer
fig.text(
    0.05,
    0.045,
    "Generated from the Indica API (see https://aninditabasu.github.io/indica/)",
    ha="left",
    fontsize=13,
    fontname=BODY_FONT,
    color=TITLE_COLOUR,
    style="italic",
    fontweight="bold",
)

# =========================
# PIE CHART
# =========================
wedges, texts, autotexts = ax.pie(
    filtered_sizes,
    labels=filtered_labels,
    colors=pie_colours,
    autopct="%1.1f%%",
    startangle=140,
    radius=0.92,
    labeldistance=1.12,
    pctdistance=0.62,
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1.2
    }
)

# Typography
for text in texts:
    text.set_fontsize(14)
    text.set_fontname(BODY_FONT)

for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontname(BODY_FONT)

ax.axis("equal")

# =========================
# FRAME
# =========================
frame = Rectangle(
    (0.015, 0.015),
    0.97,
    0.97,
    transform=fig.transFigure,
    fill=False,
    linewidth=10,
    edgecolor=FRAME_COLOUR
)
fig.add_artist(frame)

# =========================
# SAVE
# =========================
plt.savefig("meters_pie.png", dpi=600, bbox_inches="tight")
#plt.show()