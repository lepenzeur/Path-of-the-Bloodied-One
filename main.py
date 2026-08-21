"""Path of the Bloodied One — Agraphon Studios."""

from __future__ import annotations

import os
import platform
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from core.bootstrap import BOOT_DIAGNOSTICS, run

APP_VERSION = "2.1.0"


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


def _write_crash_log(exc: BaseException) -> Path | None:
    try:
        log_dir = _user_data_dir() / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = log_dir / f"crash-{stamp}.log"
        details = [
            "Path of the Bloodied One",
            "Agraphon Studios",
            f"Version: {APP_VERSION}",
            f"UTC: {datetime.now(timezone.utc).isoformat()}",
            f"Python: {sys.version}",
            f"Platform: {platform.platform()}",
            f"Executable: {sys.executable}",
            f"Frozen: {bool(getattr(sys, 'frozen', False))}",
            f"Developer mode env: {os.environ.get('PATH_BLOODIED_DEV', '<unset>')}",
            f"Boot diagnostics: {BOOT_DIAGNOSTICS[-16:]}",
            "",
            "".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
        ]
        path.write_text("\n".join(details), encoding="utf-8")
        return path
    except Exception as log_exc:
        print(f"POTBO crash logging failed: {log_exc!r}", file=sys.stderr)
        return None


if __name__ == "__main__":
    try:
        run(__file__)
    except SystemExit:
        raise
    except BaseException as exc:
        path = _write_crash_log(exc)
        if path is not None:
            print(f"Crash log: {path}", file=sys.stderr)
        raise
