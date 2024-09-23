##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="코드 검색기")

    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')    

    st.header("📃검색기")
    st.markdown('---')
    
    text = st.text_area("필요한 정보를 입력하세요")
    if st.button("검색"):
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''
        if open_apikey:
            try:
                # API 키가 유효한 경우 요약 작업을 수행합니다.
                response = askGpt(prompt, open_apikey)
                st.info(response)
            except Exception as e:
                # 에러가 발생한 경우 에러 메시지를 표시합니다.
                st.error(f"요약 작업 중 에러가 발생했습니다: {str(e)}")

        else:
            st.info("API 키를 입력하세요")
        

if __name__=="__main__":
    main()
