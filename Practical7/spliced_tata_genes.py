import re
import datetime

start_time=datetime.datetime.now()
print('Start time: ',start_time)

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
           
        lines_merged=re.sub('\n','',lines)
        lines_processed=re.sub(r'(?=>)','\n',lines_merged)
        lines_processed=re.sub(r'\n','',lines_processed,count=1)
        lines_processed=lines_processed.split('\n')
        spliced_tata_genes=[]

        for line in lines_processed:
                if re.findall(rf'{splice_donor}.+{splice_acceptor}',line):
                    spliced_sequences=re.findall(rf'{splice_donor}.+{splice_acceptor}',line)
                    if re.findall(tata,spliced_sequences[0]):
                        count=len(re.findall(tata,spliced_sequences[0]))
                        gene_names=re.findall(r'gene:(\S+)',line)
                        gene_sequences=re.findall(r'](.+)',line)
                        spliced_tata_genes.append([gene_names[0],str(count),gene_sequences[0]])
                            
        for line in spliced_tata_genes:
            output.write(line[0]+' tata_count:'+line[1]+'\n'+line[2]+'\n')

end_time=datetime.datetime.now()
print('End time: ',end_time)
print('Total duration: ',end_time-start_time)                    

    
