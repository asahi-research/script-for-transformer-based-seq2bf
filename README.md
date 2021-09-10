# script-for-transformer-based-seq2bf

This is a repository for the Transformer-based Lexically Constrained Headline Generation (EMNLP'21). In this repository, we provide the script to preprocess the JNC corpus and split them into train/valid/test sets. Note that we use the 2019 version of the Japanese News Corpus (JNC). You can can get the JNC corpus for a fee ([more details](https://cl.asahi.com/api_data/jnc-jamul-en.html)).

## Usage
```bash
sh run.sh
```

### Example of run.sh
```bash
python ./src/jnc_filter.py \
    --input_plain_path ./data/JNC-corpus.json \
    --output_path ./output/
```
