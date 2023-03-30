


import subprocess
import os,time


def create_test_file(module_name):
  dir_path = os.path.dirname(os.path.abspath(__file__))
  file_name = os.path.join(dir_path,"test.py") 
  with open(file_name, "r") as f:
    content = f.read()

  test_content = content.replace("__MODULE_NAME__", module_name)

  with open(file_name, "w") as f:
    f.write(test_content)

def rewrite_test_file():
  dir_path = os.path.dirname(os.path.abspath(__file__))
  file_name = os.path.join(dir_path,"backup_test.py") 
  
  with open(file_name,"r") as f:
    content = f.read()

  file_name = os.path.join(dir_path,"test.py")
  with open(file_name,"w") as f:
    f.write(content)



modules = []
for filename in os.listdir():
  if filename.endswith('.py') and filename != 'test.py' and filename != "main.py" and filename != "backup_test.py":
    module_name = os.path.splitext(filename)[0]
    modules.append(module_name)


for i,module in enumerate(modules):
  create_test_file(module)
   
  # The command to run
  dir_path = os.path.dirname(os.path.abspath(__file__))
  file_name = os.path.join(dir_path,"test.py") 
  output_file = os.path.join(dir_path, "Graded",f"{module}.txt")
  print(file_name)

  command = f"pytest -v  {file_name} > {output_file}"
  # command = f"pytest -v {file_name}"
  # Run the command
  print(f"Running command {command}")
  # result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE,text = True)
  stdout, stderr = process.communicate()
  print("Command Completed")
  
  #Wait
  time.sleep(1)

rewrite_test_file() 
