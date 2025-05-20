# import pandas as pd
# import jsonlines

# # Load the CSV file
# csv_file_path = "test.csv"  # Replace with your CSV file path
# csv_data = pd.read_csv(csv_file_path)

# # Initialize lists to store data from JSONL files
# texts = []
# sub_labels = []

# # List of JSONL file paths
# jsonl_files = ["mild_test.jsonl", "noise_test.jsonl", "word_salad_test.jsonl"]  # Replace with your JSONL file paths

# # Read JSONL files and extract 'text' and 'sub_label'
# for file_path in jsonl_files:
#     with jsonlines.open(file_path) as reader:
#         for obj in reader:
#             texts.append(obj["text"])
#             sub_labels.append(obj["label"]["sub_label"])

# # Create a DataFrame from the extracted data
# jsonl_data = pd.DataFrame({"text": texts, "label": sub_labels})

# # Append JSONL data to the CSV data
# updated_csv_data = pd.concat([csv_data, jsonl_data], ignore_index=True)

# # Save the updated DataFrame back to a CSV file
# updated_csv_file_path = "updated_csv_file_test.csv"  # Replace with your desired output file path
# updated_csv_data.to_csv(updated_csv_file_path, index=False)

# print(f"Updated CSV file saved at {updated_csv_file_path}")



import json
import csv

# Input and output file paths
input_file = 'dataset/train/toxicity.jsonl'  # Replace with your JSONL file
output_file = 'dataset/train/converted_csv/toxicity.csv'  # Desired CSV output file

# Open the files
with open(input_file, 'r') as jsonl_file, open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    # CSV writer setup
    csv_writer = csv.writer(csv_file)
    
    # Write header to the CSV file
    csv_writer.writerow(['text', 'label'])
    
    for line in jsonl_file:
        line = line.strip() 
        if not line:  
            continue
        try:
            json_obj = json.loads(line)  
            csv_writer.writerow([json_obj['toxic_comment'], 'toxicity']) 
        except json.JSONDecodeError as e:
            print(f"Skipping invalid JSON line: {line}")
            continue

print(f"Conversion complete! File saved as {output_file}.")