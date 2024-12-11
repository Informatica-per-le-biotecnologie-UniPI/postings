from typing import Sequence, Tuple


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

def sequence_pair(start, finish, sequence: Sequence, with_index: bool = False) -> bool:
    """La sequenza data inizia con `start` e finisce con `finish`?

    :param start: Inizio sequenza
    :param finish: Fine sequenza
    :param sequence: La sequenza
    :param with_index: Restituisci anche gli indici?
    :return: True se inizia con `start` e finisce con `finish`, False altrimenti. Se `with_index` e' True, restituisce
             anche gli indici.
    """
    posting_list = posting(sequence)

    # non ho entrambi gli elementi: sicuramente False
    if not(start in posting_list and finish in posting_list):
        if with_index:
            return False, None, None

        return False

    for start_index in posting_list[start]:
        # estraggo tutti gli indici di b successivi all'indice corrente di a
        candidate_indexes = [
            finish_index
            for finish_index in posting_list[finish]
            if finish_index > start_index
        ]

        # se non ho trovato indici...
        if len(candidate_indexes) == 0:
            if with_index:
                return False, None, None
            else:
                return False

        # se ho trovato indici...
        else:
            if with_index:
                return True, start_index, candidate_indexes[0]
            else:
                return True

    if with_index:
        return False, None, None
    else:
        return False

def sequence_triple(start, middle, finish, sequence: Sequence) -> bool:
    """La sequenza data inizia con `start` e finisce con `finish`?

    :param start: Inizio sequenza
    :param middle: Elemento in mezzo alla sequenza
    :param finish: Fine sequenza
    :param sequence: La sequenza
    :return: True se inizia con `start` e finisce con `finish`, con un `middle` in mezzo. False altrimenti.
    """
    start_middle, occurrence_start, occurrence_middle = sequence_pair(start, middle, sequence,
                                                                      with_index=True)
    if start_middle:
        return sequence_pair(middle, finish, sequence[occurrence_middle:], with_index=False)

    return False
