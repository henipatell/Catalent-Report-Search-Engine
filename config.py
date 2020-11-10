import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "dsdfsvcbcvmbcvmcvcvdfjgndifvndnvdjnvjnxvcvnxjnvdjfdsvvnxj238rryh7ery74r"
    
    MONGODB_SETTINGS = {'db' : 'catalent_reports_db', 'host' : 'mongodb+srv://henipatel:henipatel@cluster0.fjtgv.mongodb.net/catalent_reports_db?retryWrites=true&w=majority'}
