from fastapi import FastAPI
from .models.users import db
from .views import users 


def get_app():
	app = FastAPI(title="GINO FastAPI Demo")
	db.init_app(app)
	users.init_app(app)
	return app




