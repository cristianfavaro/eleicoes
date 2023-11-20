import styled from 'styled-components';

export const BarContainer = styled.div`
  height: 15px;
  padding: 0.2rem 0;
  display: flex;
  .w3-grey{
    background-color: gray;
  }
`

export const Container = styled.div.attrs(
    ({x, y})=>({
        style:{
            transform: `translateY(${y}px) translateX(${x}px)`,
        }
    })
)`
  border: 1px solid darkgray;
  background-color: white; 
  width: 200px;
  position: fixed;
  display: ${props => props.show ? "block" : "none"};
  transition: transform 0.23s; //Sticking effect
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