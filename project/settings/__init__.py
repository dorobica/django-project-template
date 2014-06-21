import os

from common import *

env = os.getenv('APP_ENV', 'development')
if env == 'staging':
    from staging import *
elif env == 'production':
    from production import *
else:
    from development import *