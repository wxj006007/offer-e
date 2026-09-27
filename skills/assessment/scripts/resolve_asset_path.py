#!/usr/bin/env python3
"""Resolve the bundled offline career-assessment HTML asset."""

from pathlib import Path
import sys


def main() -> int:
    skill_dir = Path(__file__).resolve().parent.parent
    html_path = skill_dir / "assets" / "index.html"

    if not html_path.is_file():
        print(f"ASSESSMENT_ASSET_NOT_FOUND:{html_path}", file=sys.stderr)
        return 2

    try:
        html = html_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"ASSESSMENT_ASSET_UNREADABLE:{html_path}:{exc}", file=sys.stderr)
        return 3

    required_markers = (
        'id="page-welcome"',
        "function startQuiz()",
        "html2canvas v1.4.1, MIT License. Inlined",
    )
    missing_markers = [marker for marker in required_markers if marker not in html]
    if missing_markers:
        print(
            "ASSESSMENT_ASSET_INCOMPLETE:"
            + html_path.as_posix()
            + ":"
            + ",".join(missing_markers),
            file=sys.stderr,
        )
        return 4

    print(str(html_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
