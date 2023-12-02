import styled from "styled-components";

export const GeoChartContainer = styled.div`
    display: flex;
    .container{
          >span{
            position: absolute;
            top: 80px;
            margin: 0.5rem;
            background-color: blue;
            color: #fff;
            border-radius: 50px;
            padding: 0.2rem;
            cursor: pointer;
          }
    }
`;

export const Container = styled.div`
  width: 500px;
  display: flex;
  svg {
    display: block;
    width: 100%;
    height: 300px;
  };
  
  svg .place:hover {
    stroke: black;
    stroke-width: 1px;
    cursor: pointer;
  };
`;