import streamlit as st
import random

st.set_page_config(page_title="감정별 위로 한마디", page_icon="🌸", layout="centered")

st.markdown("""
<style>
    .big-font {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .message-box {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 12px;
        font-size: 20px;
        text-align: center;
        color: #333;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-font'>💖 지금 당신의 감정은 어떤가요?</div>", unsafe_allow_html=True)
st.markdown(" ")

# 감정별 위로 메시지
messages = {
    "우울해요": [
        "오늘 하루도 잘 버텨줘서 고마워요.",
        "당신이 느끼는 감정은 모두 괜찮아요.",
        "어둠 속에도 분명히 작은 빛이 있어요.",
    ],
    "불안해요": [
        "모든 게 완벽하지 않아도 괜찮아요.",
        "천천히, 한 걸음씩 가도 괜찮아요.",
        "지금 이 순간도 잘 지나갈 거예요.",
    ],
    "지쳤어요": [
        "쉬어갈 시간이에요. 당신은 이미 충분히 잘했어요.",
        "너무 애쓰지 않아도 괜찮아요. 당신은 소중한 존재예요.",
        "무엇보다 당신의 마음이 가장 중요해요.",
    ],
    "괜찮아요": [
        "지금의 평온함이 오래도록 이어지길 바라요.",
        "마음의 여유가 느껴져요. 그 모습 참 멋져요.",
        "스스로를 돌볼 줄 아는 당신, 정말 멋져요.",
    ],
    "행복해요": [
        "당신의 행복이 다른 사람에게도 전해지고 있어요 😊",
        "이 기분 오래 간직하길 바라요!",
        "당신의 웃음은 주변을 따뜻하게 만들어요.",
    ]
}

# 버튼들 (1줄에 나란히 감정 표현)
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

with col1:
    if st.button("😔 우울해요"):
        mood = "우울해요"
with col2:
    if st.button("😟 불안해요"):
        mood = "불안해요"
with col3:
    if st.button("😩 지쳤어요"):
        mood = "지쳤어요"
with col4:
    if st.button("🙂 괜찮아요"):
        mood = "괜찮아요"
with col5:
    if st.button("😊 행복해요"):
        mood = "행복해요"

# 선택한 감정에 맞는 메시지 출력
if "mood" in locals():
    msg = random.choice(messages[mood])
    st.markdown(f"<div class='message-box'>{msg}</div>", unsafe_allow_html=True)


        ai_reply = response.choices[0].message.content
        st.success("✨ 추천 진로")
        st.markdown(ai_reply)

