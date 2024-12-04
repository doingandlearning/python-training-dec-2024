import os
import shutil

def organize_files(directory):
	 for filename in os.listdir(directory):
			if os.path.isfile(os.path.join(directory, filename)):
				file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension
				if file_extension:  # Skip files without an extension
					 dest_dir = os.path.join(directory, file_extension)
					 if not os.path.exists(dest_dir):
							os.makedirs(dest_dir)
					 shutil.move(os.path.join(directory, filename), os.path.join(dest_dir, filename))

if __name__ == "__main__":
	 organize_files("/Users/kevincunningham/code/indicia/edinburgh-uni-dec-2024/")