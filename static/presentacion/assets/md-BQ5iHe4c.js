import{E as e,Q as t,_ as n,_t as r,v as i,x as a,yt as o,z as s}from"./modules/shiki-DgM9Q0bi.js";import{nt as c,rt as l}from"./index-tlN_EetR.js";import{t as u}from"./slidev/default-Cm5SlYWo.js";var d={__name:`slides.md__slidev_9`,setup(d){let{$slidev:f,$nav:p,$clicksContext:m,$clicks:h,$page:g,$renderContext:_,$frontmatter:v}=l();return m.setup(),(l,d)=>(s(),i(u,o(e(r(c)(r(v),8))),{default:t(()=>[...d[0]||=[n(`p`,{class:`eyebrow`},`Escena 13`,-1),n(`h1`,null,`El reloj convierte instrucciones en tiempo`,-1),n(`div`,{class:`timing-deep`},[n(`div`,{class:`timing-code-panel`},[n(`div`,{class:`timing-code-card`,"aria-label":`Código Arduino que controla el LED`},[n(`span`,null,[n(`b`,null,`01`),a(` digitalWrite(LED_BUILTIN, HIGH);`)]),n(`span`,null,[n(`b`,null,`02`),a(` delay(1000);`)]),n(`span`,null,[n(`b`,null,`03`),a(` digitalWrite(LED_BUILTIN, LOW);`)]),n(`span`,null,[n(`b`,null,`04`),a(` delay(1000);`)]),n(`i`,{class:`code-scan`})]),n(`pre`,null,[n(`code`,null,`<div class="assembly-window" aria-label="Instrucciones tipo ensamblador">
  <div><b>STR</b><span>HIGH → registro GPIO</span><small>escritura a periférico</small></div>
  <div><b>LDR</b><span>R0 ← contador ms</span><small>leer tiempo acumulado</small></div>
  <div><b>CMP</b><span>elapsed, #1000</span><small>comparar contra 1 s</small></div>
  <div><b>BNE</b><span>wait_loop</span><small>seguir esperando</small></div>
</div>
`)])]),n(`div`,{class:`clock-lab`,"aria-label":`Modelo de oscilador, frecuencia, ciclos y temporizador`},[n(`div`,{class:`osc-core`},[n(`b`,null,`Oscilador`),n(`small`,null,`genera el pulso base`),n(`span`,null,`F_CPU`)]),n(`pre`,null,[n(`code`,null,`<div class="wave-scope">
  <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
  <i class="cycle-runner"></i>
</div>

<div class="cycle-math">
  <div><b>frecuencia</b><span>ciclos / segundo</span></div>
  <div><b>ciclo</b><span>unidad mínima de ritmo</span></div>
  <div><b>instrucción</b><span>consume varios ciclos</span></div>
</div>

<div class="delay-engine">
  <div class="timer-ring"><span>1000 ms</span></div>
  <div class="delay-steps">
    <div><b>1</b><span>SysTick/timer recibe pulsos</span></div>
    <div><b>2</b><span>prescaler baja la frecuencia</span></div>
    <div><b>3</b><span>contador acumula milisegundos</span></div>
    <div><b>4</b><span>cuando llega a 1000, avanza</span></div>
  </div>
</div>

<a href="../actividades/primer-parpadeo" target="_top" class="mcu-prepare-link timing-next-link" aria-label="Ir a la Actividad 2 Primer parpadeo">
  <span class="mcu-prepare-kicker">Siguiente actividad</span>
  <strong>Actividad 2: primer parpadeo</strong>
  <small>controlar GPIO, LED y tiempos</small>
  <span class="mcu-prepare-arrow">-&gt;</span>
</a>
`)])])],-1)]]),_:1},16))}};export{d as default};