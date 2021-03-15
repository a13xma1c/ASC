import random
from concurrent.futures import ThreadPoolExecutor, as_completed

SAMPLE_LEN = 10000
NUM_SAMPLES = 420
SEED = 42069
MAX_WORKERS = 30


def find_sequence(dna, sequence, index):
    if dna[index].find(sequence) != -1:
        return "DNA sequence found in sample %s" % index

    return ""


if __name__ == "__main__":
    random.seed(SEED)

    dna = ["".join([random.choice("ATGC") for i in range(SAMPLE_LEN)]) for j in range(NUM_SAMPLES)]
    sequence = "TTGAACCTT"

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = [executor.submit(find_sequence, dna, sequence, i) for i in range(NUM_SAMPLES)]

        for res in as_completed(results):
            result_str = res.result()

            if result_str != "":
                print(result_str)
