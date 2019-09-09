# -*- coding: utf-8 -*-

import torch

def save_data():
    temp_label = [x.strip().split()[0] for x in open('/users3/xmshi/tools/NeuralNLP-NeuralClassifier/dict_symptom_relative/doc_label.dict', 'r').read().strip().split('\n')]
    temp_label = dict(zip(temp_label, list(range(len(temp_label)))))
    torch.save(temp_label, '/users3/xmshi/tools/NeuralNLP-NeuralClassifier/dict_symptom_relative/label_map.dict')
    print(len(temp_label))
    temp_token = [x.strip().split()[0] for x in open('/users3/xmshi/tools/NeuralNLP-NeuralClassifier/dict_symptom_relative/doc_token.dict', 'r').read().strip().split('\n')]
    token_map = dict(zip(temp_token, list(range(len(temp_token)))))
    torch.save(token_map, '/users3/xmshi/tools/NeuralNLP-NeuralClassifier/dict_symptom_relative/token_map.dict')
    print(len(token_map))

def view(input_file='token_map.dict'):
    a = torch.load(input_file)
    print(a)

if __name__=="__main__":
    save_data()
    #view()