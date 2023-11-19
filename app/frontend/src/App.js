import React, {Suspense, lazy} from 'react';

const BrUFMap = lazy(() => import('./Components/GeoChart/BrUFMap')); 

const Loading = () => {
  return <div>
    Baixando...
  </div>
}

function App() {
  return <div>
    <Suspense
      fallback={<Loading/>}
    >
      <BrUFMap></BrUFMap>
    </Suspense>   
    </div>
}

export default App;
