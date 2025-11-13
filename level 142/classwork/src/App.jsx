import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
function App() {
  const [count, setCount] = useState(0)
  return (
    <>
    <div>
      <p>Amount: {count}</p>
      <button onClick={() => setCount(count + 1)}>Click to sum</button>
    </div>
    </>
  )
}
export default App