import React from 'react';
import { Link } from 'react-router-dom';
import Search from "./Search";
import styled from 'styled-components';

const Container = styled.div`
    grid-area: SH; 
    padding: 0.5rem;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    a{
        margin-right: 0.2rem;
    }
    .btns{
        button{
            margin: 0 0.2rem;
            padding: 0.2rem;
            a{
                color: inherit; /* blue colors for links too */
                text-decoration: inherit; /* no underline */
            }
        }
    }
    
`

const SubHeader = ({geojson, setClicked}) => {
    
    return <Container>
        <Search {...{geojson, setClicked}}/>
        <div className='btns'>
            <button><Link className="btn btn-info btn-sm" to="/uf">Estados</Link></button>
            <button><Link className="btn btn-info btn-sm" to="/">Municípios</Link></button>
        </div>
    </Container>
}


export default SubHeader;