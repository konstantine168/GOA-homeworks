import { useState } from 'react'
import './App.css'
export default function App() {
  {/* 1) */}
  const [loshorsinisview, setloshorsinis] = useState(true)
  const [laView, setLa] = useState(true)
  function handleTrueVar() {
    setloshorsinis(true)
  }
  function handleFalseVar() {
    setloshorsinis(false)
  }
  return (
    <>
    <button onClick={}>Backround Color Change</button>
    <button onClick={handleTrueVar}>True</button>
    <button onClick={handleFalseVar}>False</button>
      <div id='thing'>
        {loshorsinisview ? <button>
          This is a test website made by Konstantine Papava!
        </button> : null}
        {/* 2) */}

      </div> 
    </>
  )
}