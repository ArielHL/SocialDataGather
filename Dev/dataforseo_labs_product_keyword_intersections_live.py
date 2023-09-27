from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    asins={
        "1":"019005476X",
        "2":"0190074442"
    },
    language_name="English",
    location_code=2840,
    limit=3
)
# POST /v3/dataforseo_labs/amazon/product_keyword_intersections/live
response = client.post("/v3/dataforseo_labs/amazon/product_keyword_intersections/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
