#!/usr/bin/env python3
"""Check that all external image URLs in README.md return HTTP 200.

Extracts every <img> tag from the entire README, skips local file paths
(assets/), and validates each external URL returns a successful HTTP status.

Optional external widgets (e.g. github-profile-trophy.vercel.app) are
reported as warnings rather than hard failures, since they depend on
third-party public services beyond the template's control.

Exits with code 1 if any *required* URL is broken.
"""

import re
import sys
import urllib.parse
import urllib.request
import urllib.error

README_PATH = "README.md"
TIMEOUT = 15  # seconds per request

# Optional external widget domains — failures here are warnings, not errors.
# These are third-party services that the template does not control.
OPTIONAL_EXTERNAL_DOMAINS: set[str] = {
    "github-profile-trophy.vercel.app",
}

# Expected template placeholder URL substrings — these are literal placeholder
# URLs in the template that users are expected to replace after forking.
# They are not real URLs and should not be treated as blocking failures.
# Example: raw.githubusercontent.com/USERNAME/USERNAME/output/snake.svg
PLACEHOLDER_URL_PATTERNS: set[str] = {
    "USERNAME/USERNAME/output/snake.svg",
}


def classify_url(url: str) -> str:
    """Classify a URL as 'required', 'optional', or 'placeholder'.

    Optional URLs point to external third-party widgets that the template
    does not own or control. They are reported as warnings rather than
    blocking errors.

    Placeholder URLs contain literal template markers (e.g. USERNAME) that
    indicate they are expected to be replaced after forking. They are also
    reported as non-blocking warnings.
    """
    url_lower = url.lower()
    for pattern in PLACEHOLDER_URL_PATTERNS:
        if pattern.lower() in url_lower:
            return "placeholder"
    domain = urllib.parse.urlparse(url).netloc.lower()
    for optional_domain in OPTIONAL_EXTERNAL_DOMAINS:
        if domain == optional_domain or domain.endswith("." + optional_domain):
            return "optional"
    return "required"


def extract_all_image_urls(content: str) -> list[tuple[str, str, str]]:
    """Extract (alt_text, url, section_name) from all <img> tags.

    Skips local file references (assets/*).
    """
    img_pattern = re.compile(r'<img[^>]*\s+src="([^"]+)"[^>]*\s+alt="([^"]*)"[^>]*>')
    urls: list[tuple[str, str, str]] = []

    lines = content.splitlines()
    current_section = "(top)"

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Track current section heading
        if stripped.startswith("## "):
            current_section = stripped.lstrip("#").strip()
            continue

        for match in img_pattern.finditer(line):
            url = match.group(1)
            alt = match.group(2)

            # Skip local file references
            if url.startswith("assets/") or url.startswith("./") or url.startswith("../"):
                continue

            urls.append((alt, url, current_section))

    return urls


def check_url(alt: str, url: str) -> tuple[str, int | str, bool]:
    """Check a single URL. Returns (alt, status_or_error, is_ok)."""
    try:
        req = urllib.request.Request(
            url,
            method="GET",
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (compatible; IconChecker/1.0)"
                ),
            },
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            status = resp.status
            # Accept 200 and 304 (Not Modified — cached but valid)
            return (alt, status, status in (200, 304))
    except urllib.error.HTTPError as e:
        return (alt, f"HTTP {e.code}", False)
    except urllib.error.URLError as e:
        return (alt, str(e.reason), False)
    except Exception as e:
        return (alt, str(e), False)


def main() -> int:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    images = extract_all_image_urls(content)
    if not images:
        print(f"::error::No external image URLs found in {README_PATH}")
        return 1

    print(f"Checking {len(images)} external image URLs...\n")

    failed = 0
    warned = 0
    current_section = None

    for alt, url, section in images:
        # Print section header when section changes
        if section != current_section:
            current_section = section
            print(f"\n--- {section} ---")

        classification = classify_url(url)
        alt_text, status, ok = check_url(alt, url)

        if ok:
            status_icon = "[OK]"
        elif classification in ("optional", "placeholder"):
            status_icon = "[WARN]"
            warned += 1
        else:
            status_icon = "[FAIL]"
            failed += 1

        safe_url = url.encode("utf-8", errors="replace").decode("utf-8")
        print(f"  {alt_text}: {safe_url}")
        print(f"    {status_icon} {status}")
        print()

    # Count warnings by classification type
    placeholder_count = sum(
        1 for _, url, section in images
        if classify_url(url) == "placeholder"
    )
    optional_count = warned - placeholder_count

    parts = [f"{len(images)} URLs checked across all sections"]
    if failed:
        parts.append(f"{failed} failed")
    if optional_count:
        label = "warned (optional external widget" + ("s" if optional_count != 1 else "") + ")"
        parts.append(f"{optional_count} {label}")
    if placeholder_count:
        label = "warned (expected template placeholder" + ("s" if placeholder_count != 1 else "") + ")"
        parts.append(f"{placeholder_count} {label}")
    if not failed and not warned:
        parts.append("all OK")

    summary = f"\n{'='*50}\n{', '.join(parts)}"

    if failed:
        print(f"{summary}\n::error::[FAIL] {failed} required URL(s) returned errors")
    elif warned:
        print(f"{summary}\n[WARN] Non-blocking warnings — no required failures")
    else:
        print(f"{summary}\n[OK] All external image URLs OK")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
