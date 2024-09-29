import os.path
import re

file_path = input("Enter the slurm out file name (Format: slurm-63344459): ") + ".out"
if os.path.isfile(file_path):
    with open(file_path, mode='r') as file:
            text = file.read()
    model_output_pattern = r"MODEL OUTPUT:\s(.{1,2})"
    correct_output_pattern = r"CORRECT OUTPUT:\s([A-D]{1})"
    model_outputs = re.findall(model_output_pattern, text)
    correct_outputs = re.findall(correct_output_pattern, text)

    if len(model_outputs) != len(correct_outputs):
        raise ValueError("Lists must have the same length")
   
    correct_predictions = sum(1 for a, p in zip(model_outputs, correct_outputs) if a == p)
    accuracy = correct_predictions / len(correct_outputs)

    print("Correct Predictions: ", + correct_predictions)
    print("Total Predictions: ", + len(correct_outputs))

    print(model_outputs)
    print(correct_outputs)

    print("Accuracy: ", + accuracy) 

else:
    print("Filename not found in this directory")
