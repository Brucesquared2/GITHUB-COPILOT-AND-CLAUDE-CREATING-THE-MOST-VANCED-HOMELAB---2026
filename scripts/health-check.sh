#!/bin/bash
declare -A SERVICES
SERVICES=(
    ["maps-quadcore"]="http://localhost:8000/health"
    ["ai-warehouse"]="http://localhost:8002/health"
    ["mdps-trade"]="http://localhost:8001/health"
    ["toolbox"]="http://localhost:8004/health"
    ["omni-core"]="http://localhost:8003/health"
    ["aaw-backend"]="http://localhost:3002/health"
    ["aaw-site"]="http://localhost:3003/health"
    ["ta-library"]="http://localhost:8010/health"
    ["over-watch-quant"]="http://localhost:8020/health"
    ["the-collective-trading"]="http://localhost:8030/health"
    ["maps-dashboards"]="http://localhost:8040/health"
    ["openfang"]="http://localhost:4200/health"
    ["ollama"]="http://localhost:11434"
)
FAIL=0; PASS=0
for S in "${!SERVICES[@]}"; do
    NAME=$S; URL=${SERVICES[$S]}
    echo -n "$NAME: "
    if curl -fs --max-time 7 "$URL" | grep -i "ok\|healthy" > /dev/null 2>&1; then
        echo "? OK"; PASS=$((PASS+1))
    else
        echo "? FAIL ($URL)"; FAIL=$((FAIL+1))
    fi
done
echo "$PASS OK, $FAIL failed."
exit $FAIL
