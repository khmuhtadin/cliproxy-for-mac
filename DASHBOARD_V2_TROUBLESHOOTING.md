# 🔧 Dashboard v2 Troubleshooting Guide

## ✅ Quick Fixes

### Problem: "Failed to load data"

**Cause**: CORS error when dashboard on port 8318 tries to access API on port 8317

**Solution**: Use the proxy server (already configured)

```bash
# Make sure proxy server is running
ps aux | grep serve-dashboards-with-proxy

# If not running, start it:
python3 /Users/khmuhtadin/.cli-proxy-api/serve-dashboards-with-proxy.py &
```

---

### Problem: 404 Error

**Check if servers are running:**

```bash
# Check proxy server (port 8318)
lsof -i :8318

# Check API server (port 8317)
lsof -i :8317
```

**Fix:**

```bash
# Start proxy server
python3 /Users/khmuhtadin/.cli-proxy-api/serve-dashboards-with-proxy.py &

# API server should already be running (cliproxyapi-plus)
ps aux | grep cliproxyapi
```

---

### Problem: Dashboard loads but no data

**Test API connection:**

```bash
# Test through proxy
curl http://localhost:8318/v0/management/auth-files \
  -H "X-Management-Key: sk-dummy"

# Should return JSON with account data
```

**If fails:**

1. Check `config.yaml` has correct API key
2. Verify API server is running
3. Clear browser cache and reload

---

### Problem: Chart not showing

**Possible causes:**

1. **Chart.js CDN not loaded** - Check internet connection
2. **No quota data** - Verify accounts have quota info
3. **JavaScript error** - Check browser console

**Fix:**

1. Open browser DevTools (F12)
2. Check Console for errors
3. Check Network tab for failed requests
4. Verify Chart.js loaded: Look for `chart.umd.min.js` in Network

---

### Problem: Auto-refresh not working

**Check:**

1. Is auto-refresh checkbox checked?
2. Is countdown timer showing?
3. Any console errors?

**Fix:**

```javascript
// Open browser console and check:
console.log(autoRefreshEnabled);
console.log(refreshInterval);
console.log(countdownInterval);
```

---

### Problem: Theme toggle not working

**Check localStorage:**

```javascript
// In browser console:
localStorage.getItem('theme')
```

**Fix:**

```javascript
// Clear and retry:
localStorage.clear();
// Reload page
```

---

## 🔍 Advanced Troubleshooting

### Check Server Logs

```bash
# API server logs
tail -f /Users/khmuhtadin/.cli-proxy-api/logs/main.log

# Proxy server logs
# (visible in terminal where proxy was started)
```

### Test API Endpoints Directly

```bash
# Test auth-files
curl http://localhost:8317/v0/management/auth-files \
  -H "X-Management-Key: sk-dummy"

# Test usage
curl http://localhost:8317/v0/management/usage \
  -H "X-Management-Key: sk-dummy"

# Test quota
curl http://localhost:8317/v0/management/quota \
  -H "X-Management-Key: sk-dummy"
```

### Verify File Permissions

```bash
# Check dashboard files
ls -la /Users/khmuhtadin/.cli-proxy-api/static/dashboard*.html

# Should be readable (rw-r--r--)
```

### Reset Everything

```bash
# 1. Stop all servers
pkill -f serve-dashboards
pkill -f cliproxyapi

# 2. Clear browser cache
# (Ctrl+Shift+Del in most browsers)

# 3. Restart API server
cd /Users/khmuhtadin/bin
./cliproxyapi-plus --config /Users/khmuhtadin/.cli-proxy-api/config.yaml &

# 4. Start proxy server
python3 /Users/khmuhtadin/.cli-proxy-api/serve-dashboards-with-proxy.py &

# 5. Access dashboard
open http://localhost:8318/dashboard-v2.html
```

---

## 📊 Diagnostic Commands

### Full System Check

```bash
#!/bin/bash

echo "=== Dashboard v2 Diagnostic ==="
echo ""

echo "1. Checking Proxy Server (8318)..."
lsof -i :8318 && echo "✅ Running" || echo "❌ Not running"
echo ""

echo "2. Checking API Server (8317)..."
lsof -i :8317 && echo "✅ Running" || echo "❌ Not running"
echo ""

echo "3. Testing Proxy Endpoint..."
curl -s -o /dev/null -w "Status: %{http_code}\n" \
  http://localhost:8318/v0/management/auth-files \
  -H "X-Management-Key: sk-dummy"
echo ""

echo "4. Checking Dashboard File..."
ls -lh /Users/khmuhtadin/.cli-proxy-api/static/dashboard-v2.html
echo ""

echo "5. Testing Dashboard Access..."
curl -s -o /dev/null -w "Status: %{http_code}\n" \
  http://localhost:8318/dashboard-v2.html
echo ""

echo "=== End Diagnostic ==="
```

---

## 🐛 Common Error Messages

### "Failed to fetch"

**Browser Console:**
```
Failed to fetch: TypeError: Failed to fetch
```

**Cause**: Proxy server not running or CORS issue

**Fix**: Restart proxy server with CORS support

---

### "NetworkError when attempting to fetch resource"

**Cause**: API server not reachable

**Fix**:
1. Check API server is running
2. Verify port 8317 is open
3. Check firewall settings

---

### "Uncaught ReferenceError: Chart is not defined"

**Cause**: Chart.js CDN failed to load

**Fix**:
1. Check internet connection
2. Try different CDN mirror
3. Download Chart.js locally

---

## 💡 Performance Issues

### Dashboard loads slowly

**Possible causes:**
1. Chart.js CDN slow
2. Large quota cache
3. Many accounts

**Optimizations:**
1. Use local Chart.js
2. Reduce auto-refresh interval
3. Optimize quota cache

---

### High CPU usage

**Check:**
```bash
# Monitor processes
top -pid $(pgrep -f serve-dashboards-with-proxy)
top -pid $(pgrep -f cliproxyapi)
```

**Fix:**
- Increase auto-refresh interval
- Reduce number of active accounts
- Check for JavaScript memory leaks

---

## 📞 Getting Help

If issues persist:

1. **Check browser console** for errors
2. **Check server logs** in `logs/main.log`
3. **Review documentation**:
   - `DASHBOARD_V2_FEATURES.md`
   - `DASHBOARD_V2_QUICKSTART.md`
   - `IMPLEMENTATION_SUMMARY.md`

4. **Test with different browser**
5. **Try incognito/private mode**

---

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Proxy server running on port 8318
- [ ] API server running on port 8317
- [ ] Dashboard file exists and readable
- [ ] Browser cache cleared
- [ ] No console errors
- [ ] Network requests successful
- [ ] Firewall not blocking ports
- [ ] Internet connection active (for CDN)

---

**Last Updated**: December 28, 2025  
**Version**: 2.0
