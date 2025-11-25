#!/usr/bin/env python3
"""Migration script: book-source → PanaversityFS storage.

This script migrates content from the Docusaurus book-source structure
to the PanaversityFS storage format (ADR-0018 aligned).

Source structure (book-source/):
    docs/
        {NN-Part}/
            README.md
            {NN-Chapter}/
                README.md
                {NN-lesson}.md
    static/
        img/
        slides/
        ...

Target structure (data/books/{book-id}/):
    content/                    # Maps to docs/
        {NN-Part}/
            README.md
            {NN-Chapter}/
                README.md
                {NN-lesson}.md
                {NN-lesson}.summary.md  (if exists)
    static/                     # Maps to static/
        images/                 # Renamed from img/
        slides/
        ...
    book.yaml

Usage:
    # Dry run (preview changes)
    python scripts/migrate_book_source.py --dry-run

    # Migrate to local filesystem
    python scripts/migrate_book_source.py --target ./data

    # Migrate to specific book ID
    python scripts/migrate_book_source.py --book-id ai-native-dev --target ./data

    # With verbose output
    python scripts/migrate_book_source.py --verbose --target ./data
"""

import argparse
import os
import shutil
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone


def get_book_metadata(book_id: str, source_dir: Path) -> dict:
    """Generate book.yaml metadata."""
    return {
        "book_id": book_id,
        "title": "AI-Native Software Development",
        "description": "Comprehensive guide to AI-driven development practices",
        "version": "1.0.0",
        "authors": ["Panaversity Team"],
        "storage_backend": "fs",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_migrated_from": str(source_dir),
        "adr": "ADR-0018"
    }


def create_registry_entry(book_id: str, title: str) -> dict:
    """Create registry.yaml entry for the book."""
    return {
        "book_id": book_id,
        "title": title,
        "storage_backend": "fs",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "active"
    }


def migrate_content(source_docs: Path, target_content: Path, dry_run: bool, verbose: bool) -> dict:
    """Migrate docs/ content to content/.

    Returns stats dict with counts.
    """
    stats = {
        "files_copied": 0,
        "dirs_created": 0,
        "errors": []
    }

    if not source_docs.exists():
        stats["errors"].append(f"Source docs directory not found: {source_docs}")
        return stats

    for root, dirs, files in os.walk(source_docs):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        rel_path = Path(root).relative_to(source_docs)
        target_dir = target_content / rel_path

        # Create target directory
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
        stats["dirs_created"] += 1

        if verbose:
            print(f"  DIR: {target_dir}")

        for file in files:
            if file.startswith('.'):
                continue

            source_file = Path(root) / file
            target_file = target_dir / file

            if verbose:
                print(f"  FILE: {source_file} → {target_file}")

            if not dry_run:
                shutil.copy2(source_file, target_file)

            stats["files_copied"] += 1

    return stats


def migrate_static(source_static: Path, target_static: Path, dry_run: bool, verbose: bool) -> dict:
    """Migrate static/ assets.

    Handles renaming:
    - img/ → images/

    Returns stats dict.
    """
    stats = {
        "files_copied": 0,
        "dirs_created": 0,
        "errors": []
    }

    if not source_static.exists():
        stats["errors"].append(f"Source static directory not found: {source_static}")
        return stats

    # Mapping for directory renames
    dir_mapping = {
        "img": "images"  # Standardize to 'images'
    }

    for item in source_static.iterdir():
        if item.name.startswith('.'):
            continue

        # Apply directory mapping
        target_name = dir_mapping.get(item.name, item.name)
        target_path = target_static / target_name

        if item.is_dir():
            if verbose:
                print(f"  DIR: {item} → {target_path}")

            if not dry_run:
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(item, target_path)

            # Count files in directory
            file_count = sum(1 for _ in item.rglob('*') if _.is_file())
            stats["files_copied"] += file_count
            stats["dirs_created"] += 1

        elif item.is_file():
            if verbose:
                print(f"  FILE: {item} → {target_path}")

            if not dry_run:
                target_static.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_path)

            stats["files_copied"] += 1

    return stats


