import Header from "./components/Header"
import MachineList from "./components/MachineList"
import AlertList from "./components/AlertList"
import MachineForm from "./components/MachineForm"
import { alerts, machines } from "./data/mockData"

function App() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />
      <MachineList machines={machines} />
      <AlertList alerts={alerts} />
      <MachineForm />
    </div>
  )
}

export default App