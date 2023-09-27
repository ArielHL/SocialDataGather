from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    app_id="org.telegram.messenger",
	language_name="English",
	location_code=2840,
	filters=["keyword_data.keyword_info.search_volume", ">", 10000],
	limit=10
)
# POST /v3/dataforseo_labs/google/keywords_for_app/live
# POST /v3/dataforseo_labs/apple/keywords_for_app/live
response = client.post("/v3/dataforseo_labs/google/keywords_for_app/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
