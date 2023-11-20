import React, {useEffect, useRef} from 'react';
import styled from 'styled-components';
import useMousePosition from '../../hooks/useMousePosition';
import {kFormatter} from '../../utils/kFormatter';
import { colorPicker } from '../../utils/colorPicker';

const Container = styled.div`
  border: 1px solid darkgray;
  background-color: white; 
  width: 200px;
  position: fixed;
  transition: transform 0.23s; Sticking effect
  pointer-events: none; /* Allow clicking trough the div */
  border-radius: 5px;

  .header{
    background-color: lightblue;
    font-size: small;
  }
  >div{
    padding: 0.2rem;
  }
  
  .cand{
    display: flex;
    justify-content: space-between;
    small{
      font-size: 0.6rem;
    }
    small:first-child{
      width: 60%;
      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;
    }
  };
`

const Cand = ({cand}) => {
  const {e, n, nmu, p, pvap, seq, st, vap} = cand; 
  return <div className="cand">
    <small>{nmu} - {p}</small> 
    <small>{kFormatter(vap)} ({pvap}%)</small>
  </div>
}

const BarContainer = styled.div`
  height: 15px;
  padding: 0.2rem 0;
  display: flex;
  .w3-grey{
    background-color: gray;
  }
`

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