import streamlit as st

# 게임 추천 데이터 (샘플)
games = [
    {"name": "마피아", "min": 5, "max": 15, "type": "심리", "time": "30분 이상"},
    {"name": "저글링 챌린지", "min": 2, "max": 4, "type": "활동", "time": "10~20분"},
    {"name": "캐치마인드", "min": 3, "max": 8, "type": "그림", "time": "20~30분"},
    {"name": "우노", "min": 2, "max": 10, "type": "카드", "time": "10~30분"},
    {"name": "코드네임", "min": 4, "max": 8, "type": "단어", "time": "15~25분"},
]

st.title("인원수에 맞는 게임 추천기 🎲")

# 사용자 인원수 입력
num_players = st.slider("몇 명이 참가하나요?", 2, 20)

# 필터링된 게임 리스트
recommended = [g for g in games if g["min"] <= num_players <= g["max"]]

if recommended:
    st.subheader(f"추천 게임 리스트 ({len(recommended)}개)")
    for game in recommended:
        st.markdown(f"**{game['name']}**  \n"
                    f"▶️ 유형: {game['type']} / ⏱️ 소요시간: {game['time']}")
else:
    st.warning("해당 인원수에 맞는 게임이 없습니다.")


