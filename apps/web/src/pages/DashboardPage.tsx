import AlertChart from "../components/AlertChart"
import AlertList from "../components/AlertList"
import ApiMessage from "../components/ApiMessage"
import Header from "../components/Header"
import SummaryCards from "../components/SummaryCards"
import { useAlerts } from "../hooks/useAlerts"
import { useDashboardSummary } from "../hooks/useDashboardSummary"

function DashboardPage() {
  const {
    summary,
    loading: summaryLoading,
    error: summaryError,
    refetch: refetchSummary,
  } = useDashboardSummary()

  const {
    alerts,
    loading: alertsLoading,
    error: alertsError,
    refetch: refetchAlerts,
  } = useAlerts()

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <Header />

      {summaryLoading && <ApiMessage message="Loading dashboard summary..." />}
      {summaryError && (
        <>
          <ApiMessage message={summaryError} type="error" />
          <button onClick={refetchSummary}>Retry Summary</button>
        </>
      )}
      {!summaryLoading && !summaryError && summary && <SummaryCards summary={summary} />}

      {alertsLoading && <ApiMessage message="Loading alerts..." />}
      {alertsError && (
        <>
          <ApiMessage message={alertsError} type="error" />
          <button onClick={refetchAlerts}>Retry Alerts</button>
        </>
      )}
      {!alertsLoading && !alertsError && (
        <>
          <AlertChart alerts={alerts} />
          <AlertList alerts={alerts} />
        </>
      )}
    </div>
  )
}

export default DashboardPage