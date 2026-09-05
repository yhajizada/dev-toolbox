import json
import csv
import sys

def convert_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            data = [data]
            
        if not data:
            print("[-] JSON file is empty.")
            return

        keys = data[0].keys()
        
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
            
        print(f"[+] Successfully converted {json_file_path} to {csv_file_path}")
    except Exception as e:
        print(f"[-] Error during conversion: {e}")

if __name__ == "__main__":
    print("JSON to CSV converter utility ready.")