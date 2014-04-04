from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

_engine = create_engine('sqlite:///site.db')

make_session = sessionmaker(bind=_engine)

_Base = declarative_base()

@contextmanager
def open():
    s = make_session()
    yield _session(s)
    s.close()

class _session:

    def __init__(self, sess):
        self._sess = sess
        self.query = sess.query
        self.execute = sess.execute
        self.add = sess.add
        self.commit = sess.commit

    def get_url(self, url):
        return self.query(URL).filter(URL.url == url).first()

    def get_url_for_name(self, name):
        """
        get full url given a short name
        """
        return self.query(URL).filter(URL.name == name).first()


class URL(_Base):

    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    name = Column(String, nullable=False)


_Base.metadata.create_all(_engine)
