from pathlib import Path

DIRECTORY = r"E:\Coding\wowie\omg"

OLD_TEXT = "bubbls/UGS-file-encryption"
NEW_TEXT = "RacerPilot2011/romsigforart"

RECURSIVE = True

FILE_EXTENSIONS = {".py", ".txt", ".html", ".css", ".js", ".json", ".lua"}

folder = Path(DIRECTORY)

files = folder.rglob("*") if RECURSIVE else folder.glob("*")

total_files = 0
total_replacements = 0

for file in files:
    if not file.is_file():
        continue

    if file.suffix.lower() not in FILE_EXTENSIONS:
        continue

    try:
        content = file.read_text(encoding="utf-8")

        count = content.count(OLD_TEXT)

        if count == 0:
            continue

        updated = content.replace(OLD_TEXT, NEW_TEXT)

        file.write_text(updated, encoding="utf-8")

        total_files += 1
        total_replacements += count

        print(f"[UPDATED] {file} ({count} replacements)")

    except (UnicodeError, OSError) as e:
        print(f"[ERROR] {file}: {e}")

print("\nFinished!")
print(f"Files modified: {total_files}")
print(f"Total replacements: {total_replacements}")
