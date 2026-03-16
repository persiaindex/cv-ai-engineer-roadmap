export type DashboardSummary = {
  machine_count: number
  inspection_count: number
  open_alert_count: number
  defective_inspection_count: number
}

export type AlertApiItem = {
  id: number
  alert_id: string
  source_type: string
  source_id: string
  message: string
  severity: string
  is_open: boolean
  created_at: string
}

type PaginatedResponse<T> = {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

export type AlertsApiResponse = PaginatedResponse<AlertApiItem>