import sys
import json
import spacy
nlp = spacy.load("en_core_web_sm")
import mining_literature

disease_info = { 'coronavirus':'Coronavirus',
                 'coronaviruses':'Coronavirus',
                 'sars-coronavirus':'SARS',
                 'SARS':'SARS',
                 'sars-cov':'SARS',
                 'MERS':'MERS',
                 'mers-coronavirus':'MERS',
                 'mers-cov':'MERS',
                 'HIV':'HIV',
                 'human immunodeficiency virus':'HIV',
                 'viral pneumonia':'Viral Pneumonia'
                }

if __name__ == "__main__":

    for line in open(sys.argv[1]):
        line = json.loads(line.strip())
        if len(line['gene']) == 0:
            continue
    
        pmid = line['path'].split('/')[-1].replace('.xlm','')
        gene_list = line['gene']
        disease_list = line['disease']

        documentx = nlp(line['abstract'])
        for sentx in documentx.sents:
            sentx = str(sentx)
            for disease in disease_list:
                if disease.lower() == disease:
                    for gene in gene_list:
                        if mining_literature.in_string_en2(disease,sentx) and mining_literature.in_string_en2(gene,sentx,ignore_case=False):
                            print('\t'.join([disease_info[disease],gene,pmid,sentx]))
                if disease.lower() != disease:
                    for gene in gene_list:
                        if mining_literature.in_string_en2(disease,sentx,ignore_case=False) and mining_literature.in_string_en2(gene,sentx,ignore_case=False):
                            print('\t'.join([disease_info[disease],gene,pmid,sentx]))
                    


