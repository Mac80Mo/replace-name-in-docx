# Name Replace Script

## ∎∎ Beschreibung
Dieses Python-Skript durchsucht alle `.docx`-Dateien in einem angegebenen Quellordner und ersetzt einen bestimmten Namen durch einen neuen. Die bearbeiteten Dateien werden im Zielordner gespeichert und optional mit einem benutzerdefinierten Suffix versehen.

## 🗂 Ordnerstruktur
```
Projektverzeichnis/
│-- Source/          # Original-Dokumente (.docx)
│-- Destination/     # Bearbeitete Dokumente
│-- main.py          # Python-Skript
│-- .gitignore       # (Falls gewünscht, um Source & Destination zu ignorieren)
│-- README.md        # Diese Datei
```

## ⚡ Nutzung
1. **Python & Abhängigkeiten installieren** (falls nicht bereits vorhanden):
   ```bash
   pip install python-docx
   ```
2. **Skript ausführen:**
   ```bash
   python main.py
   ```

## 🎨 Anpassbare Parameter
Die folgenden Parameter können in `main.py` geändert werden:
```python
source_dir = "./Source"  # Quellordner mit Originaldateien
destination_dir = "./Destination"  # Zielordner für bearbeitete Dateien
old_name = "Max Mustermann"  # Der Name, der ersetzt wird
new_name = "Dein Name"  # Neuer Name
filename_suffix = ""  # Optional: Text, der an den Dateinamen angehängt wird
```

### 🔧 Beispiel
Wenn `filename_suffix = "Name"` gesetzt ist:
- `Bericht.docx` → `Bericht_Name.docx`
- `Protokoll.docx` → `Protokoll_Name.docx`

Falls `filename_suffix = ""`, bleibt der ursprüngliche Dateiname erhalten.

## ⛔ Ignorieren von Source & Destination in Git
Falls du die Ordner von Git ausschließen möchtest, füge dies in `.gitignore` hinzu:
```
Source/
Destination/
```
Falls du nur den Inhalt ignorieren willst, aber die Ordner behalten möchtest:
```
Source/*
Destination/*
!.gitkeep
```

## ✅ Features
✅ Automatische Namensersetzung in `.docx`-Dateien  
✅ Beibehaltung des Originaldateinamens mit optionalem Suffix  
✅ Bearbeitete Dateien werden in einem separaten Ordner gespeichert  
✅ Funktioniert mit Absätzen & Tabellen  
✅ Unterstützung für beliebig viele Dateien im Quellordner  

---
📡 **Lizenz:** MIT  
 


