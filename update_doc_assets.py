from pathlib import Path
import os
from itertools import product
import shutil

TOPFOLDER = Path(__file__).parent / "src"
DATAMODEL_TOPFOLDER = TOPFOLDER / "cloudclient" / "datamodel"
DIAGRAM_FOLDER = TOPFOLDER.parent / "doc" / "html"
DATAMODEL_ASSETS = DATAMODEL_TOPFOLDER / "assets"

topfolder = ["actors.py", "gridconnections.py", "gridnodes.py", "contracts.py"]
assets = ["consumption.py", "conversion.py", "production.py", "storage.py"]

do_these_please = [
    *product([DATAMODEL_TOPFOLDER], topfolder),
    *product([DATAMODEL_ASSETS], assets),
]

for base_path, file in do_these_please:
    path = base_path / file
    stem = path.stem
    os.chdir(base_path)
    os.system(f"pyreverse {file} -o html")
    shutil.move(base_path / "classes.html", DIAGRAM_FOLDER / f"{stem}_classes.html")

from util import generate_excel
from mvp import payload

generate_excel(
    payload=payload, file_id="example", path=Path(__file__).parent / "doc" / "assets"
)
