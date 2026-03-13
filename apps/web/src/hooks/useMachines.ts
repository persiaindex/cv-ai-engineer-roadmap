import { useEffect, useState } from "react"
import { api } from "../lib/api"
import { mapMachineFromApi } from "../lib/mappers"
import type { Machine, MachineApiItem } from "../types/machine"

type MachineApiResponse = {
  count: number
  next: string | null
  previous: string | null
  results: MachineApiItem[]
}

export function useMachines() {
  const [machines, setMachines] = useState<Machine[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    async function fetchMachines() {
      try {
        const response = await api.get<MachineApiResponse>("/machines/")
        const mappedMachines = response.data.results.map(mapMachineFromApi)
        setMachines(mappedMachines)
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