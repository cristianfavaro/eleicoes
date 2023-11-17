import React, {useEffect, useRef} from 'react';
import styled from 'styled-components';
import useMousePosition from '../../hooks/useMousePosition';

const Container = styled.div`
  border: 2px solid black;
  background-color: white;
  width: 200px;
  position: fixed;
  display: ${ props => props.show ? "block" : "none"};  
  transition: transform 0.23s; /* Sticking effect */
  pointer-events: none; /* Allow clicking trough the div */
  
  border-radius: 5px;
  .header{
    background-color: lightgray;
  }
  .cand{
    display: flex;
    justify-content: space-between;
  };
`

const Cand = () => {

  return <div className="cand">
    <small>Nome - Partido</small> 
    <small>votos (%)</small>
  </div>
}

const PopOver = ({data, show}) => {

  const popOverRef = useRef(null);
  const mousePosition = useMousePosition();

  useEffect(()=>{

    popOverRef.current.style.transform = `translateY(${+mousePosition.y + 10}px)`;
    popOverRef.current.style.transform += `translateX(${+mousePosition.x + 10}px)`;            
      
    return 

  }, [mousePosition])

  return <Container show={show} ref={popOverRef}>
    <div className="header">{data && data.properties.cd}</div>
    
    <div>bar</div>

    <div className="cands">
      <Cand/>
      <Cand/>
      <Cand/>
    </div>
    
  </Container>
}

export default PopOver