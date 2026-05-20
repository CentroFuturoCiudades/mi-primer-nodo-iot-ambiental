# actualizar_slides_mineria_y_materiales.py
# Corrige las primeras slides de Slidev:
# - Usa la imagen real de minería / minerales como escena documental.
# - Quita las imágenes SVG raras de image-right.
# - Deja conductores, aislantes y semiconductores como tarjetas hechas con código.
#
# Uso:
#   1) Guarda este archivo en la raíz del proyecto.
#   2) Guarda mineria-tierras-raras.png junto a este archivo.
#   3) Ejecuta:
#        python .\actualizar_slides_mineria_y_materiales.py
#        npm run slides:dev
#
# Después:
#        npm run slides:build
#        npm start

from pathlib import Path
import shutil

ROOT = Path.cwd()
slides_path = ROOT / "slides" / "slides.md"
style_path = ROOT / "slides" / "style.css"

if not slides_path.exists():
    raise FileNotFoundError("No encontré slides/slides.md. Ejecuta este script desde la raíz del proyecto.")

# 1) Copiar imagen real de minería
src_img = ROOT / "mineria-tierras-raras.png"
dst_img = ROOT / "slides" / "assets" / "imagenes" / "mineria-tierras-raras.png"
dst_img.parent.mkdir(parents=True, exist_ok=True)

if src_img.exists():
    shutil.copy(src_img, dst_img)
    print(f"OK: imagen copiada a {dst_img}")
else:
    print("AVISO: No encontré mineria-tierras-raras.png junto al script.")
    print("       Puedes copiar tu foto manualmente a:")
    print(f"       {dst_img}")

# 2) Reemplazar bloque inicial desde Escena 2 hasta antes del transistor
text = slides_path.read_text(encoding="utf-8")

start_marker = '<p class="kicker">Escena 2'
start = text.find(start_marker)

possible_end_markers = [
    '<p class="kicker">Escena 5 — Transistor</p>',
    '<p class="kicker">Escena 6 — Transistor</p>',
    '<p class="kicker">Escena 5 - Transistor</p>',
    '<p class="kicker">Escena 6 - Transistor</p>',
]

end = -1
for marker in possible_end_markers:
    end = text.find(marker)
    if end != -1:
        break

if start == -1 or end == -1:
    raise ValueError(
        "No encontré los marcadores esperados. Busca en slides.md 'Escena 2' y 'Transistor'."
    )

new_block = r'''
<p class="kicker">Escena 2 — De la Tierra al chip</p>

# Minerales, elementos y materiales electrónicos

<div class="mining-scene">
  <img src="./assets/imagenes/mineria-tierras-raras.png" />

  <div class="mining-overlay">
    <p class="kicker">De la Tierra al chip</p>
    <h2>Antes del sensor, hubo materiales</h2>
    <p>
      Un microcontrolador no aparece de la nada: está hecho con materiales que vienen de la Tierra
      y que después se transforman con muchísima precisión.
    </p>
  </div>
</div>

---

<p class="kicker">Escena 3 — Precisión importante</p>

# No todo mineral se convierte en chip

<div class="documentary-grid">
  <div class="doc-card">
    <span>1</span>
    <h2>Minerales</h2>
    <p>Son materiales naturales que se extraen de la Tierra. Algunos contienen elementos útiles para tecnología.</p>
  </div>

  <div class="doc-card">
    <span>2</span>
    <h2>Elementos</h2>
    <p>De ciertos minerales se obtienen elementos como silicio, cobre, aluminio y otros materiales importantes.</p>
  </div>

  <div class="doc-card">
    <span>3</span>
    <h2>Materiales electrónicos</h2>
    <p>Después de purificarlos y procesarlos, pueden formar cables, sensores, baterías, pantallas o chips.</p>
  </div>
</div>

<v-click>

<div class="note-box dark-note">
  Para los chips, el silicio es uno de los materiales más importantes. Las tierras raras son importantes en muchas tecnologías, pero no son “la base” de todos los chips.
</div>

</v-click>

---

<p class="kicker">Escena 4 — Tres comportamientos eléctricos</p>

# Conductores, aislantes y semiconductores

<div class="material-cards">
  <div class="material-card conductor">
    <div class="material-icon">⚡</div>
    <h2>Conductor</h2>
    <p>Deja pasar corriente con facilidad.</p>
    <strong>Ejemplos: cobre, aluminio, oro.</strong>
  </div>

  <div class="material-card insulator">
    <div class="material-icon">■</div>
    <h2>Aislante</h2>
    <p>Dificulta o bloquea el paso de corriente.</p>
    <strong>Ejemplos: plástico, vidrio, cerámica.</strong>
  </div>

  <div class="material-card semiconductor">
    <div class="material-icon">◐</div>
    <h2>Semiconductor</h2>
    <p>Puede cambiar su comportamiento si lo controlamos.</p>
    <strong>Ejemplo: silicio.</strong>
  </div>
</div>

<v-click>

## <span class="accent">La clave de un chip no es solo tener electricidad: es poder controlarla.</span>

</v-click>

---

<p class="kicker">Escena 5 — La idea que conecta todo</p>

# Un semiconductor permite construir decisiones

<div class="decision-scene">
  <div class="decision-box off">
    <span>0</span>
    <p>bloquea corriente</p>
  </div>

  <div class="decision-arrow">↔</div>

  <div class="decision-box on">
    <span>1</span>
    <p>deja pasar corriente</p>
  </div>
</div>

<v-clicks>

- Con un comportamiento controlable podemos representar ceros y unos.
- Con ceros y unos podemos construir instrucciones.
- Con instrucciones podemos prender un LED, esperar un segundo o leer un sensor.

</v-clicks>

## <span class="accent">Aquí empieza el camino hacia el transistor.</span>

---

'''

