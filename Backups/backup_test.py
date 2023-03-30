import os
import subprocess
import importlib
import pytest
import io,sys
from main import modules
from main import N

def test_module():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_name =os.path.join(dir_path,f"{modules[N.file_num]}.py") 
   
  
    expected_output = "expected_output.txt"

    result = subprocess.run(["python", file_name], stdout=subprocess.PIPE, text = True)

    with open(expected_output, "r") as f:
      expected = f.read()
    assert result.stdout.strip() == expected.strip()

def test_function():
  module = importlib.import_module(modules[N.file_num])
  
  #test that function is present in module
  assert hasattr(module, 'my_fun'), "No 'my_fun' function found"
  
  #test function that prints output
  expected_output = "Hello World" #expected output should include any newline characters \n
  captured_output = io.StringIO()
  sys.stdout = captured_output
  module.my_fun()
  sys.stdout = sys.__stdout__
  assert captured_output.getvalue().strip() == expected_output.strip(), f"Expected {expected_output}, but got {captured_output.getvalue()}"