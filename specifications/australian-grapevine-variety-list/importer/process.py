import csv
import json
import urllib.request
import unicodedata

if __name__== "__main__":

    def find_longest_dict_keys_as_string(list_of_dicts):
        longest_length = 0
        longest_dict_keys = []
        for dictionary in list_of_dicts:
            if len(dictionary) > longest_length:
                longest_length = len(dictionary)
                longest_dict_keys = list(dictionary.keys())
        return longest_dict_keys

    def get_variety_list(url, output_path):
        try:
            with urllib.request.urlopen(url) as response:
                file_contents = response.read()

            with open(output_path, 'wb') as local_file:
                local_file.write(file_contents)

        except urllib.error.URLError:
            print("Error: There was an error downloading the file")
        except IOError:
            print("Error: There was an error writing the file")

    def extract_synonyms(dictionary):
        synonyms = []
        for key, value in dictionary.items():
            if "synonym" in key:
                synonyms.append(value)
        return synonyms

    def create_json_from_csv(path_to_csv_file, path_to_json_file):
        try:
            with open(path_to_csv_file, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                with open(path_to_json_file, 'w', encoding="utf-8") as json_file:
                    csv_data = []
                    id = 1
                    for row in csv_reader:
                        #Remove empty synonymns and throw them away
                        synonyms_list = extract_synonyms({k: v for k, v in row.items() if v})
                        #Filter out synonyms only
                        filtered_row = {key: value for key, value in row.items() if "synonym" not in key}
                        filtered_row['synonyms'] = [{'name': k, 'code': v} for k, v in zip(synonyms_list[::2], synonyms_list[1::2])]
                        
                        csv_data.append(filtered_row)
                    
                    json_file.write(json.dumps(csv_data, indent=4, ensure_ascii=False).encode('utf8').decode())

        except FileNotFoundError:
            print("Error: The CSV file could not be found")
        except IOError:
            print("Error: There was an error reading or writing to the file")

    def create_variety_list_csv_from_raw(label_input_path, bottle_input_path, output_path):
        try:
            bottle_details = {}

            #Get the full label list
            with open(bottle_input_path, 'r') as bottle_input_csv:
                csv_reader = csv.DictReader(bottle_input_csv)

                for row in csv_reader:
                    bottle_details[unicodedata.normalize("NFKD",row['Value']).rstrip()] = unicodedata.normalize("NFKD",row['Description']).rstrip()

            #Get the composition list and extract synonymns
            with open(label_input_path, 'r') as label_input_csv:
                csv_reader = csv.DictReader(label_input_csv)

                # Open the output CSV file and create a writer object
                with open(output_path, 'w', newline='',encoding="utf-8") as output_csv:
                    id = 1
                    csv_rows = []

                    # Iterate through the rows of the CSV
                    for row in csv_reader:
                        # Split the value field by '/'
                        synonyms = unicodedata.normalize("NFKD",row['Value']).rstrip().split('/')

                        #There is an unspecified entry in the list - catch it and throw it away
                        if str(synonyms[0]).lower() == 'unspecified':
                            continue

                        new_row = {'id': id, 'prime_name': synonyms[0]}

                        for i, synonym in enumerate(synonyms[1:]):
                            new_row[f'synonym_{i+1}'] = synonym
                            syn_code = bottle_details.get(synonym)

                            #If there is no code for some reason - catch it and throw the error away
                            if not syn_code: syn_code = 'n/a'
                                
                            new_row[f'synonym_{i+1}_code'] = syn_code

                        
                        new_row['code'] = unicodedata.normalize("NFKD",row["Description"]).rstrip()
                        id += 1
                        csv_rows.append(new_row)

                    fieldnames = find_longest_dict_keys_as_string(csv_rows)
                    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
                    writer.writeheader()

                    for row in csv_rows:
                        writer.writerow(row)

        except FileNotFoundError:
            print("Error: The input CSV file could not be found")
        except IOError:
            print("Error: There was an error reading or writing to the file")



    label_url = 'https://drive.google.com/uc?export=download&id=1diQRBAJO9dYwoR5MBl78z_zS7pFvbP4f'
    bottle_url = 'https://drive.google.com/uc?export=download&id=1rxNnJHWXuItwi_gKZFEBdyFmdTLUZ2Qq'

    get_variety_list(label_url, '/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/raw/raw-label.csv')
    get_variety_list(bottle_url, '/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/raw/raw-bottle.csv')
    create_variety_list_csv_from_raw('/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/raw/raw-label.csv', '/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/raw/raw-bottle.csv', '/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/csv/variety-list.csv')
    create_json_from_csv('/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/csv/variety-list.csv', '/home/runner/work/project-harmony/project-harmony/specifications/australian-grapevine-variety-list/variety-list/json/variety-list.json')


