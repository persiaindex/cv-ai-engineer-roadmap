import { BarChart, Bar, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts"
import type { AlertApiItem } from "../types/dashboard"

type AlertChartProps = {
  alerts: AlertApiItem[]
}

function AlertChart({ alerts }: AlertChartProps) {
  const chartData = ["low", "medium", "high"].map((level) => ({
    name: level.charAt(0).toUpperCase() + level.slice(1),
    value: alerts.filter((alert) => alert.severity === level).length,
  }))

  return (
    <section style={{ marginTop: "1.5rem" }}>
      <h2>Alert Severity Chart</h2>
      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis allowDecimals={false} />
            <Tooltip />
            <Bar dataKey="value" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </section>
  )
}

export default AlertChart