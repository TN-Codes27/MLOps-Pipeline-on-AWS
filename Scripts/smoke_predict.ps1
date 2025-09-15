param(
  [Parameter(Mandatory=$true)]
  [string]$AlbUrl
)

$body = '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
$response = Invoke-WebRequest -Uri "$AlbUrl/predict" -Method POST -ContentType "application/json" -Body $body -TimeoutSec 10 -ErrorAction Stop
if ($response.StatusCode -ne 200) {
  Write-Error "Smoke test failed with status $($response.StatusCode)"
  exit 1
}
Write-Output "Smoke test OK"
