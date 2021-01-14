from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Pets
woofly = Pet(
    name="Woofly",
    species='dog',
    photo_url=
    "http://www.cockapooclubgb.co.uk/uploads/9/4/2/9/9429470/801808973.jpg?194",
    age=3,
    notes='this dog is nice',
    available=True)

cow = Pet(
    name="Mad Cow",
    species='cow',
    photo_url="https://giraffopia.files.wordpress.com/2011/01/mad-cow-2.jpg",
    age=9,
    notes='this cow is crazy!',
    available=True)

cat = Pet(
    name="Snargle",
    species='cat',
    photo_url=
    "https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg",
    age=4,
    notes='I hate cats!',
    available=False)

db.session.add(woofly)
db.session.add(cow)
db.session.add(cat)

db.session.commit()
