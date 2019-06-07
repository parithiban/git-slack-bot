from config import get_env
from app import create_app
from app.worker import rq


app = create_app(get_env('APP_ENV'))
app.app_context().push()
rq.init_app(app)


if __name__ == '__main__':
    app.run(port=get_env('PORT') or 5000)
