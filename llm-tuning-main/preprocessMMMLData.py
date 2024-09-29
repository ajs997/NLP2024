import csv
import json
import os

csv_directory= "data/MMML/test"
data = []

for filename in os.listdir(csv_directory):
     if filename.endswith('.csv'):
        print("Processing: ",filename)
        csv_file_path = os.path.join(csv_directory, filename)
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                question_data = {
                    "instruction": "Which is the correct answer for the input question? Display the correct answer from the options.",
                    "input": row[0],
                    # "options": [f"A. {row[1]}", f"B. {row[2]}", f"C. {row[3]}", f"D. {row[4]}"],
                    "options": f"#{row[1]} #{row[2]} #{row[3]} #{row[4]}",
                    "output": row[5]
                }
                data.append(question_data)

json_data = json.dumps(data, indent=4)

jsonname = csv_directory.split('/')[-1]
with open('data/MMML/out_preprocess/' + jsonname + '.json', 'w') as json_file:
    json_file.write(json_data)

print("CSV data has been successfully converted to JSON and saved to 'dev.json'.")
