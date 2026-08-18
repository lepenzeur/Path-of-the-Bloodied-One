from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STAGE_RE = re.compile(r"^# <POTBO_STAGE (S\d{4})>\n(.*?)^# </POTBO_STAGE \1>$", re.MULTILINE | re.DOTALL)

def test_all_python_files_compile():
    for path in ROOT.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

def test_bootstrap_manifest_has_every_stage():
    import ast
    text = (ROOT / "core" / "bootstrap.py").read_text(encoding="utf-8")
    module = ast.parse(text)
    manifest = None
    for node in module.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "MANIFEST" for t in node.targets):
            manifest = ast.literal_eval(node.value)
            break
    assert manifest
    cache = {}
    for relative, stage in manifest:
        path = ROOT / relative
        cache.setdefault(relative, {m.group(1): m.group(2) for m in STAGE_RE.finditer(path.read_text(encoding="utf-8"))})
        assert stage in cache[relative], (relative, stage)
