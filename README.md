# 소프트웨어공학및실습 텀 프로젝트

## 개발

정보통신공학과 유지훈(2016113519)

## 소개

![personal_diary](https://user-images.githubusercontent.com/42791408/121642063-f9516e00-caca-11eb-9656-df2d76874ade.gif)
> youtube : https://www.youtube.com/watch?v=OJgLutsxpb0  
  
- flask 기반의 personal diary 개발  
- 나만의 diary 업로드 및 삭제
- 회원가입, 로그인, 로그아웃 기능 지원
- 이미지 업로드

## installation

터미널을 열어 소스코드가 저장될 적당한 디렉토리로 이동한 뒤, github 저장소에 있는 소스코드를 가져옵니다.  

> 본 프로젝트는 anaconda env 아래에서 개발되었습니다.  

``` git clone https://github.com/sonagi784/SoftwareEngineering_hw.git ```  

SoftwareEngineering_hw 폴더안으로 이동합니다.  

``` cd SoftwareEngineering_hw ```

requirements.txt 에 기록된 라이브러리를 한번에 인스톨합니다.

``` pip install -r requirements.txt ```  

flask 서버를 실행시킵니다.

``` python app.py ```  

이후, 인터넷 브라우저를 통해 ```127.0.0.1:5000``` 에 접속해주세요.

## 환경

- flask  
- flask_sqlalchemy  
- anaconda
- sqlite
