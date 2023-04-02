import os
import subprocess
import pytest
import io,sys
import __MODULE_NAME__ as module #ignore error (used as place holder")

module_name = "__MODULE_NAME__"#ignore error (used as place holder")
dir_path = os.path.dirname(os.path.abspath(__file__))

expected_output_file = "_expected_output.txt"

#tests the output of the module(file) not contained in a function definition
def test_module_output():
  
  file_name =os.path.join(dir_path,f"{module_name}.py") 
  

  expected_output = os.path.join(dir_path,expected_output_file) #used to store the output to check against
  #expect_output = "Output Place Holder" #used with short outputs

  result = subprocess.run(["python", file_name], stdout=subprocess.PIPE,stderr = subprocess.PIPE, text = True)

  with open(expected_output, "r") as f:
    expected = f.read()

#ignore above ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#assertions===========================================================================================================================================
  assert result.stdout.strip() == expected.strip()

def test_function_output():

  #test that the function definition is present in module
  assert hasattr(module, 'print_fun'), "'print_fun' function definition not found"
  

  #test printed output of a function

  #expected_output = os.path.join(dir_path, expected_output_file) #used to store the output to check against
  expected_output = "Hello World" #used with short outputs 
  #NOTE: expected output should include any newline characters \n


  captured_output = io.StringIO()
  sys.stdout = captured_output

  module.print_fun() #change to function name

  sys.stdout = sys.__stdout__
#ignore above ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#assertions===========================================================================================================================================
  assert captured_output.getvalue().strip() == expected_output.strip(), f"Expected {expected_output}, but got {captured_output.getvalue()}"

def test_function_return():

#ignore above ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#assertions===========================================================================================================================================
  assert module.return_fun() == "Hello World"

  assert module.add_example(2,2) == 4
  assert module.add_example(3,-3) == 0
  assert module.add_example(-4,-9) == -13









