import os
import reflex as rx

config = rx.Config(
    app_name="my_app",
    api_url= "https://8000-" + os.environ['WEB_HOST'],
)