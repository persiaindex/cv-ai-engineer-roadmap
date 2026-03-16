import { useCallback, useEffect, useState } from "react"
import { api } from "../lib/api"
import type { DashboardSummary } from "../types/dashboard"

export function useDashboardSummary() {
  const [summary, setSummary] = useState<DashboardSummary | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  const fetchSummary = useCallback(async () => {
    setLoading(true)
    setError("")

    try {
      const response = await api.get<DashboardSummary>("/dashboard/summary/")
      setSummary(response.data)
    } catch {
      setError("Could not load dashboard summary.")
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchSummary()
  }, [fetchSummary])

  return { summary, loading, error, refetch: fetchSummary }
}