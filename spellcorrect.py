import sys	#import modules
import pickle
import difflib
import os.path

#method for creating a unique file
def uniq(wList): #takes as input a list of words
	uList={} #creates a new dictionary
	for i in wList:	#iterates through word list and sets word as a key in dictionary
		uList[i]="HA"
	return uList.keys()	#returns the keys of the dictionary... therefore only unique words

#checks
if len(sys.argv)!=3:	#check if threre are enough arguments in command line
	print "Error: Must follow the program name with 2 words!"
	sys.exit()
if not os.path.isfile("save.p"):	#check if the file exists
	print "Error: The pickled file does not exist!"
	sys.exit()

#store arguments from commandline as word1 and word2
word1=(sys.argv[1]).lower()
word2=(sys.argv[2]).lower()

#format 
d = pickle.load(open("save.p","rb"))
dk=[]
for i in d.keys():			#iterates over the keys of dictionary
	temp=i.replace("'","")		#removes the unnecessary characters
	temp=temp.replace("[","")
	temp=temp.replace("]","")
	temp=temp.replace(",","")
	dk+=temp.split()		#adds it to a new list, dk-->dictionary_keys
dk=uniq(dk)	#makes dk only contain unique words

#spell checker
spelt=False
for i in dk:	#iterates over words in dk to see if any match with word1
	if i==word1:
		spelt=True
		break

if spelt:	#will be true if there is a match
	print "The spelling of "+`word1`+" is correct"
else:	#else if no match
	wl=difflib.get_close_matches(word1, dk, 10)	#uses the difflib function
	if len(wl)>0:	#checks if there are any matches
		mKey=""
		mCount=0
		for i in wl:	#iterates through the matches to find most freqency pair
			key=str([i,word2])	#formats it to the format of the dictionary keys
			for k in d.keys():	#iterates over possible pairs
				if k==key and d[key]>mCount:	#checks if match + greatest count
					mKey=i
					mCount=d[key]
					break

		if mKey!="": #checks to make sure that there is a suggestion
			print "You wrote "+`sys.argv[1]`+'... did you mean '+`mKey`+'?'
		else:	#else no suggestions
			print "Nothing in the dictionary matches "+`sys.argv[1]`
	else:	#if no matches at all, print nothing in disctionary
		print "Nothing in the dictionary matches "+`sys.argv[1]`

