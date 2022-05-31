from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(60)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_website_and_retrieve_the_browser(self):
        # '이성'은 웹 사이트를 확인하러간다.
        self.browser.get('http://localhost:8000/')
        # 웹 페이지 타이틀과 헤더가 'To-Do' 를 표시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# '이성'은 바로 작업을 추가한다.

# " 클린코드를 위한 테스트 주도 개발" 이라고 텍스트 상자에 입력한다.

# 엔터키를 치면 페이지가 갱신되고 작업목록에 "1: 클린코드를 위한 테스트 주도 개발"이 추가 된다.

# 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
# 다시 "클린코드를 위한 테스트 주도 개발"이 라고 입력한다.

# 페이지가 다시 갱신되고, 두 개의 목록이 보인다.
# '이성'은 사이트가 입력한 목록을 저장하고 있는지 궁금하다.
# 사이트는 그를 위한 특정 URl을 생성해준다.
# 이때 URL에 대한 설명도 함께 제공된다.

# 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있을 것을 확인할 수 있다.
if __name__ == "__main__":
    unittest.main(warnings='ignore')