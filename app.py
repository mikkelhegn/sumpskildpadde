from spin_http import Response

def handle_request(request):

    body = "Hello from Pelle og Nelle 🐢🐢🐢🐢"

    return Response(200,
                    [("content-type", "text/plain")],
                    bytes(body, "utf-16"))