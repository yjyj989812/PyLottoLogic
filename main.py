import argparse
from src import data_utils
from src import time_utils
from src import random_utils

def init_dataset(target_url, data_path="./data/number_count.json"):
    request_result = data_utils.crawl_data(target_url)
    matches = data_utils.get_numbers_in_request(request_result)
    data_utils.dump_numbers_to_json(data=matches,file_path=data_path, update_date=time_utils.return_date())

def suggest_numbers(data_path="./data/number_count.json"):
    data = data_utils.get_data(data_path)
    lotto_timestamps = time_utils.return_next_saturday_timestamp()
    selected_numbers = [list(random_utils.choice_numbers(data['data'], timestamp)) for timestamp in lotto_timestamps]
    
    return {"date": time_utils.return_date(lotto_timestamps[0]), "data": selected_numbers}


def main(args):
    if args.url:
        if args.path:
            init_dataset(args.url, args.path)
        else:
            init_dataset(args.url)
    
    if args.path:
        get_result = suggest_numbers(data_path=args.path)
    else:
        get_result = suggest_numbers()

    number_result = '\n\t'.join(map(str, get_result['data']))
    print(f"{get_result['date']}, suggest numbers:\n\t{number_result}")


if __name__ == '__main__':
    # argparse 객체 생성
    parser = argparse.ArgumentParser(description="giving some arg for set file path, target url")

    # 명령줄 인자 정의
    parser.add_argument("--path", type=str, help="The first argument about data file path")
    parser.add_argument("--url", type=str, help="The second argument about target url for parsing")

    # 명령줄 인자를 파싱
    args = parser.parse_args()
    
    # main 함수 호출
    main(args)