from models.store import StoreModel
from models.item import ItemModel
from models.tag import TagModel
from models.item_tags import ItemTags


# Docker Command to build docker image: docker build -t store-python-api .
# Docker Command to run docker in the back ground with portforwarding and constant updating: docker run -dp 5005:5000 -w /app -v "$(pwd):/app" store-python-api
# Docker Command to run the docker terminal for the particular container: docker run -it store-api-python /bin/bash


# To activate Alembic in Flask - flask db init
# To create the flask migrations - flask db migrate
# To apply the migrations - flask db upgrate