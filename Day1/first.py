from typing import List
from pathlib import Path

ELVES_CALS_FILE = 'elves_list.txt'

def parse_elves(file_path: str) -> List[str]:
    """Extract the elven data"""
    content = Path.cwd() / Path(file_path)
    return [line for line in content.read_text().split('\n')]


def aggregate_calories(raw_list: List[str]) -> List[int]:
    """Return list of total elven calories"""
    empty_line = ''
    lst, cumul = [], 0
    for line in raw_list:
        if line != empty_line:
            cumul += int(line)
        else:
            lst.append(cumul)
            cumul =0
    else:
        lst.append(cumul)
    return lst

def get_cals(file_path: str) -> List[int]:
    """Calculate individual elf's calories"""
    return aggregate_calories(parse_elves(file_path))


def main():
    elves_summed = get_cals(ELVES_CALS_FILE)
    max_cals = max(elves_summed)
    elven_champ = elves_summed.index(max_cals)

    print(f"The champ is the {elven_champ + 1} elf")

if __name__ == "__main__":
    main()
