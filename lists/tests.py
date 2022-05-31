from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)



class HomePageTest(TestCase):
    # 1. 특정 URL에 대한 HTTP Request를 받는다.
    # 2. django는 특정 규칙을 이용해서 해당 요청에 어떤 뷰 함수를 실행할지 결정한다.(URL "해석"이라고 하는 처리)
    # 3. 이 뷰 기능이 Request를 처리해서 HTTP Response로 반환한다.
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)