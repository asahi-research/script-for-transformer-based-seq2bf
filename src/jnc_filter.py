#-*-coding:utf-8-*-

import json
import os
import random
import argparse
from collections import Counter

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str)
    parser.add_argument("--output_path", type=str)
    return parser.parse_args()

def make_pair(path, idx, dataset):
    kiji, midashi = [], []
    for d in idx:
        x = dataset[d]
        kiji.append(''.join(x['kiji']))
        midashi.append(x['midashi'])
    with open('{}_kiji.txt'.format(path), 'w') as f:
        f.write('\n'.join(kiji))
    with open('{}_midashi.txt'.format(path), 'w') as f:
        f.write('\n'.join(midashi))

def write_ids(path, data):
    with open(path, 'w') as f:
        f.write('\n'.join(data))

def make_dataset(lines, split_path, data_path):
    # remove duplicate kiji, midashi
    kiji_counts = Counter([''.join(line['kiji']) for line in lines])
    midashi_counts = Counter([ line['midashi'] for line in lines])
    IDs = []
    dataset = {}
    # sort
    lines = sorted(lines, key=lambda k: k['kijiid'])
    for line in lines:
        kiji = ''.join(line['kiji'])
        midashi = line['midashi']
        kijiid = line['kijiid']
        # Use only kiji and midashi appeared only once and exclude txt including '='
        if kiji_counts[kiji] == 1 and midashi_counts[midashi] == 1 and '=' not in kiji:
            IDs.append(kijiid)
            dataset[kijiid] = line
            
    random.seed(0)        
    random.shuffle(IDs)
    
    # data split
    train_size = int(len(IDs) * 0.98)
    holdout_size = int((len(IDs) - train_size) / 2)
    train = IDs[:train_size]
    valid = IDs[train_size:-holdout_size]
    test = IDs[-holdout_size:]
    print('total size: {}'.format(len(IDs)))
    print('size of train: {} valid: {} test: {}'.format(len(train), len(valid), len(test)))
    # write
    if not os.path.exists(split_path):
        os.mkdir(split_path)
    write_ids(os.path.join(split_path, 'train.txt'), train)
    write_ids(os.path.join(split_path, 'valid.txt'), valid)
    write_ids(os.path.join(split_path, 'test.txt'), valid)
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    split = [(os.path.join(data_path, 'train'), train), 
             (os.path.join(data_path, 'valid'), valid),
             (os.path.join(data_path, 'test'), test)]
    for s in split:
        path, data = s
        make_pair(path, data, dataset)

if __name__ == '__main__':

    args = parse_arg()  
    INPUT_PATH = args.input_path
    OUTPUT_PATH = args.output_path
    
    with open(INPUT_PATH) as f:
        lines = [json.loads(s.strip()) for s in f.readlines()]
    print('json lines {}'.format(len(lines)))
    
    if not os.path.isdir(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    make_dataset(lines, OUTPUT_PATH+'split', OUTPUT_PATH+'data_pair')
