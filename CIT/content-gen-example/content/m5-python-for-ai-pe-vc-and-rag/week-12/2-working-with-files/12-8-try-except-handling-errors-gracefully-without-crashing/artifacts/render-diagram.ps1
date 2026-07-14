# Render diagram.mmd -> diagram.png for topic 12.8
# Run from repo root or this directory

$mmd = "content/m5-python-for-ai-pe-vc-and-rag/week-12/2-working-with-files/12-8-try-except-handling-errors-gracefully-without-crashing/artifacts/diagram.mmd"
$png = "content/m5-python-for-ai-pe-vc-and-rag/week-12/2-working-with-files/12-8-try-except-handling-errors-gracefully-without-crashing/artifacts/diagram.png"

mmdc -i $mmd -o $png -w 1400 -b transparent
if ($LASTEXITCODE -eq 0) {
    $size = (Get-Item $png).Length
    Write-Host "PNG rendered successfully. Size: $size bytes"
} else {
    Write-Host "mmdc failed with exit code $LASTEXITCODE"
}
