# function used to translate to aminoacid from DNA sequence
def DNA_translation(codingSequences):
    codon_table ={  'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
                    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
                    'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
                    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
                    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
                    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
                    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
                    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
                    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
                    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
                    'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
                    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
                    'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
                    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
                    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
                    'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
    Protein_sequence = ""
    for i in range(0,len(codingSequences),3):
        Protein_sequence += codon_table[codingSequences[i:i+3]]
    return Protein_sequence

# Filehandling
sequence_FileName = "SARS_CoV2_genome.fasta"
annotation_FileName = "GCF_009858895.2_ASM985889v3_genomic.gff"
sequence_FileHandle = open(sequence_FileName,'r')
annotation_FileHandle = open(annotation_FileName,'r')

#genome into a string convertion from data set
genome_sequence_string = ""
# I took i= 0 to drop the first line from the data set i.e sequence.fasta because it is not needed in our program
i = 0
for line in sequence_FileHandle:
    if(i!=0):
        line = line.strip()
        genome_sequence_string+=line
    i+=1

new_string =""

# Selecting the CDS sequences from the genome.
for line in annotation_FileHandle:
    if line[0] != '#':
        codingSequences = ""
        Protein_sequence = ""
        information_list = line.split()
        if information_list[2] == 'CDS' and int(information_list[3])== 21563 :
            if int(information_list[3])< 25385 :
                codingSequences = genome_sequence_string[int(information_list[3])-1:int(information_list[4])]
                Protein_sequence = DNA_translation(codingSequences)
                new_string += Protein_sequence


spike_list = list(new_string.split("*"))
new_string2= ""
for element in spike_list:
    new_string2 +=element

spike_list2 = list(new_string2)
# print(spike_list2[500])
if spike_list2[500] == "N":  spike_list2[500] = "Y"
# print(spike_list2[500])
if spike_list2[569] == "A":  spike_list2[569] = "D"
if spike_list2[613] == "D":  spike_list2[613] = "G"
if spike_list2[680] == "P":  spike_list2[680] = "H"
if spike_list2[715] == "T":  spike_list2[715] = "I"
if spike_list2[981] == "S":  spike_list2[981] = "A"
if spike_list2[1117] == "D": spike_list2[1117] = "H"
# print(len(spike_list2))
# print(spike_list2[68])
del spike_list2[68]
# print(spike_list2[68])
del spike_list2[68]
# print(spike_list2)
# print(spike_list2[68])
# print(len(spike_list2))
# print(spike_list)
# print(new_string2)
new_string3= ""
for element in spike_list2:
    new_string3 +=element

output_file = open("spikeee.fasta","w")
output_file.write(new_string3)
# print(new_string3)
output_file.close()
annotation_FileHandle.close()
sequence_FileHandle.close()
