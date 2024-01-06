# Asks for the input of a FASTA file
print("Import your FASTA file, and after enter type #")
fasta_file = ""


# To be able to read multiple line that have "enter", as someone would have inputted the FASTA file, until the "#"
# that the user has entered
while True:
    line = raw_input()
    if line.strip() == "#":
        break

    fasta_file += line + "\n"


# Storing every line, so we can latter subtract only the amino acid sequence.
lines = fasta_file.split("\n")
protein_sequences = []
current_sequence = ""


# Reads through the lines and stores only the amino acid sequences found after the ">" sequences, and combines all them
# in a single sequence.
for line in lines:
    if line.startswith(">"):
        x = 0
    else:
        current_sequence += line.strip()

protein_sequences.append(current_sequence)



# Joins the list in order to look better, and also adds a "*", used later in the code to understand when the
# protein sequence has ended.
final_protein_sequence = ''.join(protein_sequences) + "*"
print("Protein Sequence:", final_protein_sequence)


# A dictionary of the hydrophobic scale of amino acids, using one-letter code for the keys and the
# numbers of the hydrophobic scale as values
amino_acid_hydrophobic_scale = {
    "A": 0.616, "C": 0.680, "D": 0.028, "E": 0.043, "F": 1.000,
    "G": 0.501, "H": 0.165, "I": 0.943, "K": 0.283, "L": 0.943,
    "M": 0.738, "N": 0.236, "P": 0.711, "Q": 0.251, "R": 0.000,
    "S": 0.359, "T": 0.450, "V": 0.825, "W": 0.878, "Y": 0.880
}


# From literature the amino acids grouped as hydrophobic are the following: Phenylalanine(F), Leucine(L),
# Isoleucine(I), Tyrosine(Y), Tryptophan(W), Valine(V), Methionine(M), Proline(P), Cysteine (C), and Alanine(A)
# so a score >= 0.616

# Function that accesses if the amino acid is hydrophobic or not,and returns "H"
# if it is and "N" if it is not, using the hydrophobic dictionary created.
def hydrophobic_acid(amino_acid):
    nature_of_acid = amino_acid_hydrophobic_scale[amino_acid]

    if nature_of_acid >= 0.616:
        return "Y"
    else:
        return "N"


# A function that finds if there are hydrophobic sequences that are at least 7 amino acid long. From literature, the amino acid sequence should be at least
# 15 amino acid long to cross the membrane, but this is a very strict parameter for continuous hydrophobic amino acids so a score of 7 will be used.
def find_hydrophobic_sequences(sequence):
    # A variable i is used to stop the while when "*" is read.
    i = 1
    while i > 0:
        hydrophobic_sequence = []
        found_hydrophobic_sequence = []
        score = 0
        for amino_acid in final_protein_sequence:
            if amino_acid == "*":
                if len(found_hydrophobic_sequence) >= 7:
                    print(f"Found a possible transmembrane sequence: {found_hydrophobic_sequence}")
                    i = -1
                else:
                    i = -1
            elif hydrophobic_acid(amino_acid) == "N":
                hydrophobic_sequence = []
                score = 0
                if len(found_hydrophobic_sequence) != 0:
                    print(f"Found a possible transmembrane sequence: {found_hydrophobic_sequence}")
                    found_hydrophobic_sequence = []
                    hydrophobic_sequence = []
            elif hydrophobic_acid(amino_acid) == "Y":
                hydrophobic_sequence.append(amino_acid)
                score += 1
                if score >= 7:
                    found_hydrophobic_sequence = hydrophobic_sequence
                    found_hydrophobic_sequence = " ".join(found_hydrophobic_sequence)


# Calling the function that finds the hydrophobic sequences
find_hydrophobic_sequences(final_protein_sequence)


# Final check that a transmembrane sequence was found, and if not a text indicating the absence is printed
if final_protein_sequence is True:
    a = 1
else:
    print("No possible transmembrane sequences found")

