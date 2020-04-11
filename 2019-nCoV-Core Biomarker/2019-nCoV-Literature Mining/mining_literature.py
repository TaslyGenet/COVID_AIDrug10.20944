import json
import os,sys
from xml.dom.minidom import parse
import xml.dom.minidom
import time
import re

def obtain_dir(number):
    number = int(number)
    if number%10000 == 0:
        number -= 1
    start = number-number%10000
    end = start + 10000
    start += 1
    return '%d_%d'%(start,end)

def in_string_en2(keyx,stringx,ignore_case=True):
    if ignore_case:
        keyx = keyx.lower()
        stringx = stringx.lower()

    if re.search("[^a-zA-Z0-9]%s[^a-zA-Z0-9]"%keyx,stringx) or re.search("^%s[^a-zA-Z0-9]"%keyx,stringx) or re.search("[^a-zA-Z0-9]%s$"%keyx,stringx):
        return True
    else:
        return False

if __name__ == "__main__":
    indir = 'literature_path'
    keys_list = [item.strip().lower() for item in open('virus.list')]
    keys_list1 = list(set(keys_list) - set(['sars', 'mers','hiv']))
    keys_list2 = [item.upper() for item in ['sars', 'mers','hiv']]
    # gene
    gene_list_all = []
    for line in open('Homo_sapiens.gene_info'):
        if line.startswith('#'):
            continue
        array = line.strip().split('\t')
        if array[9] != 'protein-coding':
            continue
        gene_list_all.append(array[2])
    
    gene_exclude = ['SARS','not','CI','TM','DBS','ART','VL','HCC','DES','HR','CAD','CS',
                    'TG','PPL','FH','C3','EMB','MB','SI','CP','DCK','F12','F5','F2','GC',
                    'PAH','MOS-HIV','MOS','TF','PC','C6','C2','C9']
    gene_list_all = list(set(gene_list_all) - set(gene_exclude))
    gene_list_all = [gene for gene in gene_list_all if len(gene)>1]

    for line in open('pmid.list'):
        array = line.strip().split('\t')
        pmid = array[0]
        current_file = os.path.join(indir,obtain_dir(pmid),'%s.xlm'%pmid)
        text_xlm = open(current_file).read().replace('\n','zzmtext')
        abstract_xlm = re.findall(u'<Abstract>(.+)</Abstract>',text_xlm)
        abstract = ''
        if len(abstract_xlm)!= 0:
            for each_line in abstract_xlm[0].split('zzmtext'):
                each_line = re.sub('<.*?>', '', each_line)
                each_line = each_line.strip()
                if each_line == '':
                    continue
                abstract += each_line + ' '
        
        disease_list = []
        for item in keys_list1:
            if in_string_en2(item,abstract):
                disease_list.append(item)
        for item in keys_list2:
            if in_string_en2(item,abstract,ignore_case=False):
                disease_list.append(item)
        
        gene_list = []
        for gene in gene_list_all:
            if gene in abstract:
                if in_string_en2(gene,abstract,ignore_case=False):
                    gene_list.append(gene)

        current_info = {'path':current_file,'abstract':abstract,'disease':disease_list,'gene':gene_list}
        if len(disease_list) > 0:
            print(json.dumps(current_info,ensure_ascii=False))
        
