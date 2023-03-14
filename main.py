from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os

root = Path(__file__).parent
templates_dir = Path(root, "templates")
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("index.html")

filename = Path(root, "html", "index.html")

# def component(filepath: str):
    # return "./components/"+filepath

# env.globals["component"]=component
    
with open(filename, "w") as fh:
    fh.write(template.render())