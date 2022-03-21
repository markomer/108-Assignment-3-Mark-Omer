from flask import Flask, abort  # from file or mdule import X
import json
from mock_data import catalog # fn or something...




app = Flask("Server")


@app.route("/")
def home():
  return "Hello from Flask"



@app.route("/me") # add /me to the URL
def about_me():
  return "Mark Omer"



#####################################
####  API ENDPOINTS  ################
####   RETURN JSON   ################
#####################################


# @app.route("/api/catalog")
@app.route("/api/catalog", methods=["get"])
def get_catalog():

  """ return "catalog data"
  return json.dumps(prod) # this is how parse..."""
  return json.dumps(catalog)

  """prod = {
    "title":"test",
    "price": 123.423
  }"""

@app.route("/api/catalog", methods=["post"])
def save_product():
  pass



# GET /api/catalog/count -> how many products exist in the catalog

@app.route("/api/catalog/count", methods=["get"])
def count_prods():
  count = len(catalog)
  return json.dumps(count)
  # or... return json.dumps(len(count))

# get /api/catalog/total => the sum of all porduct's prices
@app.route("/api/catalog/total")
def total_of_catalog():
  total = 0
  for prod in catalog: # into prods in catalog array
    total += prod["price"]

  return json.dumps(total)



@app.route("/api/product/<id>") # whatever is in <xx> is an id var
def get_by_id(id):
  # find the product with _id is equal to id

  for prod in catalog:
    if prod["_id"] == id:
      return json.dumps(prod)

  # not found, return an error 404
  return abort(404, "No product with such id")


app.run(debug=True)