import requests, re, json

def crawl_data(parsing_url):
    return requests.get(parsing_url)

def get_numbers_in_request(request_result, pattern=r"drwtNoPop\[\d+\] = \'(\d+)\'"):
    return re.findall(pattern, request_result.text)

def dump_numbers_to_json(data, file_path="./data/number_count.json", update_date="2024-10-17"):
    json_format = {
        "version": "2024-10-16",
        "statement": "Save count of lotto numbers",
        "last_update": update_date,
        "data": {}
    }

    for i, n in enumerate(data):
        json_format["data"][i+1] = n

    with open(file_path, "w") as f:
        json.dump(json_format, f, indent=4)

def get_data(file_path="./data/number_count.json"):
    with open(file_path, "r") as f:
        result = json.load(f)
    
    return result
