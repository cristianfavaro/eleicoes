import styled from "styled-components";


export const Container = styled.div`
  display: flex;
  position: relative;
  grid-area: CT;
  padding: 0 0.5rem;

  >span{
    position: absolute;
    top: 40px;
    left: 40px;
    background-color: blue;
    color: #fff;
    border-radius: 50px;
    padding: 0.5rem;
    cursor: pointer;
    font-weight: 800;
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