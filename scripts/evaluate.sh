#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/sampled_data
configs=$base/configs

translations=$base/translations

mkdir -p $translations

src=de
trg=nl


num_threads=4
device=0,1


# measure time

SECONDS=0

model_name=transformer_denl_config_bpe_smaller_voc

#ckpt=models/transformer_denl/53000.ckpt
#ckpt=models/transformer_denl_bpe/91000.ckpt
ckpt=models/transformer_denl_bpe_smallvoc/105500.ckpt

#torch.load("D:/CL/mt-exercise-4/models/transformer_denl/53000.ckpt", map_location="cpu")

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name

mkdir -p $translations_sub


CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate --ckpt $ckpt $configs/$model_name.yaml < $data/test.$src > $translations_sub/test.$model_name.$trg


# Clean up encoding
iconv -f utf-8 -t utf-8 -c "$translations_sub/test.$model_name.$trg" > temp.cleaned.out
dos2unix temp.cleaned.out

# compute case-sensitive BLEU 
sacrebleu "$data/test.$trg" < temp.cleaned.out
#sacrebleu $data/test.$trg < $translations_sub/test.$model_name.$trg

echo "time taken:"
echo "$SECONDS seconds"

#CUDA_VISIBLE_DEVICES=1 OMP_NUM_THREADS=4 python -m joeynmt translate configs/transformer_denl_config.yaml < sampled_data/test.de > translations/test.transformer_denl_config.nl
