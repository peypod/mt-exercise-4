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
MILLISECONDS=0

model_name=transformer_denl_config_bpe_smaller_voc

#ckpt=models/transformer_denl/53000.ckpt
#ckpt=models/transformer_denl_bpe/91000.ckpt
ckpt=models/transformer_denl_bpe_smallvoc/105500.ckpt

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name

mkdir -p $translations_sub

for beam in 1 2 3 4 5 6 7 8 9 10; do

    echo "#### BEAM SIZE: $beam ####"
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python -m joeynmt translate --ckpt $ckpt $configs/$model_name.b_$beam.yaml < $data/test.$src > $translations_sub/test.$model_name.b_$beam.$trg 


    # Clean up encoding output of joeynmt
    iconv -f utf-8 -t utf-8 -c "$translations_sub/test.$model_name.b_$beam.$trg" > temp.cleaned.out
    dos2unix temp.cleaned.out

    # compute case-sensitive BLEU 
    sacrebleu "$data/test.$trg" < temp.cleaned.out >> $translations/b_$beam.txt
    #sacrebleu $data/test.$trg < $translations_sub/test.$model_name.$trg

    echo $SECONDS > b_ts_$beam.txt
    echo $MILLISECONDS > b_tms_$beam.txt


    done

echo "time taken:"
echo "$SECONDS seconds"

