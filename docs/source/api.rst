API
===

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

List
*******

바디미터에서 측정된 사용자의 목록을 조회하는 API입니다.

* URL: {{API 주소}}/list
* Request Type: `GET`
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