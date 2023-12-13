import styled from "styled-components";


export const Container = styled.div`
  display: flex;
  grid-area: CT;
  padding: 0 0.5rem;

  >span{
    position: absolute;
    top: 80px;
    margin: 0.5rem;
    background-color: blue;
    color: #fff;
    border-radius: 50px;
    padding: 0.2rem;
    cursor: pointer;
  }; 

  #map {
    flex: 1 1 auto;
    display: block;
    width: 100%;
    .place:hover {
      stroke: black;
      stroke-width: 1px;
      cursor: pointer;
    };
  };
`;