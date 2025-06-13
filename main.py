import streamlit as st
from hanspell import spell_checker

st.title("📝 맞춤법 검사기 + 글자 수 세기")

# 텍스트 입력
user_input = st.text_area("검사할 문장을 입력하세요:", height=200)

# 글자 수
if user_input:
    total_length = len(user_input)
    no_space_length = len(user_input.replace(" ", ""))

    st.write(f"🔤 총 글자 수 (띄어쓰기 포함): {total_length}")
    st.write(f"🔤 총 글자 수 (띄어쓰기 제외): {no_space_length}")

    # 맞춤법 검사 실행
    if st.button("맞춤법 검사하기"):
        result = spell_checker.check(user_input)
        checked_text = result.checked
        errors = result.errors

        st.subheader("✅ 교정된 문장")
        st.write(checked_text)

        if errors:
            st.subheader("❗ 오탈자 정보")
            for e in errors:
                st.write(f"- `{e['token']}` → `{e['suggestion']}` ({e['info']})")
        else:
            st.success("맞춤법 오류가 없습니다.")


        ai_reply = response.choices[0].message.content
        st.success("✨ 추천 진로")
        st.markdown(ai_reply)

