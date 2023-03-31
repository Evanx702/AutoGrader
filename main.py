import subprocess
import os,time
import datetime

dir_path = os.path.dirname(os.path.abspath(__file__))


graded_dir = os.path.join(dir_path, "Graded")
to_grade_dir = os.path.join(dir_path,"To_Grade")
tests_dir = to_grade_dir

test_file = "_test.py"
generic_test_file = "_generic_test.py"

def create_test_file(module_name):
  
  file_name = os.path.join(tests_dir,test_file) 
  with open(file_name, "r") as f:
    content = f.read()

  test_content = content.replace("__MODULE_NAME__", module_name)

  with open(file_name, "w") as f:
    f.write(test_content)

def rewrite_test_file():
  
  file_name = os.path.join(tests_dir,generic_test_file) 
  
  with open(file_name,"r") as f:
    content = f.read()

  file_name = os.path.join(tests_dir,test_file)
  with open(file_name,"w") as f:
    f.write(content)



modules = []
for filename in os.listdir(to_grade_dir):
  if filename.endswith('.py') and filename != test_file and filename != generic_test_file :
    module_name = os.path.splitext(filename)[0]
    modules.append(module_name)


for i,module in enumerate(modules):
  create_test_file(module)
   
  # The command to run
  file_name = os.path.join(tests_dir,test_file) 
  output_file = os.path.join(graded_dir,f"{module}.txt")
  
  #commands
  #command = f"pytest -vv {file_name} > {output_file}" #max verbosity
  command = f"pytest -vv --continue-on-collection-errors {file_name} > {output_file}" #continue even when assertions fail

  # Run the command
  print(f"====Running Tests on {module} ====\n{command}")
  # result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE,text = True)
  stdout, stderr = process.communicate()
  print(f"====Testing Completed on {module}====\n")
  
  #Wait
  time.sleep(1)

  with open(output_file, "r+") as f:
    content = f.read()
    f.seek(0,0)
    f.write(f"Name: {module}'s assignment\n")
    f.write(f"Date/Time: {datetime.datetime.now()}\n\n")
    f.write(content)


  rewrite_test_file() 
print("Grading Completed")
