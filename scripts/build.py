"""Build distributables for the radar capsule.

Produces:
  dist/radar.zip       -- skill folder for upload to claude.ai.
  chat-instruction.md  -- merged instruction for ChatGPT / Codex.

Usage: python3 scripts/build.py
"""

from __future__ import annotations

import hashlib
import logging
import re
import sys
import zipfile
from pathlib import Path

logger = logging.getLogger(__name__)

REPO = Path(__file__).resolve().parent.parent
RADAR_DIR = REPO / "plugins/radar/skills/radar"
DIST = REPO / "dist"
ZIP_DATE = (2026, 1, 1, 0, 0, 0)

RADAR_APPENDICES: list[tuple[str, str]] = [
    ("references/sources.md", "Приложение 1. Подключение почты, календаря и задач"),
    ("references/briefing-rules.md", "Приложение 2. Правила сводки"),
    ("templates/briefing.md", "Приложение 3. Шаблон сводки"),
    ("templates/settings.md", "Приложение 4. Шаблон блока «Настройки радара»"),
]
RADAR_INTRO = [
    "# Инструкция для чата: капсула «Радар» от labopsai",
    "",
    "Добавь этот файл в проект ChatGPT или Codex (файлом или в инструкции) "
    "и напиши: «Работай по инструкции из файлов проекта». Дальше — фраза «радар».",
    "",
    "Ты работаешь в обычном чате. Источники: встроенные коннекторы этого чата (если они есть), "
    "подключение Битрикс24 через MCP (ключ — только в настройках, не в чате), файлы или текст, который он вставил. "
    "Других доступов к его почте, календарю и задачам у тебя нет. Работаешь только на чтение.",
]


def build_zip(skill_dir: Path, out: Path) -> Path:
    """Zip the skill folder so that the folder itself is the archive root."""
    out.parent.mkdir(parents=True, exist_ok=True)
    root = skill_dir.name
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if (path.is_file() and not path.name.startswith(".")
                    and "__pycache__" not in path.parts):
                info = zipfile.ZipInfo(f"{root}/{path.relative_to(skill_dir).as_posix()}",
                                       date_time=ZIP_DATE)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                info.create_system = 3
                zf.writestr(info, path.read_bytes())
    with zipfile.ZipFile(out) as zf:
        names = zf.namelist()
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    listing = out.with_name(out.name + ".txt")
    listing.write_text(f"sha256 {digest}\n" + "\n".join(names) + "\n", encoding="utf-8")
    logger.info("Saved %s (%d files, sha256 %s)", out, len(names), digest[:12])
    return out


def strip_frontmatter(text: str) -> str:
    """Remove the YAML frontmatter block from a markdown file."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def build_chat_text(skill_dir: Path, out: Path, intro: list[str],
                    appendices: list[tuple[str, str]]) -> Path:
    """Merge SKILL.md and appendix files into one self-contained instruction text."""

    def relink(text: str) -> str:
        for rel, title in appendices:
            text = text.replace(f"`{rel}`", f"«{title.split('. ', 1)[0]}» ниже")
        text = text.replace("по «Приложение ", "по «Приложению ")
        return text.replace("из «Приложение ", "из «Приложения ")

    body = relink(strip_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8")))
    parts = [*intro, "", "---", "", body.strip()]
    for rel, title in appendices:
        ref = (skill_dir / rel).read_text(encoding="utf-8").strip()
        ref = relink(re.sub(r"\A# .*\n", "", ref).strip())
        parts += ["", "---", "", f"# {title}", "", ref]
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    logger.info("Saved %s (%d chars)", out, out.stat().st_size)
    return out


def build_radar_chat_instruction(out: Path) -> Path:
    """Build chat-instruction.md for ChatGPT / Codex."""
    return build_chat_text(RADAR_DIR, out, RADAR_INTRO, RADAR_APPENDICES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    build_zip(RADAR_DIR, DIST / "radar.zip")
    build_radar_chat_instruction(REPO / "chat-instruction.md")
