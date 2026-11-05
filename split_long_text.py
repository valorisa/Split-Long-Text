from pathlib import Path

SOURCE = Path("long_texte.txt")
OUTPUT = Path("parties")
LINES_PER_FILE = 500


def split_file():
    OUTPUT.mkdir(exist_ok=True)

    with SOURCE.open(
        "r", encoding="utf-8", errors="replace"
    ) as file:
        part = 1
        while True:
            lines = []
            for _ in range(LINES_PER_FILE):
                line = file.readline()
                if not line:
                    break
                lines.append(line)

            if not lines:
                break
            destination = OUTPUT / f"partie_{part}.txt"
            destination.write_text(
                "".join(lines),
                encoding="utf-8"
            )
            print(f"Partie créée : {destination}")
            part += 1


if __name__ == "__main__":
    if SOURCE.is_file():
        split_file()
    else:
        print("Fichier introuvable.")
