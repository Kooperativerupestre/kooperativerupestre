import json
import os
import urllib.request
from collections import defaultdict
from pathlib import Path

USERNAME = os.environ["GITHUB_USERNAME"]
TOKEN = os.environ["GITHUB_TOKEN"]

OUTPUT = Path("assets/languages.svg")

BACKGROUND = "#2b2b2b"
TEXT = "#E8E8E8"
MUTED = "#8E8E93"

COLORS = [
    "#8B3A4A",
    "#74458A",
    "#6D0E0E",
    "#5A1A5A",
    "#3D0E5C",
    "#A44A5A",
    "#9257A6",
    "#C16A7A",
]


def github_get(url):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USERNAME,
        },
    )

    with urllib.request.urlopen(request) as response:
        return json.load(response)


def get_repositories():
    repositories = []
    page = 1

    while True:
        url = (
            f"https://api.github.com/users/{USERNAME}/repos"
            f"?per_page=100&page={page}&type=owner"
        )

        batch = github_get(url)

        if not batch:
            break

        repositories.extend(batch)

        if len(batch) < 100:
            break

        page += 1

    return repositories


def get_languages(repository):
    return github_get(repository["languages_url"])


def collect_languages():
    totals = defaultdict(int)

    for repository in get_repositories():
        if repository["fork"]:
            continue

        print(f"Reading {repository['full_name']}")

        for language, bytes_count in get_languages(repository).items():
            totals[language] += bytes_count

    return totals


def polar_to_cartesian(cx, cy, radius, angle):
    import math

    angle -= 90

    radians = math.radians(angle)

    return (
        cx + radius * math.cos(radians),
        cy + radius * math.sin(radians),
    )


def pie_slice(cx, cy, radius, start_angle, end_angle):

    x1, y1 = polar_to_cartesian(cx, cy, radius, end_angle)
    x2, y2 = polar_to_cartesian(cx, cy, radius, start_angle)

    large_arc = 1 if end_angle - start_angle > 180 else 0

    return (
        f"M {cx} {cy} "
        f"L {x1:.2f} {y1:.2f} "
        f"A {radius} {radius} 0 {large_arc} 0 {x2:.2f} {y2:.2f} "
        "Z"
    )


def escape_xml(value):
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def generate_svg(totals):

    total = sum(totals.values())

    if total == 0:
        raise RuntimeError("No language data was found.")

    sorted_languages = sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    # Keep the chart readable by grouping tiny languages.
    visible = []
    other = 0

    for language, value in sorted_languages:
        percentage = value / total * 100

        if percentage < 2:
            other += value
        else:
            visible.append((language, value))

    if other:
        visible.append(("Other", other))

    width = 760
    height = 420

    cx = 210
    cy = 210
    radius = 145

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" rx="18" fill="{BACKGROUND}"/>',
        (
            f'<text x="380" y="42" text-anchor="middle" '
            f'fill="{TEXT}" font-family="sans-serif" '
            f'font-size="22" font-weight="600">'
            "Language Distribution"
            "</text>"
        ),
    ]

    current_angle = 0

    for index, (language, value) in enumerate(visible):
        percentage = value / total * 100

        start_angle = current_angle
        end_angle = current_angle + percentage / 100 * 360

        path = pie_slice(
            cx,
            cy,
            radius,
            start_angle,
            end_angle,
        )

        color = COLORS[index % len(COLORS)]

        svg.append(
            f'<path d="{path}" fill="{color}" stroke="{BACKGROUND}" stroke-width="2"/>'
        )

        current_angle = end_angle

    legend_x = 405
    legend_y = 105
    row_height = 38

    for index, (language, value) in enumerate(visible):
        percentage = value / total * 100
        color = COLORS[index % len(COLORS)]
        y = legend_y + index * row_height

        svg.append(
            f'<rect x="{legend_x}" y="{y - 14}" width="14" height="14" '
            f'rx="3" fill="{color}"/>'
        )

        svg.append(
            f'<text x="{legend_x + 25}" y="{y}" '
            f'fill="{TEXT}" font-family="sans-serif" '
            f'font-size="15">'
            f"{escape_xml(language)}"
            "</text>"
        )

        svg.append(
            f'<text x="{width - 35}" y="{y}" '
            f'text-anchor="end" fill="{MUTED}" '
            f'font-family="sans-serif" font-size="14">'
            f"{percentage:.1f}%"
            "</text>"
        )

    svg.append("</svg>")

    return "\n".join(svg)


def main():
    print(f"Collecting languages for {USERNAME}...")

    totals = collect_languages()

    if not totals:
        raise RuntimeError("No language information was found.")

    svg = generate_svg(totals)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")

    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
