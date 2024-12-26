# 🛒스파르타 마켓(DRF) 🛒

---

## 목차

1.  [프로젝트 개요](#1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%9C%EC%9A%94)
2.  [기능 소개](#2-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C)
3.  [실행 사진](#3-%EC%8B%A4%ED%96%89-%EC%82%AC%EC%A7%84)
4.  [트러블 슈팅](#4-%ED%8A%B8%EB%9F%AC%EB%B8%94-%EC%8A%88%ED%8C%85)
5.  [사용 기술](#5-%EC%82%AC%EC%9A%A9-%EA%B8%B0%EC%88%A0)
6.  [성과 및 회고](#6-%EC%84%B1%EA%B3%BC-%EB%B0%8F-%ED%9A%8C%EA%B3%A0)

---

## **1\. 프로젝트 개요**

spartamarket은 개인 사용자가 자신의 물건을 등록하고, 다른 사용자의 물건을 찜할 수 있는 플랫폼입니다. 회원가입이 필수이며, 모든 유저는 서로의 물건을 쉽게 탐색하고 소통할 수 있습니다.

---

## **2\. 기능 소개**

-   회원 기능  
    -   username, 비밀번호, 이메일, 이름, 닉네임을 필수로 입력하고 성별과 생일 자기소개도 선택적으로 입력하면 회원가입이 가능하다.
    -   회원 가입 후 이메일과 비밀번호를 입력하면 로그인이 가능하다.
    -   로그인한 상태에서 refresh에 토큰을 무효화하는 값이 들어오면 로그아웃이 가능하다.
-   유저 기능  
    -   로그인한 상태에서 프로필 정보를 가져와 로그인 한 사람의 이메일 주소, 닉네임, 이름, 팔로워 수, 팔로잉 수, 프로필 이미지등을 볼 수 있다.
    -   로그인한 상태에서 다른 유저를 팔로우할 수 있다.
-   게시 기능  
    -   로그인한 상태에서 상품 이미지와 제목, 글 내용을 적으면 상품이 등록이 가능하다.
    -   로그인 하지 않아도 get 요청을 보내서 등록된 상품 목록을 확인이 가능하다.
    -   상품 목록에서 상세 페이지 확인이 가능하다.
    -   상세 페이지에서 해당 상품에 좋아요를 누르거나 취소하여 찜을 할 수 있다.
    -   로그인 한 상태에서 본인이 등록한 상품들만 put 요청을 보내 다시 상품의 이미지, 제목, 글 내용을 수정이 가능하다.
    -   로그인 한 상태에서 본인이 등록한 상품들만 delete 요청을 보내 상품을 등록 해제가 가능하다.
    -   로그인 한 상태에서 본인이 등록하지 않은 상품들에도 comment를 입력하여 댓글을 달 수 있다.
    -   로그인 한 상태에서 본인이 쓴 댓글만 delete 요청을 보내 삭제가 가능하다.
    -   로그인 한 상태에서 본인이 쓴 댓글만 put 요청을 보내 comment를 수정하여 댓글을 수정할 수 있다.
    -   로그인 한 상태에서 댓글에 좋아요를 누르거나 취소할 수 있다.

---

## **3. 실행 사진**

<details>
<summary>닉네임 또는 이메일이 중복일 경우</summary>
![닉네임 또는 이메일이 중복일 경우](https://your-image-url.com/중복.PNG)
</details>

<details>
<summary>필수 사항을 입력 안 했을 경우</summary>
![필수 사항을 입력 안 했을 경우](https://your-image-url.com/필수_사항_노입력.PNG)
</details>

<details>
<summary>필수 사항을 입력했을 경우</summary>
![필수 사항을 입력했을 경우](https://your-image-url.com/회원가입_성공.PNG)
</details>

<details>
<summary>로그인 실패</summary>
![로그인 실패](https://your-image-url.com/로그인_실패.PNG)
</details>

<details>
<summary>로그인 성공</summary>
![로그인 성공](https://your-image-url.com/로그인_성공.PNG)
</details>

<details>
<summary>로그아웃 성공</summary>
![로그아웃 성공](https://your-image-url.com/로그아웃_성공.PNG)
</details>

<details>
<summary>로그아웃 실패</summary>
![로그아웃 실패](https://your-image-url.com/로그아웃_실패.PNG)
</details>

<details>
<summary>프로필 조회</summary>
![프로필 조회](https://your-image-url.com/프로필.PNG)
</details>

<details>
<summary>프로필 수정</summary>
![프로필 수정](https://your-image-url.com/수정.PNG)
</details>

<details>
<summary>게시글 생성</summary>
![게시글 생성](https://your-image-url.com/게시글_생성.PNG)
</details>

<details>
<summary>목록 조회</summary>
![목록 조회](https://your-image-url.com/목록_조회.PNG)
</details>

<details>
<summary>상세 조회</summary>
![상세 조회](https://your-image-url.com/상세_조회.PNG)
</details>

<details>
<summary>게시글 삭제</summary>
![게시글 삭제](https://your-image-url.com/삭제.PNG)
</details>

<details>
<summary>게시글 수정</summary>
![게시글 수정](https://your-image-url.com/게시글_수정.PNG)
</details>

<details>
<summary>게시글 찜</summary>
![게시글 찜](https://your-image-url.com/게시글_찜.PNG)
</details>

<details>
<summary>찜 해제</summary>
![찜 해제](https://your-image-url.com/찜_취소.PNG)
</details>

<details>
<summary>댓글 생성</summary>
![댓글 생성](https://your-image-url.com/댓글_생성.PNG)
</details>

<details>
<summary>댓글 목록</summary>
![댓글 목록](https://your-image-url.com/댓글_목록.PNG)
</details>

<details>
<summary>댓글 좋아요</summary>
![댓글 좋아요](https://your-image-url.com/댓글_좋아요.PNG)
</details>

<details>
<summary>댓글 좋아요 취소</summary>
![댓글 좋아요 취소](https://your-image-url.com/댓글_좋아요_취소.PNG)
</details>


  
  
  
  
  
  
  
  
  
  

---

## **4\. 트러블 슈팅**

1.  -   아직 미완성

---

## **5\. 사용 기술**

📀 백엔드

-   Python
-   Django REST Framework

💬 협업도구

-   GitHub
-   Slack
-   Postman

---

## **6\. 성과 및 회고**

-   잘된 점
    -   회원 가입이 정상적으로 가능하고 로그인을 하면 Access Token과 Refresh Token이 발급되어 로그아웃도 가능하고 리소스 접근이 가능하게 한 점이 좋았다.
    -   로그인 했을때만 글이 작성이 가능하고 본인의 프로필은 팔로우가 안되게 하는 등의 처리를 한 점이 좋았다.
    -   팔로우와 팔로워 수를 볼 수 있게 한 점이 좋았다. 
    -   댓글을 적을 수 있어 물건 거래를 할 때 유용하게 사용이 가능하다는 점이 좋았다.
    -   댓글에 좋아요가 가능하고 본인이 쓴 댓글만 수정과 삭제가 가능하게 한 점이 좋았다.
    -   게시물에 좋아요를 눌러 찜을 할 수 있는 점이 좋았다.
    -   본인이 쓴 게시물만 삭제 및 수정이 가능하게 한 점이 좋았다.
-   아쉬운 점  
    -   상품 이미지도 같이 삽입이 되게 구현을 해보았으나 상품이미지는 같이 저장이 안 되는 점이 아쉬웠다.
    -   회원 가입은 가능하지만 회원 탈퇴가 불가능하고 비밀번호 변경이 안되는 점이 아쉬웠다.
-   향후 계획
    -   상품 이미지도 같이 삽입이 가능하게 할 계획이다.
    -   현재는 회원 탈퇴가 안되기 때문에 회원 탈퇴 기능도 구현할 계획이다.
    -   현재는 패스워드를 첨에 설정한 값밖에는 안되기 때문에 비밀번호 변경 기능도 구현해 볼 계획이다.
    -   물건 검색 기능을 구현해 볼 계획이다.