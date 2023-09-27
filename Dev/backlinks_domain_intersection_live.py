from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    targets={
        "1":"adidas.com", 
        "2":"nike.com"
    },
    exclude_targets=[
        "puma.com"
    ],
    limit=5,
    include_subdomains=False,
    exclude_internal_backlinks=True,
    order_by=[
        "1.backlinks,desc"
    ]
)
# POST /v3/backlinks/domain_intersection/live
response = client.post("/v3/backlinks/domain_intersection/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))