from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    keyword="logitech",
    keyword_fields= dict(
        snippet="logitech"
    ),
    page_type=[
        "ecommerce",
        "news",
        "blogs",
        "message-boards",
        "organization"
    ],
    search_mode="as_is",
    filters=[
        "main_domain", "=", "reviewfinder.ca"
    ],
    internal_list_limit=8,
    order_by=[
        "content_info.sentiment_connotations.anger,desc"
    ],
    limit=10
)
# POST /v3/content_analysis/search/live
response = client.post("/v3/content_analysis/search/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))