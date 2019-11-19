import pickle	#importing the modules I need
import sys
import os.path

if len(sys.argv)!=2:	#Checks to make sure that the input from command line is valid
	print "Error: Must follow the program name with the name of a text file!"
	sys.exit()
if not os.path.isfile(sys.argv[1]):	#check to see if file does not exist
	print "Error: The file does not exist"
	sys.exit()

fName=sys.argv[1]
doc = open(fName, "r")	#open file
words = doc.read()	#get words from file
doc.close()		#close file
if words=="":		#check to see if there is anything in the file
	print "The file is empty!"
	sys.exit()

#reduce the words of a file to a list of words
DelChars = ["[","]","(",")",",",".",":",";","'","'",'"',"!"]
for i in DelChars:
	words=words.replace(i,"")

words=words.lower()
words=words.split()

#groups the words into a dictionary
i=0
d={}
while i<len(words)-1:	#first loop will iterate over all the words until the second last word
	key=str([words[i],words[i+1]])	#will set create a key for two words
	d2=d.keys()	#sets d2 as a list containing key values of the dictionary d
	if len(d2)>0:	#if there are words in d2 then 
		T=True
		for k in d2:	# then k will iterate through the list and check frequency of pairs
			if k==key:	#if pair is equal to the key
				d[key]+=1	#will count the frequency of the pair
				T=False
				break	#will break out of loop
		if T:
			d[key]=1
	else:	#will set the first key in the dictionary to point to a frequency of 1
		d[key]=1
	i+=1	#will increase the index i by 1 for the next loop

#output onto the command line
for i in d.keys():
	print i+" "+`d[i]`

pickle.dump(d, open("save.p","wb"))	#save the dictionary into a pickled file named "save.p"
