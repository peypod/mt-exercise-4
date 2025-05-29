import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("models/spm_model.model")

src_file = "data/train.en-it.en"
trg_file = "data/train.en-it.it"
max_len = 1000  # from your YAML

src_valid, trg_valid = 0, 0

with open(src_file, encoding="utf-8") as f:
    for line in f:
        tokens = sp.encode(line.strip(), out_type=str)
        if 0 < len(tokens) <= max_len:
            src_valid += 1

with open(trg_file, encoding="utf-8") as f:
    for line in f:
        tokens = sp.encode(line.strip(), out_type=str)
        if 0 < len(tokens) <= max_len:
            trg_valid += 1

print(f"Valid source sentences: {src_valid}")
print(f"Valid target sentences: {trg_valid}")