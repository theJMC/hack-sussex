from app import db, create_app

def main():

    app = create_app()
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    with app.app_context():
        db.create_all()
        print("done")

if __name__ == "__main__":
    main()
