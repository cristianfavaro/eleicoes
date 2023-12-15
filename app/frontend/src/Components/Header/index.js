import styled from 'styled-components';
import {useControls} from '../../contexts/ControlsContext';

const Container = styled.div`
    grid-area: MH;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.2rem 0;
    background-color: lightgray;
    h3{
        margin: 0.5rem;
    };
    a{
        margin: 0.2rem;
    };
`

export default function Header(){
    const {setEle, ele} = useControls();
    return <Container>        
        <h3> Eleições - Dashboard</h3>
        <select value={ele} onChange={ e => setEle(e.target.value)}>
            <option value="544">Presidencial 2022 (1º turno)</option>
            <option value="545">Presidencial 2022 (2º turno)</option>
            <option value="546">Governador 2022 (1º turno)</option>
            <option value="547">Governador 2022 (2º turno)</option>
        </select>
        
    </Container>
}