import{$ as e,B as t,D as n,T as r,U as i,_ as a,b as o,bt as s,v as c,vt as l,x as u,xt as d,y as f}from"../modules/shiki-BJVPiDca.js";import{nt as p,rt as m}from"../index-DBlocvy_.js";function h(e){return e.startsWith(`/`)?`/mi-primer-nodo-iot-ambiental/presentacion/`+e.slice(1):e}function g(e,t=!1){let n=e&&[`#`,`rgb`,`hsl`].some(t=>e.indexOf(t)===0),r={background:n?e:void 0,color:e&&!n?`white`:void 0,backgroundImage:n?void 0:e?t?`linear-gradient(#0005, #0008), url(${h(e)})`:`url("${h(e)}")`:void 0,backgroundRepeat:`no-repeat`,backgroundPosition:`center`,backgroundSize:`cover`};return r.background||delete r.background,r}var _={class:`my-auto w-full`},v=r({__name:`cover`,props:{background:{default:``}},setup(e){let{$slidev:n,$nav:r,$clicksContext:o,$clicks:s,$page:l,$renderContext:f,$frontmatter:p}=m(),h=e,v=a(()=>g(h.background,!0));return(e,n)=>(t(),u(`div`,{class:`slidev-layout cover`,style:d(v.value)},[c(`div`,_,[i(e.$slots,`default`)])],4))}}),y={__name:`slides.md__slidev_1`,setup(r){let{$slidev:i,$nav:a,$clicksContext:u,$clicks:d,$page:h,$renderContext:g,$frontmatter:_}=m();return u.setup(),(r,i)=>(t(),f(v,s(n(l(p)(l(_),0))),{default:e(()=>[o(`
GUÍA RÁPIDA PARA EDITAR

1. Cada diapositiva está separada por:
   ---

2. Para poner una imagen:
   ![Texto alternativo](./assets/imagenes/mi-imagen.jpg)

3. Para poner un GIF:
   ![Animación](./assets/gifs/transistor.gif)

4. Para poner video:
   <video controls class="media-video">
     <source src="./assets/videos/desierto.mp4" type="video/mp4" />
   </video>

5. Para que un enlace salga del recuadro de Docusaurus:
   target="_top"
`),i[0]||=c(`div`,{class:`cover-scene`},[c(`p`,{class:`kicker`},`Taller IoT ambiental`),c(`h1`,null,`De la arena al sensor inteligente`),c(`p`,{class:`subtitle`},` Una historia sobre materia, electricidad, microcontroladores y ciudades que aprenden a observarse. `),c(`div`,{class:`mt-10 flex gap-4 justify-center`},[c(`a`,{href:`../actividades/antes-de-empezar`,target:`_top`,class:`btn-main`},`Ir a actividades`)])],-1)]),_:1},16))}};export{y as default};