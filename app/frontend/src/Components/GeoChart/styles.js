import styled from "styled-components";

export const GeoChartContainer = styled.div`
    display: flex;
`

export const Container = styled.div`
  width: 500px;
  display: flex;
  svg {
    display: block;
    width: 100%;
    height: 300px;
  }
  
  svg .place:hover {
    stroke: black;
    stroke-width: 1px;
    cursor: pointer;
  }
`;