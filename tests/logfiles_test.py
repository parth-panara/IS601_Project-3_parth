import os, pytest

from app import logs

def test_logfile_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(logfile) == True

def test_logfile_second_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/flask.log')
    assert os.path.exists(logfile) == True

def test_logfile_third_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/myapp.log')
    assert os.path.exists(logfile) == True

def test_logfile_fourth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/request.log')
    assert os.path.exists(logfile) == True

def test_logfile_fifth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/sqlalchemy.log')
    assert os.path.exists(logfile) == True

def test_logfile_sixth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../app/logs/werkzeug.log')
    assert os.path.exists(logfile) == True
