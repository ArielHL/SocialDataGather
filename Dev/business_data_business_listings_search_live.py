from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    categories=[
        "pizza_restaurant"
    ],
    description="pizza",
    title="pizza",
    is_claimed=True,
    location_coordinate="53.476225,-2.243572,10",
    order_by=["rating.value,desc"],
    filters=[
        ["rating.value",">",3]
    ],
    limit=3
)
# POST /v3/business_data/business_listings/search/live
response = client.post("/v3/business_data/business_listings/search/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
