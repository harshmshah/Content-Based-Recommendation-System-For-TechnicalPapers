import shutil, sys ,os

''' function: moveFiles
	Arguments: src -> path to the nested source directory from where files need to be extracted.
			   dest -> path to the EXISTING destination directory to where the files are to be copied.
	Returns: void
'''

def moveFiles(src,dest):
	if(os.path.isdir(src)):
		dirList = os.listdir(src)
		for df in dirList:
			new_path = src + "/" + df
			moveFiles(new_path,dest)
	else:
		shutil.copy2(src,dest)


if __name__ == "__main__":
	srcPath = sys.argv[1]
	destPath = sys.argv[2]

	moveFiles(srcPath,destPath)


