import{E as e,Q as t,_ as n,_t as r,v as i,yt as a,z as o}from"./modules/shiki-DgM9Q0bi.js";import{nt as s,rt as c}from"./index-IkxV_qc0.js";import{t as l}from"./slidev/default-Cm5SlYWo.js";var u={__name:`slides.md__slidev_9`,setup(u){let{$slidev:d,$nav:f,$clicksContext:p,$clicks:m,$page:h,$renderContext:g,$frontmatter:_}=c();return p.setup(),(c,u)=>(o(),i(l,a(e(r(s)(r(_),8))),{default:t(()=>[...u[0]||=[n(`p`,{class:`eyebrow`},`Escena 13`,-1),n(`h1`,null,`El reloj convierte instrucciones en tiempo`,-1),n(`div`,{class:`timing-machine`},[n(`div`,{class:`timing-left`},[n(`pre`,{class:`code-card`},[n(`code`,null,`digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
digitalWrite(LED_BUILTIN, LOW);
delay(1000);`)]),n(`pre`,null,[n(`code`,null,`<div class="asm-strip">
  <span>STR HIGH, [GPIO]</span>
  <span>LDR R0, millis()</span>
  <span>CMP elapsed, #1000</span>
  <span>BNE wait_loop</span>
</div>
`)])]),n(`div`,{class:`timing-right`},[n(`div`,{class:`oscillator-model`},[n(`div`,{class:`oscillator-chip`},[n(`b`,null,`Oscilador`),n(`small`,null,`pulso estable`)]),n(`div`,{class:`clock-train`,"aria-label":`Pulsos de reloj`},[n(`span`),n(`span`),n(`span`),n(`span`),n(`span`),n(`span`),n(`span`),n(`span`)]),n(`div`,{class:`frequency-note`},[n(`b`,null,`F_CPU`),n(`span`,null,`millones de ciclos por segundo, según la configuración del core`)])]),n(`pre`,null,[n(`code`,null,`<div class="timer-pipeline">
  <div><b>1</b><span>oscilador genera ciclos</span></div>
  <div><b>2</b><span>prescaler divide la frecuencia</span></div>
  <div><b>3</b><span>timer/SysTick acumula milisegundos</span></div>
  <div><b>4</b><span>\`delay()\` espera hasta cumplir 1000 ms</span></div>
</div>

<a href="../actividades/tiempo-dentro-del-chip" target="_top" class="mcu-prepare-link theory-activity-link" aria-label="Regresar a la Actividad 1 Código memoria y tiempo">
  <span class="mcu-prepare-kicker">Regresar</span>
  <strong>Actividad 1: código, memoria y tiempo</strong>
  <small>probar delays y dibujar el flujo interno</small>
  <span class="mcu-prepare-arrow">-&gt;</span>
</a>
`)])])],-1)]]),_:1},16))}};export{u as default};