import re
import datetime

start_time=datetime.datetime.now()
print('Start time: ',start_time)

with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input:
    lines=input.read()
with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/tata_genes.fa','w') as output:

    tata=r'TATA[AT]A[AT]'

        
    lines_merged=re.sub('\n','',lines)
    lines_processed=re.sub(r'(?=>)','\n',lines_merged)
    lines_processed=re.sub(r'\n','',lines_processed,count=1)
    lines_processed=lines_processed.split('\n')

    tata_genes=[]
    for line in lines_processed:
        if re.search(tata,line):
            gene_names=re.findall(r'gene:(\S+)',line)
            gene_sequences=re.findall(r'](.+)',line)
            tata_genes.append([gene_names[0],gene_sequences[0]])
        
    for line in tata_genes:
        output.write(line[0]+'\n'+line[1]+'\n')

end_time=datetime.datetime.now()
print('End time: ',end_time)
print('Total duration: ',end_time-start_time)
