#!/bin/bash

# Path to the Python program
PYTHON_PROGRAM="python t5.py"

# Test cases
for i in {1..9}; do
  input_file="testes/arq0${i}.in"
  output_file="testes/arq${i}.res"
  res_file="testes/arq0${i}.out"

  # Execute the Python program with the current input file and save output to a file
  $PYTHON_PROGRAM < "$input_file" > "$output_file"

  # Print the test case number
  echo "Test Case $i:"
  echo "================"

  # Display the output
  echo "Output:"
  cat "$output_file"
  echo

  echo "Res: "
  cat "$res_file"
  echo
  # Add a separator between test cases
  echo "--------------------"
done
