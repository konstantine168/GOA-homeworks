import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SU from "/public/StevenUniverse.jpg"

function App() {
  return (
    <>
      <div className='MainDiv'>
        <header>
            <h1>Home</h1>
            <h1>About</h1>
            <h1>Other</h1>
            <h1>Blog</h1>
        </header>
        <main>
          <img src={SU} alt="Universe" />
        </main>
      </div>
    </>
  )
}
export default App