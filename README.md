# RPI를 활용한 미니 프로젝트
## 제목 : 랜덤 메뉴 추출기

## 작품 개요
밥을 먹을 때마다 메뉴를 쉽게 정하지 못하는 어려움을 해결하고자<br/>
LED와 부저, mqtt를 활용하여 메뉴의 후보를 입력하면<br/>
그 중 랜덤으로 하나를 지정해주는 룰렛 프로그램을 만들고자 함.

## 작품 제작에 사용한 센서와 액추에이터와 역할
-LED : LED 3개를 차례대로 점등하며 룰렛 같은 효과를 위함.<br/>
-SWICH : 스위치를 누름으로써 프로그램을 시작하게 함.<br/>
-BUZZER : 메뉴가 정해지면 부저로 사운드를 출력함.

## 완성 작품
### 작품 회로도
<img width="604" alt="회로도" src="https://github.com/yenn222/Arduino_pj_menu/assets/131340704/029e8a0a-a94f-493b-9fe5-a7bd9ad7b0fd">

### 작품 사진
![회로 사진](https://github.com/yenn222/Arduino_pj_menu/assets/131340704/2a969320-4088-4b73-97b3-70bad2fd9c44)

### 동작 영상
https://github.com/yenn222/Arduino_pj_menu/assets/131340704/66b86e54-fb26-4b18-857a-44d2302148d4

## 동작 시나리오
1. 메뉴 입력 : 고민하는 메뉴를 입력받아 띄어쓰기로 구분( split() )하여 저장한다.<br/>
2. 버튼 대기 : 메뉴 개수를 프린트하고 버튼 동작이 있을 때까지 대기한다.<br/>
3. 랜덤 추출 : 버튼이 눌리면 3개의 LED가 차례대로 점등, 부저가 울린 후 랜덤으로 하나의 메뉴를 선정한다.<br/>
4. Mqtt 전송 : 선정된 메뉴의 결과값을 "오늘의 메뉴" : "결과" 형식으로 전송한다.

## 기대 효과
1. 혼자 고르기 어려운 메뉴를 쉽고 재밌게 정함.
2. 여러 사람이 모여 메뉴를 정할 때에도 사용 가능.
3. Mqtt를 통해 어떤 날 어떤 메뉴를 먹었는 지 확인 가능.
