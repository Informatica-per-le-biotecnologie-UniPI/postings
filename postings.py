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

def sequence_pair(start, finish, sequence: Sequence) -> bool:
    """La sequenza data inizia con `start` e finisce con `finish`?

    :param start: Inizio sequenza
    :param finish: Fine sequenza
    :param sequence: La sequenza
    :return: True se inizia con `start` e finisce con `finish`, False altrimenti.
    """
    posting_list = posting(sequence)

    # non ho entrambi gli elementi: sicuramente False
    if not(start in posting_list and finish in posting_list):
        return False

    # la condizione e' vera se per almeno un indice di start, trovo un indice di finish
    # di valore maggiore!
    for start_index in posting_list[start]:
        if any([
            finish_index > start_index
            for finish_index in posting_list[finish]
        ]):
            return True

    return False
