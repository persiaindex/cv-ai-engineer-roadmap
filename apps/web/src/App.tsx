// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import StatusCard from "./components/StatusCard"

function App() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>Smart Feeder Platform</h1>
      <p>Frontend setup is working.</p>
      <StatusCard title="Backend Status" value="Ready for API connection" />
    </div>
  )
}

export default App
