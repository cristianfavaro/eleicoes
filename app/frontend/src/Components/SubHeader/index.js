import React from 'react';
import { Link } from 'react-router-dom';
import Search from "./Search";
import styled from 'styled-components';

const Container = styled.div`
    grid-area: SH; 
    padding: 0.5rem;
    display: flex;
    width: 100%;
    justify-content: space-evenly;
    align-items: center;
    a{
        margin-right: 0.2rem;
    }
`

const SubHeader = ({geojson, setClicked}) => {
    
    return <Container>
        <Search {...{geojson, setClicked}}/>
        <div>
            <Link className="btn btn-info btn-sm" to="uf">Estados</Link>
            <Link className="btn btn-info btn-sm" to="/">Municípios</Link>
        </div>
    </Container>
}


export default SubHeader;