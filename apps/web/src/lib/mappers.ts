import type { Machine, MachineApiItem } from "../types/machine"

export function mapMachineFromApi(item: MachineApiItem): Machine {
  return {
    id: item.id,
    machineId: item.machine_id,
    name: item.name,
    location: item.location,
    isActive: item.is_active,
    createdAt: item.created_at,
  }
}