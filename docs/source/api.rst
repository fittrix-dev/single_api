API
=================================

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

.. warning::

   해당 API는 아직 안정적이지 않으며, 변경될 가능성이 있습니다.

.. http:get:: /api/v1/list

   바디미터에서 측정된 사용자의 목록을 조회하는 API입니다.

   .. Request

   :query page: 페이지 번호, 생략시 전체 리스트 반환
   :query limit: 페이지당 항목 수, 기본 값 20

   .. Response

   :>json int member_no: 사용자 번호
   :>json string user_name: 사용자 이름
   :>json string phone: 사용자 전화번호
   :>json string gender: 성별(male|female)
   :>json string last_evaluate_date: 마지막 측정일
   :>json string memo: 사용자 메모

