import os.path	#importing the modules I need
import sys

if len(sys.argv)!=2:	#check to see if the there are 2 arguments from the command line
	print "Error: Must follow the program name with the name of a text file!"
	sys.exit()
else:
	fName=sys.argv[1]	#sets the name of the file as argv[1]

if os.path.isfile(fName):	#check to see if the file exists
	doc = open(fName, "r")	#Open the given file
	words = doc.read()	#read from the given file
	doc.close()		#Close the given file
	if words=="":		#check to see if there is anything in the file
		print "The file is empty!"
		sys.exit()

	#code to separate the words and get rid of symbols
	DelChars = ["[","]","(",")",",",".",":",";","'","'",'"',"!"]
	for i in DelChars:
		words=words.replace(i,"")

	words=words.lower()	#makes all words lower case
	words=words.split()	#splits the words into a list of words

	#code for dictionary
	d={}			#declare a dictionary d
	for i in words:
		count=0
		for j in words:
			if j==i:
				count=count+1
		d[i]=count	#fill dictionary with frequency of word

	#code for output
	for i in d.keys():
		output=i+" "+`d[i]`
		print output	#outputs dictionary to the command line
	sys.exit()
else:
	print "The file does not exist" #if the file does not exist, will exit the program
	sys.exit()
