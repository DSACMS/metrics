import React from 'react';
import {Route, Routes} from "react-router-dom";
import Nav from './components/Nav/Nav';
import Home from './components/pages/Home';
import Weekly from './components/pages/weekly';
import Monthly from './components/pages/monthly';

function App() {
  return (
    <>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/weekly" element={<Weekly />} />
          <Route path="/monthly" element={<Monthly />} />
        </Routes>
    </div>
  </>
  );
}
export default App;
