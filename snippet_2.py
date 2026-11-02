#!/usr/bin/env python3
"""
snippet_2.py
------------
Coded reference links for the Luminaria-Organic-Token project
and all repositories under the GitHub account piersonkevin290-ux
(Kevin Frank Pierson).

Created: 2026-11-02
Author:  Kevin Frank Pierson
"""

# Project ID / Primary Repository
PROJECT_ID = "Luminaria-Organic-Token"
PROJECT_URL = "https://github.com/piersonkevin290-ux/Luminaria-Organic-Token"
PROJECT_DESCRIPTION = (
    "Truth and transparency repository for Kevin Frank Pierson "
    "(Angelo Dr, Kronenwetter, WI). Documentation and license key "
    "reference for new_luminaria_organic_token."
)

# Token / License Identifier declared in this project
TOKEN_IDENTIFIER = "new_luminaria_organic_token"
TRANSPARENCY_ID = "Lumina-Trans-ID-KP-001"

# All known repositories under the account (GitHubKevinGitHub)
GITHUB_ACCOUNT = "piersonkevin290-ux"
GITHUB_PROFILE = f"https://github.com/{GITHUB_ACCOUNT}"

REPOSITORIES = [
    {
        "name": "Luminaria-Organic-Token",
        "full_name": "piersonkevin290-ux/Luminaria-Organic-Token",
        "url": "https://github.com/piersonkevin290-ux/Luminaria-Organic-Token",
        "private": False,
        "description": "Truth and transparency repository + new_luminaria_organic_token declaration",
        "created": "2026-11-02",
    },
    {
        "name": "Lumina-Nexus-Partnership",
        "full_name": "piersonkevin290-ux/Lumina-Nexus-Partnership",
        "url": "https://github.com/piersonkevin290-ux/Lumina-Nexus-Partnership",
        "private": True,
        "description": "Private partnership / development repository",
        "created": "2026-03-07",
    },
]

def print_links():
    """Print all project and repository links in a clean format."""
    print("=" * 60)
    print("PROJECT LINKS – Kevin Frank Pierson")
    print("=" * 60)
    print(f"Primary Project ID : {PROJECT_ID}")
    print(f"Primary URL        : {PROJECT_URL}")
    print(f"Token Identifier   : {TOKEN_IDENTIFIER}")
    print(f"Transparency ID    : {TRANSPARENCY_ID}")
    print()
    print(f"GitHub Account     : {GITHUB_ACCOUNT}")
    print(f"Profile            : {GITHUB_PROFILE}")
    print()
    print("All Repositories:")
    print("-" * 60)
    for repo in REPOSITORIES:
        visibility = "Private" if repo["private"] else "Public"
        print(f"  • {repo['name']} ({visibility})")
        print(f"    {repo['url']}")
        print(f"    {repo['description']}")
        print()
    print("=" * 60)

if __name__ == "__main__":
    print_links()
