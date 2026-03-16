import { useState } from "react"
import type { AlertApiItem } from "../types/dashboard"

type AlertListProps = {
  alerts: AlertApiItem[]
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
              <strong>{alert.alert_id}</strong> - {alert.severity} - {alert.message}
            </li>
          ))}
        </ul>
      )}
    </section>
  )
}

export default AlertList