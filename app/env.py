prod = True
if prod :     
    settings = {"PROJECT_NAME": "API",
                "PROJECT_VERSION": "1.0.0",
                "POSTGRES_USER": 'vfpwklgadzhtuv',
                "POSTGRES_PASSWORD": 'c887860979f5d3724feb47d99942d0c068d0770b1146504b3dbdd0f1a2d8e4d9',
                "POSTGRES_SERVER": 'ec2-23-20-224-166.compute-1.amazonaws.com',
                "POSTGRES_PORT": 5432,
                "POSTGRES_DB": "d756qvhgdpbbvg",
                }
else :
    settings = {"PROJECT_NAME": "API TEST",
                "PROJECT_VERSION": "1.0.0",
                "POSTGRES_USER": 'postgres',
                "POSTGRES_PASSWORD": 'ena',
                "POSTGRES_SERVER": 'localhost',
                "POSTGRES_PORT": 5432,
                "POSTGRES_DB": "postgres",
                }

