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
* {API 주소}/authorize
API 주소는 개발용과 서비스용으로 분리하여 제공합니다. 각 주소는 다음과 같습니다.
* 개발용: https://test.fittrix.co.kr
* 실서비스용: https://apiservice.fittrix.io
호출은 다음과 같이 진행됩니다.

.. code-block:: console
   curl -X POST \
      '{API 주소}/authorize' \
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


Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