def migrate_book(
    source_dir: Path,
    target_dir: Path,
    book_id: str,
    dry_run: bool = False,
    verbose: bool = False
) -> dict:
    """Migrate a complete book from book-source to PanaversityFS format.

    Args:
        source_dir: Path to book-source (containing docs/ and static/)
        target_dir: Path to PanaversityFS storage root (e.g., ./data)
        book_id: Book identifier
        dry_run: If True, only preview changes
        verbose: If True, print detailed output

    Returns:
        Migration stats dict
    """
    stats = {
        "content": {},
        "static": {},
        "registry_created": False,
        "book_yaml_created": False,
        "errors": []
    }

    source_docs = source_dir / "docs"
    source_static = source_dir / "static"
    target_book = target_dir / "books" / book_id
    target_content = target_book / "content"
    target_static = target_book / "static"

    print(f"\n{'='*60}")
    print(f"PanaversityFS Migration (ADR-0018)")
    print(f"{'='*60}")
    print(f"Source:     {source_dir}")
    print(f"Target:     {target_dir}")
    print(f"Book ID:    {book_id}")
    print(f"Dry Run:    {dry_run}")
    print(f"{'='*60}\n")

    # Create target structure
    if not dry_run:
        target_content.mkdir(parents=True, exist_ok=True)
        target_static.mkdir(parents=True, exist_ok=True)

    # Migrate content
    print("Migrating content (docs/ → content/)...")
    stats["content"] = migrate_content(source_docs, target_content, dry_run, verbose)
    print(f"  ✓ {stats['content']['files_copied']} files, {stats['content']['dirs_created']} directories")

    # Migrate static assets
    print("\nMigrating static assets (static/ → static/)...")
    stats["static"] = migrate_static(source_static, target_static, dry_run, verbose)
    print(f"  ✓ {stats['static']['files_copied']} files, {stats['static']['dirs_created']} directories")

    # Create book.yaml
    print("\nCreating book.yaml...")
    book_yaml_path = target_book / "book.yaml"
    if not dry_run:
        book_metadata = get_book_metadata(book_id, source_dir)
        with open(book_yaml_path, 'w') as f:
            yaml.dump(book_metadata, f, default_flow_style=False, sort_keys=False)
        stats["book_yaml_created"] = True
    print(f"  ✓ {book_yaml_path}")

    # Create/update registry.yaml
    print("\nUpdating registry.yaml...")
    registry_path = target_dir / "registry.yaml"
    if not dry_run:
        registry_entry = create_registry_entry(book_id, "AI-Native Software Development")

        if registry_path.exists():
            with open(registry_path, 'r') as f:
                registry = yaml.safe_load(f) or {"books": []}
        else:
            registry = {"books": []}

        # Check if book already exists
        existing_ids = [b.get("book_id") for b in registry.get("books", [])]
        if book_id not in existing_ids:
            registry["books"].append(registry_entry)

        with open(registry_path, 'w') as f:
            yaml.dump(registry, f, default_flow_style=False, sort_keys=False)
        stats["registry_created"] = True
    print(f"  ✓ {registry_path}")

    # Summary
    total_files = stats["content"]["files_copied"] + stats["static"]["files_copied"]
    total_dirs = stats["content"]["dirs_created"] + stats["static"]["dirs_created"]

    print(f"\n{'='*60}")
    print(f"Migration {'Preview' if dry_run else 'Complete'}!")
    print(f"{'='*60}")
    print(f"Total files:       {total_files}")
    print(f"Total directories: {total_dirs}")

    if stats["content"]["errors"] or stats["static"]["errors"]:
        print(f"\nErrors:")
        for err in stats["content"]["errors"] + stats["static"]["errors"]:
            print(f"  ✗ {err}")

    if not dry_run:
        print(f"\nNext steps:")
        print(f"  1. Test locally:")
        print(f"     export PANAVERSITY_STORAGE_ROOT={target_dir}")
        print(f"     export PANAVERSITY_STORAGE_BACKEND=fs")
        print(f"     uv run python -m panaversity_fs.server")
        print(f"")
        print(f"  2. Verify with MCP client:")
        print(f"     curl http://localhost:8000/mcp -d '{{\"method\":\"list_books\"}}'")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Migrate book-source to PanaversityFS storage format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).parent.parent.parent / "book-source",
        help="Source book-source directory (default: ../book-source)"
    )

    parser.add_argument(
        "--target",
        type=Path,
        default=Path(__file__).parent.parent / "data",
        help="Target storage directory (default: ./data)"
    )

    parser.add_argument(
        "--book-id",
        type=str,
        default="ai-native-dev",
        help="Book identifier (default: ai-native-dev)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without making them"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    # Validate source exists
    if not args.source.exists():
        print(f"ERROR: Source directory not found: {args.source}")
        sys.exit(1)

    # Run migration
    stats = migrate_book(
        source_dir=args.source,
        target_dir=args.target,
        book_id=args.book_id,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    # Exit with error code if there were errors
    all_errors = stats["content"].get("errors", []) + stats["static"].get("errors", [])
    sys.exit(1 if all_errors else 0)


if __name__ == "__main__":
    main()
