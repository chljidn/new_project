# 배달 서비스 토이 프로젝트
  
## 목표
- 배달 서비스에 대한 api 기능 구현 및 해당 기능에 맞는 최적화된 솔루션 찾기
- 테스트와 빌드의 자동화를 통한 서버 아키텍처 구성의 경험 및 이해
- erd 및 데이터 베이스 스키마 작업을 통한 데이터 베이스 구현에 대한 이해
- django4.0에 추가된 django.core.cache.redis를 통한 캐시DB 사용하여 DB서버 부하 줄이기.

## 기술 스택
- Python 3.8
- Django
- Mariadb
- jenkins
- AWS(EC2)
- Gunicorn
- Docker
- Redis


## 서버 아키텍처
<P align="center">
  <img src="https://github.com/chljidn/new_project/blob/master/%EB%B0%B0%EB%8B%AC%EC%84%9C%EB%B9%84%EC%8A%A4.png" />
</p>

## ERD 
![](https://github.com/chljidn/new_project/blob/master/ev_erd.png)


## 이슈 및 해결방법
- [유저모델을 2개로 나누어야 할 경우](https://chljidn-django.tistory.com/5)
- redis적용
- [각 요청 별로 두 개의 DB처리를 요할 경우 에러 처리](https://chljidn-django.tistory.com/4)
- 테스트 및 빌드 자동화
