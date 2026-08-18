"""Path of the Bloodied One — Agraphon Studios."""

from __future__ import annotations

import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from core.bootstrap import run


def _user_data_dir() -> Path:
    if sys.platform.startswith("win"):
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        if not base:
            base = str(Path.home() / "AppData" / "Local")
        return Path(base) / "Agraphon Studios" / "Path of the Bloodied One"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Agraphon Studios" / "Path of the Bloodied One"
    base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / "agraphon-studios" / "path-of-the-bloodied-one"


def _write_crash_log(exc: BaseException) -> None:
    try:
        log_dir = _user_data_dir() / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = log_dir / f"crash-{stamp}.log"
        path.write_text(
            "Path of the Bloodied One\n"
            "Agraphon Studios\n"
            f"UTC: {datetime.now(timezone.utc).isoformat()}\n"
            f"Python: {sys.version}\n\n"
            + "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
            encoding="utf-8",
        )
    except Exception:
        pass


if __name__ == "__main__":
    try:
        run(__file__)
    except SystemExit:
        raise
    except BaseException as exc:
        _write_crash_log(exc)
        raise
