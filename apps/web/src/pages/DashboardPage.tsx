import Header from "../components/Header"
import AlertChart from "../components/AlertChart"
import AlertList from "../components/AlertList"
import { alertChartData, alerts } from "../data/mockData"

function DashboardPage() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />
      <AlertChart data={alertChartData} />
      <AlertList alerts={alerts} />
    </div>
  )
}

export default DashboardPage