updated = text[:start] + new_block + text[end:]
slides_path.write_text(updated, encoding="utf-8")
print("OK: slides/slides.md actualizado.")

# 3) Añadir CSS robusto sin romper lo anterior
css_patch = r'''
/* ============================================================
   Bloque documental: minería, materiales y semiconductores
   ============================================================ */

.mining-scene {
  position: relative;
  width: 100%;
  height: 560px;
  overflow: hidden;
  border-radius: 28px;
  box-shadow: 0 28px 80px rgba(0,0,0,.35);
  background: #000;
}

.mining-scene img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  filter: saturate(1.05) contrast(1.05);
}

.mining-scene::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(0,0,0,.78), rgba(0,0,0,.42), rgba(0,0,0,.08)),
    linear-gradient(0deg, rgba(0,0,0,.45), transparent 45%);
}

.mining-overlay {
  position: absolute;
  left: 52px;
  bottom: 48px;
  z-index: 2;
  max-width: 760px;
  color: white;
  text-align: left;
}

.mining-overlay h2 {
  font-size: 3.4rem;
  line-height: .95;
  font-weight: 950;
  letter-spacing: -0.06em;
  margin: .5rem 0 1rem 0;
}

.mining-overlay p {
  font-size: 1.25rem;
  line-height: 1.35;
  color: rgba(255,255,255,.82);
}

.documentary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.15rem;
  margin-top: 2rem;
}

.doc-card {
  text-align: left;
  padding: 1.1rem;
  min-height: 260px;
  border-radius: 1.3rem;
  background:
    radial-gradient(circle at top right, rgba(245,176,65,.14), transparent 38%),
    rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
}

.doc-card span {
  display: inline-grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 999px;
  background: rgba(0,184,148,.22);
  border: 1px solid rgba(0,184,148,.55);
  color: #00b894;
  font-weight: 950;
  margin-bottom: .8rem;
}

.doc-card h2 {
  font-size: 1.45rem;
  margin-bottom: .55rem;
}

.doc-card p {
  font-size: 1rem;
  color: rgba(255,255,255,.78);
  line-height: 1.38;
}

.dark-note {
  color: white !important;
  background: rgba(0,184,148,.18) !important;
}

.material-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.1rem;
  margin-top: 2.2rem;
}

.material-card {
  text-align: left;
  min-height: 330px;
  border-radius: 1.5rem;
  padding: 1.25rem;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
  box-shadow: 0 20px 60px rgba(0,0,0,.18);
}

.material-card h2 {
  font-size: 1.7rem;
  margin: .7rem 0 .8rem;
}

.material-card p {
  font-size: 1.08rem;
  line-height: 1.35;
  color: rgba(255,255,255,.78);
}

.material-card strong {
  display: block;
  color: #f5b041;
  margin-top: 1rem;
  font-size: .98rem;
}

.material-icon {
  display: grid;
  place-items: center;
  width: 72px;
  height: 72px;
  border-radius: 1rem;
  font-size: 2.2rem;
  background: rgba(255,255,255,.1);
}

.material-card.conductor {
  border-color: rgba(245,176,65,.45);
}

.material-card.insulator {
  border-color: rgba(255,255,255,.22);
}

.material-card.semiconductor {
  border-color: rgba(0,184,148,.9);
  box-shadow: 0 0 50px rgba(0,184,148,.16);
}

.decision-scene {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;
  margin: 2.5rem 0 1.5rem;
}

.decision-box {
  width: 270px;
  height: 180px;
  border-radius: 1.4rem;
  display: grid;
  place-items: center;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
}

.decision-box span {
  font-size: 4rem;
  font-weight: 950;
  color: #00b894;
  line-height: 1;
}

.decision-box p {
  margin: 0;
  color: rgba(255,255,255,.78);
  font-weight: 800;
}

.decision-box.on {
  border-color: #00b894;
  background: rgba(0,184,148,.17);
}

.decision-arrow {
  font-size: 4rem;
  color: #f5b041;
  font-weight: 950;
}
'''

existing_css = style_path.read_text(encoding="utf-8") if style_path.exists() else ""
if "Bloque documental: minería, materiales y semiconductores" not in existing_css:
    style_path.write_text(existing_css.rstrip() + "\n\n" + css_patch.strip() + "\n", encoding="utf-8")
    print("OK: slides/style.css actualizado.")
else:
    print("OK: slides/style.css ya tenía este bloque.")

print("\nListo. Ahora corre:")
print("  npm run slides:dev")
print("\nCuando te guste:")
print("  npm run slides:build")
print("  npm start")
