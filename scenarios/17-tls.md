# 17 — TLS/certificate failure

**Symptoms:** clients report certificate errors, handshake failures, or sudden connection failures.

```bash
openssl s_client -connect example.com:443 -servername example.com -showcerts </dev/null
curl -Iv https://example.com
date -u
```

Use only an endpoint you are authorized to test. Check expiry, hostname/SAN, full chain/intermediate CA, trust store, system clock, and whether the correct certificate is served by the load balancer/ingress.

**Mitigation:** renew/restore the correct chain and verify from the client path. Do not disable certificate validation as a permanent workaround.
