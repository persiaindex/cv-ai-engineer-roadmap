import { useState } from "react"

type MachineFormData = {
  machineId: string
  name: string
  location: string
}

type MachineFormErrors = {
  machineId?: string
  name?: string
  location?: string
}

function MachineForm() {
  const [formData, setFormData] = useState<MachineFormData>({
    machineId: "",
    name: "",
    location: "",
  })

  const [errors, setErrors] = useState<MachineFormErrors>({})
  const [successMessage, setSuccessMessage] = useState("")

  function validate(values: MachineFormData): MachineFormErrors {
    const newErrors: MachineFormErrors = {}

    if (!values.machineId.trim()) {
      newErrors.machineId = "Machine ID is required."
    }

    if (!values.name.trim()) {
      newErrors.name = "Name is required."
    }

    if (!values.location.trim()) {
      newErrors.location = "Location is required."
    }

    return newErrors
  }

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const { name, value } = event.target

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }))
  }

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const validationErrors = validate(formData)
    setErrors(validationErrors)

    if (Object.keys(validationErrors).length > 0) {
      setSuccessMessage("")
      return
    }

    setSuccessMessage(`Machine ${formData.machineId} saved locally.`)
    setFormData({ machineId: "", name: "", location: "" })
    setErrors({})
  }

  return (
    <section style={{ marginTop: "2rem" }}>
      <h2>Add Machine</h2>

      <form onSubmit={handleSubmit} style={{ display: "grid", gap: "0.75rem", maxWidth: "400px" }}>
        <div>
          <label htmlFor="machineId">Machine ID</label>
          <input id="machineId" name="machineId" value={formData.machineId} onChange={handleChange} />
          {errors.machineId && <p style={{ color: "red" }}>{errors.machineId}</p>}
        </div>

        <div>
          <label htmlFor="name">Name</label>
          <input id="name" name="name" value={formData.name} onChange={handleChange} />
          {errors.name && <p style={{ color: "red" }}>{errors.name}</p>}
        </div>

        <div>
          <label htmlFor="location">Location</label>
          <input id="location" name="location" value={formData.location} onChange={handleChange} />
          {errors.location && <p style={{ color: "red" }}>{errors.location}</p>}
        </div>

        <button type="submit">Save Machine</button>
      </form>

      {successMessage && <p style={{ color: "green", marginTop: "1rem" }}>{successMessage}</p>}
    </section>
  )
}

export default MachineForm