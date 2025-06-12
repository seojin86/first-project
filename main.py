import streamlit as st
import random

st.set_page_config(
    page_title="👥 인원 수에 따른 게임 추천",
    page_icon="🎉",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>👥 인원 수로 게임 추천 🎲</h1>", unsafe_allow_html=True)
st.markdown("## 몇 명이서 게임하나요?")

# 인원 수 입력
people = st.slider("👫 인원 수를 선택하세요", min_value=1, max_value=20, value=1)

# 게임 리스트 (한국에서 인기 있거나 할 만한 게임 기준)
games_by_people = {
    "혼자 (1명)": [
        "📱 모바일 게임: 쿠키런: 킹덤",
        "🧩 퍼즐 게임: 2048",
        "🎮 닌텐도 싱글 게임: 젤다의 전설",
        "💡 스도쿠, 크로스워드 퍼즐",
        "🎧 리듬 게임: Cytus, 디제이맥스",
    ],
    "소규모 (2~4명)": [
        "🕵️ 마피아 게임",
        "🃏 카드게임: 우노, 루미큐브",
        "🎨 제시어 게임",
        "🎭 몸으로 말해요",
        "🍻 간단한 술게임 (눈치게임 등)",
    ],
    "중간 규모 (5~8명)": [
        "🕵️ 확장형 마피아 게임",
        "🎲 보드게임: 카탄, 다빈치 코드",
        "🗣️ 팀 퀴즈 대결",
        "📦 상자 속 물건 맞추기",
        "🎤 노래방 게임",
    ],
    "대규모 (9명 이상)": [
        "🎭 대규모 마피아 게임",
        "📢 제시어 릴레이 게임",
        "🎤 대형 노래방 파티",
        "🏃‍♂️ 숨바꼭질, 술래잡기",
        "🕹️ 온라인 배틀로얄 (배틀그라운드, 롤 등)",
    ],
}

# 인원수에 따른 추천 리스트 결정
if people == 1:
    category = "혼자 (1명)"
elif 2 <= people <= 4:
    category = "소규모 (2~4명)"
elif 5 <= people <= 8:
    category = "중간 규모 (5~8명)"
else:
    category = "대규모 (9명 이상)"

st.markdown(f"### 🏷️ 현재 인원 수: **{people}명** → **{category} 게임** 추천!")

# 게임 추천
recommended_game = random.choice(games_by_people[category])
st.success(f"🎯 추천 게임: {recommended_game}")

# 버튼 클릭 시 다른 게임 추천
if st.button("🔄 다른 게임 추천 받기"):
    new_game = random.choice(games_by_people[category])
    st.info(f"🎉 새로운 추천: {new_game}")

st.markdown("---")
st.markdown("<p style='text-align: center;'>🇰🇷 한국에서 많이 하는 게임들로 추천해드려요!<br>즐거운 시간 보내세요! 😊</p>", unsafe_allow_html=True)
