import streamlit as st

# -------------------------------
# 🎮 게임 추천 데이터셋
# -------------------------------
games = [
    {"name": "마피아", "min": 5, "max": 15, "type": "심리/추리", "time": "30분 이상"},
    {"name": "고요 속의 외침", "min": 3, "max": 10, "type": "신체/활동형", "time": "15~30분"},
    {"name": "코드네임", "min": 4, "max": 8, "type": "전략/두뇌", "time": "20~30분"},
    {"name": "캐치마인드", "min": 3, "max": 8, "type": "그림/창의력", "time": "20~30분"},
    {"name": "우노", "min": 2, "max": 10, "type": "카드/보드", "time": "10~30분"},
    {"name": "스무고개", "min": 2, "max": 10, "type": "언어/토론형", "time": "5~15분"},
    {"name": "진실 혹은 거짓", "min": 3, "max": 10, "type": "엽기/파티용", "time": "10~20분"},
    {"name": "눈치게임", "min": 3, "max": 10, "type": "순발력/반응형", "time": "5분 이내"},
]

# -------------------------------
# 🎨 Streamlit UI 구성
# -------------------------------
st.set_page_config(page_title="게임 추천기", page_icon="🎲")

st.title("🎲 인원수 + 유형 기반 게임 추천기")

# 인원수 입력 슬라이더
num_players = st.slider("👥 참가 인원 수를 선택하세요", 2, 20, step=1)

# 게임 유형 선택 드롭다운
game_types = sorted(set(game["type"] for game in games))
selected_type = st.selectbox("🎯 원하는 게임 유형을 선택하세요", ["전체"] + game_types)

st.markdown("---")

# -------------------------------
# 🔍 추천 로직
# -------------------------------
filtered_games = [
    game for game in games
    if game["min"] <= num_players <= game["max"]
    and (selected_type == "전체" or game["type"] == selected_type)
]

# -------------------------------
# 📋 결과 출력
# -------------------------------
if filtered_games:
    st.subheader(f"✅ 추천 게임 목록 ({len(filtered_games)}개)")
    for game in filtered_games:
        st.markdown(f"""
        **🎮 {game['name']}**  
        - 👥 인원: {game['min']}~{game['max']}명  
        - 🧩 유형: {game['type']}  
        - ⏱️ 소요 시간: {game['time']}  
        """)
else:
    st.warning("❌ 해당 조건에 맞는 게임이 없습니다. 인원수나 유형을 바꿔보세요.")

# -------------------------------
# 👣 하단 정보
# -------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")


