import React, {useEffect, useRef} from 'react';
import styled from 'styled-components';
import useMousePosition from '../../hooks/useMousePosition';
import {kFormatter} from '../../utils/kFormatter';

const Container = styled.div`
  border: 2px solid black;
  background-color: white;
  width: 200px;
  position: fixed;
  /* display: ${ props => props.show ? "block" : "none"};   */
  transition: transform 0.23s; /* Sticking effect */
  pointer-events: none; /* Allow clicking trough the div */
  
  border-radius: 5px;
  .header{
    background-color: lightgray;
  }
  .cand{
    display: flex;
    justify-content: space-between;
    small{
      font-size: 0.6rem;
    }
    small:first-child{
      width: 60%;
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

const PopOver = ({properties}) => {
  const {a, c, pa, vb, vn} = properties.data;
  const mousePosition = useMousePosition();

  const cands = c.sort(function(a,b){
    if(Number(a.vap) === Number(b.vap)){
      return 0
    }else{
      return Number(a.vap) < (b.vap) ? 1 : -1;
    }
  })

  useEffect(()=>{
    if(popOverRef.current){
      popOverRef.current.style.transform = `translateY(${+mousePosition.y + 10}px)`;
      popOverRef.current.style.transform += `translateX(${+mousePosition.x + 10}px)`;            
    };
  }, [mousePosition])
  
  const popOverRef = useRef(null);

  return <Container ref={popOverRef}>

    <div className="header">{properties.cd}</div>
    
    <div>bar</div>

    <div className="cands">
      {
        cands.slice(0, 3).map( (cand, i)=> <Cand key={i} cand={cand}/>)
      }
    </div>
    
  </Container>
}

export default PopOver