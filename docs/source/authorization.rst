Authorization
=====

자사의 API를 호출하기 위해서 먼저 인증된 사용자인지 확인하는 절차를 거치도록 하고 있습니다. 먼저 API를 호출하기 위해서는 인증 절차를 거쳐야 합니다.
자사의 API는 `JWT(Json Web Token) <https://jwt.io/>`_ 방식의 인증을 사용하고 있습니다.
인증 절차를 진행하기 위해서는 다음의 정보가 필요하며, 해당 정보는 메일을 통해서 안내하고 있습니다.

* group_id: 귀사의 그룹 아이디
* client_token: 클라이언트 키
* secret_key: 비밀키

.. _installation:

인증
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

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

