import { useState } from 'react'
import './App.css'

export default function App() {
  /*      STEVEN UNIVERSE!!      */
  const [counter, setCounter] = useState(0)
  function HandleAddition() {
      setCounter(counter + 1)
  }
  function HandleDecreastion() {
    setCounter(counter - 1)
  }
  function HandleMultiplication() {
    setCounter(counter * 2)
  }
  function HandleDivision() {
    setCounter(counter / 2)
  }
  return (
      <div>
        <div className="TxtAsDiv">{counter}</div>
        <button className='button1' onClick={HandleAddition}>Increase</button>
        <button className='button2' onClick={HandleDecreastion}>Decrease</button>
        <button className='button3' onClick={HandleMultiplication}>Multiply</button>
        <button className='button4' onClick={HandleDivision}>Divide</button>
      </div>
  )
}