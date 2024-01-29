from Bio import SeqIO
import pandas as pd

def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences[record.id] = str(record.seq)
    return sequences

# Paths to the FASTA files
train_fasta_path = 'train/train_sequences.fasta'
test_fasta_path = 'test/testsuperset.fasta'

# Extract sequences
train_sequences = read_fasta(train_fasta_path)
test_sequences = read_fasta(test_fasta_path)


def read_annotations(file_path):
    annotations = pd.read_csv(file_path, sep='\t', header=None)
    
    # Check the number of columns and adjust accordingly
    num_cols = len(annotations.columns)
    if num_cols == 2:
        annotations.columns = ['Protein_ID', 'Annotation']
    elif num_cols == 3:
        annotations.columns = ['Protein_ID', 'Annotation', 'Additional_Info']
    else:
        raise ValueError(f"Unexpected number of columns ({num_cols}) in annotations file.")

    return annotations

annotations_path = 'train/train_terms.tsv'
annotations = read_annotations(annotations_path)

'''
# Define the path to the file
test_taxonomy_path = 'test/testsuperset-taxon-list.tsv'

# Define a function to read the file
def read_test_taxonomy(file_path):
    try:
        # Attempt to read the file with the specified encoding
        taxonomy = pd.read_csv(file_path, sep='\t', header=None, encoding='ISO-8859-1')
        taxonomy.columns = ['Protein_ID', 'Taxonomy']
        print("File read successfully with 'ISO-8859-1' encoding.")
        return taxonomy.head()  # Return the first few rows for inspection
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the function and print the output
read_test_taxonomy(test_taxonomy_path)
'''

def read_taxonomy(file_path, encoding='utf-8'):
    taxonomy = pd.read_csv(file_path, sep='\t', header=None, encoding=encoding)
    taxonomy.columns = ['Protein_ID', 'Taxonomy']
    return taxonomy

# Paths to the taxonomy files
train_taxonomy_path = 'train/train_taxonomy.tsv'
test_taxonomy_path = 'test/testsuperset-taxon-list.tsv'

# Extract taxonomy information with the correct encodings
train_taxonomy = read_taxonomy(train_taxonomy_path, encoding='utf-8')  # 'utf-8' for train_taxonomy.tsv
test_taxonomy = read_taxonomy(test_taxonomy_path, encoding='ISO-8859-1')  # 'ISO-8859-1' for testsuperset-taxon-list.tsv
