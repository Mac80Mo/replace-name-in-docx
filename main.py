from docx import Document

def replace_name_in_docx(input_file, output_file, old_name, new_name):
    # Öffne das Word-Dokument
    doc = Document(input_file)
    
    # Durchlaufe alle Absätze und ersetze den Namen
    for para in doc.paragraphs:
        if old_name in para.text:
            para.text = para.text.replace(old_name, new_name)
    
    # Durchlaufe alle Tabelle (falls der Name in Tabellen vorkommt)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if old_name in cell.text:
                    cell.text = cell.text.replace(old_name, new_name)
                    
    # Speichere das bearbeitete Dokument
    doc.save(output_file)
    print(f"Ersetzung abgeschlossen! Neue Datei gespeichert als: {output_file}")

# Aufruf:
input_file = "original_bericht.docx"
output_file = "geänderter_bericht.docx"
old_name = "Max Mustermann"
new_name = "Mein Name"