from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    targets={
        "1":"football.com", 
        "2":"fifa.com"
    },
    exclude_targets=[
        "skysports.com"
    ],
    limit=5,
    order_by=[
       "1.rank,desc"
    ],
    filters=[
        [
          "2.domain_from_rank",
          ">",
          400
        ],
        "and", 
        [
          "1.dofollow",
          "=",
          True
        ]
    ]
)
# POST /v3/backlinks/page_intersection/live
response = client.post("/v3/backlinks/page_intersection/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))