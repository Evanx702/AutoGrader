import os
import subprocess
import pytest
import io,sys
import __MODULE_NAME__ as module #ignore error

module_name = "__MODULE_NAME__"#ignore error

def test_module():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_name =os.path.join(dir_path,f"{module_name}.py") 
   
  
    expected_output = "expected_output.txt"

    result = subprocess.run(["python", file_name], stdout=subprocess.PIPE,stderr = subprocess.PIPE, text = True)

    with open(expected_output, "r") as f:
      expected = f.read()
    assert result.stdout.strip() == expected.strip()

def test_function():
  
  #test that function is present in module
  assert hasattr(module, 'my_fun'), "No 'my_fun' function found"
  
  #test function that prints output
  expected_output = "Hello World" #expected output should include any newline characters \n
  captured_output = io.StringIO()
  sys.stdout = captured_output
  module.my_fun()
  sys.stdout = sys.__stdout__
  assert captured_output.getvalue().strip() == expected_output.strip(), f"Expected {expected_output}, but got {captured_output.getvalue()}"