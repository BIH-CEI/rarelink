import subprocess
import yaml
from pathlib import Path
import importlib.resources as ilr
import shutil

RDCDM_PKG = "rd_cdm"

def get_latest_rdcdm_version() -> str:
    inst = Path(ilr.files(RDCDM_PKG)) / "instances"
    versions = sorted([p.name for p in inst.iterdir() if p.is_dir()])
    return versions[-1]

def sync_and_generate(dest_root: Path) -> Path:
    version = get_latest_rdcdm_version()
    src = Path(ilr.files(RDCDM_PKG)) / "instances" / version
    dest = dest_root / version
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    
    # Generate LinkML schema for code systems
    code_yaml = src / "code_systems.yaml"
    schema_yaml = dest / "schema_definitions" / "rarelink_code_systems.yaml"
    schema_yaml.parent.mkdir(parents=True, exist_ok=True)
    with open(code_yaml) as f:
        codes = yaml.safe_load(f)
    schema = _generate_linkml_schema(codes)
    with open(schema_yaml, "w") as f:
        yaml.safe_dump(schema, f, sort_keys=False)
    
    # Regenerate Python classes from schema
    out_dir = dest / "python_datamodel"
    subprocess.run([
        "gen-python",
        str(schema_yaml),
        "--output", str(out_dir / "rarelink_code_systems.py")
    ], check=True)
    return dest

def _generate_linkml_schema(codes: dict) -> dict:
    fields = {}
    for name, cfg in codes.items():
        fields[name] = {"range": "CodeSystem", "description": cfg.get("title", name)}
    return {
        "name": "rarelink_code_systems",
        "id": "https://rarelink/rarelink_code_systems",
        "prefixes": {"linkml": "https://w3id.org/linkml/"},
        "imports": ["linkml:types"],
        "classes": {
            "CodeSystem": {
                "attributes": {
                    "name": {"range": "string"},
                    "url": {"range": "uri"},
                    "version": {"range": "string"},
                    "prefix": {"range": "string"},
                    "iri_prefix": {"range": "uri"}
                }
            },
            "CodeSystemsContainer": {
                "attributes": fields
            }
        }
    }