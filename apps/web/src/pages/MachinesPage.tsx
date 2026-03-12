import Header from "../components/Header"
import MachineForm from "../components/MachineForm"
import MachineTable from "../components/MachineTable"
import { useMachines } from "../hooks/useMachines"

function MachinesPage() {
  const { machines, loading, error } = useMachines()

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />

      {loading && <p>Loading machines...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!loading && !error && <MachineTable machines={machines} />}

      <MachineForm />
    </div>
  )
}

export default MachinesPage