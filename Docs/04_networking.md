# Networking Protocol Design

The MQTT protocol is used for communication between the sensor and the application layer.

## Design Rationale
- Lightweight and low bandwidth
- Publish/subscribe model
- Ideal for IoT environments

## Topic Structure
raspi5/sensor/dht11

## Data Format
JSON format is used for message payloads:
{
  "temperature": 24,
  "humidity": 51,
  "time": "ISO timestamp"
}

## Data Flow Diagram
See `/diagrams/data_flow.png`
