'''
Original code by Arnab Borah.
Submission for Question.2 of FLNN assignment, Spring 2016.
'''

import numpy as np

def training():				#trains on patterns
	final_weights = np.zeros((35,35))
	patterns = []
	for g in range(4):
		fname = str(g+1)+'.txt'
		arr = np.loadtxt(fname)
		lol = []
		for k in range(7):
			megalol = arr[k]
			lol.extend(megalol)
		#print len(lol)
		patterns.append(lol)
		print 'one pattern trained!'
		for j in range(len(lol)):
			lol[j] = int(lol[j])	
		#print lol
		lol = np.matrix(lol)
		lolt = lol.T
		multx = np.dot(lolt,lol)
		final_weights = np.add(final_weights,multx)
	#print final_weights,'\n'
	return final_weights, patterns

def match_pattern(patx):			#matches a new pattern with an existing pattern
	for l in range(4):
		matchwith = patterns[l]
		if np.array_equal(matchwith,patx) == True:
			print 'matched with pattern ', l+1
			return l+1
	return 0
	
def check_pattern(patt):			#takes a pattern and computes its corresponding output 
	patt2 = np.matrix(patt)			#using weights computed in function 'training()'
	#print patt2.shape
	generated = []
	for t in range(35):
		hola = final_weights[:,t]
		hola2 = np.matrix(hola)
		#print hola2.shape
		matx = np.dot(patt2,hola2)
		#print 'mm>', matx
		if matx>0:
			generated.append(1)
		else:
			generated.append(-1)
	return generated
	
def check_newpattern(fnamex):				#directly checks if a pattern if present from file
	brr = np.loadtxt(fnamex)
	lol = []
	for k in range(7):
		megalol = brr[k]
		lol.extend(megalol)
	tacobell = check_pattern(lol)
	numx = match_pattern(tacobell)
	return numx
	
final_weights,patterns = training()
print '...trained on......',len(patterns),'patterns!'

correct = 0
for f in range(4):
	gotit = check_pattern(patterns[f])
	numx = match_pattern(gotit) 
	if numx!= 0:
		correct+=1
		print 'matched pattern',numx
print 'correct=',correct
if correct==4:
	print 'all trained patterns can be retrieved!\n\nSUCCESS!'
	
print '\n\n'
print 'matched',check_newpattern('2_distorted1.txt')			#one noise
print 'matched',check_newpattern('2_distorted2.txt')			#two noise

'''
ANSWER: Only one noise can be handled, because it gives a correct output with one noise. But wrong output with two noise!
'''