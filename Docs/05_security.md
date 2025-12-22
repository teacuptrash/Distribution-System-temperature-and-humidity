# Security Implementation

Network-layer security is implemented using MQTT authentication.

## Security Measures
- Username and password required for MQTT clients
- Anonymous access disabled
- Unauthorized subscription attempts rejected

## Verification
- Authorized MQTT clients successfully receive data
- Unauthorized clients receive "not authorised" errors

This mechanism prevents unauthorized devices from accessing sensor data.

Leave YOUR_USERNAME / YOUR_PASSWORD as placeholders in /src/dht11_mqtt.py