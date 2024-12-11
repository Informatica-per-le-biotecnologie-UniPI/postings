from typing import Sequence


def posting(sequence: Sequence) -> dict:
    """Crea una posting list per la data `sequence`.

    :param sequence: La sequenza.
    :return: Un dizionario elemento -> posting list
    """
    posting_list = dict()

    for index, element in enumerate(sequence):
        # metodo .get(A, B) nei dizionari: cosa fa? cerca nella documentazione
        posting_list[element] = posting_list.get(element, list()) + [index]

    return posting_list
