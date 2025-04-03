import re

with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input:
    lines=input.read()
with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/tata_genes.fa','w') as output:

    tata=r'TATA[AT]A[AT]'

    lines=re.sub(r'_mRNA.+?]','',lines)
    lines=re.sub(r' cdna.+?]','',lines)     
    lines_merged=re.sub('\n','',lines)
    lines_processed=re.sub(r'(?=>)','\n',lines_merged)
    lines_processed=lines_processed.split('\n')

    gene=[]
    for line in lines_processed:
        if re.search(tata,line):
            gene.append(line)
        
    gene_str='\n'.join(gene)
    lines_splited=re.sub(r'>(.{7})',r'>\1\n',gene_str)

    output.write(lines_splited)
