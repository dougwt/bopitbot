from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

engine = create_engine('sqlite:///../data.db', echo=True)
models.Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Populate Commands
for name in ['bop', 'twist', 'pull', 'spin', 'flick']:
    command = models.Command(name=name, username='%sitbot' % name)
    session.add(command)
session.commit()

player = models.Player(name='dougwt')
session.add(player)
