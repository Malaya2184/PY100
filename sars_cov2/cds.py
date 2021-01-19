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
sequence_FileName = "sequence.fasta"
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

protein_fhand = open("protein_CDS.fasta",'w')
# Selecting the CDS sequences from the genome.
for line in annotation_FileHandle:
    if line[0] != '#':
        codingSequences = ""
        Protein_sequence = ""
        information_list = line.split()
        if information_list[2] == 'CDS':
            codingSequences = genome_sequence_string[int(information_list[3])-1:int(information_list[4])]
            Protein_sequence = DNA_translation(codingSequences)

            prot_id = information_list[8].split(";") #ProtID of the protein

            # Writing onto the fasta file
            protein_fhand.write('===>'+ prot_id[0]+'\n'+ '-------------------------------\n' +Protein_sequence+'\n\n\n\n')

annotation_FileHandle.close()
sequence_FileHandle.close()
protein_fhand.close()
