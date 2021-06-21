Durch eine Web Applikation sollte die Auswahl der Cocktails ermöglicht werden. Zunächst wollten wir diese mit dem Framework Angular und Java Script erstellen. Bei dem bearbeiten wurde jedoch entschieden das Framework und die Sprache zu wechseln. Von nun an benutzten wir als Framework  Blazor und als Programmiersprache c#. Durch diese Umstellung wurde das Entwickeln der Web app erleichtert. Die vorgesehenen Funktionen der Web App waren das Anzeigen und das Auswählen der Cocktails. Auch die Erstellung neuer Cocktails war als eine Möglichkeit der Bedienung in Betracht gezogen worden. Die Getränke, die Zutaten und die Zuordnung werden von einer Datenbank gestellt. Zunächst wollten wir eine DynDNS Datenbank verwendet werden, jedoch wurde auch hier eine andere Datenbank verwendet. Die verwendete Datenbank war MySql. Um diese zu erstellen musste man sich zuerst mit der neuen Programmiersprache und den Framework vertraut machen. Danach musste eine Web Applikation erstellt werden. Danach musste eine Verbindung zu der Datenbank erstellt werden.     

Probleme:

    • Blazor Web Assembly konnte nur schwer mit der Datenbank verknüpfen
    • 	
Durch eine Web Applikation sollte die Auswahl der Cocktails ermöglicht werden. Zunächst wollten wir diese mit dem Framework Angular und Java Script erstellen. Bei dem bearbeiten wurde jedoch entschieden das Framework und die Sprache zu wechseln. Von nun an benutzten wir als Framework  Blazor und als Programmiersprache c#. Durch diese Umstellung wurde das Entwickeln der Web app erleichtert. Die vorgesehenen Funktionen der Web App waren das Anzeigen und das Auswählen der Cocktails. Auch die Erstellung neuer Cocktails war als eine Möglichkeit der Bedienung in Betracht gezogen worden. Die Getränke, die Zutaten und die Zuordnung werden von einer Datenbank gestellt. Zunächst wollten wir eine DynDNS Datenbank verwendet werden, jedoch wurde auch hier eine andere Datenbank verwendet. Die verwendete Datenbank war MySql. Um diese zu erstellen musste man sich zuerst mit der neuen Programmiersprache und den Framework vertraut machen. Danach musste eine Web Applikation erstellt werden. Danach musste eine Verbindung zu der Datenbank erstellt werden.     

Geplante Implementierung:
 -   Progressive Web App
 -   Eine Liste der möglichen Cocktails sollte gezeigt werden
 -   Anbindung an eine Datenbank

Erreichte Implementierung:
 -   Blazor Web Applikation
 -   Alle Getränke und die daraus resultierenden Cocktails werden angezeigt
 -   Anbindung an eine MySql Datenbank

Probleme:
 -  Einarbeitung in eine nicht bekannte Programmiersprache und in Programmierung einer Web App
 -  Blazor Web Assembly konnte nur schwer mit der Datenbank verknüpfen da es ein Front end Framework ist und eine API benötigt hätte
 -  Blazor Webassembly hat im speziellen ein Problem sich mit einer MySql Datenbank zu verbinden
 -  Nur mit einer Blazor Web Assembly Application konnte eine progressive Web App erstellt werden	
 -  Auch bei einem lesenden ZUgriff auf die Datenbank können noch falsche Informationen übermittelt werden
   