# -*- coding: utf-8 -*-
import json

def read_file():

    for line in open('test.json', 'r'):
    #for line in open('rcv1_dev.json'):
        print(line)
        
    '''
    a = dict()
    a['a'] = 1
    b = dict()
    b['b'] = 1
    all_dict = [a, b]

    output_file = open('test.json', 'w')
    for x in all_dict:
        output_file.write(json.dumps(x))
        output_file.write('\n')
    output_file.close()
    '''     

if __name__=="__main__":
    read_file()