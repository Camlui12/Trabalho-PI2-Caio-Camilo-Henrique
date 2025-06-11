SECRET_KEY = "CamiloCaioHenrique"

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='dbmasteruser',
        password='H2Hr8.{6lla_aVW1j20Ipvkhimx[eqQ<',
        server='ls-111a6f7254d2ffe7f91235b3d16623ec5822a0ea.c87e0omqcw29.us-east-1.rds.amazonaws.com',
        database='trabalho'
    )
    
SQLALCHEMY_TRACK_MODIFICATIONS = False