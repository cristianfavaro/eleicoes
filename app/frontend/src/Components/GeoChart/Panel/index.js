import React, {useEffect} from "react";
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

const Header = ({clicked, headerField}) =>{
  return <div className="header">
      <div>
        <h4>{clicked && clicked.properties[headerField]}</h4>
        <small>Abstenção: {clicked.properties.data.pa}%</small>
      </div>

      <CircleProgress
        value={parseFloat(clicked.properties.data.psa)}
        title="Seções apuradas"
      />    
  </div>
}

export default function Panel({clicked, headerField}){
    useEffect(()=>{
      console.log(clicked, ' vendo aqui')
    }, [clicked])

    return clicked && clicked.properties.data &&  <Container>
      <Header headerField={headerField} clicked={clicked}/>
      {
        clicked.properties.data.c.map(
          (cand, i) => <Cand 
                        key={i}
                        {...cand}
                        img={`https://resultados.tse.jus.br/oficial/ele2022/544/fotos/br/${cand.sqcand}.jpeg`}
                      />
        )
      }
      <Cand nmu="Brancos" vap={clicked.properties.data.vb} pvap={clicked.properties.data.pvb}/>
      <Cand nmu="Nulos" vap={clicked.properties.data.vn} pvap={clicked.properties.data.ptvn}/>
         
    </Container>
  }