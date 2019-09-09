# -*- coding: utf-8 -*-
import json

def test(input_relative_file='train_relative.json', input_target_file='train.json'):
    input_relative = []
    for item in open(input_relative_file, 'r'): 
        input_relative.append(json.loads(item))
    input_target = []
    for item in open(input_target_file, 'r'):
        input_target.append(json.loads(item))
    output_relative = []
    output_target = []
    for x in input_target:
        for y in input_relative:
            if x['doc_token'] == y['doc_token']:
                output_relative.append(y)
                output_target.append(x)
                continue
    print(output_relative[0])
    print(output_target[0])
    with open('train_relative_v2.json', 'w') as f:
        for i in range(len(output_relative)):
            f.write(json.dumps(output_relative[i]))
            f.write('\n')

    with open('train_target_v2.json', 'w') as f:
        for i in range(len(output_target)):
            f.write(json.dumps(output_target[i]))
            f.write('\n')

    print(len(output_target))
    print(len(output_relative))

def count_token_num(input_file_path='train_target_v2.json'):
    output_sentence = []
    for item in open(input_file_path, 'r'):
        output_sentence.append(len(json.loads(item)['doc_token']))
    print(float(sum(output_sentence))/float(len(output_sentence)))

def select_data(input_relative_file='train_relative.json'):
    input_relative = []
    for item in open(input_relative_file, 'r'): 
        input_relative.append(json.loads(item))
    output_relative = input_relative[:10000]
    with open('train_relative_10000.json', 'w') as f:
        for i in range(len(output_relative)):
            f.write(json.dumps(output_relative[i]))
            f.write('\n')

def save_json(input_list, output_file):
    with open(output_file, 'w') as f:
        for i in range(len(input_list)):
            f.write(json.dumps(input_list[i]))
            f.write('\n')

def change_train_data_scale(input_file_path='train_relative.json'):    
    output_sentence = []
    for item in open(input_file_path, 'r'):
        output_sentence.append(json.loads(item))
    output1 = output_sentence[:20000]
    save_json(output1, 'train_relative_20000')
    output2 = output_sentence[:30000]
    save_json(output2, 'train_relative_30000')
    output3 = output_sentence[:40000]
    save_json(output3, 'train_relative_40000')
    output4 = output_sentence[:50000]
    save_json(output4, 'train_relative_50000')
    output5 = output_sentence[:60000]
    save_json(output5, 'train_relative_60000')

def change_train_relative_target(input_file_path='train_relative.json'):
    symptom_list = ['腹痛', '头痛', '疼痛', '胸痛', '腰痛', '咽喉痛', '肢体疼痛', '牙痛', '头晕', '发热', '关节疼痛', '背痛', '腹胀', '尿痛', '下腹痛', '痛风', '无力', '感冒', '咳嗽', '呕吐', '腹泻', '恶心', '全身酸痛', '腰酸', '失眠', '尿频', '便秘', '胸闷', '眼痛']    
    input_sentence = []
    for item in open(input_file_path, 'r'):
        temp = json.loads(item)
        temp_token = ' '.join(temp["doc_token"])
        temp_label = [i for i in symptom_list if i in temp_token]
        if temp_label:
            temp["doc_label"] = temp_label
            input_sentence.append(temp)
    save_json(input_sentence, 'train_relative_10000_rule')


if __name__=="__main__":
    #test()
    #count_token_num()
    #select_data()
    #change_train_data_scale()
    change_train_relative_target()

