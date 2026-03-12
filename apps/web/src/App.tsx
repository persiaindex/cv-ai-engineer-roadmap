import { Link, Route, Routes } from "react-router-dom"
import DashboardPage from "./pages/DashboardPage"
import MachinesPage from "./pages/MachinesPage"

function App() {
  return (
    <div>
      <nav style={{ padding: "1rem 2rem", borderBottom: "1px solid #ccc" }}>
        <Link to="/" style={{ marginRight: "1rem" }}>Dashboard</Link>
        <Link to="/machines">Machines</Link>
      </nav>

      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/machines" element={<MachinesPage />} />
      </Routes>
    </div>
  )
}

export default App