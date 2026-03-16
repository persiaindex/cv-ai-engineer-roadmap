import { useCallback, useEffect, useState } from "react"
import { api } from "../lib/api"
import type { AlertApiItem, AlertsApiResponse } from "../types/dashboard"

export function useAlerts() {
  const [alerts, setAlerts] = useState<AlertApiItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  const fetchAlerts = useCallback(async () => {
    setLoading(true)
    setError("")

    try {
      const response = await api.get<AlertsApiResponse>("/alerts/")
      setAlerts(response.data.results)
    } catch {
      setError("Could not load alerts from the API.")
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchAlerts()
  }, [fetchAlerts])

  return { alerts, loading, error, refetch: fetchAlerts }
}