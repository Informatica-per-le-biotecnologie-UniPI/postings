from postings import posting


inputs = [
    [],
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
