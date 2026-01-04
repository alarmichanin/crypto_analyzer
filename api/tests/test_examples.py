# # Sending Requests with the Test Client¶

# def test_request_example(client):
#     response = client.get("/posts")
#     assert b"<h2>Hello, World!</h2>" in response.data

# Pass a dict query_string={"key": "value", ...} to set arguments in the query string (after the ? in the URL). 
# Pass a dict headers={} to set request headers.
# To send a request body in a POST or PUT request, pass a value to data.

# # JSON Data¶

# To send JSON data, pass an object to json. The Content-Type header will be set to application/json automatically.

# Similarly, if the response contains JSON data, the response.json attribute will contain the deserialized object.

# def test_json_data(client):
#     response = client.post("/graphql", json={
#         "query": """
#             query User($id: String!) {
#                 user(id: $id) {
#                     name
#                     theme
#                     picture_url
#                 }
#             }
#         """,
#         variables={"id": 2},
#     })
#     assert response.json["data"]["user"]["name"] == "Flask"

