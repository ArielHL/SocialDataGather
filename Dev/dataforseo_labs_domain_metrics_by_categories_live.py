from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    category_codes=[
		13418, 
		10004
	],
	language_name="English",
	location_code=2840,
	first_date="2021-06-01",
	second_date="2021-10-01",
	filters=[
		["metrics_history.202106.organic.pos_1", ">", 0],
		"and",
		["organic_etv", ">", 10000]
	],
	limit= 3
)
# POST /v3/dataforseo_labs/google/domain_metrics_by_categories/live
response = client.post("/v3/dataforseo_labs/google/domain_metrics_by_categories/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
