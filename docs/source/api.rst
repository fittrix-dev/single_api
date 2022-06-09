API
=================================

API는 인증을 통해서 JWT 토큰을 발급받은 이후에 호출이 가능합니다.

.. warning::

   해당 API는 아직 안정적이지 않으며, 변경될 가능성이 있습니다.

.. http:get:: /api/v2/search/

   Return a list of search results for a project,
   including results from its :doc:`/subprojects`.
   Results are divided into sections with highlights of the matching term.

   .. Request

   :query q: Search query
   :query project: Project slug
   :query version: Version slug
   :query page: Jump to a specific page
   :query page_size: Limits the results per page, default is 50

   .. Response

   :>json string type: The type of the result, currently page is the only type.
   :>json string project: The project slug
   :>json string project_alias: Alias of the project if it's a subproject.
   :>json string version: The version slug
   :>json string title: The title of the page
   :>json string domain: Canonical domain of the resulting page
   :>json string path: Path to the resulting page
   :>json object highlights: An object containing a list of substrings with matching terms.
                             Note that the text is HTML escaped with the matching terms inside a <span> tag.
   :>json object blocks:

    A list of block objects containing search results from the page.
    Currently, there are two types of blocks:

    - section: A page section with a linkable anchor (``id`` attribute).
    - domain: A Sphinx :doc:`domain <sphinx:usage/restructuredtext/domains>`
      with a linkable anchor (``id`` attribute).


   **Example request**:

   .. tabs::

      .. code-tab:: bash

         $ curl "https://readthedocs.org/api/v2/search/?project=docs&version=latest&q=server%20side%20search"

      .. code-tab:: python

         import requests
         URL = 'https://readthedocs.org/api/v2/search/'
         params = {
            'q': 'server side search',
            'project': 'docs',
            'version': 'latest',
         }
         response = requests.get(URL, params=params)
         print(response.json())

   **Example response**:

   .. sourcecode:: json

      {
          "count": 41,
          "next": "https://readthedocs.org/api/v2/search/?page=2&project=read-the-docs&q=server+side+search&version=latest",
          "previous": null,
          "results": [
              {
                  "type": "page",
                  "project": "docs",
                  "project_alias": null,
                  "version": "latest",
                  "title": "Server Side Search",
                  "domain": "https://docs.readthedocs.io",
                  "path": "/en/latest/server-side-search.html",
                  "highlights": {
                      "title": [
                          "<span>Server</span> <span>Side</span> <span>Search</span>"
                      ]
                  },
                  "blocks": [
                     {
                        "type": "section",
                        "id": "server-side-search",
                        "title": "Server Side Search",
                        "content": "Read the Docs provides full-text search across all of the pages of all projects, this is powered by Elasticsearch.",
                        "highlights": {
                           "title": [
                              "<span>Server</span> <span>Side</span> <span>Search</span>"
                           ],
                           "content": [
                              "You can <span>search</span> all projects at https:&#x2F;&#x2F;readthedocs.org&#x2F;<span>search</span>&#x2F"
                           ]
                        }
                     },
                     {
                        "type": "domain",
                        "role": "http:get",
                        "name": "/_/api/v2/search/",
                        "id": "get--_-api-v2-search-",
                        "content": "Retrieve search results for docs",
                        "highlights": {
                           "name": [""],
                           "content": ["Retrieve <span>search</span> results for docs"]
                        }
                     }
                  ]
              },
          ]
      }