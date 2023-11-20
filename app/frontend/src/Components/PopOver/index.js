import React, {useEffect, useRef} from 'react';
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
  const mousePosition = useMousePosition();
  return <Container show={properties.cd} x={mousePosition.x} y={mousePosition.y}>  
    {/* valido para ver se o properties nao ta vazio */}
    {
      properties.cd && <React.Fragment> 
          <div className="header"><b>{properties.cd}</b></div>
          <Bar cands={properties.data.c}/>
          <div className="cands">
            {
              properties.data.c && properties.data.c.slice(0, 3).map( (cand, i)=> <Cand key={i} cand={cand}/>)
            }
          </div>
      </React.Fragment>
    }
  </Container>
}

PopOver.defaultProps = {
  properties: {data: {}},
}

export default PopOver