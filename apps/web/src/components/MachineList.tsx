import type { Machine } from "../data/mockData"

type MachineListProps = {
  machines: Machine[]
}

function MachineList({ machines }: MachineListProps) {
  return (
    <section style={{ marginTop: "1.5rem" }}>
      <h2>Machines</h2>
      <ul>
        {machines.map((machine) => (
          <li key={machine.id}>
            <strong>{machine.machineId}</strong> - {machine.name} ({machine.location})
          </li>
        ))}
      </ul>
    </section>
  )
}

export default MachineList