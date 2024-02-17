from app import db, create_app

def main():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("done")

if __name__ == "__main__":
    main()
