from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player,Coach
from models import Base

engine = create_engine('sqlite:///futsal.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata= Faker()

if __name__=='__main__':
    for i in range(17):  
        player = Player(
            name=fakedata.name(),
            birthdate=fakedata.date_of_birth(),
            experience_years=fakedata.random_int(min=0, max=7),
            age=fakedata.random_int(min=18, max=40)
        ) 
        mysession.add(player)
    # mysession.commit()


    for i in range(3):
        coach = Coach(
        first_name=fakedata.first_name(),
        last_name=fakedata.last_name(),
        email=fakedata.email(),
        phone_number=fakedata.phone_number(),
        team=fakedata.word(),
        years_of_experience=fakedata.random_int(min=1, max=20),
        coaching_license=fakedata.word()
    )
    mysession.add(coach)

    #commit changes
mysession.commit()

print('All players Seeded, They should now be in your Database')
#close database

mysession.close()

   
   


   