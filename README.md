slack_notifier
=================

Setup
------

/etc/sre/slack.conf:

```yaml
{
"token": "T0M****************************************ODA",
}
```

Usage
----------

```python
client.publish("slack/notify", payload=b"this is a text")

