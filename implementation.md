# Implementation Details

## GPS Simulation

Random latitude and longitude values are generated around a predefined location.

## Geofencing

A safe radius of 500 meters is defined. Vehicle positions outside this radius are classified as unsafe.

## Theft Detection

When a vehicle leaves the geofence, a theft alert is triggered.

## Alert System

- LED provides visual alerts.
- Buzzer provides audible alerts.

## Data Logging

All vehicle movements are stored in a CSV file.

## Report Generation

CSV records are converted into PDF reports using ReportLab.

## Cloud Monitoring

Vehicle data is uploaded to ThingSpeak for remote monitoring and visualization.
