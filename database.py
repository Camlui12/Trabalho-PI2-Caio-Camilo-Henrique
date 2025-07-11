SECRET_KEY = "CamiloCaioHenrique"

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='dbmasteruser',
        password='H2Hr8.{6lla_aVW1j20Ipvkhimx[eqQ<',
        server='ls-111a6f7254d2ffe7f91235b3d16623ec5822a0ea.c87e0omqcw29.us-east-1.rds.amazonaws.com',
        database='trabalho'
    )

SQLALCHEMY_BINDS = {
    "baratinha": "{SGBD}://{user}:{password}@{server}/{database}?sslmode=require".format(
        SGBD='cockroachdb',
        user='camilocaiohenrique',
        password='BbhVJ788cA8lBhC543VrIA',
        server='trabalho-pi2-7607.jxf.gcp-southamerica-east1.cockroachlabs.cloud:26257',
        database='trabalho-pi2'
    )
}

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

CACHE_TYPE = "SimpleCache"

CACHE_DEFAULT_TIMEOUT = 300