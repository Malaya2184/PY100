# # bio python version 1.78
# from  Bio.Seq import  Seq
# my_rna = Seq("GUCAUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAGUUG")
# my_aa = my_rna.translate()
# print(my_aa)
# for pep in my_aa.split("*"):
#     print(pep)

# Simple python program to count 
# occurrences of pattern in dna. 

# ==========================================================
def countFreq(pattern, dna): 
	M = len(pattern)
	N = len(dna)
	res = 0
	
	for i in range(N - M + 1): 
		j = 0
		while j < M: 
			if (dna[i + j] != pattern[j]): 
				break
			j += 1

		if (j == M): 
			res += 1
			j = 0
	return res 

if __name__ == '__main__': 
	dna = "TACCAGTUAGTACCUTTATACC"
	pattern = "TACC"
	print(countFreq(pattern, dna)) 

# ====================================================

