// import logo from '../logo.svg';
// import './App.css';
import {Routes, Route } from "react-router-dom"
import Layout from "../component/layout/Layout.tsx"
import Home from "../pages/Home.js"
import Test from "../pages/Test.js"
import Testinput from "../pages/Testinput.js"

function App() {
  return (
    <Layout>
      <div className="App">
        <header className="App-header"/>
          {
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="/Test" element={<Test/>}/>
                <Route path="/Testinput" element={<Testinput/>}/>
            </Routes>
          }
      </div>
    </Layout>
  );
}

export default App;
