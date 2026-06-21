import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from collections import defaultdict

# =========================
# DATA
# =========================
mandals = [
    {"mandal":1,"sungfor":{"Aditi":7,"Aditya":4,"Agastya Maitravaruni":2,"Agnayi":1,"Agni":83,"Ahirbudhnya":1,..."Vishnu":7,"Vishwadeva":6,"Winds":1}},
    {"mandal":2,"sungfor":{"Aditi":2,"Aditya":3,"Agni":15,..."Usha":1,"Vanaspati":1,"Varun":5,"Varunani":1,"Vasu":1,"Vayu":1,"Vishwadeva":1}}
    # Add mandals 3–10 here
]

# =========================
# SETTINGS
# =========================
TOP_N = 18
MIN_PERCENT = 1.0
SECOND_LEVEL_MIN_COUNT = 27
THIRD_LEVEL_MIN_COUNT = 9
TITLE_FONT = "DejaVu Serif"
BODY_FONT = "Calibri"
TITLE_COLOUR = "#3E4A89"
colour_palette = [
    "#5B6C8F",  # slate blue
    "#C28F5C",  # warm ochre
    "#8A9A5B",  # olive green
    "#6B8E8E",  # muted teal
    "#C06C84",  # rose dust
    "#A67B5B",  # burnt sienna
    "#7D8F69",  # moss green
    "#D4A373",  # sandstone
    "#7B5E7B",  # muted plum
    "#8D99AE",  # silver blue
    "#BC8F8F",  # rosy brown
    "#9C6644",  # chestnut
    "#B5A642",  # antique gold
    "#52796F",  # sea pine
    "#C97C5D",  # terracotta
    "#7F5539",  # walnut
    "#A3B18A",  # sage
    "#9A8C98",  # faded lavender
    "#DDB892",  # parchment tan
    "#6A994E"   # softened leaf green
]

# =========================
# AGGREGATE COUNTS
# =========================
total_counts = defaultdict(int)

for mandal in mandals:
    for deity, count in mandal["sungfor"].items():
        total_counts[deity] += count

sorted_counts = sorted(
    total_counts.items(),
    key=lambda x: x[1],
    reverse=True
)

grand_total = sum(v for _, v in sorted_counts)

# =========================
# FIGURE 1
# =========================
main_labels = []
main_sizes = []
others_labels = []
others_sizes = []

for i, (label, count) in enumerate(sorted_counts):
    pct = count / grand_total * 100

    if i < TOP_N and pct >= MIN_PERCENT:
        main_labels.append(label)
        main_sizes.append(count)
    else:
        others_labels.append(label)
        others_sizes.append(count)

others_total = sum(others_sizes)

main_labels.append("Others")
main_sizes.append(others_total)

# =========================
# FIGURE 2a
# =========================
others_pie_labels = []
others_pie_sizes = []
others2_labels = []
others2_sizes = []

for label, count in zip(others_labels, others_sizes):
    if count >= SECOND_LEVEL_MIN_COUNT:
        others_pie_labels.append(label)
        others_pie_sizes.append(count)
    else:
        others2_labels.append(label)
        others2_sizes.append(count)

others2_total = sum(others2_sizes)

if others2_total > 0:
    others_pie_labels.append("Others2")
    others_pie_sizes.append(others2_total)

# =========================
# FIGURE 2b
# =========================
third_labels = []
third_sizes = []
others3_labels = []
others3_sizes = []

for label, count in zip(others2_labels, others2_sizes):
    if count >= THIRD_LEVEL_MIN_COUNT:
        third_labels.append(label)
        third_sizes.append(count)
    else:
        others3_labels.append(label)
        others3_sizes.append(count)

others3_total = sum(others3_sizes)

if others3_total > 0:
    third_labels.append("Others3")
    third_sizes.append(others3_total)

# =========================
# FIGURE LAYOUT
# =========================
fig = plt.figure(
    figsize=(24, 15),
    constrained_layout=True
)

gs = fig.add_gridspec(
    2, 3,
    width_ratios=[1.55, 1.1, 1.1],
    height_ratios=[1, 1],
    wspace=0.55,
    hspace=0.08,
    top=0.84,
    bottom=0.08
)

# Main title (right aligned)
fig.suptitle(
    "Gods in the Rig Veda",
    fontsize=28,
    fontweight="bold",
    color=TITLE_COLOUR,
    fontname=TITLE_FONT,
    x=0.15,     # left margin, horizontal placement
    ha="left",  # align left
    y=0.93      # top margin, vertical placement
)

# Footer
fig.text(
    0.05,  # left margin, horizontal placement
    0.05,  # bottom margin, vertical placement
    "Generated from the Indica API (see https://aninditabasu.github.io/indica/)",
    ha="left",
    fontsize=18,
    fontname=BODY_FONT,
    color=TITLE_COLOUR,
    style="italic",
    fontweight="bold"
)

# =========================
# FIGURE 1 PIE
# =========================
ax1 = fig.add_subplot(gs[:, 0])

wedges1, _ = ax1.pie(
    main_sizes,
    colors=[colour_palette[i % len(colour_palette)] for i in range(len(main_sizes))],
    startangle=140,
    wedgeprops=dict(edgecolor="white")
)

ax1.set_facecolor("#F8F4EC")

