# Flujo recomendado para trabajar con IA en esta presentación

## Archivos principales

```text
slides/slides.md       contenido
slides/style.css       diseño
slides/assets/         imágenes, GIFs y videos
```

## Comandos normales

```powershell
npm run slides:dev
npm run slides:build
npm start
```

## Prompt recomendado para pedirme cambios

```text
Quiero modificar la presentación Slidev.
Archivo principal: slides/slides.md.
Estilo: slides/style.css.
Quiero cambiar las slides [número o título].
Objetivo didáctico:
Texto que quiero conservar:
Texto que quiero mejorar:
Recursos disponibles:
Restricciones:
- lenguaje para bachillerato
- evitar tecnicismos innecesarios
- mantener estilo limpio tipo documentación Slidev
- no usar imágenes recortadas como fondo salvo que lo pida
Dame un bloque Markdown listo para pegar o un script Python que modifique los archivos.
```

## Integración con IA en VS Code / agentes

Puedes instalar la extensión de Slidev para VS Code y la skill de Slidev en agentes compatibles:

```powershell
npx skills add slidevjs/slidev
```
