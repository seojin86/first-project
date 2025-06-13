import streamlit as st
from hanspell import spell_checker

st.set_page_config(page_title="맞춤법 검사기 + 글자 수 세기", page_icon="📝")

st.title("📝 맞춤법 검사기 + 글자 수 세기")
st.write("텍스트를 입력하면 맞춤법을 검사하고 글자 수를 알려드립니다.")

# 사용자 입력
text = st.text_area("검사할 문장을 입력하세요:", height=200)

if text:
    # 글자 수 계산
    total_chars = len(text)
    chars_no_space = len(text.replace(" ", ""))
    st.write(f"🔤 총 글자 수 (띄어쓰기 포함): {total_chars}")
    st.write(f"🔤 총 글자 수 (띄어쓰기 제외): {chars_no_space}")

    if st.button("맞춤법 검사하기"):
        with st.spinner("맞춤법 검사 중..."):
            result = spell_checker.check(text)

        corrected_text = result.checked
        errors = result.errors

        st.subheader("✅ 교정된 문장")
        st.write(corrected_text)

        if errors:
            st.subheader("❗ 맞춤법 오류 목록")
            for err in errors:
                st.write(f"- `{err['token']}` → `{err['suggestion']}` ({err['info']})")
        else:
            st.success("맞춤법 오류가 없습니다.")


