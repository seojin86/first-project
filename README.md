import streamlit as st
import openai

# 🔑 OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# 🎨 앱 타이틀
st.title("🎓 나에게 맞는 AI 진로는?")
st.write("당신의 관심사와 성향을 알려주면, GPT가 AI 분야 진로를 추천해줄게요!")

# 💬 사용자 입력
user_input = st.text_input("AI에 관심이 있다면, 어떤 활동을 좋아하나요? (예: 그림, 문제 해결, 사람과 대화 등)")

# ▶ GPT로 응답 요청
if user_input:
    with st.spinner("AI가 당신에게 맞는 진로를 생각 중이에요..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 gpt-4
            messages=[
                {"role": "system", "content": "너는 친절한 AI 진로 컨설턴트야."},
                {"role": "user", "content": f"나는 {user_input} 같은 걸 좋아해. AI 진로 중 나한테 맞는 걸 추천해줘."}
            ]
        )

        ai_reply = response.choices[0].message.content
        st.success("✨ 추천 진로")
        st.markdown(ai_reply)
