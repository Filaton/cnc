# CNControl

MotorHAL mit Steuereinheit

## Beschreibung

Es sollte die Hardware von der Software abstrahiert werden, dazu mussten HAL´s für DC-Motor und Stepper erstellt werden.
Diese HAL nutzt dann die CnC-Klasse, um die einzelnen Stationen anzufahren.

## Setup

Damit die Software lauffähig ist, muss auf dem Zielgerät (meist Raspberry Pi) zusätzlich folgende Requirements erfüllt sein:

`pip install RPi.GPIO`
<!-- `pip install socketserver` erst mit neuerer version-->

## Zeitaufteilung

1. Einarbeiten in die Motorsteuerungen - 15h
2. Hardwareaufbau - 30h
3. Einarbeitung in die Python Bibliotheken - 20h
4. Konzeptionierung und Implementierung der StepperHAL - 20h
5. Konzeptionierung und Implementierung der MotorHAL - 20h
6. Konzeptionierung und Implementierung der CnC-HAL - 20h
7. Konzeptionierung und Implementierung des RequestHandlers - 20h
8. Implementierung und Testing des Top-Level - 20h
9. Hilfestellung bei Desktopapp und Webapp - 30h

Gesamt: 195h
