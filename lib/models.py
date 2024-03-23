# from sqlalchemy import create_engine
from  sqlalchemy.orm import declarative_base 
# from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Date
Base =declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    birthdate = Column(Date())
    age = Column(Integer())
    experience_years = Column(Integer())

    def __repr__(self):
        return f'Player(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'age={self.age})'
    
class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    phone_number = Column(String())
    team = Column(String())
    years_of_experience = Column(Integer())
    coaching_license = Column(String())

    def __repr__(self):
        return f'Coach(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name}, ' + \
            f'email={self.email}, ' + \
            f'phone_number={self.phone_number}, ' + \
            f'team={self.team}, ' + \
            f'years_of_experience={self.years_of_experience}, ' + \
            f'coaching_license={self.coaching_license})'    



engine = create_engine('sqlite:///futsal.db')
Base.metadata.create_all(engine)