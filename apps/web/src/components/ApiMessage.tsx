type ApiMessageProps = {
  message: string
  type?: "loading" | "error"
}

function ApiMessage({ message, type = "loading" }: ApiMessageProps) {
  const color = type === "error" ? "red" : "black"

  return <p style={{ color, marginTop: "1rem" }}>{message}</p>
}

export default ApiMessage