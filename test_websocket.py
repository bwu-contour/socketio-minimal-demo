import pytest
import socketio

ENDPOINT = "http://localhost:8080"

@pytest.fixture
def sio():
    if "https" in ENDPOINT.lower():
        sio = socketio.SimpleClient(ssl_verify=False)
    else:
        sio = socketio.SimpleClient()
    sio.connect(ENDPOINT, transports=['websocket'])  # WebSocket server address
    yield sio
    sio.disconnect()

@pytest.mark.repeat(10)  # Run the test 10 times
def test_send_message(sio):
    print('my sid is', sio.sid)
    print('my transport is', sio.transport)
    for num in range(1000):
        sio.emit('message', 'ping' + str(num))
        try:
            event = sio.receive(timeout=5)
        except TimeoutError:
            print('timed out waiting for event')
        else:
            print(f'received event: "{event[0]}" with arguments {event[1:]}')