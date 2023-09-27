from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# example #1 - a simple way to set a task
# this way requires you to specify a location, a language of search, and a keyword.
post_data[len(post_data)] = dict(
    location_code=1023191,
    language_code="en",
    keyword="cheap hotel"
)
# example #2 - a way to set a task with additional parameters
# high priority allows us to complete a task faster, but you will be charged more.
# after a task is completed, we will send a GET request to the address you specify. Instead of $id and $tag, you will receive actual values that are relevant to this task.
post_data[len(post_data)] = dict(
    location_name="New York,New York,United States",
    language_name="English",
    keyword="cheap hotel",
    check_in="2021-06-01",
    check_out="2021-06-30",
    currency="USD",
    adults=2,
    children=[14],
    sort_by="highest_rating",
    priority=2,
    tag="example",
    pingback_url="https://your-server.com/pingscript?id=$id&tag=$tag"
)
# POST /v3/business_data/google/hotel_searches/task_post
response = client.post("/v3/business_data/google/hotel_searches/task_post", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))