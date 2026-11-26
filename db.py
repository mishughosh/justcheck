from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql+psycopg2://websiteonline_user:dJBpK8WZSKAEDTg9VFae3eJ2tYplCKol@dpg-dc36ibgm7kps73dbj5ag-a.ohio-postgres.render.com/websiteonline"
engine=create_engine(DATABASE_URL)

session_local=sessionmaker(autocommit=False,autoflush=False,bind=engine)
base=declarative_base()