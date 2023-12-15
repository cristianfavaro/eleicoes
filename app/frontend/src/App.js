import React, {Suspense, lazy} from 'react';
import { Outlet, Route, Routes } from 'react-router-dom';
import Header from './Components/Header';
import './App.css';
import { ControlsProvider } from './contexts/ControlsContext';
import styled from 'styled-components';
const BrUFMap = lazy(() => import('./Components/GeoChart/BrUFMap')); 
const BrMunMap = lazy(() => import('./Components/GeoChart/BrMunMap')); 

const Loading = () => {
  return <div style={{margin: "1rem"}}>
    Baixando...
  </div>
}

const Container = styled.div`
  display: grid;
  grid-template-columns: auto 350px;
  grid-template-rows: 70px 50px calc(100vh - 120px);
  grid-template-areas:
  'MH MH'
  'SH SB'
  'CT SB';
`;

const Layout = () => {
  return <Outlet/>  
}

function App() {
  return  <ControlsProvider>
      <Container>
        <Header/>
        <Routes>
          <Route path="/" element={<Layout/>}>
                <Route index element={<Suspense fallback={<Loading/>}><BrMunMap/></Suspense>}/>
                <Route path="uf" element={<Suspense fallback={<Loading/>}><BrUFMap/></Suspense>}/>
          </Route>
        </Routes>
      </Container>
    </ControlsProvider>
};

export default App;
