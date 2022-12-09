import first as F

from typing import List


def top_three(lst: List[int]) -> int:
    """ Print the sum of the the biggest elements of a list"""
    total = 0
    soft_copy = lst
    for _ in range(3):
        most = max(lst)
        total += most
        soft_copy.pop(lst.index(most))
    return total


def main():
    cals = F.get_cals(F.ELVES_CALS_FILE)
    print(top_three(cals))

if __name__ == "__main__":
   main() 
