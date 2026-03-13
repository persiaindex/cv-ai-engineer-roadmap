import ApiMessage from "../components/ApiMessage"
import Header from "../components/Header"
import MachineForm from "../components/MachineForm"
import MachineTable from "../components/MachineTable"
import { useMachines } from "../hooks/useMachines"

function MachinesPage() {
  const { machines, loading, error } = useMachines()

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />

      {loading && <ApiMessage message="Loading machines..." />}
      {error && <ApiMessage message={error} type="error" />}
      {!loading && !error && <MachineTable machines={machines} />}

      <MachineForm />
    </div>
  )
}

export default MachinesPage