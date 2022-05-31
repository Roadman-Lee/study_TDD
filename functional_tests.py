from selenium import webdriver

# 1. 크롬 브라우져 창을 실행하기 위해 셀레늄의 webdriver를 실행한다.
# 2. 브라우저를 통해 로컬 PC 상의 웹페이지를 연다
# 3. 웹 페이지 타이틀에 "Django"라는 단어가 있는지 확인 한다.

browser = webdriver.Chrome()
browser.get('http://localhost:8000/')

assert 'The install worked successfully' in browser.title