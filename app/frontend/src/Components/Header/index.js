import { Link } from 'react-router-dom';
import styled from 'styled-components';

const Container = styled.div`
    a{
        margin: 0.2rem;
    }
`

export default function Header(){
    return <Container>
        <Link to="uf">Estados</Link>
        <Link to="/">Municípios</Link>
    </Container>
}