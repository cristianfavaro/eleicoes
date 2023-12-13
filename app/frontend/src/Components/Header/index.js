import { Link } from 'react-router-dom';
import styled from 'styled-components';
import {useControls} from '../../contexts/ControlsContext';

const Container = styled.div`
    grid-area: HE;
    a{
        margin: 0.2rem;
    }
`

export default function Header(){
    const {setEle, ele} = useControls();
    return <Container>        
        <h4> Eleições - Dashboard</h4>
        <select value={ele} onChange={ e => setEle(e.target.value)}>
            <option value="544">Presidencial 2022 (1º turno)</option>
            <option value="545">Presidencial 2022 (2º turno)</option>
            <option value="546">Governador 2022 (1º turno)</option>
            <option value="547">Governador 2022 (2º turno)</option>
        </select>
        <div>
            <Link to="uf">Estados</Link>
            <Link to="/">Municípios</Link>
        </div>
    </Container>
}