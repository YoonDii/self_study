# 미니실습1
## 뉴스기사 3줄요약하기

  1. 바이너리 파일을 문자열로 변경하자
  `import base64`를 사용해서 사용가능!
  이미지 가져오기 등 가능!

  2. 문자열을 원하는대로 추출하자
  `import txtwrap`
  `import re` 정규표현식
  둘 다 많은 함수들이 있으니 꼭 공식문서 확인하기!

  3. 단어 개수를 구하자
  `collections.Counter`를 사용하면 된다.
  `import collection`한 다음 원하는 단어의 개수 찾아주면 됨.
  `collections.Counter(인스턴스)`
