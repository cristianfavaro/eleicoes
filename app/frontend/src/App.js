import React, {Suspense, lazy} from 'react';
import { Outlet, Route, Routes } from 'react-router-dom';
import Header from './Components/Header';
import './App.css';
const BrUFMap = lazy(() => import('./Components/GeoChart/BrUFMap')); 
const BrMunMap = lazy(() => import('./Components/GeoChart/BrMunMap')); 

const Loading = () => {
  return <div>
    Baixando...
  </div>
}

const Layout = () => {
  return <div>

    <Outlet/>
  </div>
}



function App() {
  return <div>
      <Header/>
      <Routes>
        <Route path="/" element={<Layout/>}>
              <Route index element={<Suspense fallback={<Loading/>}><BrMunMap/></Suspense>}/>
              <Route path="uf" element={<Suspense fallback={<Loading/>}><BrUFMap/></Suspense>}/>
        </Route>
      </Routes>
    </div>
}

export default App;
