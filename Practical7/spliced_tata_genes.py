import re

with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input_file:
    lines=input_file.read()

splice_combination=input("Enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC):")
if splice_combination not in ['GTAG','GCAG','ATAC']:
    print('Invalid combination. Please enter GTAG, GCAG, or ATAC.')
else:
    with open(f'/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical7/{splice_combination}_spliced_genes.fa','w') as output:
        tata=r'TATA[AT]A[AT]'
        splice_donor=splice_combination[0:2]
        splice_acceptor=splice_combination[2:4]
           
        lines=re.sub(r'_mRNA.+?]','',lines)
        lines=re.sub(r' cdna.+?]','',lines)     
        lines_merged=re.sub('\n','',lines)
        lines_processed=re.sub(r'(?=>)','\n',lines_merged)
        lines_splited=re.sub(r'>(.{7})',r'>\1\n',lines_processed)
        lines_splited=re.sub(r'^\n','',lines_splited)
        lines_splited=lines_splited.split('\n')
        gene=[]

        for line in lines_splited:
                if line[0]=='>':
                    gene_names=line[0:8]
                else:
                    if re.findall(rf'{splice_donor}.+{splice_acceptor}',line):
                        sequences=re.findall(rf'{splice_donor}.+{splice_acceptor}',line)
                        sequences=str(sequences)
                        if re.findall(tata,sequences):
                            count=len(re.findall(tata,sequences))
                            count=str(count)
                            gene.append([gene_names,count,sequences])
                            
        for line in gene:
            output.write(line[0]+' tata_count:'+line[1]+'\n'+line[2]+'\n')

    
