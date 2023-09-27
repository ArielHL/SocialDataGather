from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# You can set only one task at a time
post_data[len(post_data)] = dict(
    search_terms = [
            "data-attrid"
    ],
    filters = [
                "country_iso_code",
                "=",
                "US"
    ],
    order_by = ["last_visited,desc"],
    limit = 10
)
# POST /v3/domain_analytics/technologies/domains_by_html_terms/live
response = client.post("/v3/domain_analytics/technologies/domains_by_html_terms/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
