import os

dir_path = os.path.dirname(os.path.abspath(__file__))
graded_path = os.path.join(dir_path, "Graded")

files = os.listdir(graded_path)

for file in files:
  file_path = os.path.join(graded_path, file)
  os.remove(file_path)

  

