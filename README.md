# cnc

## Ziel

Erstellen einer Cocktailmaschine mit Unterstützung für 16 Flaschen und 7 Kanister.

### Milestones

- Bauen des Grundgerüsts
- Konstruieren der Motoren und Schienen
- Erstellen einer MotorHAL
- Erstellen einer WebApp zur Auswahl von Cocktails
- Erstellen einer Desktop App zum Hinzufügen von Cocktails

## Aktueller Stand

- Grundgerüst und Motoren fertig gestellt (Durch Testing wurde herausgefunden, dass die Balken noch weiter herabgesetzt werden müssen)
- MotorHal fertiggestellt
- Websocket fertiggestellt
- TopLevel für Hardware mit Websocket fertiggestellt
- WebApp größtenteils fertiggestellt
- Desktop App fertiggestellt (mehr Funktionen geplant)

## Zeitaufwand

Aufgabe  |  Zeit        | Person
-------- |  ------------|---------------
Planung und Konstruktion der Cocktailmaschine | 150h | MAH, ABM
HAL für Motoren der Cocktailmaschine | 30h | MAH
HAL für Pumpen der CnC | 25h | MAH
Ansteuerung des TFT Displays | TODO | MAH, ABM
Datenbankserver mit DynDNS – Anbindung | 30h | ABM
Progressive Web App, mithilfe derer man die Cocktails bestellt werden können. | 150h | ZAP
Desktop-App um Cocktails in die Datenbank einbinden zu können | 65h | ABM

## Inhalt

Inhalt  |  Beschreibung
-------- |  ------------
[Desktop App](DesktopApp/DesktopApp.md) | The Desktop App (CnConnector)
[Web App](WebApp/WebApp.md) | The Web App (Blazor App)
[Hardwarecontrol](HardwareControl/HardwareControl.md) | Hardwareabstraktionlayer (CnControl)
