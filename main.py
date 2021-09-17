# rest api key; 3c09b7658d189bd883d39ea78ad071e4

# http 요청을 쉽게 보낼 수 있게 해주는 라이브러리
# cmd 창에서 pip install requests로 설치 가능
import requests
import json

# https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide
def daumAPI_webDocSearch():
    url = "https://dapi.kakao.com/v2/search/web"
    header = {"Authorization": "KakaoAK 3c09b7658d189bd883d39ea78ad071e4"}
    method = "GET"
    parameter = {"query": "야탑목련마을", "size": "15", "sort": "recency", "page": "5"}

    # 요청을 보냄
    request = requests.request(method=method, url=url, headers=header, params=parameter)

    # 요청 결과의 start line 출력 e.g) <Response [200]>
    print(request)

    # 요청 결과를 json 형식으로 한 줄로 출력해줌
    # print(request.json())


# print("\n")

# \t tab
# \n enter
# \s space

    # 요청 결과를 json 형식으로 이쁘게 출력해줌
    # indent="\t"는 tab 기준으로 들여쓰기 하는 옵션
    # ensure_ascii=False는 한글이 깨지지 않게 하는 옵션
    print(json.dumps(request.json(), indent="\t", ensure_ascii=False))

def daumAPI_webImageSearch():
    url = "https://dapi.kakao.com/v2/search/image"
    header = {"Authorization": "KakaoAK 3c09b7658d189bd883d39ea78ad071e4"}
    method = "GET"
    parameter = {"query": "순두부 젤라또", "sort": "accuracy", "size": "15"}
    imageRequest = requests.request(url=url, headers=header, method=method, params=parameter)
    print(imageRequest)
    print(json.dumps(imageRequest.json(), indent="\t", ensure_ascii=False))

def daumAPI_webVideoSearch():
    url = "https://dapi.kakao.com/v2/search/vclip"
    header = {"Authorization": "KakaoAK 3c09b7658d189bd883d39ea78ad071e4"}
    method = "GET"
    parameter = {"query": "아이유"}
    videoRequest = requests.request(url=url, headers=header, method=method, params=parameter)
    print(videoRequest)

    print(json.dumps(videoRequest.json(), indent="\t", ensure_ascii=False))

def daumAPI_wrongAPI():
    url = "https://dapi.kakao.com/v2/search/vclip"
    # header = {"Authorization": "KakaoAK 3c09b7658d189bd883d39ea78ad071e4"}
    header = {}
    method = "GET"
    parameter = {"query": "아이유"}
    wrongRequest = requests.request(url=url, headers=header, method=method, params=parameter)
    print(wrongRequest)

    print(json.dumps(wrongRequest.json(), indent="\t", ensure_ascii=False))
    # < Response[401] >
    # {
    #     "errorType": "AccessDeniedError",
    #     "message": "cannot find Authorization : KakaoAK header"
    # }



def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 프로그램의 시작점인 main문
# if문의 뜻은 main 프로세스만 이 부분을 실행시키라는 뜻
# main 프로세스 말고 보조 프로세스는 실행시키면 안됨
if __name__ == '__main__':
   print_hi('PyCharm')
   daumAPI_webDocSearch()
   daumAPI_webVideoSearch()
   daumAPI_wrongAPI()
   daumAPI_webImageSearch()

