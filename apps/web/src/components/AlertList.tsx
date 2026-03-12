import { useState } from "react"
import type { Alert } from "../data/mockData"

type AlertListProps = {
  alerts: Alert[]
}

function AlertList({ alerts }: AlertListProps) {
  const [showAlerts, setShowAlerts] = useState(true)

  return (
    <section style={{ marginTop: "1.5rem" }}>
      <h2>Alerts</h2>
      <button onClick={() => setShowAlerts(!showAlerts)}>
        {showAlerts ? "Hide Alerts" : "Show Alerts"}
      </button>

      {showAlerts && (
        <ul style={{ marginTop: "1rem" }}>
          {alerts.map((alert) => (
            <li key={alert.id}>
              <strong>{alert.alertId}</strong> - {alert.severity} - {alert.message}
            </li>
          ))}
        </ul>
      )}
    </section>
  )
}

export default AlertList