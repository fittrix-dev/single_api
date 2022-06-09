Authorization
=====

| 자사의 API를 호출하기 위해서 먼저 인증된 사용자인지 확인하는 절차를 거치도록 하고 있습니다. 먼저 API를 호출하기 위해서는 인증 절차를 거쳐야 합니다.
| 자사의 API는 `JWT(Json Web Token) <https://jwt.io/>`_ 방식의 인증을 사용하고 있습니다.
| 인증 절차를 진행하기 위해서는 다음의 정보가 필요하며, 해당 정보는 메일을 통해서 안내하고 있습니다.

* ``group_id``: 귀사의 그룹 아이디
* ``client_token``: 클라이언트 키
* ``secret_key``: 비밀키

인증
------------

API 인증은 다음의 주소로 진행됩니다.

* {{API 주소}}/authorize

API 주소는 개발용과 서비스용으로 분리하여 제공합니다. 각 주소는 다음과 같습니다.

* 개발용: https://test.fittrix.co.kr
* 실서비스용: https://apiservice.fittrix.io

호출은 다음과 같이 진행됩니다.

.. http:post:: /api/v1/authorize

   .. Request

   :reqheader Authorization: Basic {base64_encode({group_id}:{secret_key})}
   :param string grant_type: 인증 요청 분류, ``authorization_code``로 고정
   :param string group_id: 그룹 ID
   :param string client_token: 안내된 Client Token
   :status 200: 인증 성공
   :status 401: 인증 실패

   .. Response

   :>json string access_token: 인증키
   :>json string expires_at: 인증키 유효일시
   :>json string refresh_token: Refresh Token
   :>json string refresh_token_expires_at: Refresh Token 유효시간
   :>json string group_id: 인증된 그룹 ID
   :>json string issued_at: 인증된 시간

   **Example request**:

   .. tabs::
      .. code-tab:: bash
         curl -X POST \
            '{{API 주소}}/authorize' \
            -H 'Authorization: Basic {base64_encode({group_id}:{secret_key})}' \
            -H 'Content-Type: application/x-www-form-urlencoded' \
            -d 'grant_type=authorization_code&group_id={group_id}&client_token={client_token}'
      .. sourcecode:: http

   **Example response**:
      .. sourcecode:: http
         HTTP/1.1 200 OK
         {
            "access_token": "0iqR5nM5EJIq..........",
            "expires_at": "2022-03-01T14:00:00.000",
            "refresh_token": "JeTJ7XpnFC0P..........",
            "refresh_token_expires_at": "2022-03-03T12:00:00.000",
            "group_id ": "GN0001",
            "issued_at": "2022-03-01T12:00:00.000"
         }

.. code-block:: console

   curl -X POST \
      '{{API 주소}}/authorize' \
      -H 'Authorization: Basic {base64_encode({group_id}:{secret_key})}' \
      -H 'Content-Type: application/x-www-form-urlencoded' \
      -d 'grant_type=authorization_code&group_id={group_id}&client_token={client_token}'

호출 결과는 아래와 같습니다.

.. code-block:: console

   HTTP/1.1 200 OK
   {
      "access_token": "0iqR5nM5EJIq..........",
      "expires_at": "2022-03-01T14:00:00.000",
      "refresh_token": "JeTJ7XpnFC0P..........",
      "refresh_token_expires_at": "2022-03-03T12:00:00.000",
      "group_id ": "GN0001",
      "issued_at": "2022-03-01T12:00:00.000"
   }

access_token은 발급한 시간으로부터 2시간 동안 유효하고, refresh_token은 발급받은 시간으로부터 2일간 유효합니다.

재인증
----------------

access_token이 만료되고 refresh_token만 유효한 경우는 다음과 같이 호출하여서 access_token을 재발급받을 수 있습니다.

.. code-block:: console

   curl -X POST \
      '{{API 주소}}/authorize ' \
      -H 'Authorization: Basic {base64_encode({group_id}:{secret_key})}' \
      -H 'Content-Type: application/x-www-form-urlencoded' \
      -d 'grant_type=refresh_token&refresh_token={refresh_token}'

호출 결과는 아래와 같습니다.

.. code-block:: console

   HTTP/1.1 200 OK
   {
      "access_token": "21EZes0dGSfN..........",
      "expires_at": "2022-03-01T15:50:00.000",
      "refresh_token": "xLlhWztQHBik............",
      "refresh_token_expires_at": "2022-03-03T13:50:00.000",
      "group_id": "GN0001",
      "issued_at": "2022-03-01T13:50:00.000"
   }
