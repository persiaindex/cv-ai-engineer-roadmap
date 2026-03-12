type Machine = {
  id: number
  machine_id: string
  name: string
  location: string
}

type MachineTableProps = {
  machines: Machine[]
}

function MachineTable({ machines }: MachineTableProps) {
  return (
    <section style={{ marginTop: "1.5rem" }}>
      <h2>Machine Table</h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>Machine ID</th>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>Name</th>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>Location</th>
          </tr>
        </thead>
        <tbody>
          {machines.map((machine) => (
            <tr key={machine.id}>
              <td style={{ padding: "0.5rem 0" }}>{machine.machine_id}</td>
              <td>{machine.name}</td>
              <td>{machine.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}

export default MachineTable