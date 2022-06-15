API
=================================

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

.. warning::

   해당 API는 아직 안정적이지 않으며, 변경될 가능성이 있습니다.

.. http:get:: /api/v1/list

   바디미터에서 측정된 사용자의 목록을 조회하는 API입니다. 고객이 앱을 통해서 이름을 입력한 경우에만 이름 검색이 가능합니다. 검색타입과 검색어를 모두 입력한 경우에만 검색이 작동합니다.

   .. Request

   :query string search_type: 검색타입(name: 이름검색, mobile: 전화번호)
   :query string search_keyword: 검색어
   :query int page: 페이지 번호, 생략시 전체 리스트 반환
   :query int limit: 페이지당 항목 수, 기본 값 20

   .. Response

   :>json int member_no: 사용자 번호
   :>json string user_name: 사용자 이름
   :>json string phone: 사용자 전화번호
   :>json string gender: 성별(male|female)
   :>json string last_evaluate_date: 마지막 측정일
   :>json string memo: 사용자 메모

.. http:get:: /api/v1/bodyList

   특정 사용자의 측정 회차 정보를 조회하는 API입니다.

   .. Request

   :query int member_no: 사용자 번호

   .. Response

   :>json int body_no: 측정 번호
   :>json string evaluation_dt: 측정 일시
   :>json string mirror_id: 측정 기기 아이디

.. http:get:: /api/v1/bodyData

   사용자의 특정 측정 회차의 상세 데이터를 조회하는 API입니다.

   .. Request

   :query int body_no: 측정 번호

   .. Response

   :>json double LeftWeightBalance: 좌측무게중심 비율
   :>json int arm_length: 측정 일시
   :>json int body_lower_length: 하체 길이
   :>json int body_no: 측정 번호
   :>json string body_type: 신체 타입
   :>json string body_type_org: 신체 타입 코드
   :>json string body_upper_length: 상체 길이
   :>json string calfFlexibilityGrade: 종아리 유연성 평가 등급
   :>json string downShoulderGrade: 처진 어깨 평가 등급
   :>json string evaluation_dt: 신체 측정일
   :>json string exercise_round_home: 맞춤 운동 진행 차수(App)
   :>json string exercise_round_office: 맞춤 운동 진행 차수(BodyMeter)
   :>json float face_length: 얼굴길이
   :>json float face_width: 얼굴너비
   :>json int foot_from_wrist_formula: 허벅지 유연성
   :>json int height: 키
   :>json int hip_circum: 골반둘레
   :>json int hip_width: 골반너비
   :>json int left_lower_shoulder_formula: 왼쪽 아래팔 각도
   :>json int left_upper_shoulder_formula: 왼쪽 위팔 각도
   :>json string lowerMuscleGrade: 하체 근력 균형 평가 등급
   :>json string mirror_id: 측정 기기 아이디
   :>json string mode: 측정 모드
   :>json int neck_inclined_formula: 머리 기울기
   :>json int pelvis_distance_formula: 종아리 유연성
   :>json int pelvis_side_distance_formula: 하체근력균형
   :>json int posture_score: 신체 점수
   :>json float ratio_arm_height: 팔:키 비율
   :>json float ratio_lower_upper: 상하체 비율
   :>json float ratio_shoulder_face: 어깨:얼굴너비 비율
   :>json string right_lower_shoulder_formula: 오른쪽 아래팔 각도
   :>json string right_upper_shoulder_formula: 오른쪽 위팔 각도
   :>json string roundShoulderGrade: 둥근 어깨 평가 등급
   :>json int round_shoulder_formula: 둥근 어깨
   :>json string shoulderFlexLeftLowerGrade: 어깨유연성 평가등급(좌-하)
   :>json string shoulderFlexLeftUpperGrade: 어깨유연성 평가등급(좌-상)
   :>json string shoulderFlexRightLowerGrade: 어깨유연성 평가등급(우-하)
   :>json string shoulderFlexRightUpperGrade: 어깨유연성 평가등급(우-상)
   :>json string shoulder_inclined_formula: 어깨 기울기
   :>json string shoulder_width: 어깨 너비
   :>json string spine_inclined_formula: 허리 중심
   :>json string thighFlexibilityGrade: 허벅지 유연성 평가 등급
   :>json string trunkStrengthGrade: 몸통 근력 평가 등급
   :>json string turtleNeckGrade: 거북목 평가 등급
   :>json string turtle_neck_formula: 목 기울기(앞-뒤)
   :>json string upShoulderGrade: 솟은 어깨 평가 등급
   :>json int upper_body_flip_formula: 코어 안정성
   :>json string waistBackGrade: 허리 뒤쏠림 평가 등급
   :>json string waistFrontGrade: 허리 앞쏠림 평가 등급
   :>json int waist_circum: 허리 둘레
   :>json int waist_width: 허리 너비

.. http:get:: /api/v1/photoList

   사용자의 측정 회차의 측정 이미지 리스트를 조회하는 API입니다.

   .. Request

   :query int body_no: 측정 번호

   .. Response

   :>json string name: 파일 경로 배열
   :>json string lastModified: 마지막 수정일시
   :>json int contentSize: 파일 크기
   :>json string contentType: 파일의 Mime Type
   :>json string uri: 파일의 URI 경로(접근할 수 없음)

.. http:get:: /api/v1/photoView

   사용자의 측정 회차의 측정 이미지를 조회하는 API입니다.

   .. Request

   :query string path: 이미지 경로

   .. Response

   Image Binary File