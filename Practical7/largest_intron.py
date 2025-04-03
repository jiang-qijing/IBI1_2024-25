import re
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron=re.findall(r'GT.+AG',seq)
largest_intron_length=len(largest_intron[0])
print(f"The largest intron is:{largest_intron}")
print(f"The length of the largest intron is:{largest_intron_length}")
