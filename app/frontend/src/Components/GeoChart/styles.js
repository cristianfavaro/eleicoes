import styled from "styled-components";
export const Container = styled.div`
  width: 500px;
  display: flex;
  svg {
    display: block;
    width: 100%;
    height: 300px;
  }
  
  svg .country:hover {
    stroke: black;
    stroke-width: 1px;
    cursor: pointer;
  }
`;