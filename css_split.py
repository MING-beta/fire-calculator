import os
import re

base_dir = r"c:\Users\user\Desktop\dopaming\fire-calculator"
style_path = os.path.join(base_dir, "style.css")
index_path = os.path.join(base_dir, "index.html")
fire_path = os.path.join(base_dir, "fire.html")
sw_path = os.path.join(base_dir, "sw.js")

css_dir = os.path.join(base_dir, "css")
os.makedirs(css_dir, exist_ok=True)

# 1. index.html inline CSS extraction to css/portal.css
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

style_match = re.search(r'<style>(.*?)</style>', index_html, flags=re.DOTALL)
if style_match:
    portal_css = style_match.group(1).strip()
    with open(os.path.join(css_dir, "portal.css"), 'w', encoding='utf-8') as f:
        f.write(portal_css)
    index_html = index_html.replace(style_match.group(0), '<link rel="stylesheet" href="css/portal.css">')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Extracted portal.css from index.html")

# 2. Extract style.css segments into global.css, components.css, calculator.css
with open(style_path, 'r', encoding='utf-8') as f:
    style_content = f.read()

# Define segments by splitting with markers
# 1) global.css
global_css = ""
global_css += style_content.split("/* Toggle Switch Styles */")[0]
# Glassmorphism
glass_idx = style_content.find("/* Glassmorphism Card */")
glass_end = style_content.find("/* Main Content Layout */")
if glass_idx != -1 and glass_end != -1:
    global_css += style_content[glass_idx:glass_end]
# Animations
anim_idx = style_content.find("@keyframes pulse")
anim_end = style_content.find("/* --- Guide Quest Styles --- */")
if anim_idx != -1 and anim_end != -1:
    global_css += style_content[anim_idx:anim_end]
# Toast
toast_idx = style_content.find("/* Toast Message */")
if toast_idx != -1:
    global_css += style_content[toast_idx:]

with open(os.path.join(css_dir, "global.css"), 'w', encoding='utf-8') as f:
    f.write(global_css)


# 2) components.css
comp_css = ""
def extract_section(start_str, end_str):
    start = style_content.find(start_str)
    end = style_content.find(end_str) if end_str else -1
    if start != -1:
        return style_content[start:end] if end != -1 else style_content[start:]
    return ""

comp_css += extract_section("/* Toggle Switch Styles */", "/* Header */")
comp_css += extract_section("/* Header */", "/* Glassmorphism Card */")
comp_css += "/* Export Buttons */\n" + extract_section(".export-btn {", "/* Plan B Reply Style */")

comp_css += extract_section("/* Target Mode Toggle */", "/* Custom Select Dropdown */")
comp_css += extract_section("/* Custom Select Dropdown */", "/* Speed Dial Floating Action Menu */")
comp_css += extract_section("/* Speed Dial Floating Action Menu */", "/* Chart Modal CSS */")
comp_css += extract_section("/* Chart Modal CSS */", "/* Utilities */")
comp_css += extract_section("/* Utilities */", "/* Compare Toggle Switch Active Color */")

# Add missing inputs config and sliders
slider_start = style_content.find("/* Custom Range Slider */")
slider_end = style_content.find("/* Settings Groups Layout */")
if slider_start != -1 and slider_end != -1:
    comp_css += style_content[slider_start:slider_end]

with open(os.path.join(css_dir, "components.css"), 'w', encoding='utf-8') as f:
    f.write(comp_css)


# 3) calculator.css (Specific features)
calc_css = ""
calc_css += extract_section("/* Main Content Layout */", ".export-btn {")
calc_css += extract_section("/* Plan B Reply Style */", "/* Target Mode Toggle */")
calc_css += extract_section("/* Settings Groups Layout */", "/* Target Mode Toggle */") # just settings group config

calc_css += extract_section("/* Compare Toggle Switch Active Color */", "/* ============================\n   Help Overlay UI")
calc_css += extract_section("/* ============================\n   Help Overlay UI", "@keyframes pulse")
calc_css += extract_section("/* --- Guide Quest Styles --- */", "/* Toast Message */")

with open(os.path.join(css_dir, "calculator.css"), 'w', encoding='utf-8') as f:
    f.write(calc_css)

print("Split style.css into global.css, components.css, and calculator.css")


# 3. Update fire.html links
with open(fire_path, 'r', encoding='utf-8') as f:
    fire_html = f.read()

fire_html = fire_html.replace('<link rel="stylesheet" href="style.css">', 
   '<link rel="stylesheet" href="css/global.css">\n    <link rel="stylesheet" href="css/components.css">\n    <link rel="stylesheet" href="css/calculator.css">')

with open(fire_path, 'w', encoding='utf-8') as f:
    f.write(fire_html)
print("Updated fire.html with new CSS links")


# 4. Update sw.js to cache the new files
with open(sw_path, 'r', encoding='utf-8') as f:
    sw_js = f.read()

# Replace version and CSS cache array
sw_js = re.sub(r'const CACHE_NAME = \'.*?\'', "const CACHE_NAME = 'fire-tribe-v1.3.0'", sw_js)
sw_js = sw_js.replace("'./style.css',", "'./css/global.css',\n    './css/components.css',\n    './css/calculator.css',\n    './css/portal.css',")

with open(sw_path, 'w', encoding='utf-8') as f:
    f.write(sw_js)
print("Updated sw.js")

# Finally delete original style.css
try:
    os.remove(style_path)
    print("Deleted old style.css")
except:
    pass
