import Header from "../components/Header"
import MachineForm from "../components/MachineForm"
import MachineTable from "../components/MachineTable"
import { machines } from "../data/mockData"

function MachinesPage() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />
      <MachineTable machines={machines} />
      <MachineForm />
    </div>
  )
}

export default MachinesPage