def sequence(file):
    lines=file.readlines()
    sequence=''
    for line in lines:
        if '>' not in line:
            sequence+=line.strip()
    return sequence

with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical13/BLOSUM62.txt','r') as blosum62:
    lines=blosum62.readlines()
    blosum62={}
    amino_acid_1s=lines[0].split()
    for line in lines[1:]:
        line=line.split()
        amino_acid_2=line[0]
        scores=line[1:]
        for amino_acid_1,score in zip(amino_acid_1s,scores):
            blosum62[amino_acid_1,amino_acid_2]=int(score)
        
def score(sequence1,sequence2):
    score=0
    for i in range (len(sequence1)):
        amino_acid_1=sequence1[i]
        amino_acid_2=sequence2[i]
        score+=blosum62[amino_acid_1,amino_acid_2]
    return score

def identity(sequence1,sequence2):
    identity=0
    for i in range (len(sequence1)):
        if sequence1[i]==sequence2[i]:
            identity+=1
    identity=(identity/len(sequence1))*100
    return identity

with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical13/P04179.fasta','r') as P04179:
    with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical13/P09671.fasta','r') as P09671:
        with open('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical13/random.fasta','r') as random:
            sequence_of_P04179=sequence(P04179)
            sequence_of_P09671=sequence(P09671)
            sequence_of_random=sequence(random)

score_of_P04179_compared_with_P09671=score(sequence_of_P04179,sequence_of_P09671)
score_of_P04179_compared_with_random=score(sequence_of_P04179,sequence_of_random)
score_of_P09671_compared_with_random=score(sequence_of_P09671,sequence_of_random)

identity_of_P04179_compared_with_P09671=identity(sequence_of_P04179,sequence_of_P09671)
identity_of_P04179_compared_with_random=identity(sequence_of_P04179,sequence_of_random)
identity_of_P09671_compared_with_random=identity(sequence_of_P09671,sequence_of_random)

print('Human SODM protein sequence is: ',sequence_of_P04179)
print('Mouse SODM protein sequence is: ',sequence_of_P09671)
print('Random protein sequence is: ',sequence_of_random)
print('Alignment of Human SODM protein sequence and Mouse SODM protein sequence: ')
print('BLOSUM62 score is: ',score_of_P04179_compared_with_P09671)
print('Rercentage identity is: ',identity_of_P04179_compared_with_P09671,'%')
print('Alignment of Human SODM protein sequence and random protein sequence: ')
print('BLOSUM62 score is: ',score_of_P04179_compared_with_random)
print('Rercentage identity is: ',identity_of_P04179_compared_with_random,'%')
print('Alignment of Mouse SODM protein sequence and random protein sequence: ')
print('BLOSUM62 score is: ',score_of_P09671_compared_with_random)
print('Rercentage identity is: ',identity_of_P09671_compared_with_random,'%')
               
               
               
                
        
