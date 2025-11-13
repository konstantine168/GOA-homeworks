import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import photo from "/public/assets/StevenUniverse.jpg"
import Video from "/public/assets/SUE.mp4"
function App() {
  return (
    <>
    <video src={Video}></video>
    <img src={photo} alt="Image" />
    </>
  )
}
export default App