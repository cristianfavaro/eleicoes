import React, {useEffect, useState} from "react";
import { kFormatter } from "../../../utils/kFormatter";
import { colorPicker } from "../../../utils/colorPicker";
import { Container, CandContainer } from "./styles";
import CircleProgress from "../../../utils/CircleProgress";


const Cand = React.memo(({img, e, n, nmu, p, pvap, vap, st}) => {
  
  return <CandContainer>
    {
      <img src={img} alt="image" />
    }
    <div>
        <div className="info">
            <div className="name">
                <b>{nmu}</b>
                <span>{p}</span>
            </div>
            <div className="data">
                <b>{pvap}%</b>
                <span>{kFormatter(vap)} votos</span>
            </div>    
        </div>
        <div className="bar">
            {
                pvap && <div style={{backgroundColor: colorPicker(p), width: `${pvap.replace(",", ".")}%`}}></div>
            }
        </div>
    </div>
    
  </CandContainer>
})

Cand.defaultProps = {
  img: "user.png",
}

const Header = ({clicked, titleComponent: Title}) =>{
  return <div className="top-container">
      <div> 
        <Title selected={clicked}/>
        
        <small>Abstenção: {clicked.properties.data.pa}%</small>
      </div>

      <CircleProgress
        value={parseFloat(clicked.properties.data.psa)}
        title="Seções apuradas"
      />    
  </div>
}



export default function Panel({clicked, data, titleComponent}){

  const selected = clicked ? clicked : data;

  return selected && 
    selected.properties.data &&  <Container>
    <Header clicked={selected} titleComponent={titleComponent}/>
    {
      selected.properties.data.c.map(
        (cand, i) => <Cand 
                      key={i}
                      {...cand}
                      img={`https://resultados.tse.jus.br/oficial/ele2022/544/fotos/br/${cand.sqcand}.jpeg`}
                    />
      )
    }
    <Cand nmu="Brancos" vap={selected.properties.data.vb} pvap={selected.properties.data.pvb}/>
    <Cand nmu="Nulos" vap={selected.properties.data.vn} pvap={selected.properties.data.ptvn}/>
        
  </Container>
}