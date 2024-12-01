import datetime

def return_next_saturday_timestamp():
    now = datetime.datetime.now()
    
    # 현재 요일 (월=0, 화=1, ..., 토=5, 일=6)
    today_weekday = now.weekday()
    
    # 이번 주 토요일 날짜 계산 (토요일은 5)
    days_until_saturday = (5 - today_weekday) if today_weekday <= 5 else (5 - today_weekday + 7)
    next_saturday = now + datetime.timedelta(days=days_until_saturday)
    
    # 토요일 20시 35분으로 설정
    next_saturday_evening = next_saturday.replace(hour=20, minute=35, second=0, microsecond=0)
    
    # 현재 시간이 토요일 20시 35분 이후인 경우, 다음 주 토요일로 이동
    if now > next_saturday_evening:
        next_saturday_evening += datetime.timedelta(days=7)
    
    date_list = [next_saturday_evening.replace(minute=i) for i in range(35, 40, 1)]

    return date_list

def return_date(date=datetime.datetime.now(), foramt="%Y-%m-%d"):
    return date.strftime(foramt)