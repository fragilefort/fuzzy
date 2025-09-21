import re


def main() -> None:
    file : str = r"./in.txt"
    seq_id: str
    gc_max_content: float
    seq_id, gc_max_content = max_gc(file)
    with open("./output.txt", "w") as o:
        o.write(f"{seq_id}\n{gc_max_content:.6f}\n")


def gc_content(sequence: str) -> float:
    matches = re.finditer(r"[GC]", sequence)
    # counting matches by giving every match a 1
    n_matches : int = sum(1 for _ in matches)
    return (n_matches / len(sequence)) * 100 if len(sequence) > 0 else 0.0


def max_gc(filepath : str) -> tuple[str, float]:
    max_gc : float = -1.0
    max_id : str = ""
    seq_id : str = ""
    seq: str = ""
    with open(filepath, "r") as f:
        for line in f:
            # Line is not empty
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                # process the previous sequence
                if seq:
                    gc : float = gc_content(seq)
                    if gc > max_gc:
                        max_gc = gc
                        max_id = seq_id
                    seq = ""
                seq_id = line[1:] # remove the >
            else:
                # Sequence is not complete
                seq += line
        # last sequence
        if seq:
            gc = gc_content(seq)
            if gc > max_gc:
                max_gc = gc
                max_id = seq_id
    return max_id, max_gc 


if __name__ == "__main__":
    main()
