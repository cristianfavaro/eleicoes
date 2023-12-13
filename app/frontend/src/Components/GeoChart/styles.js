import styled from "styled-components";

export const GeoChartContainer = styled.div`
`;

export const Container = styled.div`
  width: 500px;
  display: flex;
  flex-direction: column;
  position: relative;
  grid-area: CT;
  
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