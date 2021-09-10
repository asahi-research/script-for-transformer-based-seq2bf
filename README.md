# script-for-transformer-based-seq2bf

This is a repository for Transformer-based Lexically Constrained Headline Generation (EMNLP'21). In this repository, we provide the script to preprocess Japanese News Corpus (JNC) and split them into train/valid/test sets. You can get JNC for a fee ([more details](https://cl.asahi.com/api_data/jnc-jamul-en.html)). Note that we use the 2019 version of the JNC.

## Usage

```bash
sh run.sh
```

### Example of run.sh

```bash
python ./src/jnc_filter.py \
    --input_path ./data/JNC-corpus.json \
    --output_path ./output/
```

## Check dataset

The results of the data splitting in our paper are shown in the directory `ids`. Please use it to check the processing results.
