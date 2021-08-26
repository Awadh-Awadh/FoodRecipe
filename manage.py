from app import create_app,db
from flask_migrate import Migrate
from app.models import User



app = create_app('development')

migrate = Migrate(app = app, db = db)


@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User)
if __name__ == '__main__':
    app.run()