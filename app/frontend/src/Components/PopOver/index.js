import React, {useEffect, useRef} from 'react';
import styled from 'styled-components';
import useMousePosition from '../../hooks/useMousePosition';
import {kFormatter} from '../../utils/kFormatter';
import { colorPicker } from '../../utils/colorPicker';
import { Container, BarContainer } from './styles';


const Cand = ({cand}) => {
  const {e, n, nmu, p, pvap, seq, st, vap} = cand; 
  return <div className="cand">
    <small>{nmu} - {p}</small> 
    <small>{kFormatter(vap)} ({pvap}%)</small>
  </div>
}


const Bar =  React.memo(({cands}) => {

  return <BarContainer>
    {
      cands.map(
        (cand, i)=> <div
          key={i}
          className="w3-grey" 
          style={{
            width: `${cand.pvap.replace(",", ".")}%`,
            backgroundColor: colorPicker(cand.p),
          }}
        />
      )
    }
    
  </BarContainer>
})

const PopOver = ({properties}) => {
  const {a, c, pa, vb, vn} = properties.data;
  const mousePosition = useMousePosition();

  useEffect(()=>{
    if(popOverRef.current){
      popOverRef.current.style.transform = `translateY(${+mousePosition.y + 10}px)`;
      popOverRef.current.style.transform += `translateX(${+mousePosition.x + 10}px)`;            
    };
  }, [mousePosition])
  
  const popOverRef = useRef(null);

  return <Container ref={popOverRef}>

    <div className="header"><b>{properties.cd}</b></div>
    <Bar cands={c}/>
    <div className="cands">
      {
        c.slice(0, 3).map( (cand, i)=> <Cand key={i} cand={cand}/>)
      }
    </div>
    
  </Container>
}

export default PopOver