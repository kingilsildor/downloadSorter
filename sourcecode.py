import sys, os, re, shutil

def get_files(path):
  print(f"Get all the files in {path}.")
  return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_dir(path):
  print(f"Get all the folders in {path}.")
  return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def get_file_extension(file):
    return re.search(r'\.([^\.]+)$', file).group(1)

def create_dir(path, extensions):
   for extension in extensions:
    new_dir = os.path.join(path, extension)
    if not os.path.isdir(new_dir):
      print(f"Make new folder for {extension}.")
      os.mkdir(new_dir)
    else:
       print(f"Folder for {extension} already exists.")

def move(source_path, destination_path):
  try:
    shutil.move(source_path, destination_path)          
    print(f"File moved from '{source_path}' to '{destination_path}' successfully.")
  except FileNotFoundError:
    print("Source file not found.")
  except PermissionError:
    print("Permission denied. Make sure you have the necessary permissions.")    
  except Exception as e:
    print(f"An error occurred: {e}")

def move_to_main(path, dirs):
   for dir in dirs:
      new_path = os.path.join(path, dir)
      for file in (os.listdir(new_path)):
        file_path = os.path.join(new_path, file)
        move(file_path, path)

def move_to_dir(files, dirs):
  for file in files:
    for dir in dirs:

      if get_file_extension(file) == dir:        
        source_path = os.path.join(path, file)
        destination_path = os.path.join(path, dir)
        move(source_path, destination_path)

  print(f"\nFiles succesfully moved!")

def exit(reason):
  if reason == 'no files':
    print("No files to move")

  if reason == 'finished':
    print("Sorting finished.")    

  input("Press Enter to exit.")
  sys.exit()

if __name__ == "__main__":
  path = input("Enter the file location you want to have sorterd. \nFor example C:\\Users\\NAME\\Downloads: \n")
  print(f"----------------------------------------------------")
  print(f"Code is running")
  print(f"----------------------------------------------------\n")

  files = get_files(path)  

  if len(files) == 0:
    exit('no files')
    
  file_extensions = {get_file_extension(f) for f in files}  
  create_dir(path, file_extensions)
  dirs = get_dir(path)
  move_to_dir(files, dirs)
  
  exit('finished')  
