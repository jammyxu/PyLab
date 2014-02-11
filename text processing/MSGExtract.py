#!/usr/bin/python  
# coding: UTF-8 


# MSGExtract function read content from input file, according rule extract key imformation to a CVS file.
def MSGExtract(InputPath, OutputPath):
	try:
		InputHandle=open(InputPath,"r")
	except:
		print "fail to open file"
		return

	try:	
		content=InputHandle.read() #read content into memory
	except:
		print "fail to read file"
		return 
	finally:
		InputHandle.close()

	lines=content.splitlines()

	try:
		OutputHandle=open(OutputPath,'a')
	except:
		print "fail to open output file"
		return 

	for line in lines:
		TmpArray=line.split('|')
		if TmpArray[-11]=='10295107' and TmpArray[1]=="2003" and TmpArray[5]=="12": # extract rule
			OutputHandle.write(line.replace("|",",")+"\n")


	OutputHandle.close()
	print "success!"

if __name__=="__main__":
	MSGExtract("bill-2014-01-24-20.dat","C:\\test6.csv")


