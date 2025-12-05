import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from './components/header'
import Footer from './components/footer'
import About from './pages/about'
import Navbar from './components/navbar'

function App() {
  return (
    <>
      <div>
        <h1>
          <h1>Main App Component</h1>
          <Header></Header>
          <Footer></Footer>
          <About></About>
          <Navbar></Navbar>
        </h1>
      </div>
    </>
  )
}

export default App
