type StatusCardProps = {
  title: string
  value: string
}

function StatusCard({ title, value }: StatusCardProps) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", marginTop: "1rem" }}>
      <h3>{title}</h3>
      <p>{value}</p>
    </div>
  )
}

export default StatusCard