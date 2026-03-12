export type Machine = {
  id: number
  machineId: string
  name: string
  location: string
}

export type Alert = {
  id: number
  alertId: string
  severity: string
  message: string
}

export const machines: Machine[] = [
  { id: 1, machineId: "M-100", name: "Smart Feeder Line A", location: "Aachen Plant 1" },
  { id: 2, machineId: "M-101", name: "Smart Feeder Line B", location: "Aachen Plant 1" },
  { id: 3, machineId: "M-102", name: "Smart Feeder Line C", location: "Aachen Plant 2" },
]

export const alerts: Alert[] = [
  { id: 1, alertId: "A-400", severity: "medium", message: "Feeder fill level is low." },
  { id: 2, alertId: "A-401", severity: "high", message: "Defect score exceeded threshold." },
]

export const alertChartData = [
  { name: "Low", value: 0 },
  { name: "Medium", value: 1 },
  { name: "High", value: 1 },
]