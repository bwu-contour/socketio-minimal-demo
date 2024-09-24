pip install -r requirements.txt
pytest test_websocket.py -v -s
pytest --html=report.html