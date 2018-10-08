import paho.mqtt.publish as publish

myhost="somehost.com"
msg="this is a string msg to publish on MQTT”

# Example of simple single publish
publish.single("my/topic", msg, hostname=myhost, auth={'username':"usr",'password':"pass"}, port=18090)

# More complex JSON payload
happiness="Super happy"
data = {"name":"Shop 1","location":"DK","cashiers":[{"cid":1,"satisfaction":happiness}]}
print(json.dumps(data))
publish.single("shop/cashiers/1/satisfaction", json.dumps(data), hostname=myhost, auth={'username’:”user",'password’:”pass"}, port=18090)
