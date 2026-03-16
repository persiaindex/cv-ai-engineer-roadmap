import type { DashboardSummary } from "../types/dashboard"

type SummaryCardsProps = {
  summary: DashboardSummary
}

function SummaryCards({ summary }: SummaryCardsProps) {
  const cards = [
    { title: "Machines", value: summary.machine_count },
    { title: "Inspections", value: summary.inspection_count },
    { title: "Open Alerts", value: summary.open_alert_count },
    { title: "Defective Inspections", value: summary.defective_inspection_count },
  ]

  return (
    <section style={{ marginTop: "1.5rem" }}>
      <h2>Summary</h2>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
          gap: "1rem",
        }}
      >
        {cards.map((card) => (
          <div
            key={card.title}
            style={{
              border: "1px solid #ccc",
              borderRadius: "8px",
              padding: "1rem",
              background: "#fafafa",
            }}
          >
            <h3 style={{ margin: 0, marginBottom: "0.5rem" }}>{card.title}</h3>
            <p style={{ fontSize: "1.5rem", margin: 0 }}>{card.value}</p>
          </div>
        ))}
      </div>
    </section>
  )
}

export default SummaryCards