# Postings
Esercizi su posting lists.
Il codice contiene commenti, suggerimenti, domande, e alcuni warning: provate a capire perche' son warning!


## Quickstart
**Dipendenze.** Il progetto non ha dipendenze esterne.
**Struttura.**
  - `postings_test.py` contiene alcuni test di verifica soluzioni
  - `postings.py` contiene gli esercizi:
    - `posting(sequence: Sequence) -> dict` implementa le posting list
    - `sequence_pair(start, finish, sequence: Sequence, with_index: bool = False) -> bool` esercizio 1
    - `sequence_triple(start, middle, finish, sequence: Sequence) -> bool` esercizio 2
    - `is_in_sequence(string: str, sequence: str, with_index: bool = False) -> bool` esercizio 3
    - `is_in_sequence_m_to_n_times(string: str, sequence: str, m: int, n: int) -> bool` esercizio 4


**Installazione.**
Uno tra:
- `git clone https://github.com/Informatica-per-le-biotecnologie-UniPI/postings` scarica il progetto
in una cartella `postings`. Potete poi aprire la cartella come progetto Pycharm.
- Da Github desktop, clona repository esistente. Potete poi aprire la cartella come progetto Pycharm.
- Da Pycharm, `File > Project from version control`

---

## Testi

#### Posting list 0
Una posting list associa, ad ogni elemento, le posizioni in cui appare in una sequenza. Creare una funzione che crea la posting list di una data stringa.

Esempio.
```
ACGAGGTAC
```
Ha una posting list
```
A: [0, 3, 7]
C: [1, 8]
G: [2, 4, 5]
T: [6]
```

#### Posting list 1
Si crei una funzione per verificare se una stringa `a*b` appare nella sequenza.
`a*b` indica una stringa in cui appare `a`, seguita da un numero arbitrario di caratteri, seguita da `b`.
Si sfrutti la costruzione della posting list.

Esempio.

| `a` | `b` | Appare? |
| --- | --- | ------- |
| `A` | `C` | Si      |
| `A` | `T` | Si      |
| `T` | `C` | Si      |
| `T` | `X` | No      |
| `T` | `G` | No      |

#### Posting list 2
Si crei una funzione per verificare se una stringa `a*b*c` appare nella sequenza.

#### Posting list 3
Si crei una funzione per verificare se una stringa `(a)+` appare nella sequenza. `(a)+` indica una stringa in cui la stringa `a` appare *almeno* una volta.

#### Posting list 4
Si crei una funzione per verificare se una stringa `(a){m,n}` appare nella sequenza. `(a){m,n}` indica una stringa in cui la stringa `a` appare tra `m` e `n` volte. I parametri sono opzionali.
