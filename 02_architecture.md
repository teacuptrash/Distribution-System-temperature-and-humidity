# System Architecture

The system follows the standard four-layer IoT architecture:

## Perception Layer
- DHT11 temperature and humidity sensor
- Connected via GPIO to Raspberry Pi 5

## Network Layer
- MQTT protocol
- Mosquitto broker running on Raspberry Pi
- Publish/subscribe communication model

## Application Layer
- Node-RED flow
- Data processing and dashboard visualization

## Security Layer
- MQTT username and password authentication
- Unauthorized access blocked

## Architecture Diagram
See `/diagrams/system_architecture.png`
