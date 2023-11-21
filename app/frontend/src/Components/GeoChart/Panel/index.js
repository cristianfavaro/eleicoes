import React, {useEffect} from "react";
import styled from "styled-components";
import { kFormatter } from "../../../utils/kFormatter";
import { colorPicker } from "../../../utils/colorPicker";

const CandContainer = styled.div`
    display: flex;
    align-items: center;
    font-size: 0.5rem;
    border-bottom: 1px solid lightgray;
    
    b{
        font-size: 0.8rem;
    }
    img{
        height: 70px;
        border-radius: 100%;
    }
    >div{
        width: 100%;
    }
    .info{
        display: flex;
        width: 100%;
        justify-content: space-between;
        
        div{
            display: flex;
            flex-direction: column;
        }
        .data{
            >*{
                display: flex;
                justify-content: end;
            }
        }
    };
    .bar{
        height: 10px;
        background-color: lightgray;
        >div{
            height: 10px;
        }
    };
`

const Cand = ({cand}) => {
  const {e, n, nmu, p, pvap, vap, st} = cand;

  return <CandContainer>
    
    <img src="user.png" alt="image" />
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
            <div style={{backgroundColor: colorPicker(p), width: `${pvap.replace(",", ".")}%`}}></div>
        </div>
    </div>
    
  </CandContainer>
};


export default function Panel({clicked}){
    useEffect(()=>{
      console.log(clicked, ' vendo aqui')
    }, [clicked])
    return <div>
      <h4>{clicked && clicked.properties.cd}</h4>
      {
        clicked && clicked.properties.data.c.map( (cand, i) => <Cand key={i} cand={cand}/>)
      }
    </div>
  }