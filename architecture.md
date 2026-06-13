# System Architecture

## Overview

The IoT Vehicle Tracking and Theft Prevention System monitors vehicle location, detects unauthorized movement, and provides real-time alerts.

## Architecture

```text
GPS Coordinate Simulation
          │
          ▼
    Geofence Module
          │
          ▼
   Theft Detection
          │
    ┌─────┴─────┐
    ▼           ▼
 CSV Logger   Alert System
    │           │
    ▼           ▼
 PDF Report  ThingSpeak Dashboard
```

## Components

- GPS Simulator
- Geofence Engine
- Theft Detection Module
- CSV Logger
- PDF Generator
- ESP32 Alert System
- ThingSpeak Dashboard