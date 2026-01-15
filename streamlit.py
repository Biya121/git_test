import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime as dt
import datetime 


st.title("치킨붤거가 먹고싶소")
st.header("칰필레랑 칰칰이 레전드치킨버거를 만들지")
st.subheader("치킨버거말고도 다른 게 있지")
st.text("와플프라이가진짜맛있음")

st.title("스마일☺️")
st.header("하트❤️")

st.caption("캡션을 추가할 수 있단다.")

st.markdown("**마크다운 문법도 가능하단다.**")
sample_code = """def hello() :
    print("HEllo, World!")
    """
st.code(sample_code, language = 'python')


# 마크다운 문법 지원
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 :blue[파란색]은 볼드체 설정")
st.markdown(":green[$\sqrt{x^2 + y^2} = 1$]와 같은 수식도 지원한다.")

st.latex(r'\sqrt{x^2 + y^2}=1')


# dataframe 생성
st.title("데이터프레임 출력하기")

dataframe = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 9, 18, 40]
})

# dataframe 출력
st.dataframe(dataframe)
st.table(dataframe)

# 메트릭
st.metric(label="온도", value="25°C", delta="1.2°C") # 특수문자 넣는 법 :ㄱ/ㄴ/ㄷ/ㄹ/ㅁ + 한자키
st.metric(label="삼성전자", value="140000원", delta="+3800원")

# 컬럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD",value="1,471원", delta = "+50원")
col2.metric(label="유로EUR",value="1,590원", delta = "+20원")
col3.metric(label="엔JPY",value="1,050원", delta = "-5원")

# 버튼 클릭
button = st.button("버튼을 눌러주세요")
if button :
    st.write(":blue[버튼]이 눌렸습니다!")

agree= st.checkbox("체크박스를 눌러주세요")
if agree :
    st.write("체크박스가 선택되었습니다!")

mbti = st.radio(
    "당신의 MBTI는 무엇인가요?",
    ('INTJ', 'ENFP', 'ISTP', 'ESFJ'), 
    index = 1 # 초기값을 설정할 수 있음.
)

if mbti == 'INTJ' :
    st.write("당신은 전략가형입니다.")
elif mbti == 'ENFP' :
    st.write("당신은 활동가형입니다.")
elif mbti == 'ISTP' :
    st.write("당신은 장인형입니다.")
else :
    st.write("당신은 사교형입니다.")

# 셀렉트박스
favorite_food = st.selectbox(
    "가장 좋아하는 음식은?",
    ('치킨', '피자', '햄버거', '족발')
)
# f-string을 사용하여 전체를 하나의 문자열로 감싸줍니다.
st.write(f"당신이 가장 좋아하는 음식은 :red[{favorite_food}] 입니다.")

# 멀티셀렉트박스
hobbies = st.multiselect(
    "취미를 선택해주세요",
    ['독서', '운동', '게임', '여행', '요리']
)
# join 결과값을 변수에 담거나 직접 f-string에 넣습니다.
if hobbies:
    result = ', '.join(hobbies)
    st.write(f"당신의 취미는 :green[{result}] 입니다.")
else:
    st.write("취미를 선택해주세요!")

# 슬라이더
age = st.slider("당신의 나이는?", 0, 120, 25) # 최소값, 최대값, 기본값
st.write(f"당신의 나이는 :blue[{age}]세 입니다.")

value = st.slider(
    "범위의 값을 다음과 같은 범위로 설정하세요.",
    0.0, 100.0, (25.0, 75.0)
)
st.write(f"선택한 값의 범위는 :green[{value}] 입니다.")

# 날짜 선택
start_time = st.slider(
    "언제약속잡을래빨리말해.",
    min_value=dt(2026, 1, 16, 9, 0), 
    max_value=dt(2026, 1, 30, 0, 0),
    value = dt(2026, 1, 15, 0, 0),
    step = datetime.timedelta(days=1),
    format="YYYY-MM-DD HH:mm"
)
st.write(f"약속잡힌 날짜는 :red[{start_time}] 입니다.")

# 텍스트 입력
title = st.text_input(
    label = "가고 싶은 여행지가 있나요?",
    placeholder = "예: 파리, 뉴욕, 도쿄"
)
st.write(f"당신이 가고 싶은 여행지는 :blue[{title}] 입니다.")

# 숫자 입력
number = st.number_input(
    label = "당신이 좋아하는 숫자는 무엇인가요?",
    min_value = 0,
    max_value = 100,
    value = 50,
    step = 5
)
st.write(f"당신이 좋아하는 숫자는 :green[{number}] 입니다.")

# 파일 다운로드 버튼
st.download_button(
    label = "CSV 다운로드", 
    data = dataframe.to_csv(index = False).encode('utf-8'),
    file_name = "sample_.csv",
    mime = "text/csv"
)