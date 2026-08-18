from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]


def test_preciosa_gameplay_sheet_and_original_illustrations_present():
    assert (ROOT / "assets" / "characters" / "preciosa_spriteSheet.png").is_file()
    assert (ROOT / "assets" / "portraits" / "preciosa.png").is_file()
    assert (ROOT / "assets" / "portraits" / "preciosa_card.jpeg").is_file()
    assert not (ROOT / "assets" / "portraits" / "preciosa_temp_portrait.png").exists()


def test_production_branding_present_and_injokes_absent():
    credits = (ROOT / "gameplay" / "effects.py").read_text(encoding="utf-8")
    splash = (ROOT / "ui" / "splash.py").read_text(encoding="utf-8")
    vendors = (ROOT / "ui" / "vendors.py").read_text(encoding="utf-8")
    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*.py")
        if "__pycache__" not in path.parts and "tests" not in path.parts
    )
    assert "AGRAPHON STUDIOS" in credits
    assert "AGRAPHON" in splash
    assert "Agraphon Studios" in vendors

    forbidden = ("FAKE KING", "Çaydöken", "Mırmır Cahit", "Düdüklü Efe", "VISUAL STUDIO CODE")
    assert all(token.casefold() not in combined.casefold() for token in forbidden)


def test_asset_provenance_inventory_covers_packaged_assets():
    inventory = ROOT / "LEGAL" / "ASSET_PROVENANCE.csv"
    assert inventory.is_file()
    with inventory.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    indexed = {row["path"] for row in rows}
    assets = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "assets").rglob("*")
        if path.is_file() and path.name.lower() != "desktop.ini"
    }
    assert indexed == assets
    status = {row["path"]: row["status"] for row in rows}
    assert status["assets/characters/preciosa_spriteSheet.png"] == "TEMP_DEV_ONLY"
    assert all(value == "TEMP_DEV_ONLY" for value in status.values())
