def run(client):
    client.publish("slack/notify", "Test message")