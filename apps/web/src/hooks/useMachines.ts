import { useEffect, useState } from "react"
import { api } from "../lib/api"

export type MachineApiItem = {
  id: number
  machine_id: string
  name: string
  location: string
  is_active: boolean
  created_at: string
}

type MachineApiResponse = {
  count: number
  next: string | null
  previous: string | null
  results: MachineApiItem[]
}

export function useMachines() {
  const [machines, setMachines] = useState<MachineApiItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    async function fetchMachines() {
      try {
        const response = await api.get<MachineApiResponse>("/machines/")
        setMachines(response.data.results)
      } catch {
        setError("Could not load machines from the API.")
      } finally {
        setLoading(false)
      }
    }

    fetchMachines()
  }, [])

  return { machines, loading, error }
}