from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Phylo.Consensus import majority_consensus
from Bio import Phylo
from multiprocessing import Pool, cpu_count
import random
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


def bootstrap_tree_worker(seed, calculator, constructor, alignment):
    """Helper function to create a bootstrap tree with a given seed."""
    random.seed(seed)  # Set the seed for reproducibility

    # Convert alignment to a list of sequences as strings
    sequences = [str(record.seq) for record in alignment]

    # Sample the sequences with replacement
    sampled_sequences = random.choices(sequences, k=len(sequences))

    # Reconstruct the MultipleSeqAlignment object from sampled sequences
    sampled_alignment = MultipleSeqAlignment(
        [SeqRecord(Seq(seq), id=alignment[i].id) for i, seq in enumerate(sampled_sequences)]
    )

    return constructor.build_tree(sampled_alignment)


def bootstrap_trees_parallel(alignment, num_bootstrap, calculator, constructor):
    """Generate bootstrap trees in parallel."""
    num_cores = min(cpu_count(), 4)
    seeds = [random.randint(0, 2 ** 31) for _ in range(num_bootstrap)]

    # Use a Pool to parallelize the bootstrap tree construction
    with Pool(num_cores) as pool:
        trees = pool.starmap(bootstrap_tree_worker, [(seed, calculator, constructor, alignment) for seed in seeds])

    return trees


if __name__ == '__main__':

    alignment = AlignIO.read("Cleaned_MSA.fas", "fasta")

    calculator = DistanceCalculator('blosum62')
    constructor = DistanceTreeConstructor(calculator)

    trees = bootstrap_trees_parallel(alignment, 500, calculator, constructor)


    consensus_tree = majority_consensus(trees)


    Phylo.write(consensus_tree, "consensus_tree.nwk", "newick")
    print("Consensus tree saved to 'consensus_tree.nwk'")

