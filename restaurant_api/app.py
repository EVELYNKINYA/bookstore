from flask_migrate import Migrate
from models.dbconfig import db 
from routes import create_app
from faker import Faker

# app initialization 
app = create_app()
#configure my migrations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
Migrate(app,db)


if __name__ == '__main__':
    app.run(debug=True, port=5000)