ax1.set_title(
    "Figure 1\n\nTop 18 gods + Others",
    fontsize=16,
    fontweight="bold",
    fontname=TITLE_FONT,
    color=TITLE_COLOUR,
    pad=30
)

for i, wedge in enumerate(wedges1):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))

    pct = main_sizes[i] / grand_total * 100

    if pct > 4:
        ax1.text(
            x * 0.6,
            y * 0.6,
            main_labels[i],
            ha="center",
            va="center",
            fontsize=12,
            fontname=BODY_FONT
        )
    else:
        ax1.annotate(
            main_labels[i],
            xy=(x * 0.95, y * 0.95),
            xytext=(x * 1.28, y * 1.28),
            arrowprops=dict(arrowstyle="-"),
            fontsize=12,
            fontname=BODY_FONT
        )

legend1 = [
    f"{l} {s} ({s/grand_total*100:.1f}%)"
    for l, s in zip(main_labels, main_sizes)
]

ax1.legend(
    wedges1,
    legend1,
    loc="center left",
    bbox_to_anchor=(1.20, 0.5),
    prop={"family": BODY_FONT, "size": 12, },
    borderpad=1.2,
    labelspacing=1.0,
    handletextpad=0.8
)

# =========================
# FIGURE 2a PIE
# =========================
ax2 = fig.add_subplot(gs[0, 1:])

pos = ax2.get_position()
ax2.set_position([
    pos.x0 - 0.02,
    pos.y0 + 0.02,
    pos.width,
    pos.height
])

wedges2, _ = ax2.pie(
    others_pie_sizes,
    colors=[colour_palette[i % len(colour_palette)] for i in range(len(others_pie_sizes))],
    startangle=90,
    wedgeprops=dict(edgecolor="white")
)

ax2.set_facecolor("#F8F4EC")

ax2.set_title(
    "Figure 2a\n\nGods with ≥ 27 hymns (from Others)",
    fontsize=16,
    fontweight="bold",
    fontname=TITLE_FONT,
    color=TITLE_COLOUR,
    pad=30
)

for i, wedge in enumerate(wedges2):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))

    if others_pie_labels[i] == "Others2":
        ax2.text(
            x * 0.65,
            y * 0.65,
            "Others2",
            ha="center",
            va="center",
            fontsize=12,
            fontname=BODY_FONT
        )
    else:
        ax2.annotate(
            others_pie_labels[i],
            xy=(x * 0.88, y * 0.88),
            xytext=(x * 1.28, y * 1.28),
            arrowprops=dict(arrowstyle="-"),
            fontsize=12,
            fontname=BODY_FONT
        )

legend2 = [
    f"{l} {s}"
    for l, s in zip(others_pie_labels, others_pie_sizes)
]

ax2.legend(
    wedges2,
    legend2,
    loc="center left",
    bbox_to_anchor=(1.05, 0.5),
    prop={"family": BODY_FONT, "size": 12},
    borderpad=1.2,
    labelspacing=1.0,
    handletextpad=0.8
)

# =========================
# FIGURE 2b PIE
# =========================
ax3 = fig.add_subplot(gs[1, 1:])
pos = ax3.get_position()
ax3.set_position([
    pos.x0 - 0.01,   # move left
    pos.y0,          # keep vertical position
    pos.width,
    pos.height
])

wedges3, _ = ax3.pie(
    third_sizes,
    colors=[colour_palette[(i + 7) % len(colour_palette)] for i in range(len(third_sizes))],
    startangle=90,
    wedgeprops=dict(edgecolor="white")
)

ax3.set_facecolor("#F8F4EC")

ax3.set_title(
    "Figure 2b\n\nGods with ≥ 9 hymns (from Others2)",
    fontsize=16,
    fontweight="bold",
    fontname=TITLE_FONT,
    color=TITLE_COLOUR,
    pad=30
)

for i, wedge in enumerate(wedges3):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))

    if third_labels[i] == "Others3":
        ax3.text(
            x * 0.65,
            y * 0.65,
            "Others3",
            ha="center",
            va="center",
            fontsize=12,
            fontname=BODY_FONT
        )
    else:
        ax3.annotate(
            third_labels[i],
            xy=(x * 0.88, y * 0.88),
            xytext=(x * 1.25, y * 1.25),
            arrowprops=dict(arrowstyle="-"),
            fontsize=12,
            fontname=BODY_FONT
        )

legend3 = [
    f"{l} {s}"
    for l, s in zip(third_labels, third_sizes)
]

ax3.legend(
    wedges3,
    legend3,
    loc="center left",
    bbox_to_anchor=(0.95, 0.5),
    prop={"family": BODY_FONT, "size": 12},
    borderpad=1.2,
    labelspacing=1.0,
    handletextpad=0.8
)

# =========================
# FRAME
# =========================

frame = Rectangle(
    (0.005, 0.005),
    0.99,
    0.99,
    transform=fig.transFigure,
    fill=False,
    linewidth=20,
    edgecolor="#6B4423",
    joinstyle="round"
)
fig.add_artist(frame)

fig.patch.set_facecolor("#F8F4EC")

# =========================
# SAVE
# =========================
plt.savefig(
    "gods_3step_cascade_2.png",
    dpi=600
)
