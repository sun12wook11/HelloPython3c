# 실전예제 1
# ㅁ 한자키 특문, 윈도+온점 이모지


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_password_email(customer_email, customer_name, customer_id, customer_password):
    # SMTP 서버 설정
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_email_password"

    # 이메일 본문 구성
    subject = "아이디 및 비밀번호 확인"
    body = f"""To. {customer_email}
▶ 아이디 및 비밀번호 확인
{customer_name} 고객님 안녕하세요.
{customer_name} 고객님의 아이디와 비밀번호는 아래와 같습니다.
아이디 : {customer_id}
비밀번호 : {customer_password}"""

    # 이메일 메시지 생성
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = customer_email
    msg['Subject'] = subject

    # 이메일 본문 추가
    msg.attach(MIMEText(body, 'plain'))

    # 이메일 전송
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS 사용 시작
        server.login(smtp_user, smtp_password)  # 로그인
        server.send_message(msg)  # 이메일 전송
        server.quit()  # 서버 연결 종료
        print("이메일이 성공적으로 발송되었습니다.")
    except Exception as e:
        print(f"이메일 발송 중 오류가 발생했습니다: {e}")



# 고객 정보
customer_email = "gildong@abc.com"
customer_name = "홍길동"
customer_id = "gildong"
customer_password = "1234"

# 이메일 발송 함수 호출
send_password_email(customer_email, customer_name, customer_id, customer_password)




# 실전예제 2
# 날짜와 요일을 계산하기 위해 datetime 모듈을 임포트합니다.
from datetime import datetime, timedelta

# 날씨 정보 입력 함수
def get_weather_info():
    date = input("날짜 (예: 3월 30일): ")
    morning_temp = input("아침 기온 (예: -1도): ")
    afternoon_temp = input("낮 기온 (예: 10도): ")
    rain_prob = input("비올 확률 (예: 45%): ")
    dust_level = input("미세먼지 수치 (예: 좋음): ")
    sunrise_time = input("일출 시간 (예: 오전 6시 30분): ")
    sunset_time = input("일몰 시간 (예: 오후 7시 20분): ")

    return date, morning_temp, afternoon_temp, rain_prob, dust_level, sunrise_time, sunset_time

# 내일의 날짜와 요일 계산 함수
def get_tomorrow_date():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    return tomorrow.strftime("%Y년 %m월 %d일"), tomorrow.strftime("%A")

# 날씨 정보 출력 함수
def print_weather_forecast(date, morning_temp, afternoon_temp, rain_prob, dust_level, sunrise_time, sunset_time, day_of_week):
    print(f"""내일 날씨 예보입니다.
               {day_of_week}인 {date}의 아침 최저 기온은 {morning_temp}, 
               낮 최고 기온은 {afternoon_temp}로 예보됐습니다. 
               비올 확률은 {rain_prob}이고, 
               미세먼지는 {dust_level} 수준일 것으로 예상됩니다.
               일출 시간은 {sunrise_time}이고, 
               일몰 시간은 {sunset_time}입니다.
               바다의 물결은 남해 앞바다 0.5m, 동해 앞바다 1.5m, 서해 앞바다 0.5m 높이로 일겠습니다. 
               지금까지 {date} {day_of_week} 날씨 예보였습니다.""")

# 메인 함수
def main():
    # 내일 날짜와 요일 계산
    date, day_of_week = get_tomorrow_date()

    # 날씨 정보 입력
    date, morning_temp, afternoon_temp, rain_prob, dust_level, sunrise_time, sunset_time = get_weather_info()

    # 날씨 정보 출력
    print_weather_forecast(date, morning_temp, afternoon_temp, rain_prob, dust_level, sunrise_time, sunset_time, day_of_week)

if __name__ == "__main__":
    main()



# 영수증 예제


# 만나이계산


from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    # 만나이 계산
    age = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    return age

# 사용자로부터 생년월일 입력 받기
birthdate = input("생년월일을 입력하세요 (예: 1990-03-30): ")

# 만나이 계산 및 출력
age = calculate_age(birthdate)
print(f"만나이는 {age}세입니다.")


## 구구단 7단 츨력
# 구구단 7단 출력
for i in range(1, 10):
    print(f"7 x {i} = {7 * i}")