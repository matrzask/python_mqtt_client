import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.publish("info/connect", "Python client connected", 0)
    client.subscribe("/battery/level", 0)
    client.subscribe("/info/connect", 0)
    client

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.payload))

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect("localhost", 1883, 60)

    client.loop_forever()