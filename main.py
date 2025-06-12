import streamlit as st
import random

# 🎨 페이지 구성
st.set_page_config(
    page_title="🎮 가위 ✌️ 바위 ✊ 보 🖐️ 게임!",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="auto"
)

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎮 가위 ✌️ 바위 ✊ 보 🖐️ 게임에 오신 걸 환영합니다!</h1>", unsafe_allow_html=True)
st.markdown("---")

# 📜 설명
st.markdown("""
<style>
.big-font {
    font-size:22px !important;
}
</style>
<div class='big-font'>
👋 당신은 컴퓨터와 가위 ✌️ 바위 ✊ 보 🖐️를 겨룰 수 있어요! <br><br>
🧠 컴퓨터는 무작위로 선택하고, 당신이 선택한 결과에 따라 승부가 결정됩니다!<br><br>
🎉 과연 승자는 누구일까요?
</div>
""", unsafe_allow_html=True)

# 🎲 게임 옵션
choices = ["✌️ 가위", "✊ 바위", "🖐️ 보"]
user_choice = st.selectbox("👇 하나를 선택하세요!", choices)

# 🔁 게임 로직
def get_result(user, computer):
    if user == computer:
        return "🤝 무승부예요!"
    elif (user == "✌️ 가위" and computer == "🖐️ 보") or \
         (user == "✊ 바위" and computer == "✌️ 가위") or \
         (user == "🖐️ 보" and computer == "✊ 바위"):
        return "🎉 당신이 이겼어요! 🏆"
    else:
        return "😢 컴퓨터가 이겼어요... 다시 도전해보세요!"

# ▶️ 버튼 클릭 시
if st.button("⚔️ 대결 시작!"):
    computer_choice = random.choice(choices)
    st.markdown(f"🧑 당신의 선택: **{user_choice}**")
    st.markdown(f"💻 컴퓨터의 선택: **{computer_choice}**")
    
    result = get_result(user_choice, computer_choice)
    
    # 결과 출력
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>{result}</h2>", unsafe_allow_html=True)
    st.balloons()

# 🎨 하단 꾸미기
st.markdown("---")
st.markdown("<p style='text-align: center;'>✨ 즐거운 시간 보내세요! - Made with ❤️ by Streamlit</p>", unsafe_allow_html=True)
