from fastapi import FastAPI

description = """
##### An API to produce a google-like short description of a person. Example: When you google “yoshua bengio”, you get “Canadian computer scientist” on the right information box as here. Your API will return “Canadian computer scientist” for input “Yoshua bengio”.
## Instructions:
* ### Data source
* - Your source is the English wikipedia page content of the person being asked. For this, you will use the
mediawiki API.
Example : Try the following query for Yoshua Bengio.
https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatver
sion=2&format=json&rvprop=content
You will get a json output which is copied here. You will notice {{Short description|Canadian computer
scientist}} in the content value. 
* - You can use this query as a template and replace titles with the appropriate
input that your API gets.
* #### You will have 48 hours to submit the assignment.

"""

my_fastapi_app = FastAPI(
    title="Wiki",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Omer Suliman",
        "url": "https://github.com/omerahmed41",
        "email": "omerahmed41@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    docs_url="/",
)
