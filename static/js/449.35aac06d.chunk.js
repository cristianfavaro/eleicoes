"use strict";(self.webpackChunkfrontend=self.webpackChunkfrontend||[]).push([[449],{449:(e,n,t)=>{t.r(n),t.d(n,{default:()=>o});t(791);var r=t(818),s=t(92),a=t(184);const o=function(){const{ele:e}=(0,s.M)();return(0,a.jsx)(r.Z,{urlData:"https://raw.githubusercontent.com/cristianfavaro/eleicoes/main/app/frontend/data/eleicoes/".concat(e,"/br/br.json"),urlBrief:"https://raw.githubusercontent.com/cristianfavaro/eleicoes/main/app/frontend/data/eleicoes/".concat(e,"/br/muns.json"),urlMap:"https://raw.githubusercontent.com/cristianfavaro/eleicoes/main/app/frontend/data/maps/br-mun.json",joinFunc:function(e,n){return e.map((e=>({...e,properties:{...e.properties,data:n[e.properties.cd]?{...n[e.properties.cd],c:n[e.properties.cd].c.sort((function(e,n){return Number(e.vap)===Number(n.vap)?0:Number(e.vap)<n.vap?1:-1}))}:null}})))}})}},818:(e,n,t)=>{t.d(n,{Z:()=>q});var r=t(168),s=t(791),a=t(646);const o=()=>{const[e,n]=s.useState({x:null,y:null});return s.useEffect((()=>{const e=e=>{n({x:e.clientX,y:e.clientY})};return window.addEventListener("mousemove",e),()=>{window.removeEventListener("mousemove",e)}}),[]),e};function i(e){return Math.abs(e)>999999?Math.sign(e)*(Math.abs(e)/1e6).toFixed(2)+"kk":Math.abs(e)>999?Math.sign(e)*(Math.abs(e)/1e3).toFixed(2)+"k":Math.sign(e)*Math.abs(e)}function c(e){var n;return null!==(n={PT:"#cc2d2d",PSDB:"#3237d9",REPUBLICANOS:"#6b3ee6",PSOL:"#3237d9",PDT:"#f0b52e",MDB:"#79e7eb",PCdoB:"#29c80a",PSB:"#a06f24",AGIR:"#88101d",PMN:"#d98040",CIDADANIA:"#f52f7b",PV:"#88121f",AVANTE:"#a4234e",PP:"#d7a7bc",PSTU:"#e672d7",PCB:"#bde815",PRTB:"#552fc1",DC:"#54baae",PCO:"#a659ad",PODE:"#8b62f0",PL:"#0aa974",PSD:"#ec2594",SOLIDARIEDADE:"#a238e1",NOVO:"#4487e7",REDE:"#a72732",PMB:"#ac9bd3",UP:"#9858f1","UNI\xc3O":"#92de3b",PRD:"#176ae2"}[e])&&void 0!==n?n:function(){for(var e="#",n=0;n<6;n++)e+="0123456789ABCDEF"[Math.floor(16*Math.random())];return e}()}var l,d,p=t(462);const u=p.ZP.div(l||(l=(0,r.Z)(["\n  height: 15px;\n  padding: 0.2rem 0;\n  display: flex;\n  .w3-grey{\n    background-color: gray;\n  }\n"]))),h=p.ZP.div.attrs((e=>{let{x:n,y:t}=e;return{style:{transform:"translateY(".concat(t,"px) translateX(").concat(n,"px)")}}}))(d||(d=(0,r.Z)(["\n  border: 1px solid darkgray;\n  background-color: white; \n  width: 200px;\n  position: fixed;\n  display: ",";\n  transition: transform 0.23s; //Sticking effect\n  pointer-events: none; /* Allow clicking trough the div */\n  border-radius: 5px;\n  \n  >div{\n    padding: 0.2rem;\n  }\n  \n  .cand{\n    display: flex;\n    justify-content: space-between;\n    small{\n      font-size: 0.6rem;\n    }\n    small:first-child{\n      width: 60%;\n      text-overflow: ellipsis;\n      white-space: nowrap;\n      overflow: hidden;\n    }\n  };\n"])),(e=>{let{$show:n}=e;return n?"block":"none"}));var m=t(184);const f=e=>{let{cand:n}=e;const{e:t,n:r,nmu:s,p:a,pvap:o,seq:c,st:l,vap:d}=n;return(0,m.jsxs)("div",{className:"cand",children:[(0,m.jsxs)("small",{children:[s," - ",a]}),(0,m.jsxs)("small",{children:[i(d)," (",o,"%)"]})]})},g=s.memo((e=>{let{cands:n}=e;return(0,m.jsx)(u,{children:n.map(((e,n)=>(0,m.jsx)("div",{className:"w3-grey",style:{width:"".concat(e.pvap.replace(",","."),"%"),backgroundColor:c(e.p)}},n)))})})),v=e=>{let{hovered:n,titleComponent:t}=e;const r=o();return(0,m.jsx)(h,{$show:n,x:r.x,y:r.y,children:n&&(0,m.jsxs)(s.Fragment,{children:[(0,m.jsx)(t,{selected:n}),(0,m.jsx)(g,{cands:n.properties.data.c}),(0,m.jsx)("div",{className:"cands",children:n.properties.data.c&&n.properties.data.c.slice(0,3).map(((e,n)=>(0,m.jsx)(f,{cand:e},n)))})]})})};v.defaultProps={properties:{data:{}},titleComponent:e=>{let{properties:n}=e;return(0,m.jsx)("span",{className:"header",children:(0,m.jsx)("b",{children:n.nm})})}};const x=v;var b;const j=p.ZP.div(b||(b=(0,r.Z)(["\n  display: flex;\n  grid-area: CT;\n  padding: 0 0.5rem;\n\n  >span{\n    position: absolute;\n    top: 80px;\n    margin: 0.5rem;\n    background-color: blue;\n    color: #fff;\n    border-radius: 50px;\n    padding: 0.2rem;\n    cursor: pointer;\n  }; \n\n  #map {\n    flex: 1 1 auto;\n    display: block;\n    width: 100%;\n    .place:hover {\n      stroke: black;\n      stroke-width: 1px;\n      cursor: pointer;\n    };\n  };\n"])));var w,k;const y=p.ZP.div(w||(w=(0,r.Z)(["\n    border: 1px solid lightgray;\n    height: 80vh;\n    overflow: auto;\n    grid-area: SB;\n    padding: 0 0.5rem 0 0.5rem;\n    \n    .top-container{\n        position: sticky;\n        display: flex;\n        top: 0;\n        justify-content: space-between;\n        background-color: white;\n        align-items: center;\n    };\n    \n    .header{\n        display: block;\n        font-weight: 600;\n    }\n"]))),C=p.ZP.div(k||(k=(0,r.Z)(["\n    display: flex;\n    align-items: center;\n    font-size: 0.5rem;\n    \n    border-bottom: 1px solid lightgray;\n    \n    b{\n        font-size: 0.8rem;\n    }\n    img{\n        height: 70px;\n        border-radius: 100%;\n    }\n    >div{\n        width: 100%;\n    }\n    .info{\n        display: flex;\n        width: 100%;\n        justify-content: space-between;\n        \n        div{\n            display: flex;\n            flex-direction: column;\n        }\n        .data{\n            >*{\n                display: flex;\n                justify-content: end;\n            }\n        }\n    };\n    .bar{\n        height: 10px;\n        background-color: lightgray;\n        >div{\n            height: 10px;\n        }\n    };\n"])));var P;const N=p.ZP.div(P||(P=(0,r.Z)(["\n    /* https://nikitahl.com/circle-progress-bar-css */\n\n    .progress-bar-container{\n        display: flex;\n        flex-direction: column;\n        justify-content: center;\n        align-items: center;\n    }\n    \n\n    @property --progress-value {\n        syntax: '<integer>';\n        inherits: false;\n        initial-value: 0;\n    };\n\n    @keyframes css-progress {\n        to { --progress-value: ","; }\n    }\n\n    .progress-bar {\n        width: 100px;\n        height: 100px;\n        border-radius: 50%;\n        /* to center the percentage value */\n        display: flex;\n        justify-content: center;\n        align-items: center;\n    }\n\n    .progress-bar::before {\n        counter-reset: percentage var(--progress-value);\n        content: counter(percentage) '%';\n    }\n\n    .css {\n    background: \n        radial-gradient(closest-side, white 79%, transparent 80% 100%, white 0),\n        conic-gradient("," calc(var(--progress-value) * 1%), #e2dede 0);\n        animation: css-progress 2s 1 forwards;\n    }\n\n    .css::before {\n        animation: css-progress 2s 1 forwards;\n    }\n\n    progress {\n        visibility: hidden;\n        width: 0;\n        height: 0;\n    };\n    small{\n        color: #7e7a7a;\n        padding: 0.3rem;\n    }\n\n"])),(e=>e.value),(e=>e.color)),S=e=>{let{value:n,color:t,title:r}=e;return(0,m.jsx)(N,{value:n,color:t,children:(0,m.jsxs)("div",{className:"progress-bar-container",children:[(0,m.jsx)("div",{className:"progress-bar css",children:(0,m.jsx)("progress",{})}),(0,m.jsx)("small",{children:r})]})})};S.defaultProps={title:"Urnas apuradas",value:40,color:"darkblue"};const D=S;var Z=t(92);const E=s.memo((e=>{let{img:n,e:t,n:r,nmu:s,p:a,pvap:o,vap:l,st:d}=e;return(0,m.jsxs)(C,{children:[(0,m.jsx)("img",{src:n,alt:"image"}),(0,m.jsxs)("div",{children:[(0,m.jsxs)("div",{className:"info",children:[(0,m.jsxs)("div",{className:"name",children:[(0,m.jsx)("b",{children:s}),(0,m.jsx)("span",{children:a})]}),(0,m.jsxs)("div",{className:"data",children:[(0,m.jsxs)("b",{children:[o,"%"]}),(0,m.jsxs)("span",{children:[i(l)," votos"]})]})]}),(0,m.jsx)("div",{className:"bar",children:o&&(0,m.jsx)("div",{style:{backgroundColor:c(a),width:"".concat(o.replace(",","."),"%")}})})]})]})}));E.defaultProps={img:"user.png"};const M=e=>{let{clicked:n,titleComponent:t}=e;return(0,m.jsxs)("div",{className:"top-container",children:[(0,m.jsxs)("div",{children:[(0,m.jsx)(t,{selected:n}),(0,m.jsxs)("small",{children:["Absten\xe7\xe3o: ",n.properties.data.pa,"%"]})]}),(0,m.jsx)(D,{value:parseFloat(n.properties.data.psa),title:"Se\xe7\xf5es apuradas"})]})};function B(e){let{clicked:n,data:t,titleComponent:r}=e;const a=n||t,o=n?n.properties.uf||n.properties.cd:"br",{ele:i}=(0,Z.M)();return(0,m.jsx)(y,{children:a&&a.properties.data&&(0,m.jsxs)(s.Fragment,{children:[(0,m.jsx)(M,{clicked:a,titleComponent:r}),a.properties.data.c.map(((e,n)=>(0,m.jsx)(E,{...e,img:"https://resultados.tse.jus.br/oficial/ele2022/".concat(i,"/fotos/").concat(["546","547"].indexOf(i)>-1?o.toLowerCase():"br","/").concat(e.sqcand,".jpeg")},n))),(0,m.jsx)(E,{nmu:"Brancos",vap:a.properties.data.vb,pvap:a.properties.data.pvb}),(0,m.jsx)(E,{nmu:"Nulos",vap:a.properties.data.vn,pvap:a.properties.data.ptvn})]})})}function A(e){let{method:n="GET",data:t={},params:r={}}=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};const{response:a,loading:o,error:i,fetchData:c}=function(e){let{method:n="GET",params:t={}}=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};const[r,a]=(0,s.useState)(!1),[o,i]=(0,s.useState)(!0),[c,l]=(0,s.useState)(!1);return{response:r,loading:o,error:c,fetchData:async function(){i(!0),l(!1),await fetch(e,{method:n,params:t}).then((e=>e.json())).then((e=>a(e))).catch((e=>l(e))),i(!1)}}}(e,{method:n,data:t,params:r});return(0,s.useEffect)((()=>{c()}),[]),{response:a,loading:o,error:i}}var O=t(87),F=t(223);const L=e=>{let{geojson:n,setClicked:t}=e;return(0,m.jsx)(F.Z,{isClearable:!0,loadOptions:e=>new Promise((t=>{t((e=>n.features.filter((n=>n.properties.nm.toLowerCase().includes(e.toLowerCase()))).map((e=>({value:e.properties.nm,label:e.properties.nm,selected:e}))).slice(0,15))(e))})),placeholder:"Digite o nome da localidade",onChange:e=>t(e?e.selected:null)})};var R;const T=p.ZP.div(R||(R=(0,r.Z)(["\n    grid-area: SH; \n    padding: 0.5rem;\n    display: flex;\n    width: 100%;\n    justify-content: space-evenly;\n    align-items: center;\n    a{\n        margin-right: 0.2rem;\n    }\n"]))),I=e=>{let{geojson:n,setClicked:t}=e;return(0,m.jsxs)(T,{children:[(0,m.jsx)(L,{geojson:n,setClicked:t}),(0,m.jsxs)("div",{children:[(0,m.jsx)(O.rU,{className:"btn btn-info btn-sm",to:"uf",children:"Estados"}),(0,m.jsx)(O.rU,{className:"btn btn-info btn-sm",to:"/",children:"Munic\xedpios"})]})]})};var U;function V(e){let{hovered:n,setHovered:t,geojson:r,colorScale:o,clicked:i,setClicked:c}=e;const l=(0,s.useRef)(),d=(0,s.useRef)();return(0,s.useEffect)((()=>{r&&function(e){const r=(0,a.Ys)(l.current),{width:s,height:p}=d.current.getBoundingClientRect(),u=(0,a.mw4)().fitSize([s,p],i||e).precision(100),h=(0,a.l49)().projection(u);r.selectAll(".place").data(e.features).join("path").on("mouseover",((e,r)=>{r!==n&&r.properties.data&&t(r)})).on("mouseout",(e=>t(null))).on("click",((e,n)=>{c(JSON.stringify(i)===JSON.stringify(n)?null:n)})).attr("class","place").transition().attr("stroke","#fff").attr("stroke-width","0.3px").attr("d",(e=>h(e))).attr("fill",(e=>o(e,i))).attr("opacity",(e=>e.properties.data&&"".concat(e.properties.data.c[0].pvap.replace(",","."),"%")))}(r)}),[r,i]),(0,m.jsxs)(j,{ref:d,children:[(0,m.jsx)(H,{clicked:i,setClicked:c}),(0,m.jsx)("svg",{id:"map",ref:l})]})}const z=e=>{let{urlData:n,urlMap:t,urlBrief:r,colorScale:o,joinFunc:i,titleComponent:c}=e;const{response:l,loading:d,error:p}=A(n),[u,h]=(0,s.useState)(null),[f,g]=(0,s.useState)(null),[v,b]=(0,s.useState)(!1);return(0,s.useEffect)((()=>{console.log(f)}),[f]),(0,s.useEffect)((()=>{Promise.all([(0,a.AVB)(r),(0,a.AVB)(t)]).then((e=>{let[n,t]=e;t.features=i(t.features,n),b(t)})).catch((e=>{console.error(e)}))}),[t,r]),(0,m.jsxs)(s.Fragment,{children:[(0,m.jsx)(I,{geojson:v,setClicked:g}),(0,m.jsx)(V,{colorScale:o,geojson:v,hovered:u,setHovered:h,clicked:f,setClicked:g}),(0,m.jsx)(B,{data:l&&G(l),clicked:f,titleComponent:c}),(0,m.jsx)(x,{titleComponent:c,hovered:u&&u||void 0})]})};function G(e){return{properties:{nm:"Brasil",data:{...e.brief,c:e.values}}}}const H=e=>{let{clicked:n,setClicked:t}=e;return n&&(0,m.jsx)("span",{onClick:()=>t(null),children:"< Voltar"})},Y=p.ZP.div(U||(U=(0,r.Z)([""])));z.defaultProps={joinFunc:function(e,n){return e},colorScale:(e,n)=>e.properties.data?n?n.properties.nm===e.properties.nm?c(e.properties.data.c[0].p):"gray":c(e.properties.data.c[0].p):"white",titleComponent:e=>{let{selected:n}=e;return(0,m.jsxs)(Y,{className:"header",children:[n&&n.properties.nm," "]})}};const q=z}}]);
//# sourceMappingURL=449.35aac06d.chunk.js.map