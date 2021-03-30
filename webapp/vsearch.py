
def search4vowels(phrase:str) -> set:
    """Zwraca samogloski znalezione we frazie podanej jako argument"""
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """Zwraca zbior liter ze zmiennej letters znalezionych w zmiennej phrase"""
    return set(letters).intersection(set(phrase))
