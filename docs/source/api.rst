API
===

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

List
*******

바디미터에서 측정된 사용자의 목록을 조회하는 API입니다.

* **URL**: ``{{API 주소}}/list``
* **Request Type**: ``GET``
* **Request Parameter**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 비고
      * - page
        - 페이지번호
        - X
        - 지정되지 않으면 전체 리스트 반환
      * - limit
        - 페이지당 항목 수
        - X
        - 기본값 :20

* **Response Data**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 자료형
      * - member_no
        - 사용자 번호
        - O
        - int
      * - user_name
        - 사용자 이름
        - X
        - string
      * - phone
        - 사용자 전화번호
        - O
        - string
      * - gender
        - 성별
        - O
        - string(male|female)
      * - birthday
        - 생년월일
        - X
        - string
      * - last_evaluate_date
        - 마지막 측정일
        - O
        - string
      * - memo
        - 메모
        - X
        - string

* **Example**

BodyList
*******

특정 사용자의 측정 회차 정보를 조회하는 API입니다.

* **URL**: ``{{API 주소}}/bodyList``
* **Request Type**: ``GET``
* **Request Parameter**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 비고
      * - member_no
        - 사용자 번호
        - O
        -

* **Response Data**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 자료형
      * - body_no
        - 측정 번호
        - O
        - int
      * - evaluation_dt
        - 측정 일시
        - O
        - string
      * - mirror_id
        - 측정 기기 아이디
        - O
        - string

* **Example**

BodyData
*******

사용자의 특정 측정 회차의 상세 데이터를 조회하는 API입니다.

* **URL**: ``{{API 주소}}/bodyData``
* **Request Type**: ``GET``
* **Request Parameter**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 비고
      * - body_no
        - 측정 회차 번호
        - O
        -

* **Response Data**
   .. list-table::
      :header-rows: 1

      * - 변수명
        - 항목
        - 필수 여부
        - 자료형
      * - LeftWeightBalance
        - 좌측무게중심 비율
        - X
        - double
      * - arm_length
        - 측정 일시
        - X
        - int
      * - body_lower_length
        - 하체 길이
        - X
        - int
      * - body_no
        - 측정 번호
        - O
        - int
      * - body_type
        - 신체 타입
        - X
        - string
      * - body_type_org
        - 신체 타입 코드
        - X
        - string
      * - body_upper_length
        - 상체 길이
        - X
        - string
      * - calfFlexibilityGrade
        - 종아리 유연성 평가 등급
        - X
        - string
      * - downShoulderGrade
        - 처진 어깨 평가 등급
        - X
        - string
      * - evaluation_dt
        - 신체 측정일
        - O
        - string
      * - exercise_round_home
        - 맞춤 운동 진행 차수(App)
        - O
        - string
      * - exercise_round_office
        - 맞춤 운동 진행 차수(BodyMeter)
        - O
        - string
      * - face_length
        - 얼굴길이
        - X
        - float
      * - face_width
        - 얼굴너비
        - X
        - float
      * - foot_from_wrist_formula
        - 허벅지 유연성
        - X
        - int
      * - height
        - 키
        - X
        - int
      * - hip_circum
        - 골반둘레
        - X
        - int
      * - hip_width
        - 골반너비
        - X
        - int
      * - left_lower_shoulder_formula
        - 왼쪽 아래팔 각도
        - X
        - int
      * - left_upper_shoulder_formula
        - 왼쪽 위팔 각도
        - X
        - int
      * - lowerMuscleGrade
        - 하체 근력 균형 평가 등급
        - X
        - string
      * - mirror_id
        - 측정 기기 아이디
        - O
        - string
      * - mode
        - 측정 모드
        - O
        - string
      * - neck_inclined_formula
        - 머리 기울기
        - X
        - int
      * - pelvis_distance_formula
        - 종아리 유연성
        - X
        - int
      * - pelvis_side_distance_formula
        - 하체근력균형
        - X
        - int
      * - posture_score
        - 신체 점수
        - X
        - int
      * - ratio_arm_height
        - 팔:키 비율
        - X
        - float
      * - ratio_lower_upper
        - 상하체 비율
        - X
        - float
      * - ratio_shoulder_face
        - 어깨:얼굴너비 비율
        - X
        - float
      * - right_lower_shoulder_formula
        - 오른쪽 아래팔 각도
        - X
        - string
      * - right_upper_shoulder_formula
        - 오른쪽 위팔 각도
        - X
        - string
      * - roundShoulderGrade
        - 둥근 어깨 평가 등급
        - X
        - string
      * - round_shoulder_formula
        - 둥근 어깨
        - X
        - int
      * - shoulderFlexLeftLowerGrade
        - 어깨유연성 평가등급(좌-하)
        - X
        - string
      * - shoulderFlexLeftUpperGrade
        - 어깨유연성 평가등급(좌-상)
        - X
        - string
      * - shoulderFlexRightLowerGrade
        - 어깨유연성 평가등급(우-하)
        - X
        - string
      * - shoulderFlexRightUpperGrade
        - 어깨유연성 평가등급(우-상)
        - X
        - string
      * - shoulder_inclined_formula
        - 어깨 기울기
        - X
        - string
      * - shoulder_width
        - 어깨 너비
        - X
        - string
      * - spine_inclined_formula
        - 허리 중심
        - X
        - string
      * - thighFlexibilityGrade
        - 허벅지 유연성 평가 등급
        - X
        - string
      * - trunkStrengthGrade
        - 몸통 근력 평가 등급
        - X
        - string
      * - turtleNeckGrade
        - 거북목 평가 등급
        - X
        - string
      * - turtle_neck_formula
        - 목 기울기(앞-뒤)
        - X
        - string
      * - upShoulderGrade
        - 솟은 어깨 평가 등급
        - X
        - string
      * - upper_body_flip_formula
        - 코어 안정성
        - X
        - int
      * - waistBackGrade
        - 허리 뒤쏠림 평가 등급
        - X
        - string
      * - waistFrontGrade
        - 허리 앞쏠림 평가 등급
        - X
        - string
      * - waist_circum
        - 허리 둘레
        - X
        - int
      * - waist_width
        - 허리 너비
        - X
        - int

* **Example**