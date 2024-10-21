pip install -r requirements.txt
pytest test_socketio.py -v -s
pytest --html=report.html