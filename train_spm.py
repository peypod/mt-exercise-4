import sentencepiece as spm

spm.SentencePieceTrainer.Train(
    input="data/train.de-nl.de,data/train.de-nl.nl",
    model_prefix="models/spm_model",
    vocab_size=2000,
    character_coverage=1.0,
    model_type="unigram"
)