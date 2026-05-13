from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# dbUser = "root"
# dbPass = "root"
# dbHost = "localhost"
# dbPort = 3306
# dbName = "fastapi"

# DATABASE_URL = f"mysql+pymysql://{dbUser}:{dbPass}@{dbHost}:{dbPort}/{dbName}"

# engine = create_engine(
#     DATABASE_URL, echo=True  # show SQL queries in terminal (optional)
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
