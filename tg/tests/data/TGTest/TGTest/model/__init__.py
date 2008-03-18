from sqlalchemy.orm import scoped_session, sessionmaker
from pylons import config
import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy import Column, MetaData, Table, types
from sqlalchemy.orm import mapper, relation

# Global session manager.  Session() returns the session object
# appropriate for the current web request.
DBSession = scoped_session(sessionmaker(autoflush=True, transactional=True))

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database.
metadata = MetaData()

def init_model(engine):
    """Call me before using any of the tables or classes in the model."""
    
    # 'init_model' is called from environment.py automatically in TG2.
    # But if you are using the model with reflection elsewhere, you'll need to
    # call this before using the model.
    # If you are using reflection to introspect your database and create table objects
    # for you, your tables must be defined and mapped inside the init_model function, \
    # so that the engine is available. See the following example:

    # Reflected tables must be defined and mapped here.
    #    
    # global t_reflected
    # t_reflected = Table("Reflected", metadata,
    #    autoload=True, autoload_with=engine)
    # mapper(Reflected, t_reflected)

# Normal tables may be defined and mapped at module level.
#
#foo_table = Table("Foo", meta.metadata,
#    Column("id", types.Integer, primary_key=True),
#    Column("bar", types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    def __init__(self, **kw):
#        """automatically mapping attributes"""
#        for key, value in kw.iteritems():
#            setattr(self, key, value)
#
#mapper(Foo, foo_table)


# Classes for reflected tables may be defined here, but the table and
# mapping itself must be done in the init_model function.
#
#table_reflected = None    # Updated by init_model().
#
#class Reflected(object):
#    pass
