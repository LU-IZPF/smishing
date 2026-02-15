#!/usr/bin/env python3
"""
Search engine indexing check.

Usage:
    python search-index-check.py <domain_or_url> --api-key <KEY>
    python search-index-check.py <domain_or_url> -o result.json

pip install requests
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install requests")


def check_domain(domain: str, api_key: str) -> dict:
    query = f"site:{domain}"

    resp = requests.post(
        "https://google.serper.dev/search",
        json={"q": query, "num": 1},
        headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
        timeout=15,
    )
    resp.raise_for_status()
    body = resp.json()

    indexed = len(body.get("organic", [])) > 0

    return {
        "domain": domain,
        "query": query,
        "indexed": indexed,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "api_response": body,
    }


def main():
    parser = argparse.ArgumentParser(description="Check if a domain is indexed via Google.")
    parser.add_argument("domain", help="Domain or URL to check.")
    parser.add_argument("--api-key", default=None, help="Serper API key (or set SERPER_API_KEY env var).")
    parser.add_argument("-o", "--output", default=None, help="Save JSON response to file.")
    args = parser.parse_args()

    domain = args.domain
    if "://" in domain:
        domain = urlparse(domain).hostname
    domain = domain.strip().lower()

    api_key = args.api_key or os.environ.get("SERPER_API_KEY", "")
    if not api_key:
        parser.error("Provide API key via --api-key or SERPER_API_KEY env var.")

    result = check_domain(domain, api_key)
    print(f"{domain}: {'INDEXED' if result['indexed'] else 'NOT INDEXED'}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
