from postings import posting, sequence_pair, sequence_triple, is_in_sequence


#############################################################################
# Esercizio 1 ###############################################################
#############################################################################

inputs = [
    "",
    "A",
    "AA",
    "ACGAGGTAC",
]
expected_outputs = [
    {},
    {"A": [0]},
    {"A": [0, 1]},
    {
        "A": [0, 3, 7],
        "C": [1, 8],
        "G": [2, 4, 5],
        "T": [6]
    },
]
results = [
    posting(inp)
    for inp in inputs
]

print(f"* Exercise 1 *******************************************")
print(f"Input\tExpected output\t\tOutput")
for inp, out, result  in zip(inputs, expected_outputs, results):
    print(f"{inp}\t\t{out}\t\t{result}\t")
print(f"********************************************************\n\n\n")


#############################################################################
# Esercizio 2 ###############################################################
#############################################################################

inputs = [
    ("", "", ""),
    ("", "C", ""),
    ("", "", "C"),
    ("A", "C", ""),
    ("A", "A", "A"),
    ("A", "C", "ABTCSA"),
    ("C", "A", "ABTCSA"),
    ("G", "T", "ACGAGGTAC"),
    ("G", "C", "ACGAGGTAC"),
    ("G", "X", "ACGAGGTAC"),
]
expected_outputs = [
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    False
]
results = [
    sequence_pair(a, b, sequence)
    for a, b, sequence in inputs
]

print(f"* Exercise 2 *******************************************")
print(f"Input\tExpected output\t\tOutput")
for inp, out, result  in zip(inputs, expected_outputs, results):
    print(f"{inp}\t\t\t\t{out}\t\t{result}\t")
print(f"********************************************************\n\n\n")

#############################################################################
# Esercizio 3 ###############################################################
#############################################################################
inputs = [
    ("", "", "", ""),
    ("", "C", "", ""),
    ("", "", "C", ""),
    ("A", "C", "", ""),
    ("A", "A", "A", "AA"),
    ("A", "A", "A", "AAA"),
    ("A", "B", "C", "ABC"),
    ("A", "C", "Z", "ABTCSAZ"),
    ("A", "C", "Z", "ABTZCSA"),
    ("C", "A", "Z", "ABTCSATZ"),
    ("C", "A", "Z", "ZABTCSAT"),
    ("G", "T", "Z", "ACGAGGTAZC"),
    ("G", "T", "Z", "ACGZAGGTAC"),
    ("G", "C", "Z", "ACGAGGTACZ"),
    ("G", "C", "Z", "ACGAGZGTAC"),
]
expected_outputs = [
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
]
results = [
    sequence_triple(a, b, c, sequence)
    for a, b, c, sequence in inputs
]

print(f"* Exercise 3 *******************************************")
print(f"Input\tExpected output\t\tOutput")
for inp, out, result  in zip(inputs, expected_outputs, results):
    print(f"{inp}\t\t\t\t{out}\t\t{result}\t")
print(f"********************************************************\n\n\n")

#############################################################################
# Esercizio 4 ###############################################################
#############################################################################
inputs = [
    ("", "C"), False,
    ("C", ""), False,
    ("ABC", "ABC"), True,
    ("ACZ", "ABTCSAZCACZ"), True,
    ("ACZ", "ABTCSAZCAZZC"), False,
    ("GTZ", "ACGAGGTZAZC"), True,
    ("GTZ", "ACGZAGZGTAC"), False,
]
expected_outputs = [
    False,
    False,
    True,
    True,
    False,
    True,
    False
]
results = [
    is_in_sequence(s, sequence)
    for s, sequence in inputs
]

print(f"* Exercise 4 *******************************************")
print(f"Input\tExpected output\t\tOutput")
for inp, out, result  in zip(inputs, expected_outputs, results):
    print(f"{inp}\t\t\t\t{out}\t\t{result}\t")
print(f"********************************************************\n\n\n")