from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os

root = Path.cwd()
templates_dir = str(Path(root, "templates").absolute())
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("index.jinja")

filename = Path(root, "html", "index.html")

# def component(filepath: str):
# return "./components/"+filepath

# env.globals["component"]=component

colors = {
    "blue_gradient": "linear-gradient(to bottom, #283b95, #17b2c3)",
    "blue": "rgb(31, 185, 194)",
    "text_white": """ style="color: white" """,
    "text_black": """ style="color: black" """,
    "bg_yellow": """ data-background-gradient="linear-gradient(to left, #caaf34, #b16010)" style="color: white" """,
}

with open(filename, "w") as fh:
    fh.write(template.render(**colors))
