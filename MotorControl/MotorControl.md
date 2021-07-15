# CNControl

MotorHAL mit Steuereinheit

## Beschreibung

Es sollte die Hardware von der Software abstrahiert werden, dazu mussten HAL´s für DC-Motor und Stepper erstellt werden.
Diese HAL nutzt dann die CnC-Klasse, um die einzelnen Stationen anzufahren.

## Setup

Damit die Software lauffähig ist, muss auf dem Zielgerät (meist Raspberry Pi) zusätzlich müssen folgende Requirements erfüllt sein:

`pip install RPi.GPIO`
<!-- `pip install socketserver` erst mit neuerer version-->

## Zeitaufteilung

1. Einarbeiten in die Motorsteuerungen - 15h
2. Hardwareaufbau - 10h
3. Konzeptionierung und Implementierung der StepperHAL - 10h
4. Konzeptionierung und Implementierung der MotorHAL - 10h
5. Konzeptionierung und Implementierung der CnC-HAL - 10h

Gesamt: 55h
