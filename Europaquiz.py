from cairosvg import svg2png
from PIL import Image

# Pfad zur Vektorgrafik (SVG)
svg_file = 'EuropaleereKarte.svg'  # Ersetze 'deine_vektorgrafik.svg' durch den Dateinamen deiner Vektorgrafik

# Konvertiere die Vektorgrafik in ein Rasterbild (PNG)
png_data = svg2png(url=svg_file)
with open('temp.png', 'wb') as f:
    f.write(png_data)

# Öffne und zeige das Rasterbild mit Pillow
image = Image.open('temp.png')
image.show()
