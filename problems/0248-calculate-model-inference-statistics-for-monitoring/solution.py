from numpy import percentile

def calculate_inference_stats(latencies_ms: list) -> dict:
    """
    Calculate inference statistics for model monitoring.
    
    Args:
        latencies_ms: list of latency measurements in milliseconds
    
    Returns:
        dict with keys: 'throughput_per_sec', 'avg_latency_ms', 'p50_ms', 'p95_ms', 'p99_ms'
        All values rounded to 2 decimal places.
    """    
    if not latencies_ms:
        return {}

    avg_latency_ms = sum(latencies_ms) / len(latencies_ms)
    percentiles_ms = percentile(latencies_ms, [50, 95, 99])
    p50_ms, p95_ms, p99_ms = (round(p, 2) for p in percentiles_ms) 
    
    inference_stats: dict = {
        'throughput_per_sec': round(1000 / avg_latency_ms, 2),
        'avg_latency_ms': round(avg_latency_ms, 2),
        'p50_ms': p50_ms.item(),
        'p95_ms': p95_ms.item(),
        'p99_ms': p99_ms.item(),
    }

    return inference_stats