API
===

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

List
*******

바디미터에서 측정된 사용자의 목록을 조회하는 API입니다.

* URL: ``{{API 주소}}/list``
* Request Type: ``GET``
* Request Parameter
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

* Response Data
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

* Example

BodyList
*******

특정 사용자의 측정 회차 정보를 조회하는 API입니다.

* URL: ``{{API 주소}}/bodyList``
* Request Type: ``GET``
* Request Parameter
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

* Response Data
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

* Example