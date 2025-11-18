import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from "./components/home"
import Pickle from "./components/pickle"
function App() {
  return (
    <>
      <div>
        <h1>
          If every porkchop were perfect, we wouldn't have hotdogs
          <Home/>
          <Pickle/>
        </h1>
      </div>
    </>
  )
}
export default App